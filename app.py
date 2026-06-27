"""
app.py — GUI Streamlit cho XƯỞNG SẢN XUẤT VIDEO "TOÁN LÝ ĐỜI THỰC".

Theo GUI_DESIGN.md:
  * §3  — danh sách tính năng theo khu (A..G + sidebar).
  * §4  — bố cục/ASCII mockup (sidebar + 2 cột chính ở trang biên tập).
  * §5.2 — app.py CHỈ vẽ UI + gọi app_backend; KHÔNG chứa logic pipeline.
  * §6  — tác vụ chạy lâu: thread nền + queue + session_state + rerun;
          khoá nút khi đang chạy; parse % theo bảng tín hiệu.

KHÔNG import voxcpm/manim ở đây (§9.3). Mọi việc nặng gọi qua app_backend.
"""
import os
import re
import queue
import threading
import time
from pathlib import Path

import streamlit as st

import app_backend as B

# ===================================================================
#  CẤU HÌNH TRANG
# ===================================================================
st.set_page_config(
    page_title="TOÁN LÝ ĐỜI THỰC — Xưởng video",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---- session_state mặc định ----------------------------------------------
_DEFAULTS = {
    "page": "home",        # home | library | editor | ideas | new | settings
    "slug": None,          # slug đang biên tập
    "running": False,      # có job nền không
    "job": None,           # tên việc đang chạy (sinh giọng / preview / hd / align)
    "job_slug": None,      # slug của job đang chạy
    "q": None,             # queue.Queue truyền log từ thread nền
    "log": [],             # buffer dòng log
    "thread": None,        # threading.Thread
    "handle": None,        # B._Handle (để ■ Dừng)
    "n_segments": 0,       # tổng đoạn (tính %)
    "done_mp4": None,      # mp4 kết quả khi xong
}
for _k, _v in _DEFAULTS.items():
    st.session_state.setdefault(_k, _v)


# ===================================================================
#  TIỆN ÍCH ĐIỀU HƯỚNG
# ===================================================================
def goto(page: str, slug: str | None = None):
    st.session_state.page = page
    if slug is not None:
        st.session_state.slug = slug
    st.rerun()


def _fmt_size(n) -> str:
    if not n:
        return "—"
    n = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f}{unit}" if unit == "B" else f"{n:.1f}{unit}"
        n /= 1024
    return f"{n:.1f}GB"


def _fmt_dur(sec) -> str:
    if not sec:
        return "0:00"
    sec = int(round(float(sec)))
    return f"{sec // 60}:{sec % 60:02d}"


def _fmt_mtime(ts) -> str:
    if not ts:
        return "—"
    return time.strftime("%d/%m %H:%M", time.localtime(float(ts)))


def _dir_size_gb(path: Path) -> str:
    try:
        total = 0
        for p in path.rglob("*"):
            if p.is_file():
                try:
                    total += p.stat().st_size
                except OSError:
                    pass
        return f"{total / (1024 ** 3):.1f}GB"
    except Exception:
        return "—"


# ===================================================================
#  HẠ TẦNG JOB NỀN (§6: thread + queue + session_state + rerun)
# ===================================================================
def _worker(gen, q: queue.Queue):
    """Đọc generator log trong thread nền, đẩy vào queue."""
    try:
        for line in gen:
            q.put(("log", line))
        q.put(("done", 0))
    except Exception as e:  # noqa: BLE001
        q.put(("error", str(e)))


def start_job(job_name: str, slug: str, gen, handle, n_segments: int):
    """Khởi động 1 job nền. Khoá UI bằng running=True."""
    q: queue.Queue = queue.Queue()
    t = threading.Thread(target=_worker, args=(gen, q), daemon=True)
    t.start()
    st.session_state.update(
        running=True, job=job_name, job_slug=slug,
        q=q, log=[], thread=t, handle=handle,
        n_segments=n_segments, done_mp4=None,
    )


def drain_queue():
    """Mỗi rerun: rút hết log trong queue vào buffer, cập nhật trạng thái."""
    q = st.session_state.q
    if q is None:
        return
    while not q.empty():
        kind, payload = q.get()
        if kind == "log":
            st.session_state.log.append(payload)
        elif kind == "done":
            st.session_state.running = False
        elif kind == "error":
            st.session_state.log.append("LỖI: " + str(payload))
            st.session_state.running = False
    # Giữ ~400 dòng cuối
    if len(st.session_state.log) > 400:
        st.session_state.log = st.session_state.log[-400:]


