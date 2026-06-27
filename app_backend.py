"""
app_backend.py — Lớp BỌC TOÀN BỘ PIPELINE sản xuất video (Manim + VoxCPM2 + karaoke).

ĐỘC LẬP FRAMEWORK: KHÔNG import streamlit/gradio. Chỉ dùng thư viện chuẩn (stdlib)
+ subprocess. Nhờ vậy đổi GUI (Streamlit ↔ Gradio) không phải viết lại logic.

Nguyên tắc (theo GUI_DESIGN.md §5.1, §6, §9):
  * Mọi hàm thuần Python; hàm chạy lâu trả về GENERATOR các dòng log.
  * Đọc lời thoại AN TOÀN: parse AST, KHÔNG exec/import code nặng trong process này.
  * Ghi file .py ATOMICALLY (tmp + os.replace), giữ nguyên header/docstring, validate trước.
  * TỰ DÒ FILE thật (slug có thể lệch quy ước, vd 'parabol').
  * TUYỆT ĐỐI không import voxcpm; luôn gọi qua render_pipeline.sh / VOXCPM python.
"""
import ast
import glob
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

# ===================== ĐƯỜNG DẪN GỐC (hằng số) =====================
ROOT = Path(__file__).resolve().parent
SCENES = ROOT / "scenes"
OUTPUT = ROOT / "output"
PREVIEW = OUTPUT / "preview"
MEDIA = ROOT / "media" / "videos"
VENV = ROOT / ".venv" / "bin"
VOXCPM = Path(os.path.expanduser("~/voxcpm-venv/bin/python"))
REF_VOICE = OUTPUT / "narration" / "voice-yeu_ref16k.wav"
IDEAS_MD = ROOT / "noidung" / "kho_y_tuong.md"
GUI_STATE = ROOT / "gui_state.json"
BRAND_PY = SCENES / "brand.py"
ALIGN_PY = SCENES / "align_narration.py"
PIPELINE_SH = ROOT / "render_pipeline.sh"
FFPROBE = shutil.which("ffprobe") or "/opt/homebrew/bin/ffprobe"

# Mapping cứng (fallback / hiển thị) — nhưng list_videos() vẫn tự dò file thật.
SCENE_CLASS = {
    "phanh": "PhanhVideo", "xetnghiem": "XetNghiemVideo",
    "laikep": "LaiKepVideo", "troixanh": "TroiXanhVideo", "parabol": "ParabolVideo",
}
TITLES = {
    "phanh": "L1 Quãng phanh ∝ v²", "xetnghiem": "T5 Xét nghiệm (Bayes)",
    "laikep": "T1 Lãi kép", "troixanh": "L7 Tán xạ ánh sáng", "parabol": "Parabol",
}


# ===================================================================
#  HELPER nội bộ — dò file (xử lý slug lệch quy ước như 'parabol')
# ===================================================================
def _narration_path(slug: str) -> Path | None:
    """File lời thoại của slug. Quy ước chính: narration_texts_<slug>.py;
    ngoại lệ: narration_<slug>.py (vd parabol). Trả None nếu không thấy."""
    for name in (f"narration_texts_{slug}.py", f"narration_{slug}.py"):
        p = SCENES / name
        if p.exists():
            return p
    return None


def _scene_path(slug: str) -> Path | None:
    p = SCENES / f"{slug}_video.py"
    return p if p.exists() else None


def _scene_class(slug: str) -> str | None:
    """Tên SceneClass: ưu tiên mapping cứng; nếu thiếu, dò class đầu trong scene file."""
    if slug in SCENE_CLASS:
        return SCENE_CLASS[slug]
    sp = _scene_path(slug)
    if not sp:
        return None
    try:
        tree = ast.parse(sp.read_text(encoding="utf-8"))
    except Exception:
        return None
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            return node.name
    return None


def _narration_dir(slug: str) -> Path:
    """Thư mục chứa .wav giọng clone. Quy ước: output/narration_<slug>/.
    Ngoại lệ (tự dò): clone_narration_<slug>.py có OUTDIR khác (vd parabol -> narration_cloned).
    Trả Path (có thể chưa tồn tại) — caller tự kiểm tra .exists()."""
    default = OUTPUT / f"narration_{slug}"
    if default.exists():
        return default
    # Dò OUTDIR trong clone_narration_<slug>.py nếu có
    clone = SCENES / f"clone_narration_{slug}.py"
    if clone.exists():
        try:
            src = clone.read_text(encoding="utf-8")
            m = re.search(r'OUTDIR\s*=\s*os\.path\.join\([^)]*?["\']([^"\']+)["\']\s*\)', src)
            if m:
                cand = OUTPUT / m.group(1)
                if cand.exists():
                    return cand
        except Exception:
            pass
    # parabol fallback: clone script vắng mặt nhưng giọng nằm ở narration_cloned
    if slug == "parabol":
        cand = OUTPUT / "narration_cloned"
        if cand.exists():
            return cand
    return default


