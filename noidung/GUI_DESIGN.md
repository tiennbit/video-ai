# BẢN THIẾT KẾ GUI — "TOÁN LÝ ĐỜI THỰC" (Xưởng sản xuất video)

> Tài liệu thi công. Mọi đường dẫn dưới đây dùng tương đối so với gốc dự án:
> `/Users/macbook/Nextcloud/Data/Tien/code/video-ai/`
> Mục tiêu: dựng được ngay, không cần đoán.

---

## 1. TỔNG QUAN & MỤC TIÊU

### Bối cảnh
Dự án làm video dọc 9:16 (Manim + giọng clone VoxCPM2 + karaoke whisper) cho kênh
YouTube faceless về ứng dụng Toán–Lý đời thực (lớp 10–12). Pipeline hiện tại đã
chạy hoàn chỉnh bằng **`render_pipeline.sh <slug> <SceneClass> [res] [fps]`** thuần
CPU, không gọi Claude/token. Nhưng để dùng phải gõ lệnh terminal, biết slug, biết
tên SceneClass, sửa file `.py` bằng tay — **người dùng (không phải dev) rất khó thao tác.**

### Mục tiêu của GUI
1. **Một nút là chạy** — bọc `render_pipeline.sh` và các script con bằng giao diện bấm chuột.
2. **Sửa lời thoại trực quan** — sửa từng đoạn (segment) rồi lưu vào `narration_texts_<slug>.py`, không đụng code.
3. **Theo dõi tiến trình** — stream log real-time cho các việc chạy lâu (sinh giọng ~2–3′, align ~1–2′, render HD ~15–25′).
4. **Xem kết quả ngay trong app** — phát MP4 9:16 mà không cần mở phần mềm ngoài.
5. **Quản lý kho ý tưởng** — đọc/duyệt `noidung/kho_y_tuong.md`.
6. **Chỉnh tham số bằng ngôn ngữ dễ hiểu** — không bắt người dùng nhớ `INFERENCE_TIMESTEPS` là gì.

### Ranh giới (RẤT QUAN TRỌNG — phải nói rõ trong UI)
- GUI lo **SẢN XUẤT**: tạo thư mục, nhập lời thoại, sinh giọng, align, render, xem MP4.
- GUI **KHÔNG tự viết code hoạt hình** `scenes/<slug>_video.py` — phần viết Manim vẫn cần **Claude Code**.
  → Trong khu "Tạo video mới" phải có callout nói rõ điều này + nút "Sao chép prompt cho Claude".

### Sự thật đã xác minh từ codebase (dùng làm hằng số khi code)
| Hạng mục | Giá trị thực tế |
|---|---|
| Python `.venv` | `3.12.11` (đã có sẵn) |
| Streamlit | **CHƯA cài** → phải `pip install streamlit` vào `.venv` |
| VoxCPM venv | `~/voxcpm-venv/bin/python` (tách riêng, **không import vào GUI**) |
| File giọng mẫu (bắt buộc) | `output/narration/voice-yeu_ref16k.wav` (đã có) |
| Sentinel log "sinh giọng xong" | dòng `ALL_CLONED_DONE` (in bởi `clone_narration_*.py`) |
| Log từng đoạn giọng | `OK <id>: <s>s render, <s>s audio -> <path>` |
| Sentinel render | `==> XONG: <path mp4>` (in bởi `render_pipeline.sh`) |
| Mặc định render | `1080,1920 @ 60fps`; preview `540,960 @ 12fps` |
| Karaoke | `KARAOKE_ON = False` (brand.py dòng 34) — align chỉ chạy khi bật |

### Bảng các video & SceneClass (mapping cứng — backend cần)
| slug | SceneClass | File scene | Segments (id) | Chủ đề |
|---|---|---|---|---|
| `phanh` | `PhanhVideo` | `scenes/phanh_video.py` | 01_hook 02_haiphan 03_phanxa 04_phanh 05_rapso 06_ynghia 07_cta (7) | L1 Quãng phanh ∝ v² |
| `xetnghiem` | `XetNghiemVideo` | `scenes/xetnghiem_video.py` | 01_hook 02_vande 03_danso 04_test 05_dem 06_ynghia 07_cta (7) | T5 Bayes / dương tính giả |
| `laikep` | `LaiKepVideo` | `scenes/laikep_video.py` | 01_hook 02_build 03_payoff 04_cta (4) | T1 Lãi kép |
| `troixanh` | `TroiXanhVideo` | `scenes/troixanh_video.py` | 01_hook 02_trang 03_tanxa 04_ngay 05_chieu 06_ynghia 07_cta (7) | L7 Tán xạ ánh sáng |
| `parabol` | `ParabolVideo` | `scenes/parabol_video.py` | 01_hook 02_curve 03_vertex 04_formula 05_apply (5) | Parabol |