def stop_job():
    """Nút ■ Dừng — terminate (rồi kill) tiến trình nền (§6, §9.4)."""
    h = st.session_state.handle
    if h is not None:
        try:
            h.terminate()
            time.sleep(0.4)
            h.kill()
        except Exception:  # noqa: BLE001
            pass
    st.session_state.running = False
    st.session_state.log.append("■ Đã dừng theo yêu cầu.")


# ---- PARSE TIẾN TRÌNH (§6 bảng tín hiệu) ----------------------------------
_RE_OK = re.compile(r"^\s*OK\s+\S+\s*:")                 # sinh giọng: 'OK <id>:'
_RE_ALIGN_OK = re.compile(r"✓\s*\S+\.wav")               # align: '✓ <seg>.wav'
_RE_FRAME = re.compile(r"frame\s+(\d+)\s*/\s*(\d+)", re.I)  # render: 'frame N/M'
# Manim không in 'frame N/M' mà dùng thanh tqdm dạng 'Animation k: NN%|...| cur/total'.
# Bắt cả % (đáng tin nhất) lẫn cur/total để thanh tiến trình bước 3 chạy mượt.
_RE_TQDM_PCT = re.compile(r"(\d{1,3})%\|")               # render: tqdm 'NN%|'
_RE_TQDM_FRAC = re.compile(r"\|\s*(\d+)\s*/\s*(\d+)")    # render: tqdm '| cur/total'
_RE_STAGE = re.compile(r"\[\s*([123])\s*/\s*3\s*\]")     # render: '[k/3]'
_RE_DONE_MP4 = re.compile(r"==>\s*XONG\s*:\s*(.+\.mp4)") # render xong
_RE_CLONED = re.compile(r"ALL_CLONED_DONE")             # sinh giọng xong
_RE_ALIGN_DONE = re.compile(r"ALIGN_DONE")              # align xong


def parse_progress(log: list[str], job: str, n_seg: int) -> tuple[float, str]:
    """Trả (pct 0..1, nhãn bước) theo loại job + bảng tín hiệu §6."""
    text = "\n".join(log)
    if job == "voice":
        if _RE_CLONED.search(text):
            return 1.0, "Sinh giọng — hoàn tất"
        n = sum(1 for ln in log if _RE_OK.match(ln))
        pct = min(n / n_seg, 0.99) if n_seg else 0.0
        return pct, f"Sinh giọng — {n}/{n_seg} đoạn"
    if job == "align":
        if _RE_ALIGN_DONE.search(text):
            return 1.0, "Karaoke — hoàn tất"
        n = sum(1 for ln in log if _RE_ALIGN_OK.search(ln))
        pct = min(n / n_seg, 0.99) if n_seg else 0.0
        return pct, f"Căn chỉnh karaoke — {n}/{n_seg} đoạn"
    # render (preview / hd)
    if _RE_DONE_MP4.search(text):
        return 1.0, "Render — hoàn tất"
    # stage hiện tại
    stage = 0
    for ln in log:
        m = _RE_STAGE.search(ln)
        if m:
            stage = int(m.group(1))
    # Tiến trình render Manim: ưu tiên 'frame N/M'; nếu không có, lấy thanh tqdm
    # ('NN%|...| cur/total') vì Manim CE dùng tqdm chứ không in chữ 'frame'.
    cur = total = 0
    frame_pct = 0.0
    for ln in log:
        m = _RE_FRAME.search(ln)
        if m:
            cur, total = int(m.group(1)), int(m.group(2))
            frame_pct = (cur / total) if total else 0.0
            continue
        mf = _RE_TQDM_FRAC.search(ln)
        if mf:
            cur, total = int(mf.group(1)), int(mf.group(2))
            frame_pct = (cur / total) if total else 0.0
        mp = _RE_TQDM_PCT.search(ln)
        if mp:
            frame_pct = min(int(mp.group(1)) / 100.0, 1.0)
    if stage:
        # 3 bước; bước 3 là render frame nên đo theo frame
        base = (stage - 1) / 3.0
        span = 1.0 / 3.0
        pct = base + span * (frame_pct if stage == 3 else 0.5)
        if stage == 3 and total:
            tail = f"Render frame {cur}/{total}"
        elif stage == 3 and frame_pct:
            tail = f"Render Manim {int(frame_pct * 100)}%"
        else:
            tail = {1: "Chuẩn bị giọng", 2: "Căn chỉnh", 3: "Render Manim"}.get(stage, "")
        return min(pct, 0.99), f"[{stage}/3] " + tail
    if total:
        return min(frame_pct, 0.99), f"Render frame {cur}/{total}"
    if frame_pct:
        return min(frame_pct, 0.99), f"Render Manim {int(frame_pct * 100)}%"
    return 0.02, "Đang khởi động…"


