# 🖥️ Đẩy lên server & render (KHÔNG tốn token Claude)

Toàn bộ khâu **sản xuất** (sinh giọng → căn chỉnh → render) là script Python/CPU thuần,
**không gọi Claude**. Server chỉ cần cài deps + có sẵn file dự án là render được vô hạn video.

## 1. Server cần gì (cài 1 lần)
- **Python 3.12+**, **ffmpeg**, và **font Arial** (bắt buộc — thiếu font chữ sẽ lệch/khác).
  - Linux: cài `ttf-mscorefonts-installer` hoặc copy `Arial.ttf` vào `~/.fonts` rồi `fc-cache -f`.
- **2 môi trường ảo riêng** (giống máy hiện tại):
  - `.venv` (Manim + faster-whisper + GUI):
    ```
    python -m venv .venv
    .venv/bin/pip install "manim==0.20.1" "setuptools<81" faster-whisper streamlit
    ```
  - `voxcpm-venv` (TTS clone giọng):
    ```
    python -m venv ~/voxcpm-venv
    ~/voxcpm-venv/bin/pip install "voxcpm==2.0.3" soundfile torch
    ```
- **Model cache** (tải tự động lần đầu, hoặc copy sẵn để khỏi tải lại):
  - VoxCPM2 (~12GB) trong `~/.cache/huggingface`
  - Whisper "small" (~480MB) — faster-whisper tự tải.
- **File giọng mẫu (BẮT BUỘC, copy theo):** `output/narration/voice-yeu_ref16k.wav` — đây là giọng clone của bạn, không có thì không sinh được giọng.
- **KHÔNG cần GPU** (VoxCPM chạy CPU; Manim render CPU).

## 2. Copy gì lên server
- Cả thư mục `scenes/` (code) + `output/narration/voice-yeu_ref16k.wav` + `render_pipeline.sh`.
- KHÔNG cần copy `media/` (video render ra) hay các `output/narration_*/` (sẽ tự sinh).

## 3. Render 1 video — 1 lệnh
```bash
bash render_pipeline.sh <slug> <SceneClass>
# ví dụ:
bash render_pipeline.sh xetnghiem XetNghiemVideo
bash render_pipeline.sh phanh     PhanhVideo
```
Script tự: sinh giọng (nếu chưa có) → căn chỉnh karaoke → render HD → in đường dẫn MP4.

## 4. Render hàng loạt (batch / cron)
```bash
for v in "xetnghiem XetNghiemVideo" "phanh PhanhVideo"; do
  bash render_pipeline.sh $v
done
```
→ Có thể đặt cron chạy đêm. **Mỗi video ~22 phút CPU, 0 token.**

## 5. Phân vai chi phí
| Khâu | Ở đâu | Token |
|---|---|---|
| Nghĩ ý tưởng, viết kịch bản, **viết code scene**, QA hình | Claude (máy bạn) | Tốn |
| Sinh giọng · căn chỉnh · render · re-render | **Server** | **0** |

➡️ Claude tạo "khuôn" 1 lần (các file `*_video.py`, `narration_texts_*.py`); server render mãi miễn phí.

## 6. GUI điều khiển (tuỳ chọn — Streamlit)
Nếu muốn bảng điều khiển bấm chuột thay vì gõ lệnh:
```bash
.venv/bin/streamlit run app.py --server.address=127.0.0.1 --server.port=8501
# hoặc trên máy có Finder: bấm đúp chay_giao_dien.command
```
Mở `http://127.0.0.1:8501`. GUI gọi đúng `render_pipeline.sh` nên hành vi y hệt CLI.
(Trên server không màn hình: chạy `--server.address=0.0.0.0` rồi SSH-tunnel cho an toàn.)

## 7. Đăng video lên Nextcloud
Công cụ: `upload_nextcloud.sh` (WebDAV). **Thông tin đăng nhập KHÔNG nằm trong repo** —
tạo trên server 1 lần:
```bash
mkdir -p ~/.config/toanly && umask 077
cat > ~/.config/toanly/nextcloud.env <<'EOF'
NC_URL=http://tiennb.com
NC_USER=news1
NC_PASS=<app-password>      # nên dùng App Password của Nextcloud, không phải mật khẩu chính
NC_DIR=video-ai
EOF
chmod 600 ~/.config/toanly/nextcloud.env
```
Đăng:  `bash upload_nextcloud.sh <file.mp4>`  ·  `bash upload_nextcloud.sh --all`

## Tăng tốc (tuỳ chọn)
- `WHISPER_MODEL=medium` → karaoke căn chỉnh nét hơn (chậm hơn chút) — chỉ khi bật KARAOKE_ON.
- Giảm `INFERENCE_TIMESTEPS` 16→10 trong `clone_narration_*.py` → giọng nhanh ~1.6×.
- Render nhanh xem thử: thêm tham số `540,960 12` (resolution thấp, fps 12).