> Lưu ý: `parabol` dùng `narration_parabol.py` (không có hậu tố `_texts_`) và scene
> kế thừa `Scene` (không phải `BrandScene`); `parabol` chưa có `clone_narration_parabol.py`.
> Backend nên **tự dò file** (xem §5) thay vì hard-code tuyệt đối, nhưng giữ bảng này làm fallback/hiển thị.

---

## 2. CÔNG NGHỆ ĐÃ CHỌN + LÝ DO

### Chọn: **Streamlit** (chạy local trong trình duyệt)
`pip install streamlit` vào `.venv` sẵn có → `streamlit run app.py`.

### Lý do (đã cân nhắc 5 phương án)
1. **Phạm vi GUI hẹp**: chỉ là 1 nút Render + 1 ô log cuộn + 1 khung video dọc + vài form sửa text. Không cần app desktop nặng.
2. **Người dùng không-dev**: Streamlit cho widget (nút/selectbox/slider) sẵn, không phải viết HTML/JS.
3. **Pipeline đã tách process** (bash + 2 venv): GUI chỉ cần là "người điều phối subprocess" → đúng vai Streamlit.
4. **Tái dùng `.venv`**: chỉ thêm 1 dependency, không kéo Node/Qt/Electron.
5. **Phát video dọc native**: `st.video(path)` render `<video>` HTML5; MP4 Manim đã là H.264/yuv420p → phát thẳng đúng tỷ lệ 9:16.

### Điểm yếu phải xử lý (đã có giải pháp ở §6)
Streamlit **rerun toàn bộ script mỗi tương tác** → subprocess chạy lâu phải chạy
trong **thread nền + queue + `st.session_state`**, nếu làm naïve thì UI treo 20 phút và mất log.

### Phương án dự phòng #2: **Gradio**
Nếu khi thi công thấy phần stream log của Streamlit quá lắt léo → chuyển sang Gradio
(hàm generator `yield` log ra `gr.Textbox`, `gr.Video` phát MP4, `demo.queue()`).
Backend `app_backend.py` (§5) **độc lập với framework** nên đổi GUI không phải viết lại logic.

### KHÔNG chọn
- Flask/FastAPI + HTML/JS: phải tự viết frontend → sai "altitude", tốn gấp nhiều lần.
- PyQt/PySide: dựng chậm, rủi ro codec video trên macOS, đóng gói `.app` phiền.
- Electron: cần Node + chuỗi build JS, bundle nặng, lệch hẳn stack Python.

---

## 3. DANH SÁCH TÍNH NĂNG (THEO KHU)

### KHU A — Trang chủ / Dashboard
- 3 thẻ số: **Tổng video · Đã render HD · Còn thiếu** (chưa có giọng hoặc chưa có scene).
- Thẻ **"Đang chạy"** (live): tên việc + thanh tiến trình + nút *Xem log* / *Dừng* — chỉ hiện khi có job nền.
- Danh sách **"Tiếp tục dở"**: 3 video gần nhất (theo mtime), bấm mở thẳng Trang biên tập.
- 2 nút lớn: **+ Tạo video mới**, **Mở Kho ý tưởng**.
- Dải mẹo: "Phần viết scene cần Claude; phần sản xuất GUI này lo."

### KHU B — Thư viện video (danh sách)
- Lưới thẻ video: thumbnail (frame đầu MP4), tên + slug, thời lượng.
- Mỗi thẻ có **dải huy hiệu trạng thái**: `✓Thoại · ✓Scene · ♪Giọng (n/n) · ⏱Karaoke · ✓HD` (xanh = xong, xám = thiếu).
- Ô tìm kiếm + lọc theo trạng thái (Có giọng / Đã render / Còn thiếu).
- Nút nhanh khi rê chuột (hoặc nút dưới thẻ trong Streamlit): *Mở · Phát · Sinh giọng*.
- Toggle Lưới / Danh sách.

### KHU C — Trang biên tập 1 video (trung tâm sản xuất)
- Header: tên + slug + dải huy hiệu trạng thái (đồng bộ với thẻ ở thư viện).
- **Cột trái — LỜI THOẠI**: mỗi segment 1 `textarea` (lấy từ `SEGMENTS`), nhãn thời lượng `.wav` hiện có, nút **▶ nghe thử** từng đoạn.
  - Cảnh báo nhẹ: "viết số/ký tự theo cách đọc (x → ích)" + nút *Áp dụng quy ước TTS*.
  - Nút **💾 Lưu lời thoại** → ghi vào `narration_texts_<slug>.py`.