def find_done_mp4(log: list[str]) -> str | None:
    for ln in reversed(log):
        m = _RE_DONE_MP4.search(ln)
        if m:
            p = m.group(1).strip()
            return p if Path(p).exists() else None
    return None


# ===================================================================
#  HUY HIỆU TRẠNG THÁI (dải badge, §3 KHU B/C)
# ===================================================================
def status_badges(stt: dict) -> str:
    def b(on: bool, label: str) -> str:
        return f"✅ {label}" if on else f"◻️ {label}"

    n = stt["n_segments"]
    parts = [
        b(stt["has_thoai"], "Thoại"),
        b(stt["has_scene"], "Scene"),
        ("♪ Giọng %d/%d" % (stt["voice_done"], n)) if stt["voice_done"] >= n and n
        else ("◻️ Giọng %d/%d" % (stt["voice_done"], n)),
        b(stt["karaoke"] > 0, "Karaoke"),
        b(bool(stt["hd_mp4"]), "HD"),
    ]
    return "  ·  ".join(parts)


# ===================================================================
#  SIDEBAR (§3, §4) — logo + menu + chấm vàng + trạng thái máy
# ===================================================================
def render_sidebar():
    sb = st.sidebar
    sb.markdown("## 🎬 TOÁN LÝ\n### ĐỜI THỰC")
    sb.caption("Xưởng sản xuất video 9:16")
    sb.divider()

    running = st.session_state.running
    dot = " ●" if running else ""  # chấm vàng cạnh "Video" khi có job nền

    menu = [
        ("home", "⌂ Trang chủ"),
        ("library", f"▸ Video{dot}"),
        ("new", "＋ Tạo mới"),
        ("ideas", "⌕ Kho ý tưởng"),
        ("settings", "⚙ Cài đặt"),
    ]
    keys = [m[0] for m in menu]
    labels = [m[1] for m in menu]
    # editor là trang con của Video
    cur = st.session_state.page
    cur_key = "library" if cur == "editor" else cur
    idx = keys.index(cur_key) if cur_key in keys else 0
    choice = sb.radio("Điều hướng", labels, index=idx, label_visibility="collapsed")
    new_key = keys[labels.index(choice)]
    if new_key != cur_key:
        st.session_state.page = new_key
        st.rerun()

    sb.divider()
    # ---- Khối trạng thái máy ở chân (§3 sidebar) ----
    vox_ok = B.VOXCPM.exists()
    if running:
        machine = f"● Đang chạy: {st.session_state.job or 'job'}"
    else:
        machine = "VoxCPM: CPU · rảnh" if vox_ok else "⚠ Thiếu VoxCPM venv"
    sb.markdown("**Trạng thái máy**")
    sb.write(machine)
    sb.caption(f"output/ ≈ {_dir_size_gb(B.OUTPUT)}")
    if not B.REF_VOICE.exists():
        sb.warning("Thiếu file giọng mẫu voice-yeu_ref16k.wav")


# ===================================================================
#  KHỐI JOB NỀN DÙNG CHUNG (khung LOG TRỰC TIẾP) — §3 KHU C, §6
# ===================================================================
def render_job_panel(for_slug: str | None = None):
    """Vẽ khung LOG TRỰC TIẾP + progress + nút Dừng. Tự rerun khi đang chạy.
    Trả về True nếu vừa có job kết thúc và có MP4 mới."""
    running = st.session_state.running
    job = st.session_state.job
    job_slug = st.session_state.job_slug

    # Nếu job này không thuộc slug đang xem -> vẫn hiện nhưng ghi rõ
    drain_queue()

    st.markdown("#### 🖥 LOG TRỰC TIẾP")
    log_box = st.empty()  # khung đen cuộn (§4)
    log_text = "\n".join(st.session_state.log[-400:]) if st.session_state.log else "(chưa có log)"
    log_box.code(log_text, language="log")

    if job:
        pct, label = parse_progress(st.session_state.log, job, st.session_state.n_segments or 1)
        st.progress(pct, text=label)

    c1, c2 = st.columns(2)
    with c1:
        if st.button("📋 Sao chép log", use_container_width=True,
                     disabled=not st.session_state.log, key="copy_log"):
            st.code(log_text)
            st.toast("Đã hiển thị log để sao chép.")
    with c2:
        if st.button("■ Dừng", type="primary", use_container_width=True,
                     disabled=not running, key="stop_job"):
            stop_job()
            st.rerun()

    # Khi vừa xong: tìm MP4 kết quả
    if not running and job and job_slug == for_slug:
        mp4 = find_done_mp4(st.session_state.log)
        if mp4:
            st.session_state.done_mp4 = mp4

    # Tự làm tươi khi đang chạy (§6)
    if running:
        time.sleep(0.4)
        st.rerun()


