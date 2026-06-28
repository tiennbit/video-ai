# =============================================================================
# video-ai — Xưởng video Toán Lý (Manim + VoxCPM2 + faster-whisper), CPU-only.
# Tái lập đúng kiến trúc 2 venv của repo để render_pipeline.sh / app_backend.py
# chạy KHÔNG cần sửa code:
#   /app/.venv            (manim + faster-whisper + streamlit + soundfile)
#   /root/voxcpm-venv     (voxcpm + torch CPU + soundfile)   <- = ~/voxcpm-venv
# Model VoxCPM2 (~12GB) KHÔNG nằm trong image; tải runtime về volume hf-cache.
# =============================================================================
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DEBIAN_FRONTEND=noninteractive \
    HF_HOME=/root/.cache/huggingface

# ---- Deps hệ thống: ffmpeg (mux/encode) + cairo/pango (Manim text) + fonts ----
RUN apt-get update && apt-get install -y --no-install-recommends \
        ffmpeg \
        libcairo2 libcairo2-dev \
        libpango-1.0-0 libpangocairo-1.0-0 libpango1.0-dev \
        pkg-config \
        fontconfig fonts-liberation \
        build-essential \
        git curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# ---- Font Arial thật (copy từ host Windows) -> chữ khớp đúng layout brand.py ----
COPY fonts/ /usr/share/fonts/truetype/msarial/
RUN fc-cache -f >/dev/null 2>&1 || true

WORKDIR /app

# ---- venv 1: .venv  (Manim + Whisper + GUI) ----
RUN python -m venv /app/.venv \
    && /app/.venv/bin/pip install -U pip \
    && /app/.venv/bin/pip install \
        "manim==0.20.1" "setuptools<81" faster-whisper streamlit soundfile

# ---- venv 2: ~/voxcpm-venv  (VoxCPM TTS, torch CPU-only) ----
# Cài voxcpm trước (kéo đủ deps), RỒI ép torch+torchaudio bản +cpu KHỚP index PyTorch.
# PHẢI pin "+cpu" cho torchaudio: nếu để 'torchaudio' trơn, pip kéo bản CUDA từ PyPI
# (libcudart.so.13) và import lỗi. Cài tách 2 bước + --no-deps để torchaudio không đụng torch.
RUN python -m venv /root/voxcpm-venv \
    && /root/voxcpm-venv/bin/pip install -U pip \
    && /root/voxcpm-venv/bin/pip install "voxcpm==2.0.3" soundfile \
    && /root/voxcpm-venv/bin/pip install --index-url https://download.pytorch.org/whl/cpu \
        --force-reinstall "torch==2.12.1+cpu" \
    && /root/voxcpm-venv/bin/pip install --index-url https://download.pytorch.org/whl/cpu \
        --force-reinstall --no-deps "torchaudio==2.11.0+cpu"

# ---- Mã nguồn dự án (output/ & media/ sẽ bị volume ghi đè lúc chạy) ----
COPY . /app

# Giữ container sống để exec từng bước (sinh giọng / render).
CMD ["sleep", "infinity"]