- **3 nút hành động chính**: **♪ Sinh giọng · ▣ Render preview · ★ Render HD** (kèm tooltip thời gian ước tính).
- **Cột phải — LOG TRỰC TIẾP**: khung đen cuộn theo dòng + thanh tiến trình + nhãn bước `[1/3]…[3/3]` + nút *Sao chép log* / *■ Dừng*.
- **Trình phát MP4** nhúng (xem KHU E) hiển thị kết quả mới nhất.
- Bảng **"Cài đặt nhanh cho video này"**: ghi đè resolution/fps/karaoke chỉ cho tập này.

### KHU D — Kho ý tưởng
- Render `noidung/kho_y_tuong.md` dạng đẹp, nhóm 📐 TOÁN / ⚛️ LÝ.
- Mỗi mục là 1 thẻ ý tưởng (mã T2/T5…, tiêu đề, tag 🎯 hấp dẫn / 🎨 dễ dựng / ⚠️ cần kiểm chứng).
- Tự gắn huy hiệu **✅ ĐÃ LÀM** nếu slug tương ứng đã có trong thư viện.
- Lọc theo lớp (10/11/12) và theo tag.
- Nút *Tạo video từ ý tưởng này* → nhảy sang KHU F với tiêu đề điền sẵn.
- Nút *Mở file gốc để sửa*.

### KHU E — Trình phát kết quả (Player nhúng)
- Khung `<video>` HTML5: play/pause, seek, âm lượng, full-screen.
- Hộp chọn phiên bản: liệt kê MP4 trong `output/preview/*.mp4` + `output/*.mp4` của video đó.
- Nhãn meta: độ phân giải · fps · dung lượng · ngày render.
- Nút *Mở thư mục chứa file* (`open <dir>` trên macOS) · *Đánh dấu "bản chốt"*.

### KHU F — Tạo video mới
- Form: Tên tập + slug (tự gợi ý từ tên) + chọn từ Kho ý tưởng.
- **Callout ranh giới**: "Bước viết hoạt hình `scenes/<slug>_video.py` cần Claude Code. GUI lo: tạo thư mục, nhập lời thoại, sinh giọng, render."
- Trình tạo lời thoại theo đoạn (thêm/xoá id + textarea) → ghi `narration_texts_<slug>.py`.
- Checklist: ☐ Có lời thoại ☐ Có scene (Claude) ☐ Sinh giọng ☐ Render (tự tick khi đủ điều kiện).
- Nút **Sao chép prompt cho Claude** (sinh sẵn câu nhắc mô tả tập).
- Nút **Tạo khung** → sinh `narration_texts_<slug>.py` + thư mục `output/narration_<slug>/`, rồi mở Trang biên tập.

### KHU G — Cài đặt
- **RENDER**: Độ phân giải (1080×1920 / 540×960) · FPS (60/30/15) — slider nhãn "nét hơn ↔ nhanh hơn".
- **GIỌNG (VoxCPM)**: `inference_timesteps` (10 nhanh ↔ 24 nét) · `cfg` (1.4 tự nhiên ↔ 2.6 giống) · `load_denoiser` · nút A/B nghe thử 1 câu.
- **PHỤ ĐỀ**: bật/tắt Karaoke (đồng bộ `KARAOKE_ON`) · model Whisper (tiny/base/small — "nhanh ↔ chính xác").
- Mỗi núm 1 dòng giải thích + cảnh báo thời gian ("24 bước ~ gấp 2× thời gian trên CPU").
- Đường dẫn hệ thống (chỉ đọc): VoxCPM venv, .venv, thư mục output.
- Nút *Lưu mặc định* / *Khôi phục mặc định an toàn*.

### Sidebar (luôn hiển thị)
- Logo + tên kênh "TOÁN LÝ ĐỜI THỰC".
- Menu: Trang chủ · Video · Tạo mới · Kho ý tưởng · Cài đặt.
- Chấm vàng ● cạnh "Video" khi có job nền.
- Khối trạng thái máy ở chân: "VoxCPM: CPU · rảnh / Đang render…", dung lượng `output/`.

---

## 4. BỐ CỤC MÀN HÌNH (ASCII MOCKUP — Trang biên tập, màn hình chính)

