# 🎬 TOÁN LÝ ĐỜI THỰC — Xưởng sản xuất video tự động

Hệ thống tạo video ngắn (dọc 9:16) dạy **ứng dụng đời thực của Toán & Vật lý lớp 10–12**:
animation bằng **Manim** + lồng tiếng **giọng clone của bạn** (VoxCPM) + đăng **Nextcloud**.
Toàn bộ khâu sản xuất chạy **CPU, không cần GPU, không cần Claude**.

---

## ⭐ TL;DR — Clone về máy mới chạy ngay

```bash
git clone <repo-url> video-ai && cd video-ai
bash setup_new_machine.sh          # cài 2 venv + nhắc deps hệ thống
bash render_pipeline.sh xetnghiem XetNghiemVideo   # render thử 1 video
.venv/bin/streamlit run app.py --server.address=127.0.0.1   # hoặc mở giao diện
```

---

## ❓ "Clone về máy khác có phải làm lại giọng không?"

**KHÔNG phải thu lại giọng.** Có 2 lớp "giọng", cả hai đều đi theo repo:

| Lớp | File | Trong git? | Ý nghĩa |
|---|---|---|---|
| **Giọng MẪU** (danh tính giọng của bạn) | `output/narration/voice-yeu_ref16k.wav` | ✅ Có (2.6MB) | **Không thể tái tạo** — nhờ nó mà clone được giọng bạn. Có sẵn → **không bao giờ thu lại.** |
| **Giọng đã SINH từng tập** | `output/narration_<slug>/*.wav` | ✅ Có (~34MB) | VoxCPM sinh từ giọng mẫu. Có sẵn → các tập cũ **render ngay không cần sinh lại.** |

➡️ **Kết luận:** clone về là **dùng được luôn**. Bạn chỉ cần:
1. Cài 2 môi trường ảo (script lo) + **tải model VoxCPM ~12GB lần đầu** (tự động).
2. Với **tập MỚI chưa có giọng** (10 tập batch mới), chạy sinh giọng 1 lần (~20′/tập, tự động dùng giọng mẫu — **vẫn không thu lại gì**).

> Muốn repo gọn? Bỏ giọng đã sinh ra khỏi git (mở comment `output/narration_*/` trong `.gitignore`)
> → máy mới tự sinh lại bằng `clone_narration_*.py`. Giọng mẫu thì **luôn phải giữ**.

---

## 🖥️ Cài đặt chi tiết trên máy mới

### 1. Lấy code
```bash
git clone <repo-url> video-ai
cd video-ai
```

### 2. Deps hệ thống (cần `brew`/`apt` — 1 lần)
- **macOS:** `brew install python@3.12 ffmpeg pango pkg-config cairo` (font Arial có sẵn)
- **Linux:** `sudo apt install -y python3.12 python3.12-venv ffmpeg libcairo2-dev libpango1.0-dev pkg-config fonts-liberation`
  - ⚠️ Font: cần **Arial** (hoặc Liberation Sans thay thế). Thiếu font → chữ lệch.

### 3. Môi trường Python (chạy script tự động)
```bash
bash setup_new_machine.sh
```
Script tạo 2 venv: `.venv` (Manim + faster-whisper + Streamlit) và `~/voxcpm-venv` (VoxCPM clone giọng),
rồi kiểm tra tiền đề. Lần render đầu sẽ **tải model VoxCPM2 (~12GB)** về `~/.cache/huggingface`.

### 4. (Tuỳ chọn) Đăng Nextcloud
Tạo `~/.config/toanly/nextcloud.env` — **KHÔNG để trong repo** (xem [SERVER_SETUP.md](noidung/SERVER_SETUP.md) §7).

> 💡 **Linux + GPU NVIDIA:** sửa `device="cpu"` → `"cuda"` trong `scenes/clone_narration_*.py`
> để sinh giọng **nhanh gấp nhiều lần**. (macOS giữ `cpu` vì MPS lỗi.)

