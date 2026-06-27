#!/usr/bin/env bash
# =============================================================================
# Pipeline render 1 video — THUẦN CPU, KHÔNG cần Claude/token.
# Chạy được trên máy này hoặc trên server (sau khi cài đủ deps, xem SERVER_SETUP.md).
#
# Cách dùng:
#   bash render_pipeline.sh <slug> <SceneClass> [resolution] [fps]
# Ví dụ:
#   bash render_pipeline.sh xetnghiem XetNghiemVideo
#   bash render_pipeline.sh phanh     PhanhVideo
#   bash render_pipeline.sh laikep    LaiKepVideo 1080,1920 60
#
# Quy ước file (mỗi video):
#   scenes/clone_narration_<slug>.py   -> sinh giọng  -> output/narration_<slug>/*.wav
#   scenes/align_narration.py          -> *.words.json (căn chỉnh karaoke)
#   scenes/<slug>_video.py : <SceneClass>  -> render
#
# Biến môi trường ghi đè (tuỳ chọn):
#   VOXCPM=/path/to/voxcpm-venv/bin/python   VENV=/path/to/.venv/bin   FORCE_VOICE=1
# =============================================================================
set -euo pipefail

SLUG="${1:?Thiếu <slug>, ví dụ: xetnghiem}"
SCENE="${2:?Thiếu <SceneClass>, ví dụ: XetNghiemVideo}"
RES="${3:-1080,1920}"
FPS="${4:-60}"

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

VOXCPM="${VOXCPM:-$HOME/voxcpm-venv/bin/python}"
VENV="${VENV:-$ROOT/.venv/bin}"
NARR="output/narration_${SLUG}"

echo "==> [1/3] Sinh giọng clone -> $NARR"
if [ "${FORCE_VOICE:-0}" = "1" ] || ! ls "$NARR"/*.wav >/dev/null 2>&1; then
  "$VOXCPM" "scenes/clone_narration_${SLUG}.py"
else
  echo "    (đã có file giọng, bỏ qua — đặt FORCE_VOICE=1 để sinh lại)"
fi

echo "==> [2/3] Căn chỉnh karaoke (chỉ khi bật karaoke)"
if [ "${ALIGN:-0}" = "1" ]; then
  "$VENV/python" scenes/align_narration.py "$NARR"
else
  echo "    (bỏ qua — karaoke đang TẮT. Đặt ALIGN=1 nếu bật lại KARAOKE_ON trong brand.py)"
fi

echo "==> [3/3] Render HD ($RES @ ${FPS}fps)"
"$VENV/manim" -qh --resolution "$RES" --fps "$FPS" "scenes/${SLUG}_video.py" "$SCENE"

OUT="$(find "media/videos/${SLUG}_video" -name "${SCENE}.mp4" -not -path '*partial*' | head -1)"
echo "==> XONG: $OUT"