```
┌──────────────┬──────────────────────────────────────────────────────────────┐
│  TOÁN LÝ     │  Video ▸ Tập 5 — Xét nghiệm (xetnghiem)        [Đang render ●] │
│  ĐỜI THỰC    │  ✓Thoại  ✓Scene  ♪Giọng 7/7  ⏱Karaoke  ◻HD chưa có           │
│              ├──────────────────────────────────────────────────────────────┤
│ ⌂ Trang chủ  │  LỜI THOẠI (sửa từng đoạn)        │   XEM TRƯỚC KẾT QUẢ        │
│ ▸ Video    ● │  ┌──────────────────────────────┐ │  ┌──────────────────────┐ │
│ ＋ Tạo mới   │  │ 01_hook            ▶ 0:06  ♪  │ │  │                      │ │
│ ⌕ Kho ý tưởng│  │ ┌──────────────────────────┐ │ │  │     ▶  (MP4 9:16)    │ │
│ ⚙ Cài đặt    │  │ │Xét nghiệm dương tính 99% │ │ │  │                      │ │
│              │  │ │— bạn có thật sự mắc...   │ │ │  └──────────────────────┘ │
│              │  │ └──────────────────────────┘ │ │  Phiên bản: [FULLHD  ▾]   │
│              │  ├──────────────────────────────┤ │  1080×1920·60fps·12MB     │
│              │  │ 02_vande           ▶ 0:11  ♪  │ │  [Mở thư mục] [Bản chốt]  │
│              │  │ ┌──────────────────────────┐ │ │ ├──────────────────────────┤
│              │  │ │Trong 1000 người, chỉ 1...│ │ │ │  LOG TRỰC TIẾP            │
│              │  │ └──────────────────────────┘ │ │ │  ┌──────────────────────┐ │
│              │  │ ⚠ viết "x"→"ích" [Áp dụng]   │ │ │ │ [3/3] Render HD…       │ │
│              │  └──────────────────────────────┘ │ │ │ Manim 1080,1920 @60fps │ │
│              │  [💾 Lưu lời thoại]               │ │ │ frame 842/1530 …       │ │
│              │                                   │ │ │ ████████░░░░░ 55%      │ │
│ ─────────    │  ┌──────────┬──────────┬───────┐ │ │ │ ETA ~3 phút            │ │
│ VoxCPM: CPU  │  │♪ Sinh    │▣ Render  │★ Render│ │ │ └──────────────────────┘ │
│ ● Đang render│  │  giọng   │  preview │   HD   │ │ │  [Sao chép log] [■ Dừng] │
│ output 1.2GB │  └──────────┴──────────┴───────┘ │ │                          │
└──────────────┴───────────────────────────────────┴──────────────────────────┘
```

> Trong Streamlit: dùng `st.set_page_config(layout="wide")`, sidebar = `st.sidebar`,
> hai cột chính bằng `st.columns([1.2, 1])`. Khung log = `st.empty()` + `st.code()`.
> Player = `st.video(path)`. Mỗi segment dùng `st.text_area(key=f"seg_{slug}_{id}")`.

---

## 5. KIẾN TRÚC FILE

```
video-ai/
├── app.py                 # ★ GUI Streamlit (chỉ vẽ UI + gọi app_backend, KHÔNG chứa logic pipeline)
├── app_backend.py         # ★ Bọc toàn bộ pipeline — KHÔNG import streamlit, thuần stdlib + subprocess
├── chay_giao_dien.command # ★ Launcher double-click cho người không-dev
├── gui_state.json         # (sinh ra) cài đặt mặc định người dùng lưu ở KHU G
├── render_pipeline.sh     # (đã có) — backend GỌI QUA file này
└── scenes/, output/, noidung/ ...  (đã có)
```

### 5.1 `app_backend.py` — module bọc pipeline (độc lập framework)

Nguyên tắc: **mọi hàm thuần Python, không import streamlit/gradio**; hàm chạy lâu
trả về **iterator/generator các dòng log** (hoặc nhận một `queue.Queue` để đẩy log)
+ một đối tượng "handle" để hủy. Nhờ vậy đổi GUI không phải sửa backend.