# ===================================================================
#  KHU A — TRANG CHỦ / DASHBOARD (§3)
# ===================================================================
def page_home():
    st.title("⌂ Trang chủ")
    st.caption("Xưởng sản xuất video — phần SẢN XUẤT do GUI lo; phần viết scene Manim cần Claude Code.")

    videos = B.list_videos()
    total = len(videos)
    rendered = sum(1 for v in videos if v["status"]["hd_mp4"])
    missing = sum(1 for v in videos
                  if not v["status"]["has_scene"] or v["status"]["voice_done"] < v["status"]["n_segments"])

    c1, c2, c3 = st.columns(3)
    c1.metric("Tổng video", total)
    c2.metric("Đã render HD", rendered)
    c3.metric("Còn thiếu", missing, help="Chưa có scene hoặc chưa đủ giọng")

    # Thẻ "Đang chạy" (live) — chỉ hiện khi có job nền
    if st.session_state.running:
        st.divider()
        with st.container(border=True):
            st.markdown(f"**▶ Đang chạy:** {st.session_state.job} — `{st.session_state.job_slug}`")
            drain_queue()
            pct, label = parse_progress(st.session_state.log, st.session_state.job,
                                        st.session_state.n_segments or 1)
            st.progress(pct, text=label)
            cc1, cc2 = st.columns(2)
            if cc1.button("Xem log", use_container_width=True):
                goto("editor", st.session_state.job_slug)
            if cc2.button("■ Dừng", type="primary", use_container_width=True):
                stop_job()
                st.rerun()
        time.sleep(0.5)
        st.rerun()

    st.divider()
    st.subheader("Tiếp tục dở")
    recent = sorted(videos, key=lambda v: v["status"]["last_render"], reverse=True)[:3]
    cols = st.columns(3)
    for col, v in zip(cols, recent):
        with col, st.container(border=True):
            st.markdown(f"**{v['title']}**")
            st.caption(f"`{v['slug']}` · {_fmt_mtime(v['status']['last_render'])}")
            st.write(status_badges(v["status"]))
            if st.button("Mở biên tập", key=f"home_open_{v['slug']}", use_container_width=True):
                goto("editor", v["slug"])

    st.divider()
    b1, b2 = st.columns(2)
    if b1.button("＋ Tạo video mới", type="primary", use_container_width=True):
        goto("new")
    if b2.button("⌕ Mở Kho ý tưởng", use_container_width=True):
        goto("ideas")

    st.info("💡 Phần viết scene cần Claude Code; phần sản xuất (giọng, render, xem video) do GUI này lo.")


# ===================================================================
#  KHU B — THƯ VIỆN VIDEO (§3)
# ===================================================================
def page_library():
    st.title("▸ Thư viện video")
    videos = B.list_videos()

    c1, c2 = st.columns([2, 1])
    qsearch = c1.text_input("Tìm kiếm", placeholder="tên hoặc slug…", label_visibility="collapsed")
    flt = c2.selectbox("Lọc", ["Tất cả", "Có giọng", "Đã render", "Còn thiếu"],
                       label_visibility="collapsed")

    def keep(v):
        s = v["status"]
        if qsearch and qsearch.lower() not in (v["slug"] + " " + v["title"]).lower():
            return False
        if flt == "Có giọng":
            return s["voice_done"] >= s["n_segments"] and s["n_segments"] > 0
        if flt == "Đã render":
            return bool(s["hd_mp4"])
        if flt == "Còn thiếu":
            return not s["has_scene"] or s["voice_done"] < s["n_segments"]
        return True

    shown = [v for v in videos if keep(v)]
    if not shown:
        st.warning("Không có video khớp bộ lọc.")
        return

    # Lưới thẻ (3 cột)
    cols = st.columns(3)
    for i, v in enumerate(shown):
        s = v["status"]
        with cols[i % 3], st.container(border=True):
            st.markdown(f"**{v['title']}**")
            st.caption(f"`{v['slug']}` · {v['scene_class'] or '?'} · {s['n_segments']} đoạn")
            # Thumbnail = frame đầu MP4 nếu có
            if s["hd_mp4"] and Path(s["hd_mp4"]).exists():
                st.video(s["hd_mp4"])
            st.write(status_badges(s))
            bcols = st.columns(2)
            if bcols[0].button("Mở", key=f"lib_open_{v['slug']}", use_container_width=True):
                goto("editor", v["slug"])
            if bcols[1].button("♪ Sinh giọng", key=f"lib_voice_{v['slug']}",
                               use_container_width=True,
                               disabled=st.session_state.running):
                _trigger_voice(v["slug"], s["n_segments"])
                goto("editor", v["slug"])


