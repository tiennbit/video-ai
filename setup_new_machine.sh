#!/usr/bin/env bash
# =============================================================================
# CÀI ĐẶT TRÊN MÁY MỚI (macOS hoặc Linux). Chạy TỪ thư mục gốc dự án:
#   bash setup_new_machine.sh
# Script lo phần Python (2 venv + pip). Phần hệ thống (ffmpeg, font, cairo/pango)
# in hướng dẫn để bạn tự cài (cần brew/apt). Model VoxCPM tải tự động lần chạy đầu.
# =============================================================================
set -e
cd "$(dirname "$0")"
OS="$(uname -s)"
echo "==> Máy: $OS"

# ---- 0. Nhắc cài deps hệ thống (không tự sudo) ----
echo
echo "==> [0] DEPS HỆ THỐNG (cài trước, 1 lần):"
if [ "$OS" = "Darwin" ]; then
  echo "    brew install python@3.12 ffmpeg pango pkg-config cairo"
  echo "    (Font Arial: macOS có sẵn)"
else
  echo "    sudo apt update && sudo apt install -y python3.12 python3.12-venv ffmpeg \\"
  echo "        libcairo2-dev libpango1.0-dev pkg-config fonts-liberation"
  echo "    # Font: cần Arial — hoặc dùng Liberation Sans thay thế, hoặc copy Arial.ttf vào ~/.fonts && fc-cache -f"
fi
read -r -p "    Đã cài deps hệ thống chưa? Enter để tiếp tục, Ctrl-C để dừng..." _

PY="${PYTHON:-python3}"

# ---- 1. .venv: Manim + Whisper + GUI ----
echo
echo "==> [1] Tạo .venv (Manim + faster-whisper + Streamlit)..."
"$PY" -m venv .venv
.venv/bin/pip install -q -U pip
.venv/bin/pip install -q "manim==0.20.1" "setuptools<81" faster-whisper streamlit soundfile
echo "    ✓ .venv xong: $(.venv/bin/python -c 'import manim,faster_whisper,streamlit; print("manim",manim.__version__)')"

# ---- 2. ~/voxcpm-venv: TTS clone giọng ----
echo
echo "==> [2] Tạo ~/voxcpm-venv (VoxCPM clone giọng)..."
"$PY" -m venv "$HOME/voxcpm-venv"
"$HOME/voxcpm-venv/bin/pip" install -q -U pip
"$HOME/voxcpm-venv/bin/pip" install -q voxcpm soundfile torch
echo "    ✓ voxcpm-venv xong"
echo "    Lưu ý: lần CHẠY ĐẦU sẽ tải model VoxCPM2 (~12GB) về ~/.cache/huggingface."
if [ "$OS" != "Darwin" ] && command -v nvidia-smi >/dev/null 2>&1; then
  echo "    💡 PHÁT HIỆN GPU NVIDIA: sửa device=\"cpu\" -> \"cuda\" trong scenes/clone_narration_*.py"
  echo "       để sinh giọng NHANH GẤP NHIỀU LẦN (Mac thì giữ cpu vì MPS lỗi)."
fi

# ---- 3. Kiểm tra tiền đề ----
echo
echo "==> [3] Kiểm tra tiền đề bắt buộc:"
[ -f output/narration/voice-yeu_ref16k.wav ] && echo "    ✓ giọng mẫu (voice-yeu_ref16k.wav)" \
  || echo "    ✗ THIẾU output/narration/voice-yeu_ref16k.wav — PHẢI copy theo từ máy cũ!"
command -v ffmpeg >/dev/null 2>&1 && echo "    ✓ ffmpeg" || echo "    ✗ THIẾU ffmpeg"
[ -f "$HOME/.config/toanly/nextcloud.env" ] && echo "    ✓ cấu hình Nextcloud" \
  || echo "    ⓘ Chưa có ~/.config/toanly/nextcloud.env (chỉ cần nếu muốn đăng Nextcloud — xem SERVER_SETUP.md §7)"

echo
echo "==> XONG. Cách dùng:"
echo "    • Render 1 video : bash render_pipeline.sh xetnghiem XetNghiemVideo"
echo "    • Mở giao diện   : .venv/bin/streamlit run app.py --server.address=127.0.0.1"
echo "    • Đăng Nextcloud : bash upload_nextcloud.sh --all"