```python
# app_backend.py — chữ ký hàm (đặc tả thi công)
import os, re, json, glob, subprocess, signal
from pathlib import Path

ROOT     = Path(__file__).resolve().parent
SCENES   = ROOT / "scenes"
OUTPUT   = ROOT / "output"
PREVIEW  = OUTPUT / "preview"
VENV     = ROOT / ".venv" / "bin"
VOXCPM   = Path(os.path.expanduser("~/voxcpm-venv/bin/python"))
REF_VOICE = OUTPUT / "narration" / "voice-yeu_ref16k.wav"

# Mapping cứng (fallback) — nhưng list_videos() vẫn tự dò file thật
SCENE_CLASS = {
    "phanh": "PhanhVideo", "xetnghiem": "XetNghiemVideo",
    "laikep": "LaiKepVideo", "troixanh": "TroiXanhVideo", "parabol": "ParabolVideo",
}
TITLES = {
    "phanh": "L1 Quãng phanh ∝ v²", "xetnghiem": "T5 Xét nghiệm (Bayes)",
    "laikep": "T1 Lãi kép", "troixanh": "L7 Tán xạ ánh sáng", "parabol": "Parabol",
}

# ---------- TRẠNG THÁI / LIỆT KÊ (nhanh, không subprocess) ----------
def list_videos() -> list[dict]:
    """Dò scenes/*_video.py + narration_texts_*.py để ra danh sách slug.
       Trả [{slug, title, scene_class, n_segments, status}] (status = get_status)."""

def get_status(slug: str) -> dict:
    """Trả {
        has_thoai:  bool,  # có narration_texts_<slug>.py (hoặc narration_<slug>.py)
        has_scene:  bool,  # có scenes/<slug>_video.py + class
        n_segments: int,
        voice_done: int,   # số .wav trong output/narration_<slug>/
        karaoke:    int,   # số .words.json
        hd_mp4:     str|None,  # mp4 mới nhất ở output/preview hoặc media/videos/<slug>_video
        last_render: float,    # mtime để sắp 'tiếp tục dở'
    }"""

def list_segments(slug: str) -> list[dict]:
    """Đọc SEGMENTS từ narration_texts_<slug>.py (import module động hoặc parse AST).
       Trả [{id, text, wav_path|None, wav_dur|None}]. KHÔNG chạy code nặng."""

def list_outputs(slug: str) -> list[dict]:
    """MP4 liên quan slug: glob output/preview/*<gợi ý>*.mp4 + output/*.mp4 +
       media/videos/<slug>_video/*.mp4. Trả [{path, res, fps, size, mtime}] (ffprobe meta)."""

# ---------- ĐỌC/GHI LỜI THOẠI (an toàn, không chạy code) ----------
def read_narration(slug: str) -> dict[str, str]:
    """Trả {id: text}. Dùng AST hoặc import module trong subprocess riêng để an toàn."""

def write_narration(slug: str, segments: dict[str, str]) -> None:
    """Ghi LẠI file narration_texts_<slug>.py giữ nguyên header/docstring,
       chỉ thay khối SEGMENTS = {...}. Validate: mỗi text >= 1 từ. Ghi atomically (tmp + rename)."""

def apply_tts_convention(text: str) -> str:
    """Chuẩn hoá cách đọc: 'x'→'ích', số → chữ (tuỳ chọn), thêm . ? ! cuối câu. Trả text mới."""

# ---------- TÁC VỤ CHẠY LÂU (trả về generator log) ----------
def run_voice(slug: str, force=True, env_overrides=None):
    """yield từng dòng stdout của: VOXCPM scenes/clone_narration_<slug>.py
       Báo xong khi gặp 'ALL_CLONED_DONE'. Tiến trình = đếm dòng 'OK <id>:' / n_segments."""

def run_align(slug: str, whisper_model="small"):
    """yield log của: VENV/python scenes/align_narration.py output/narration_<slug>
       env WHISPER_MODEL=<model>. Chỉ gọi khi KARAOKE_ON=True."""

def run_render(slug, quality="hd", res="1080,1920", fps=60, align=False):
    """Gọi render_pipeline.sh để TẬN DỤNG hợp đồng env sẵn có:
       cmd = ['bash','render_pipeline.sh', slug, SCENE_CLASS[slug], res, str(fps)]
       env: FORCE_VOICE=0 (giọng đã có), ALIGN='1' nếu align, VOXCPM/VENV.
       quality 'preview' => res='540,960', fps=12 (gọi manim -ql trực tiếp nếu muốn nhanh hơn).
       yield log; tiến trình parse 'frame N/M' của manim; kết thúc đọc '==> XONG: <mp4>'."""

# ---------- HẠ TẦNG SUBPROCESS (dùng chung bởi 3 hàm run_*) ----------
def _stream(cmd: list[str], env=None, cwd=ROOT):
    """Popen(cmd, stdout=PIPE, stderr=STDOUT, text=True, bufsize=1,
            env={**os.environ, 'PYTHONUNBUFFERED':'1', **(env or {})})
       for line in iter(p.stdout.readline, ''): yield line
       Lưu p để terminate(). Trả cả (gen, handle)."""

# ---------- CÀI ĐẶT / IDE ----------
def read_settings() -> dict:   # đọc brand.py (KARAOKE_ON, FONT, SZ_*) + clone_*.py + gui_state.json
def write_settings(d: dict):   # ghi lại đúng dòng trong brand.py / clone_narration_<slug>.py (regex theo dòng đã biết)
def read_ideas() -> list[dict] # parse noidung/kho_y_tuong.md thành thẻ ý tưởng
def scaffold_video(slug, title, segments: dict[str,str]) -> None  # tạo narration_texts_<slug>.py + output/narration_<slug>/
def claude_prompt(slug, title, segments) -> str  # sinh prompt dán cho Claude viết scene
def open_in_finder(path: str)  # subprocess.run(['open', path]) — macOS
```