# ===================================================================
#  TRIGGERS JOB (gọi backend — đọc đúng chữ ký)
# ===================================================================
def _trigger_voice(slug: str, n_seg: int):
    try:
        gen, handle = B.run_voice(slug, force=True)
    except FileNotFoundError as e:
        st.session_state.log = [f"LỖI: {e}"]
        st.error(str(e))
        return False
    start_job("voice", slug, gen, handle, n_seg)
    return True


def _trigger_align(slug: str, n_seg: int, whisper="small"):
    gen, handle = B.run_align(slug, whisper_model=whisper)
    start_job("align", slug, gen, handle, n_seg)


def _trigger_render(slug: str, n_seg: int, quality: str, res: str, fps: int, align: bool):
    try:
        gen, handle = B.run_render(slug, quality=quality, res=res, fps=fps, align=align)
    except ValueError as e:
        st.error(str(e))
        return False
    start_job("preview" if quality == "preview" else "hd", slug, gen, handle, n_seg)
    return True


# ===================================================================
#  KHU C — TRANG BIÊN TẬP 1 VIDEO (§3, §4) — 2 cột chính
# ===================================================================
def page_editor(slug: str | None):
    if not slug:
        st.warning("Chưa chọn video. Quay lại Thư viện để chọn.")
        if st.button("← Thư viện"):
            goto("library")
        return

    stt = B.get_status(slug)
    title = B.TITLES.get(slug, slug)

    # Header (§4): tên + slug + dải huy hiệu
    top1, top2 = st.columns([3, 1])
    top1.markdown(f"## Video ▸ {title}  \n`{slug}` · {B.SCENE_CLASS.get(slug, '?')}")
    if top2.button("← Thư viện", use_container_width=True):
        goto("library")
    st.write(status_badges(stt))
    st.divider()

    # Cấu hình nhanh cho tập này (lưu trong session) — đọc default từ settings
    settings = B.read_settings()
    gs = settings.get("gui_state") or {}
    karaoke_default = bool(settings["brand"].get("KARAOKE_ON", False))
    res_default = gs.get("res", "1080,1920")
    fps_default = int(gs.get("fps", 60))
    whisper_default = settings.get("whisper_model", "small")

    # Hai cột chính (§4): trái LỜI THOẠI [1.2] · phải XEM TRƯỚC + LOG [1]
    left, right = st.columns([1.2, 1])

    # ----------------- CỘT TRÁI: LỜI THOẠI -----------------
    with left:
        st.markdown("### 📝 LỜI THOẠI (sửa từng đoạn)")
        st.caption("⚠ Viết số/ký tự theo cách đọc (x → ích). Lưu sẽ ghi vào "
                   f"`narration_texts_{slug}.py`.")
        segments = B.list_segments(slug)
        if not segments:
            st.warning("Chưa có lời thoại cho video này.")
        edited: dict[str, str] = {}
        for seg in segments:
            sid = seg["id"]
            dur = _fmt_dur(seg["wav_dur"]) if seg["wav_dur"] else "—"
            has_wav = "♪" if seg["wav_path"] else "—"
            st.markdown(f"**{sid}**  ·  ▶ {dur}  ·  {has_wav}")
            val = st.text_area(
                sid, value=seg["text"], key=f"seg_{slug}_{sid}",
                height=110, label_visibility="collapsed",
            )
            edited[sid] = val
            cseg = st.columns([1, 1])
            if seg["wav_path"] and Path(seg["wav_path"]).exists():
                with cseg[0]:
                    st.audio(seg["wav_path"])
            if cseg[1].button("Áp dụng quy ước TTS", key=f"tts_{slug}_{sid}",
                              use_container_width=True):
                st.session_state[f"seg_{slug}_{sid}"] = B.apply_tts_convention(val)
                st.rerun()

        bcol = st.columns([1, 1])
        if bcol[0].button("💾 Lưu lời thoại", type="primary", use_container_width=True,
                          disabled=not segments):
            try:
                B.write_narration(slug, edited)
                st.success("Đã lưu lời thoại.")
            except (ValueError, Exception) as e:  # noqa: BLE001
                st.error(f"Không lưu được: {e}")
        if bcol[1].button("Áp dụng TTS toàn bộ", use_container_width=True, disabled=not segments):
            for seg in segments:
                k = f"seg_{slug}_{seg['id']}"
                st.session_state[k] = B.apply_tts_convention(st.session_state.get(k, seg["text"]))
            st.rerun()

        st.divider()
        # ---- 3 nút hành động chính (§3 KHU C, §4) — khoá khi đang chạy ----
        st.markdown("### 🎬 Hành động")
        busy = st.session_state.running
        a1, a2, a3 = st.columns(3)
        if a1.button("♪ Sinh giọng", use_container_width=True, disabled=busy,
                     help="VoxCPM CPU · ~2–3 phút"):
            _trigger_voice(slug, stt["n_segments"])
            st.rerun()
        if a2.button("▣ Render preview", use_container_width=True, disabled=busy,
                     help="540×960 @12fps · ~30–60 giây"):
            _trigger_render(slug, stt["n_segments"], "preview", res_default,
                            fps_default, align=False)
            st.rerun()
        if a3.button("★ Render HD", type="primary", use_container_width=True, disabled=busy,
                     help="1080×1920 @60fps · ~15–25 phút"):
            _trigger_render(slug, stt["n_segments"], "hd", res_default, fps_default,
                            align=karaoke_default)
            st.rerun()

        # Cài đặt nhanh cho tập này
        with st.expander("⚙ Cài đặt nhanh cho video này"):
            res_opt = st.selectbox("Độ phân giải", ["1080,1920", "540,960"],
                                   index=0 if res_default == "1080,1920" else 1,
                                   key=f"res_{slug}")
            fps_opt = st.selectbox("FPS", [60, 30, 15],
                                   index=[60, 30, 15].index(fps_default) if fps_default in (60, 30, 15) else 0,
                                   key=f"fps_{slug}")
            kar_opt = st.checkbox("Bật Karaoke (align) khi render HD", value=karaoke_default,
                                  key=f"kar_{slug}")
            if st.button("Lưu cài đặt nhanh", key=f"savecfg_{slug}"):
                B.write_settings({"gui_state": {"res": res_opt, "fps": int(fps_opt)},
                                  "brand": {"KARAOKE_ON": bool(kar_opt)}})
                st.success("Đã lưu. Lần render sau sẽ dùng giá trị này.")
                st.rerun()

    # ----------------- CỘT PHẢI: XEM TRƯỚC + LOG -----------------
    with right:
        st.markdown("### ▶ XEM TRƯỚC KẾT QUẢ")
        outputs = B.list_outputs(slug)
        # Ưu tiên mp4 vừa render xong nếu có
        done_mp4 = st.session_state.done_mp4 if st.session_state.job_slug == slug else None
        if outputs or done_mp4:
            labels = []
            paths = []
            if done_mp4 and Path(done_mp4).exists():
                labels.append("★ Vừa render")
                paths.append(done_mp4)
            for o in outputs:
                name = Path(o["path"]).name
                labels.append(f"{name} · {o['res'] or '?'} · {o['fps'] or '?'}fps")
                paths.append(o["path"])
            sel = st.selectbox("Phiên bản", labels, key=f"ver_{slug}")
            chosen = paths[labels.index(sel)]
            if Path(chosen).exists():
                st.video(chosen)
                meta = next((o for o in outputs if o["path"] == chosen), None)
                if meta:
                    st.caption(f"{meta['res'] or '?'} · {meta['fps'] or '?'}fps · "
                               f"{_fmt_size(meta['size'])} · {_fmt_mtime(meta['mtime'])}")
                bb = st.columns(2)
                if bb[0].button("📂 Mở thư mục", key=f"open_{slug}", use_container_width=True):
                    B.open_in_finder(str(Path(chosen).parent))
                if bb[1].button("✓ Bản chốt", key=f"final_{slug}", use_container_width=True):
                    st.toast("Đã đánh dấu bản chốt (ghi nhớ phiên).")
                    st.session_state[f"final_mp4_{slug}"] = chosen
            else:
                st.info("File không còn tồn tại.")
        else:
            st.info("Chưa có MP4. Bấm Render preview/HD để tạo.")

        st.divider()
        render_job_panel(for_slug=slug)