def _parse_segments_ast(path: Path) -> dict[str, str]:
    """Trích SEGMENTS = {...} từ file .py bằng AST (KHÔNG exec code).
    Hỗ trợ giá trị là literal string, implicit string concatenation, và
    parenthesised concatenation. Trả {} nếu không tìm thấy."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if "SEGMENTS" in names and isinstance(node.value, ast.Dict):
                out: dict[str, str] = {}
                for k, v in zip(node.value.keys, node.value.values):
                    if not isinstance(k, ast.Constant) or not isinstance(k.value, str):
                        continue
                    try:
                        val = ast.literal_eval(v)
                    except Exception:
                        val = None
                    if isinstance(val, str):
                        out[k.value] = val
                return out
    return {}


def _wav_duration(path: Path) -> float | None:
    """Độ dài .wav (giây). Dùng module wave của stdlib — KHÔNG gọi subprocess."""
    try:
        import wave
        with wave.open(str(path), "rb") as w:
            fr = w.getframerate()
            return round(w.getnframes() / fr, 2) if fr else None
    except Exception:
        return None


def _ffprobe_meta(path: Path) -> dict:
    """res ('WxH'), fps (float), size (bytes), mtime. Bền: trả None khi thiếu."""
    meta = {"res": None, "fps": None, "size": None, "mtime": None}
    try:
        meta["size"] = path.stat().st_size
        meta["mtime"] = path.stat().st_mtime
    except Exception:
        pass
    if not FFPROBE or not Path(FFPROBE).exists():
        return meta
    try:
        out = subprocess.run(
            [FFPROBE, "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=width,height,r_frame_rate",
             "-of", "json", str(path)],
            capture_output=True, text=True, timeout=20,
        )
        data = json.loads(out.stdout or "{}")
        streams = data.get("streams") or []
        if streams:
            s = streams[0]
            w, h = s.get("width"), s.get("height")
            if w and h:
                meta["res"] = f"{w}x{h}"
            rfr = s.get("r_frame_rate") or "0/1"
            try:
                num, den = rfr.split("/")
                meta["fps"] = round(float(num) / float(den), 2) if float(den) else None
            except Exception:
                pass
    except Exception:
        pass
    return meta


# ===================================================================
#  TRẠNG THÁI / LIỆT KÊ (nhanh, KHÔNG subprocess nặng)
# ===================================================================
def list_videos() -> list[dict]:
    """Dò scenes/*_video.py + narration_texts_*.py / narration_*.py để ra danh sách slug.
    Trả [{slug, title, scene_class, n_segments, status}] (status = get_status(slug))."""
    slugs: set[str] = set()
    # Slug từ scene files
    for p in SCENES.glob("*_video.py"):
        name = p.stem  # '<slug>_video'
        if name.endswith("_video"):
            slug = name[: -len("_video")]
            # Bỏ biến thể như parabol_video_v2 (slug = 'parabol_v2' không thật)
            if slug and not slug.endswith("_v2"):
                slugs.add(slug)
    # Slug từ narration files
    for p in SCENES.glob("narration_texts_*.py"):
        slugs.add(p.stem[len("narration_texts_"):])
    for p in SCENES.glob("narration_*.py"):
        s = p.stem[len("narration_"):]
        # narration_texts.py -> 'texts' (mẫu chung, bỏ); chỉ giữ nếu có scene tương ứng
        if s and not s.startswith("texts") and (_scene_path(s) or s in SCENE_CLASS):
            slugs.add(s)
    # Luôn đảm bảo các slug đã biết trong mapping cứng
    slugs.update(SCENE_CLASS.keys())

    out = []
    for slug in sorted(slugs):
        st = get_status(slug)
        out.append({
            "slug": slug,
            "title": TITLES.get(slug, slug),
            "scene_class": _scene_class(slug),
            "n_segments": st["n_segments"],
            "status": st,
        })
    return out


def get_status(slug: str) -> dict:
    """Trả trạng thái đầy đủ 1 video (xem GUI_DESIGN.md §5.1)."""
    npath = _narration_path(slug)
    segs = _parse_segments_ast(npath) if npath else {}
    n_seg = len(segs)

    ndir = _narration_dir(slug)
    wavs = sorted(ndir.glob("*.wav")) if ndir.exists() else []
    words = sorted(ndir.glob("*.words.json")) if ndir.exists() else []

    sp = _scene_path(slug)
    cls = _scene_class(slug)

    # MP4 mới nhất: ưu tiên preview/, rồi media/videos/<slug>_video/
    mp4_candidates = []
    if PREVIEW.exists():
        mp4_candidates += list(PREVIEW.glob("*.mp4"))
    mdir = MEDIA / f"{slug}_video"
    if mdir.exists():
        mp4_candidates += [p for p in mdir.rglob("*.mp4") if "partial" not in str(p)]
    # Lọc preview theo gợi ý slug (preview/ trộn nhiều video)
    hint = _slug_hints(slug)
    slug_mp4 = [p for p in mp4_candidates if (
        p.parent.name == f"{slug}_video" or _matches_hint(p.name, hint))]
    hd = None
    last_render = 0.0
    if slug_mp4:
        newest = max(slug_mp4, key=lambda p: p.stat().st_mtime)
        hd = str(newest)
        last_render = newest.stat().st_mtime

    return {
        "has_thoai": npath is not None,
        "has_scene": sp is not None and cls is not None,
        "n_segments": n_seg,
        "voice_done": len(wavs),
        "karaoke": len(words),
        "hd_mp4": hd,
        "last_render": last_render,
    }


def _slug_hints(slug: str) -> list[str]:
    """Các chuỗi gợi ý để khớp tên file MP4 trong preview/ (trộn nhiều video).
    Dựa trên title + slug; viết hoa để khớp tên file như L1_PHANH_..."""
    hints = {slug, slug.upper()}
    title = TITLES.get(slug, "")
    # Lấy mã (L1, T5, ...) và từ khóa nổi bật trong title
    for tok in re.findall(r"[A-Za-zÀ-ỹ0-9]+", title):
        if len(tok) >= 2:
            hints.add(tok.upper())
    # Heuristic riêng cho từng slug (tên file thực tế trong preview/)
    extra = {
        "phanh": ["PHANH", "L1"], "xetnghiem": ["XETNGHIEM", "T5"],
        "laikep": ["LAIKEP", "TAP1"], "troixanh": ["TROIXANH", "L7"],
        "parabol": ["PARABOL"],
    }
    hints.update(extra.get(slug, []))
    return [h for h in hints if h]


def _matches_hint(filename: str, hints: list[str]) -> bool:
    up = filename.upper()
    return any(h.upper() in up for h in hints)


def list_segments(slug: str) -> list[dict]:
    """Đọc SEGMENTS từ file lời thoại (AST — KHÔNG chạy code nặng).
    Trả [{id, text, wav_path|None, wav_dur|None}] theo đúng thứ tự khai báo."""
    npath = _narration_path(slug)
    segs = _parse_segments_ast(npath) if npath else {}
    ndir = _narration_dir(slug)
    out = []
    for sid, text in segs.items():
        wav = ndir / f"{sid}.wav"
        if wav.exists():
            out.append({"id": sid, "text": text,
                        "wav_path": str(wav), "wav_dur": _wav_duration(wav)})
        else:
            out.append({"id": sid, "text": text, "wav_path": None, "wav_dur": None})
    return out


def list_outputs(slug: str) -> list[dict]:
    """MP4 liên quan slug: preview/ (khớp gợi ý) + output/*.mp4 (khớp gợi ý) +
    media/videos/<slug>_video/*.mp4. Trả [{path, res, fps, size, mtime}]."""
    hint = _slug_hints(slug)
    found: dict[str, Path] = {}

    def _add(p: Path):
        found[str(p.resolve())] = p

    if PREVIEW.exists():
        for p in PREVIEW.glob("*.mp4"):
            if _matches_hint(p.name, hint):
                _add(p)
    for p in OUTPUT.glob("*.mp4"):
        if _matches_hint(p.name, hint):
            _add(p)
    mdir = MEDIA / f"{slug}_video"
    if mdir.exists():
        for p in mdir.rglob("*.mp4"):
            if "partial" not in str(p):
                _add(p)

    out = []
    for p in found.values():
        meta = _ffprobe_meta(p)
        out.append({"path": str(p), "res": meta["res"], "fps": meta["fps"],
                    "size": meta["size"], "mtime": meta["mtime"]})
    out.sort(key=lambda d: d["mtime"] or 0, reverse=True)
    return out


# ===================================================================
#  ĐỌC / GHI LỜI THOẠI (AN TOÀN, KHÔNG chạy code)
# ===================================================================
def read_narration(slug: str) -> dict[str, str]:
    """Trả {id: text}. Parse bằng AST — không exec/import module nặng."""
    npath = _narration_path(slug)
    if not npath:
        return {}
    return _parse_segments_ast(npath)


def _render_segments_block(segments: dict[str, str]) -> str:
    """Sinh khối 'SEGMENTS = { ... }' chuẩn (mỗi value 1 chuỗi, escape an toàn)."""
    lines = ["SEGMENTS = {"]
    for sid, text in segments.items():
        lines.append(f"    {json.dumps(sid, ensure_ascii=False)}: "
                     f"{_py_str(text)},")
    lines.append("}")
    return "\n".join(lines)


def _py_str(s: str) -> str:
    """Chuỗi Python an toàn (giữ Unicode tiếng Việt, escape \\ \" \\n)."""
    body = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return f'"{body}"'


def _atomic_write(path: Path, content: str) -> None:
    """Ghi atomically: tmp cùng thư mục + os.replace (đổi tên nguyên tử)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def write_narration(slug: str, segments: dict[str, str]) -> None:
    """Ghi lại file lời thoại, GIỮ NGUYÊN header/docstring + mọi dòng ngoài khối
    SEGMENTS = {...}; chỉ thay khối SEGMENTS. Validate: mỗi text >= 1 từ.
    Nếu file chưa có -> tạo mới (qua scaffold_video). Ghi atomically."""
    if not segments:
        raise ValueError("Lời thoại rỗng — cần ít nhất 1 đoạn.")
    for sid, text in segments.items():
        if not isinstance(text, str) or len(text.split()) < 1:
            raise ValueError(f"Đoạn '{sid}' rỗng — mỗi đoạn phải có ít nhất 1 từ.")

    npath = _narration_path(slug)
    if npath is None:
        # Chưa có file -> dùng quy ước chuẩn, sinh skeleton có docstring tối thiểu
        npath = SCENES / f"narration_texts_{slug}.py"
        header = (f'"""\nLời thoại — {TITLES.get(slug, slug)} (slug: {slug}).\n'
                  f'NGUỒN DUY NHẤT cho sinh giọng clone + karaoke.\n"""\n\n')
        new_content = header + _render_segments_block(segments) + "\n"
        # Validate AST trước khi ghi
        _validate_py(new_content)
        _atomic_write(npath, new_content)
        return

    original = npath.read_text(encoding="utf-8")
    new_block = _render_segments_block(segments)
    new_content = _replace_segments_block(original, new_block)
    _validate_py(new_content)  # đảm bảo file vẫn parse được trước khi thay
    _atomic_write(npath, new_content)


def _validate_py(content: str) -> None:
    """Đảm bảo nội dung là Python hợp lệ trước khi ghi (chống làm hỏng file)."""
    try:
        ast.parse(content)
    except SyntaxError as e:
        raise ValueError(f"Nội dung sinh ra không hợp lệ Python: {e}") from e


def _replace_segments_block(original: str, new_block: str) -> str:
    """Thay đúng câu lệnh 'SEGMENTS = {...}' trong source, giữ nguyên phần còn lại.
    Dùng AST để xác định khoảng dòng của assignment SEGMENTS."""
    tree = ast.parse(original)
    target = None
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(t, ast.Name) and t.id == "SEGMENTS" for t in node.targets):
                target = node
                break
    if target is None:
        # Không có khối -> nối thêm vào cuối
        sep = "" if original.endswith("\n") else "\n"
        return original + sep + "\n" + new_block + "\n"

    lines = original.splitlines(keepends=True)
    start = target.lineno - 1                  # 0-based, dòng bắt đầu 'SEGMENTS'
    end = (target.end_lineno or target.lineno)  # 1-based, dòng cuối (gồm '}')
    before = "".join(lines[:start])
    after = "".join(lines[end:])
    # Đảm bảo new_block kết thúc bằng newline để nối liền 'after'
    rep = new_block if new_block.endswith("\n") else new_block + "\n"
    return before + rep + after


def apply_tts_convention(text: str) -> str:
    """Chuẩn hoá cách đọc cho TTS:
       * 'x' (biến/ký hiệu) -> 'ích'   (chỉ khi đứng tách, không phải trong từ)
       * chuẩn hoá khoảng trắng thừa
       * thêm dấu kết câu ('.') nếu câu chưa có dấu kết.
    Trả text mới (không phá vỡ Unicode tiếng Việt)."""
    if not text:
        return text
    t = text
    # 'x' đứng riêng (biến toán) -> 'ích'. \b không bắt tốt với Unicode VN nên dùng lookaround.
    t = re.sub(r"(?<![A-Za-zÀ-ỹ0-9])x(?![A-Za-zÀ-ỹ0-9])", "ích", t)
    # Gom khoảng trắng
    t = re.sub(r"[ \t]+", " ", t).strip()
    # Thêm dấu kết câu nếu thiếu
    if t and t[-1] not in ".?!…":
        t += "."
    return t


# ===================================================================
#  HẠ TẦNG SUBPROCESS (dùng chung bởi 3 hàm run_*)
# ===================================================================
class _Handle:
    """Handle để hủy tiến trình nền (nút ■ Dừng)."""
    def __init__(self):
        self.proc: subprocess.Popen | None = None

    def terminate(self):
        p = self.proc
        if p and p.poll() is None:
            try:
                p.terminate()
            except Exception:
                pass

    def kill(self):
        p = self.proc
        if p and p.poll() is None:
            try:
                p.kill()
            except Exception:
                pass

    @property
    def returncode(self):
        return self.proc.returncode if self.proc else None


def _stream(cmd: list[str], env=None, cwd=ROOT):
    """Chạy cmd, YIELD từng dòng stdout (gộp stderr). Chống 'đơ' do buffering:
       PYTHONUNBUFFERED=1 + bufsize=1.
    Trả về (generator, handle). handle.terminate()/kill() để hủy.

    Dùng:
        gen, h = _stream([...])
        for line in gen: ...    # h.proc đã sẵn sàng để h.terminate()
    """
    handle = _Handle()
    full_env = {**os.environ, "PYTHONUNBUFFERED": "1", **(env or {})}

    def _gen():
        p = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, bufsize=1, env=full_env, cwd=str(cwd),
        )
        handle.proc = p
        try:
            for line in iter(p.stdout.readline, ""):
                yield line.rstrip("\n")
        finally:
            if p.stdout:
                p.stdout.close()
            p.wait()

    return _gen(), handle


# ===================================================================
#  TÁC VỤ CHẠY LÂU (trả về generator log) — KHÔNG chạy trong test
# ===================================================================
def run_voice(slug: str, force=True, env_overrides=None):
    """Sinh giọng clone: VOXCPM scenes/clone_narration_<slug>.py
    Báo xong khi gặp 'ALL_CLONED_DONE'. Tiến trình = (số dòng 'OK <id>:') / n_segments.
    Trả về (generator, handle). force chỉ để hợp ngữ nghĩa (script tự ghi đè .wav)."""
    clone = SCENES / f"clone_narration_{slug}.py"
    if not clone.exists():
        raise FileNotFoundError(
            f"Thiếu scenes/clone_narration_{slug}.py — slug '{slug}' chưa có script sinh giọng "
            f"(vd 'parabol' chưa hỗ trợ clone)."
        )
    if not VOXCPM.exists():
        raise FileNotFoundError(f"Thiếu trình thông dịch VoxCPM: {VOXCPM}")
    env = {"FORCE_VOICE": "1" if force else "0", **(env_overrides or {})}
    cmd = [str(VOXCPM), f"scenes/clone_narration_{slug}.py"]
    return _stream(cmd, env=env)


def run_align(slug: str, whisper_model="small"):
    """Căn chỉnh karaoke: VENV/python scenes/align_narration.py output/narration_<slug>
    env WHISPER_MODEL=<model>. Chỉ gọi khi KARAOKE_ON=True. Xong khi gặp 'ALIGN_DONE'.
    Trả về (generator, handle)."""
    ndir = _narration_dir(slug)
    py = VENV / "python"
    cmd = [str(py), "scenes/align_narration.py", str(ndir)]
    env = {"WHISPER_MODEL": whisper_model}
    return _stream(cmd, env=env)


def run_render(slug, quality="hd", res="1080,1920", fps=60, align=False):
    """Gọi render_pipeline.sh để TẬN DỤNG hợp đồng env sẵn có:
       cmd = ['bash','render_pipeline.sh', slug, <SceneClass>, res, str(fps)]
       env: FORCE_VOICE=0 (giọng đã có), ALIGN='1' nếu align, VOXCPM/VENV.
       quality 'preview' => res='540,960', fps=12.
    Tiến trình parse 'frame N/M' của manim; kết thúc đọc '==> XONG: <mp4>'.
    Trả về (generator, handle)."""
    scene = _scene_class(slug) or SCENE_CLASS.get(slug)
    if not scene:
        raise ValueError(f"Không xác định được SceneClass cho slug '{slug}'.")
    if quality == "preview":
        res, fps = "540,960", 12
    cmd = ["bash", "render_pipeline.sh", slug, scene, res, str(fps)]
    env = {
        "FORCE_VOICE": "0",
        "ALIGN": "1" if align else "0",
        "VOXCPM": str(VOXCPM),
        "VENV": str(VENV),
    }
    return _stream(cmd, env=env)


# ===================================================================
#  CÀI ĐẶT / IDE
# ===================================================================
# Regex theo dòng đã biết (GUI_DESIGN.md §5.1). Dùng pattern thay vì số dòng cứng
# vì các file clone_narration_*.py có số dòng lệch nhau.
_BRAND_KEYS = ["FONT", "KARAOKE_ON", "SZ_HERO", "SZ_TITLE", "SZ_BODY",
               "SZ_LABEL", "SZ_SMALL", "CW"]
_CLONE_KEYS = ["INFERENCE_TIMESTEPS", "CFG_VALUE", "LOAD_DENOISER"]


def _read_assignments(src: str, keys: list[str]) -> dict:
    """Đọc giá trị literal của các biến gán top-level bằng regex theo dòng.
    Chỉ khớp dòng dạng 'KEY = <giá trị>' (đầu dòng, không thụt)."""
    out = {}
    for key in keys:
        m = re.search(rf"(?m)^{re.escape(key)}\s*=\s*([^\n#]+?)\s*(?:#.*)?$", src)
        if m:
            raw = m.group(1).strip()
            out[key] = _coerce(raw)
    return out


def _coerce(raw: str):
    """Chuyển literal text -> giá trị Python (an toàn qua literal_eval)."""
    try:
        return ast.literal_eval(raw)
    except Exception:
        return raw


def read_settings() -> dict:
    """Đọc brand.py (KARAOKE_ON, FONT, SZ_*, CW) + clone_narration_<slug>.py
    (INFERENCE_TIMESTEPS, CFG_VALUE, LOAD_DENOISER) + gui_state.json.
    Trả {brand:{...}, clone:{<slug>:{...}}, whisper_model, gui_state:{...}}."""
    result: dict = {"brand": {}, "clone": {}, "whisper_model": "small", "gui_state": {}}

    if BRAND_PY.exists():
        result["brand"] = _read_assignments(BRAND_PY.read_text(encoding="utf-8"), _BRAND_KEYS)

    for cp in SCENES.glob("clone_narration_*.py"):
        slug = cp.stem[len("clone_narration_"):]
        if not slug:
            continue
        vals = _read_assignments(cp.read_text(encoding="utf-8"), _CLONE_KEYS)
        if vals:
            result["clone"][slug] = vals

    # WHISPER_MODEL: mặc định trong align_narration.py
    if ALIGN_PY.exists():
        m = re.search(r'WHISPER_MODEL"\s*,\s*"([^"]+)"', ALIGN_PY.read_text(encoding="utf-8"))
        if m:
            result["whisper_model"] = m.group(1)

    if GUI_STATE.exists():
        try:
            result["gui_state"] = json.loads(GUI_STATE.read_text(encoding="utf-8"))
        except Exception:
            result["gui_state"] = {}

    return result


def write_settings(d: dict) -> None:
    """Ghi lại đúng dòng setting trong brand.py / clone_narration_<slug>.py (regex theo dòng).
    Ghi atomically, giữ nguyên mọi dòng khác. gui_state lưu vào gui_state.json.

    d = {
      'brand':   {'KARAOKE_ON': True, 'FONT': 'Arial', ...},   # tuỳ chọn
      'clone':   {'<slug>': {'INFERENCE_TIMESTEPS': 16, ...}},  # tuỳ chọn
      'gui_state': {...},   # lưu thẳng vào gui_state.json
    }
    """
    # --- brand.py ---
    brand = d.get("brand") or {}
    if brand and BRAND_PY.exists():
        src = BRAND_PY.read_text(encoding="utf-8")
        for key, val in brand.items():
            if key not in _BRAND_KEYS:
                continue
            src = _set_assignment(src, key, val)
        _validate_py(src)
        _atomic_write(BRAND_PY, src)

    # --- clone_narration_<slug>.py ---
    clone = d.get("clone") or {}
    for slug, vals in clone.items():
        cp = SCENES / f"clone_narration_{slug}.py"
        if not cp.exists():
            continue
        src = cp.read_text(encoding="utf-8")
        changed = False
        for key, val in vals.items():
            if key not in _CLONE_KEYS:
                continue
            new = _set_assignment(src, key, val)
            if new != src:
                src, changed = new, True
        if changed:
            _validate_py(src)
            _atomic_write(cp, src)

    # --- gui_state.json ---
    if "gui_state" in d:
        merged = {}
        if GUI_STATE.exists():
            try:
                merged = json.loads(GUI_STATE.read_text(encoding="utf-8"))
            except Exception:
                merged = {}
        merged.update(d["gui_state"] or {})
        _atomic_write(GUI_STATE, json.dumps(merged, ensure_ascii=False, indent=2) + "\n")


def _set_assignment(src: str, key: str, value) -> str:
    """Thay 'KEY = ...' (top-level, không thụt) bằng 'KEY = <repr>', GIỮ comment đuôi dòng.
    Nếu không tìm thấy dòng -> trả nguyên src (không tự thêm, tránh phá file)."""
    literal = repr(value)

    def _sub(m):
        comment = m.group("comment") or ""
        pad = "  " if comment else ""
        return f"{key} = {literal}{pad}{comment}"

    pattern = rf"(?m)^{re.escape(key)}\s*=\s*[^\n#]*?(?P<comment>#.*)?$"
    new, n = re.subn(pattern, _sub, src, count=1)
    return new if n else src


# ===================================================================
#  KHO Ý TƯỞNG
# ===================================================================
def read_ideas() -> list[dict]:
    """Parse noidung/kho_y_tuong.md -> [{code, title, group, tags, details, done, slug}].
    group ∈ {'TOÁN','LÝ'}; done=True nếu có '✅ ĐÃ LÀM' trên dòng tiêu đề; tag từ 🎯/🎨/⚠️."""
    if not IDEAS_MD.exists():
        return []
    text = IDEAS_MD.read_text(encoding="utf-8")
    lines = text.splitlines()
    ideas: list[dict] = []
    group = None
    cur = None

    # Map mã ý tưởng -> slug đã làm (theo title/codebase đã biết)
    code_to_slug = {"T1": "laikep", "T5": "xetnghiem", "L1": "phanh", "L7": "troixanh"}

    for ln in lines:
        s = ln.strip()
        # Nhóm: '## 📐 TOÁN' / '## ⚛️ VẬT LÝ'
        if s.startswith("## "):
            label = s[3:]
            if "TOÁN" in label:
                group = "TOÁN"
            elif "LÝ" in label or "VẬT" in label:
                group = "LÝ"
            else:
                group = None
            continue
        # Thẻ ý tưởng: '### T2. Hàm mũ — "..."'
        m = re.match(r"^###\s+([TL]\d+)\.\s*(.+)$", s)
        if m:
            if cur:
                ideas.append(cur)
            code = m.group(1)
            rest = m.group(2)
            done = "ĐÃ LÀM" in rest or "✅" in rest
            title = re.sub(r"✅\s*ĐÃ LÀM.*$", "", rest).strip()
            cur = {
                "code": code, "title": title, "group": group,
                "tags": [], "details": [], "done": done,
                "slug": code_to_slug.get(code),
            }
            continue
        if cur is None:
            continue
        # Tag dòng có 🎯/🎨/⚠️
        if any(e in ln for e in ("🎯", "🎨", "⚠️")):
            for e in ("🎯", "🎨", "⚠️"):
                if e in ln and e not in cur["tags"]:
                    cur["tags"].append(e)
        if s.startswith("- ") or s.startswith("**"):
            cur["details"].append(s)

    if cur:
        ideas.append(cur)

    # Đối chiếu slug đã có trong thư viện -> đánh dấu done
    existing = {v["slug"] for v in list_videos()}
    for it in ideas:
        if it["slug"] and it["slug"] in existing:
            it["done"] = True
    return ideas


# ===================================================================
#  TẠO VIDEO MỚI
# ===================================================================
def scaffold_video(slug: str, title: str, segments: dict[str, str]) -> None:
    """Tạo scenes/narration_texts_<slug>.py + thư mục output/narration_<slug>/.
    KHÔNG viết scene Manim (phần đó cần Claude). Ghi atomically, validate trước."""
    if not re.fullmatch(r"[a-z0-9_]+", slug or ""):
        raise ValueError("slug chỉ gồm chữ thường, số, gạch dưới (vd 'tenlua').")
    npath = SCENES / f"narration_texts_{slug}.py"
    if npath.exists():
        raise FileExistsError(f"Đã tồn tại {npath.name} — chọn slug khác hoặc sửa trực tiếp.")
    if not segments:
        # Tạo skeleton 1 đoạn rỗng tối thiểu để người dùng điền sau
        segments = {"01_hook": "Viết lời thoại đoạn mở đầu ở đây."}
    for sid, t in segments.items():
        if not isinstance(t, str) or len(t.split()) < 1:
            raise ValueError(f"Đoạn '{sid}' rỗng — mỗi đoạn cần ≥ 1 từ.")

    header = (
        f'"""\n'
        f'Lời thoại — {title or slug} (slug: {slug}).\n'
        f'NGUỒN DUY NHẤT cho: sinh giọng clone (clone_narration_{slug}.py) + karaoke.\n'
        f'Quy ước TTS: số/công thức viết theo CÁCH ĐỌC; mỗi câu kết . ? ! để chia cụm.\n'
        f'"""\n\n'
    )
    content = header + _render_segments_block(segments) + "\n"
    _validate_py(content)
    _atomic_write(npath, content)
    # Thư mục giọng
    (OUTPUT / f"narration_{slug}").mkdir(parents=True, exist_ok=True)


def claude_prompt(slug: str, title: str, segments) -> str:
    """Sinh prompt dán cho Claude Code để viết scenes/<slug>_video.py.
    segments: dict {id:text} hoặc list[{id,text}]. Trả chuỗi prompt."""
    if isinstance(segments, dict):
        items = list(segments.items())
    else:
        items = [(s.get("id"), s.get("text", "")) for s in (segments or [])]
    cls = _scene_class(slug) or SCENE_CLASS.get(slug) or f"{slug.capitalize()}Video"
    seg_lines = "\n".join(f'  - {sid}: {text}' for sid, text in items)
    return (
        f'Hãy viết file Manim `scenes/{slug}_video.py` cho kênh "TOÁN LÝ ĐỜI THỰC".\n\n'
        f'Bối cảnh: video dọc 9:16 (1080×1920), kế thừa `BrandScene` từ `scenes/brand.py` '
        f'(đã có intro con vẹt, khung template, phụ đề karaoke khớp giọng, outro).\n'
        f'Tên class: `{cls}`. Chủ đề: {title or slug}.\n\n'
        f'Lời thoại đã chốt (trong `scenes/narration_texts_{slug}.py`, biến SEGMENTS), '
        f'mỗi đoạn là 1 beat hình:\n{seg_lines}\n\n'
        f'Yêu cầu:\n'
        f'  - Mỗi segment id ở trên = 1 beat; đồng bộ animation với độ dài giọng đọc '
        f'(file output/narration_{slug}/<id>.wav).\n'
        f'  - Dùng hằng số cỡ chữ/màu trong brand.py (SZ_*, ACCENT, GROW, ...); bố cục XẾP DỌC.\n'
        f'  - Không tự sinh lời thoại mới; lấy text từ SEGMENTS.\n'
        f'  - Sau khi viết xong, render bằng: '
        f'`bash render_pipeline.sh {slug} {cls}`.\n'
    )


def open_in_finder(path: str) -> None:
    """Mở file/thư mục trong Finder (macOS)."""
    subprocess.run(["open", str(path)], check=False)


# ===================================================================
#  CLI tự kiểm thử nhanh (không chạy render/sinh giọng thật)
# ===================================================================
if __name__ == "__main__":
    import sys
    out = {"videos": list_videos()}
    for slug in ("phanh", "xetnghiem", "laikep", "troixanh", "parabol"):
        out[slug] = {
            "status": get_status(slug),
            "n_segments": len(list_segments(slug)),
            "narration_keys": list(read_narration(slug).keys()),
            "outputs": len(list_outputs(slug)),
        }
    out["ideas_count"] = len(read_ideas())
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2, default=str)
    print()