**Vị trí ghi setting đã biết (để `write_settings` đặt regex chính xác):**
- `scenes/brand.py`: `FONT` (dòng 33), `KARAOKE_ON` (dòng 34), `SZ_HERO` (49), `SZ_TITLE` (50), `SZ_BODY` (51), `SZ_LABEL` (52), `SZ_SMALL` (53), `CW` (54).
- `scenes/clone_narration_<slug>.py`: `INFERENCE_TIMESTEPS` (16), `CFG_VALUE` (17), `LOAD_DENOISER` (18).
- `scenes/align_narration.py`: `MODEL = os.environ.get("WHISPER_MODEL", ...)` (16) — chỉnh qua env, không sửa file.

### 5.2 `app.py` — GUI Streamlit
- Chỉ chứa: routing trang (sidebar radio → render hàm `page_home()`, `page_library()`, `page_editor(slug)`, `page_ideas()`, `page_new()`, `page_settings()`).
- Gọi `app_backend` cho mọi dữ liệu/hành động.
- Giữ trạng thái job nền trong `st.session_state` (xem §6).

### 5.3 `chay_giao_dien.command` (double-click trong Finder)
```bash
#!/usr/bin/env bash
cd "$(dirname "$0")"
.venv/bin/streamlit run app.py --server.address=127.0.0.1 --server.port=8501
```
`chmod +x chay_giao_dien.command`. Ép `127.0.0.1` để chỉ truy cập local (an toàn mạng chung).

---

## 6. XỬ LÝ TÁC VỤ CHẠY LÂU + STREAM LOG + THANH TIẾN TRÌNH

### Nguyên tắc lõi
GUI **không** chạy Manim/VoxCPM trong process của nó. Nó `subprocess.Popen([...])`
(qua `app_backend._stream`), đọc stdout dòng-theo-dòng, đẩy lên UI. Lý do: VoxCPM bắt
buộc CPU (RTF ~6×), Manim nặng — chạy ngoài để GUI luôn phản hồi và để tránh xung đột
deps giữa `.venv` và `~/voxcpm-venv`.

### Popen đúng cách (chống "đơ" do buffering)
```python
p = subprocess.Popen(
    cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    text=True, bufsize=1,
    env={**os.environ, "PYTHONUNBUFFERED": "1", **extra_env},
    cwd=ROOT,
)
for line in iter(p.stdout.readline, ""):
    yield line.rstrip("\n")
```
- `PYTHONUNBUFFERED=1` + `bufsize=1` để log chảy đều thay vì dồn cục.
- Manim/VoxCPM in progress bằng `\r`; nếu thanh % cần mượt thì bọc `stdbuf -oL` hoặc đọc theo ký tự. Mức cơ bản đọc theo dòng là đủ.

### Mẫu Streamlit (thread + queue + session_state)
```python
import threading, queue, time
from app_backend import run_render

def _worker(gen, q):
    try:
        for line in gen:
            q.put(("log", line))
        q.put(("done", 0))
    except Exception as e:
        q.put(("error", str(e)))

# Khi bấm nút:
if st.button("★ Render HD", disabled=st.session_state.get("running")):
    q = queue.Queue()
    gen = run_render(slug, quality="hd", res="1080,1920", fps=60)
    t = threading.Thread(target=_worker, args=(gen, q), daemon=True)
    t.start()
    st.session_state.update(running=True, q=q, log=[], thread=t)

# Mỗi rerun: rút queue, vẽ lại
if st.session_state.get("running"):
    q = st.session_state.q
    while not q.empty():
        kind, payload = q.get()
        if kind == "log":   st.session_state.log.append(payload)
        elif kind == "done": st.session_state.running = False
        elif kind == "error":
            st.session_state.log.append("LỖI: " + payload); st.session_state.running = False
    log_box = st.empty()
    log_box.code("\n".join(st.session_state.log[-400:]))   # giữ ~400 dòng cuối
    # thanh tiến trình
    pct = _parse_progress(st.session_state.log)            # từ 'frame N/M' hoặc 'OK <id>:'
    st.progress(pct, text=_stage_label(st.session_state.log))
    if st.session_state.running:
        time.sleep(0.3); st.rerun()                        # tự làm tươi
    else:
        mp4 = _find_done_mp4(st.session_state.log)         # từ '==> XONG: <path>'
        if mp4: st.video(mp4)
```
> Tuỳ chọn: `pip install streamlit-autorefresh` thay cho `sleep+rerun` để cuộn log mượt hơn.