# ===================================================================
#  KHU D — KHO Ý TƯỞNG (§3)
# ===================================================================
def page_ideas():
    st.title("⌕ Kho ý tưởng")
    ideas = B.read_ideas()
    if not ideas:
        st.warning("Không đọc được noidung/kho_y_tuong.md.")
        return

    c1, c2 = st.columns([1, 1])
    grp = c1.selectbox("Nhóm", ["Tất cả", "📐 TOÁN", "⚛️ LÝ"])
    tag = c2.selectbox("Tag", ["Tất cả", "🎯 hấp dẫn", "🎨 dễ dựng", "⚠️ cần kiểm chứng"])

    def keep(it):
        if grp == "📐 TOÁN" and it["group"] != "TOÁN":
            return False
        if grp == "⚛️ LÝ" and it["group"] != "LÝ":
            return False
        tagmap = {"🎯 hấp dẫn": "🎯", "🎨 dễ dựng": "🎨", "⚠️ cần kiểm chứng": "⚠️"}
        if tag != "Tất cả" and tagmap[tag] not in it["tags"]:
            return False
        return True

    shown = [it for it in ideas if keep(it)]
    st.caption(f"{len(shown)} ý tưởng")

    if st.button("📂 Mở file gốc để sửa"):
        B.open_in_finder(str(B.IDEAS_MD))

    cols = st.columns(2)
    for i, it in enumerate(shown):
        with cols[i % 2], st.container(border=True):
            badge = "  ✅ ĐÃ LÀM" if it["done"] else ""
            grp_icon = "📐" if it["group"] == "TOÁN" else "⚛️" if it["group"] == "LÝ" else "•"
            st.markdown(f"**{grp_icon} {it['code']}. {it['title']}**{badge}")
            if it["tags"]:
                st.write(" ".join(it["tags"]))
            if it["details"]:
                with st.expander("Chi tiết"):
                    for d in it["details"]:
                        st.markdown(d)
            if not it["done"]:
                if st.button("Tạo video từ ý tưởng này", key=f"idea_{it['code']}",
                             use_container_width=True):
                    st.session_state["new_prefill_title"] = it["title"]
                    st.session_state["new_prefill_code"] = it["code"]
                    goto("new")


