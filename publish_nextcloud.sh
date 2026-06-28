#!/usr/bin/env bash
# =============================================================================
# Đăng 1 tập video + file mô tả lên Nextcloud, rồi DỌN bản staging khi thành công.
#
# Luồng:
#   1) Stage  : copy MP4 render xong -> output/upload/<slug>/<slug>.mp4
#   2) Mô tả  : đảm bảo noidung/mota/<slug>.txt (seed từ lời thoại nếu chưa có)
#               -> copy sang staging thành <slug>.txt
#   3) Upload : đẩy CẢ video + mô tả lên Nextcloud (qua upload_nextcloud.sh / WebDAV)
#   4) Dọn    : CHỈ KHI cả 2 file upload OK -> xoá bản staging.
#               Upload thất bại -> GIỮ NGUYÊN mọi file (KHÔNG xoá), thoát != 0.
#
# Dùng:
#   bash publish_nextcloud.sh <slug> <đường-dẫn-mp4>
#
# Cấu trúc trên Nextcloud (trong NC_DIR):
#   <NC_DIR>/video/<slug>.mp4      # CHỈ chứa video
#   <NC_DIR>/thongtin/<slug>.txt   # CHỉ chứa file thông tin (title SEO + hashtag)
# (script tự tạo 2 thư mục con nếu chưa có — qua ensure_collection của upload_nextcloud.sh)
#
# Biến môi trường (tuỳ chọn):
#   PYTHON=/path/to/python   # trình thông dịch để sinh mô tả (mặc định tự dò)
#   VENV=/path/to/.venv/bin  # nơi tìm python (đồng bộ render_pipeline.sh)
#   CLEAN_MEDIA=1            # xoá luôn bản render gốc trong media/ (mặc định: GIỮ)
#   NC_VIDEO_DIR=video       # tên thư mục con chứa video  (mặc định: video)
#   NC_INFO_DIR=thongtin     # tên thư mục con chứa thông tin (mặc định: thongtin)
#   NEXTCLOUD_ENV=...        # ghi đè đường dẫn file cấu hình (mặc định ~/.config/toanly/nextcloud.env)
# =============================================================================
set -euo pipefail

SLUG="${1:?Thiếu <slug>, ví dụ: carbon14}"
MP4="${2:?Thiếu đường dẫn MP4 render xong}"

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

[ -f "$MP4" ] || { echo "✗ Không thấy MP4: $MP4"; exit 1; }

UPLOADER="$ROOT/upload_nextcloud.sh"
[ -f "$UPLOADER" ] || { echo "✗ Thiếu $UPLOADER"; exit 1; }

VENV="${VENV:-$ROOT/.venv/bin}"
STAGE="$ROOT/output/upload/$SLUG"
VIDEO_NAME="$SLUG.mp4"
DESC_NAME="$SLUG.txt"
NC_VIDEO_DIR="${NC_VIDEO_DIR:-video}"      # thư mục con chứa video trên Nextcloud
NC_INFO_DIR="${NC_INFO_DIR:-thongtin}"     # thư mục con chứa file thông tin

# --------------------------------------------------------------------------
# 1) Bảo đảm file mô tả (seed từ lời thoại nếu chưa có)
# --------------------------------------------------------------------------
_detect_python() {
  for cand in "${PYTHON:-}" "$VENV/python" "$VENV/python3" python3 python; do
    [ -n "$cand" ] || continue
    if command -v "$cand" >/dev/null 2>&1 || [ -x "$cand" ]; then
      echo "$cand"; return 0
    fi
  done
  return 1
}

DESC=""
if PY="$(_detect_python)"; then
  DESC="$("$PY" "$ROOT/scenes/make_description.py" "$SLUG" | tail -1)" || DESC=""
fi
# Fallback nếu không có Python: tạo template tối thiểu để vẫn có mô tả đẩy lên.
if [ -z "$DESC" ] || [ ! -f "$DESC" ]; then
  mkdir -p "$ROOT/noidung/mota"
  DESC="$ROOT/noidung/mota/$SLUG.txt"
  [ -f "$DESC" ] || printf '%s\n\n%s\n\n%s\n' \
    "$SLUG" "(Mô tả tập — soạn nội dung tại đây.)" \
    "#toanly #toanhoc #vatly #shorts #fyp" > "$DESC"
  echo "ℹ Dùng mô tả: $DESC"
fi

# --------------------------------------------------------------------------
# 2) Stage: copy video + mô tả vào output/upload/<slug>/
# --------------------------------------------------------------------------
mkdir -p "$STAGE"
cp -f "$MP4" "$STAGE/$VIDEO_NAME"
cp -f "$DESC" "$STAGE/$DESC_NAME"
echo "→ Staging: $STAGE  ($(du -h "$STAGE/$VIDEO_NAME" | cut -f1))"

# --------------------------------------------------------------------------
# 3) Upload CẢ video + mô tả (cả hai phải OK mới coi là thành công)
# --------------------------------------------------------------------------
ok=1
bash "$UPLOADER" "$STAGE/$VIDEO_NAME" "$NC_VIDEO_DIR/$VIDEO_NAME" || ok=0
bash "$UPLOADER" "$STAGE/$DESC_NAME"  "$NC_INFO_DIR/$DESC_NAME"   || ok=0

if [ "$ok" != "1" ]; then
  echo "✗ Upload THẤT BẠI — GIỮ NGUYÊN file cục bộ (không xoá). Bản staging: $STAGE"
  exit 1
fi

# --------------------------------------------------------------------------
# 4) Dọn dẹp khi upload thành công
# --------------------------------------------------------------------------
rm -f "$STAGE/$VIDEO_NAME" "$STAGE/$DESC_NAME"
rmdir "$STAGE" 2>/dev/null || true
echo "✓ Đã đăng video + mô tả, đã xoá bản staging."

if [ "${CLEAN_MEDIA:-0}" = "1" ]; then
  rm -f "$MP4"
  echo "✓ Đã xoá bản render gốc: $MP4  (CLEAN_MEDIA=1)"
else
  echo "ℹ Giữ bản render gốc: $MP4  (đặt CLEAN_MEDIA=1 để xoá luôn)"
fi