### Thanh tiến trình — cách parse từng stage
| Việc | Tín hiệu trong log | Cách tính % |
|---|---|---|
| Sinh giọng | dòng `OK <id>:` | (số dòng OK) / `n_segments` |
| Align | `✓ <seg>.wav: N từ` | (số dòng ✓) / `n_segments` |
| Render | `frame N/M` của Manim, và `[1/3] [2/3] [3/3]` | `N/M` trong stage [3/3]; nhãn lấy từ `[k/3]` |
| Kết thúc | `ALL_CLONED_DONE` hoặc `==> XONG: <mp4>` | set 100%, nạp player |

### Nút Dừng (chống tiến trình mồ côi)
- Lưu `Popen` handle trong session_state; nút **■ Dừng** gọi `handle.terminate()` (rồi `kill()` nếu cần).
- Khoá 3 nút hành động khi `running=True` để không chạy 2 job CPU song song.

---

## 7. DEPENDENCIES & LỆNH CHẠY

### Cài (1 lần)
```bash
# vào .venv sẵn có (Python 3.12.11)
.venv/bin/pip install streamlit
# TUỲ CHỌN cuộn log mượt:
.venv/bin/pip install streamlit-autorefresh
```
- `subprocess`, `threading`, `queue`, `glob`, `json`, `ast` — đã có trong stdlib.
- `ffmpeg` 8.0 đã có ở `/opt/homebrew/bin/ffmpeg` — chỉ dùng khi cần `ffprobe` lấy meta / re-encode pixel format.
- **Không cài thêm gì** cho VoxCPM/Manim — GUI gọi qua `render_pipeline.sh` + `~/voxcpm-venv`.

### Tiền đề bắt buộc (kiểm tra khi khởi động app, báo lỗi thân thiện nếu thiếu)
1. `output/narration/voice-yeu_ref16k.wav` tồn tại (mẫu giọng clone).
2. `~/voxcpm-venv/bin/python` tồn tại.
3. Font Arial cài trên máy (macOS có sẵn).

### Chạy app
```bash
# cách 1: terminal
.venv/bin/streamlit run app.py --server.address=127.0.0.1

# cách 2: double-click (người không-dev)
# mở Finder → bấm đúp chay_giao_dien.command
```
Mở tự động `http://127.0.0.1:8501`.

---

## 8. KẾ HOẠCH THI CÔNG (CHIA BƯỚC — để workflow build chia việc)

> Mỗi bước là 1 đơn vị giao việc độc lập, test được riêng.

**BƯỚC 0 — Khung & cài đặt** *(nhỏ)*
- `.venv/bin/pip install streamlit`. Tạo `app.py` rỗng có sidebar + 5 trang placeholder + `chay_giao_dien.command`.
- Tiêu chí xong: `streamlit run app.py` mở được, chuyển trang được.

**BƯỚC 1 — `app_backend.py`: phần ĐỌC (không subprocess)** *(vừa)*
- `list_videos`, `get_status`, `list_segments`, `list_outputs`, `read_narration`, `read_ideas`.
- Test bằng `python -c` in ra JSON cho từng slug; đối chiếu bảng §1.
- Tiêu chí xong: in đúng 5 slug + đúng số segment + đúng số `.wav`/`.words.json`.

**BƯỚC 2 — KHU B Thư viện + KHU A Dashboard** *(vừa)*
- Vẽ lưới thẻ + huy hiệu trạng thái từ `get_status`. Dashboard 3 thẻ số + "tiếp tục dở".
- Thumbnail: `ffmpeg -i <mp4> -frames:v 1` (cache vào `output/.thumbs/`).
- Tiêu chí xong: thấy 5 video, bấm vào mở Trang biên tập (rỗng tạm).

**BƯỚC 3 — KHU C đọc + sửa + lưu lời thoại** *(vừa)*
- `read_narration` → textarea từng segment; `write_narration` ghi atomically; `apply_tts_convention`.
- Nút ▶ nghe thử `.wav` (`st.audio`).
- Tiêu chí xong: sửa 1 đoạn, lưu, mở lại file `.py` thấy đúng; diff không phá header/docstring.

**BƯỚC 4 — Hạ tầng subprocess + stream log** *(lõi, vừa–lớn)*
- `_stream`, `run_voice`, `run_align`, `run_render`. Mẫu thread+queue+session_state ở §6.
- Khung log `st.empty()` + `st.progress` + nút Dừng + khoá nút khi chạy.
- Test trước với `run_render(..., quality="preview")` (nhanh ~30–60s).
- Tiêu chí xong: bấm Render preview → log chảy real-time, thanh % nhích, xong tự nạp player.