# ===================================================================
#  KHU F — TẠO VIDEO MỚI (§3)
# ===================================================================
def page_new():
    st.title("＋ Tạo video mới")

    # Callout ranh giới (§3 KHU F)
    st.warning(
        "**Ranh giới:** Bước viết hoạt hình `scenes/<slug>_video.py` cần **Claude Code**. "
        "GUI lo: tạo thư mục, nhập lời thoại, sinh giọng, render."
    )

    prefill_title = st.session_state.get("new_prefill_title", "")
    title = st.text_input("Tên tập", value=prefill_title, placeholder="vd: Tán xạ Rayleigh")

    def suggest_slug(t: str) -> str:
        s = re.sub(r"[^a-z0-9]+", "", (t or "").lower().replace(" ", ""))
        return s[:24] or "video_moi"

    default_slug = suggest_slug(title)
    slug = st.text_input("slug (chữ thường, số, gạch dưới)", value=default_slug)

    st.markdown("### Lời thoại theo đoạn")
    st.caption("Mỗi đoạn 1 id (vd 01_hook) + nội dung. Sẽ ghi vào "
               "`narration_texts_<slug>.py`.")

    # Trình tạo segment đơn giản (số đoạn + id mặc định)
    n = st.number_input("Số đoạn", min_value=1, max_value=12, value=4, step=1)
    default_ids = ["01_hook", "02_build", "03_payoff", "04_cta",
                   "05_extra", "06_extra", "07_extra", "08_extra",
                   "09_extra", "10_extra", "11_extra", "12_extra"]
    segments: dict[str, str] = {}
    for i in range(int(n)):
        c1, c2 = st.columns([1, 3])
        sid = c1.text_input(f"id #{i+1}", value=default_ids[i], key=f"new_id_{i}")
        txt = c2.text_area(f"nội dung #{i+1}", value="", key=f"new_txt_{i}",
                           height=70, label_visibility="collapsed",
                           placeholder="Lời thoại đoạn này…")
        if sid:
            segments[sid] = txt or "..."

    # Checklist
    st.markdown("### Tiến độ")
    has_text = any(t.strip() not in ("", "...") for t in segments.values())
    scene_exists = (B.SCENES / f"{slug}_video.py").exists() if slug else False
    st.write(f"{'✅' if has_text else '☐'} Có lời thoại")
    st.write(f"{'✅' if scene_exists else '☐'} Có scene (Claude)")
    st.write("☐ Sinh giọng")
    st.write("☐ Render")

    b1, b2 = st.columns(2)
    # Nút copy prompt cho Claude
    if b1.button("📋 Sao chép prompt cho Claude", use_container_width=True, disabled=not slug):
        prompt = B.claude_prompt(slug, title, segments)
        st.code(prompt, language="text")
        st.caption("Sao chép đoạn trên dán vào Claude Code để viết scene.")

    if b2.button("✚ Tạo khung", type="primary", use_container_width=True, disabled=not slug):
        try:
            B.scaffold_video(slug, title, segments)
            st.success(f"Đã tạo khung cho `{slug}`. Mở Trang biên tập.")
            st.session_state.pop("new_prefill_title", None)
            goto("editor", slug)
        except (ValueError, FileExistsError) as e:
            st.error(str(e))