---

## 🎞️ Sản xuất 1 video

### Cách A — dòng lệnh (1 lệnh trọn gói)
```bash
bash render_pipeline.sh <slug> <SceneClass>
# vd:
bash render_pipeline.sh docao DoCaoVideo
```
Tự: sinh giọng (nếu chưa có) → căn chỉnh (nếu bật karaoke) → render HD → in đường dẫn MP4.

### Cách B — giao diện (bấm chuột)
```bash
.venv/bin/streamlit run app.py --server.address=127.0.0.1
# hoặc bấm đúp chay_giao_dien.command (macOS)
```
Mở `http://127.0.0.1:8501`: chọn video → sửa lời thoại → bấm Sinh giọng / Render / xem MP4.

### Đăng lên Nextcloud
```bash
bash upload_nextcloud.sh <file.mp4>     # hoặc --all
```

---

## ✍️ Tạo video MỚI (ranh giới cần Claude)

| Khâu | Ai làm | Cần Claude? |
|---|---|---|
| Nghĩ ý tưởng, **viết code hoạt hình** `scenes/<slug>_video.py` | Claude Code | **CÓ** |
| Sinh giọng · render · đăng · sửa thoại · đổi tham số | Máy (script/GUI) | Không |

→ Hiện có **15 tập đã code sẵn** + **100 ý tưởng** trong [noidung/kho_y_tuong.md](noidung/kho_y_tuong.md).
Server tự sản xuất 15 tập này **không cần Claude**. Muốn thêm tập mới thì nhờ Claude viết scene
(GUI có nút "copy prompt cho Claude").

---

## 📁 Cấu trúc

```
video-ai/
├── README.md, .gitignore
├── render_pipeline.sh        # render 1 video (giọng→[align]→render)
├── upload_nextcloud.sh       # đăng MP4 lên Nextcloud (WebDAV)
├── setup_new_machine.sh      # cài đặt máy mới
├── chay_giao_dien.command    # mở GUI (double-click)
├── app.py, app_backend.py    # GUI Streamlit + backend bọc pipeline
├── scenes/
│   ├── brand.py              # template chung (BrandScene, cỡ chữ, intro/outro, cue)
│   ├── <slug>_video.py       # code hoạt hình từng tập (Scene)
│   ├── narration_texts_<slug>.py   # lời thoại từng tập
│   ├── clone_narration_<slug>.py   # sinh giọng clone (VoxCPM)
│   └── align_narration.py    # căn chỉnh karaoke (faster-whisper) — chỉ khi KARAOKE_ON
├── output/narration/voice-yeu_ref16k.wav   # ⭐ GIỌNG MẪU (bắt buộc)
├── output/narration_<slug>/  # giọng đã sinh từng tập
└── noidung/                  # kho ý tưởng, tài liệu (SERVER_SETUP, GUI_DESIGN)
```

## 🔧 Quy ước quan trọng (khi sửa/thêm code)
- Khung **DỌC 9:16**; dùng `Text` (KHÔNG `MathTex`/LaTeX — server không có LaTeX); cỡ chữ dùng hằng `SZ_*` trong `brand.py`.
- Mỗi tập kế thừa `BrandScene`, không gọi `play_intro()`, karaoke tắt (`KARAOKE_ON=False`), canh nhịp bằng `self.cue()`.
- Số/công thức trong lời thoại viết theo cách ĐỌC; mỗi câu kết `. ? !`.

## ⚠️ Khắc phục sự cố
- `st.video` không phát: `ffmpeg -i in.mp4 -c:v libx264 -pix_fmt yuv420p out.mp4`.
- Giọng sinh chậm: bình thường (CPU ~10× thời gian thực). Giảm `INFERENCE_TIMESTEPS` 16→10 cho nhanh.
- Chi tiết triển khai server/cron: xem [noidung/SERVER_SETUP.md](noidung/SERVER_SETUP.md).