**BƯỚC 5 — KHU E Player + chọn phiên bản** *(nhỏ–vừa)*
- `list_outputs` + `st.video` + selectbox phiên bản + meta (ffprobe) + nút Mở thư mục / Bản chốt.
- Tiêu chí xong: phát được MP4 9:16 trong app, đổi phiên bản được.

**BƯỚC 6 — 3 nút hành động đầy đủ (giọng → preview → HD)** *(vừa)*
- Nối nút "♪ Sinh giọng" (FORCE_VOICE), "★ Render HD" (3 bước qua `render_pipeline.sh`, ALIGN theo KARAOKE_ON).
- Tiêu chí xong: chạy trọn 1 tập từ sửa thoại → sinh giọng → render HD, không gõ terminal.

**BƯỚC 7 — KHU G Cài đặt** *(vừa)*
- `read_settings`/`write_settings` (regex theo dòng đã biết §5.1) + `gui_state.json` cho mặc định.
- A/B nghe thử 1 câu (sinh 2 `.wav` tạm với cfg khác nhau).
- Tiêu chí xong: đổi resolution/fps/karaoke/timesteps → lần render sau dùng đúng giá trị.

**BƯỚC 8 — KHU D Kho ý tưởng + KHU F Tạo video mới** *(vừa)*
- `read_ideas` render thẻ + huy hiệu ĐÃ LÀM; `scaffold_video` + `claude_prompt`.
- Tiêu chí xong: từ 1 ý tưởng → tạo khung `narration_texts_<slug>.py` + thư mục + nút copy prompt.

**BƯỚC 9 — Hoàn thiện & chống lỗi** *(nhỏ)*
- Kiểm tra tiền đề khi khởi động (§7), thông báo lỗi tiếng Việt thân thiện.
- Dọn tiến trình mồ côi khi thoát; giới hạn log; thử trên màn nhỏ.
- Tiêu chí xong: demo end-to-end mượt cho người không-dev.

> Thứ tự ưu tiên nếu thiếu thời gian: **0 → 1 → 3 → 4 → 6** cho lõi dùng được;
> 2/5/7/8/9 là lớp hoàn thiện.

---

## 9. RỦI RO & LƯU Ý

1. **Stream log bị "đơ" do buffering** — Manim/VoxCPM in `\r` + Python buffer khi không phải TTY.
   → `PYTHONUNBUFFERED=1` + `bufsize=1`; cân nhắc `stdbuf -oL`; hiện rõ "Đang sinh giọng… (~2–3′)" / "Render HD ~15–25′" để người dùng không tắt giữa chừng.
2. **Bẫy rerun Streamlit** — chạy subprocess naïve sẽ treo UI 20′ và mất log. PHẢI dùng thread + queue + session_state (§6).
3. **Hai venv tách biệt** — GUI ở `.venv`, VoxCPM ở `~/voxcpm-venv`. **TUYỆT ĐỐI không `import voxcpm` trong process Streamlit** (xung đột deps + crash). Luôn gọi qua `render_pipeline.sh`/`VOXCPM` python.
4. **Tiến trình mồ côi** — đóng tab khi đang render → subprocess vẫn ngốn CPU. Cần nút Dừng `terminate()` + bắt sự kiện thoát.
5. **Codec video hiếm khi lệch** — nếu `st.video` không phát, re-encode: `ffmpeg -i in.mp4 -c:v libx264 -pix_fmt yuv420p out.mp4`.
6. **Chạy đồng thời ngốn CPU** — khoá nút hành động khi có job, không cho render nhiều video song song.
7. **Bảo mật cổng** — ép `--server.address=127.0.0.1` để không mở ra mạng chung (Streamlit mặc định 0.0.0.0:8501).
8. **Ghi file `.py` an toàn** — `write_narration`/`write_settings` ghi atomically (tmp + `os.replace`), giữ nguyên header/docstring, validate trước khi ghi; tránh làm hỏng file scene đang dùng.
9. **`parabol` không đồng bộ quy ước** — dùng `narration_parabol.py` (thiếu `_texts_`), scene kế thừa `Scene`, thiếu `clone_narration_parabol.py`. Backend phải tự dò file & xử lý ngoại lệ, không giả định mọi slug giống nhau.
10. **Karaoke phụ thuộc `KARAOKE_ON`** — chỉ chạy align khi True; nếu False, ẩn/disable bước Karaoke và đặt `ALIGN=0` khi gọi pipeline.
```

`````