# ===================================================================
#  KHU G — CÀI ĐẶT (§3)
# ===================================================================
def page_settings():
    st.title("⚙ Cài đặt")
    settings = B.read_settings()
    brand = settings["brand"]
    clone = settings["clone"]
    gs = settings.get("gui_state") or {}

    st.subheader("🎞 RENDER")
    res_cur = gs.get("res", "1080,1920")
    res = st.radio("Độ phân giải (nét hơn ↔ nhanh hơn)",
                   ["1080,1920", "540,960"],
                   index=0 if res_cur == "1080,1920" else 1,
                   format_func=lambda r: "1080×1920 (nét)" if r == "1080,1920" else "540×960 (nhanh)",
                   horizontal=True)
    fps_cur = int(gs.get("fps", 60))
    fps = st.select_slider("FPS (nét hơn ↔ nhanh hơn)", [15, 30, 60],
                           value=fps_cur if fps_cur in (15, 30, 60) else 60)

    st.divider()
    st.subheader("🎙 GIỌNG (VoxCPM)")
    st.caption("Áp cho 1 video — chọn slug để chỉnh clone_narration_<slug>.py")
    clone_slugs = sorted(clone.keys())
    if clone_slugs:
        sel_slug = st.selectbox("Video", clone_slugs)
        cur = clone[sel_slug]
        ts = st.slider("inference_timesteps (10 nhanh ↔ 24 nét)", 8, 24,
                       int(cur.get("INFERENCE_TIMESTEPS", 16)))
        st.caption("⚠ 24 bước ~ gấp 2× thời gian sinh giọng trên CPU.")
        cfg = st.slider("cfg (1.4 tự nhiên ↔ 2.6 giống)", 1.4, 2.6,
                        float(cur.get("CFG_VALUE", 2.0)), step=0.1)
        denoiser = st.checkbox("load_denoiser (khử ồn — chậm hơn)",
                               value=bool(cur.get("LOAD_DENOISER", False)))
    else:
        sel_slug = None
        st.info("Chưa có clone_narration_<slug>.py nào để chỉnh.")

    st.divider()
    st.subheader("📜 PHỤ ĐỀ")
    karaoke = st.checkbox("Bật Karaoke (đồng bộ KARAOKE_ON trong brand.py)",
                          value=bool(brand.get("KARAOKE_ON", False)))
    whisper = st.select_slider("Model Whisper (nhanh ↔ chính xác)",
                               ["tiny", "base", "small"],
                               value=settings.get("whisper_model", "small"))

    st.divider()
    st.subheader("📁 Đường dẫn hệ thống (chỉ đọc)")
    st.code(f"VoxCPM venv : {B.VOXCPM}\n.venv       : {B.VENV}\noutput/     : {B.OUTPUT}",
            language="text")

    st.divider()
    c1, c2 = st.columns(2)
    if c1.button("💾 Lưu mặc định", type="primary", use_container_width=True):
        payload = {
            "brand": {"KARAOKE_ON": bool(karaoke)},
            "gui_state": {"res": res, "fps": int(fps), "whisper_model": whisper},
        }
        if sel_slug:
            payload["clone"] = {sel_slug: {
                "INFERENCE_TIMESTEPS": int(ts),
                "CFG_VALUE": float(cfg),
                "LOAD_DENOISER": bool(denoiser),
            }}
        try:
            B.write_settings(payload)
            st.success("Đã lưu cài đặt.")
        except Exception as e:  # noqa: BLE001
            st.error(f"Không lưu được: {e}")
    if c2.button("↺ Khôi phục mặc định an toàn", use_container_width=True):
        try:
            B.write_settings({
                "brand": {"KARAOKE_ON": False},
                "gui_state": {"res": "1080,1920", "fps": 60, "whisper_model": "small"},
            })
            st.success("Đã khôi phục mặc định an toàn.")
            st.rerun()
        except Exception as e:  # noqa: BLE001
            st.error(str(e))


# ===================================================================
#  ROUTER
# ===================================================================
def main():
    render_sidebar()
    page = st.session_state.page
    if page == "home":
        page_home()
    elif page == "library":
        page_library()
    elif page == "editor":
        page_editor(st.session_state.slug)
    elif page == "ideas":
        page_ideas()
    elif page == "new":
        page_new()
    elif page == "settings":
        page_settings()
    else:
        page_home()


if __name__ == "__main__":
    main()
