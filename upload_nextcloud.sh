#!/usr/bin/env bash
# =============================================================================
# Đăng video lên Nextcloud (qua WebDAV). KHÔNG nhúng mật khẩu trong file này —
# đọc từ ~/.config/toanly/nextcloud.env (NC_URL, NC_USER, NC_PASS, NC_DIR).
#
# Dùng:
#   bash upload_nextcloud.sh <file.mp4> [tên-trên-server.mp4]
#   bash upload_nextcloud.sh --all          # đăng tất cả MP4 "bản chốt" trong output/preview/
# =============================================================================
set -euo pipefail

CFG="${NEXTCLOUD_ENV:-$HOME/.config/toanly/nextcloud.env}"
[ -f "$CFG" ] || { echo "✗ Thiếu file cấu hình: $CFG"; exit 1; }
set -a; . "$CFG"; set +a
: "${NC_URL:?}" "${NC_USER:?}" "${NC_PASS:?}" "${NC_DIR:?}"
BASE="$NC_URL/remote.php/dav/files/$NC_USER"

ensure_dir() {  # tạo thư mục đích (bỏ qua nếu đã có: 405)
  curl -s -o /dev/null -u "$NC_USER:$NC_PASS" -X MKCOL "$BASE/$NC_DIR/" || true
}

put_one() {
  local file="$1" name="${2:-$(basename "$1")}"
  [ -f "$file" ] || { echo "✗ Không thấy file: $file"; return 1; }
  local code
  code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 600 \
        -u "$NC_USER:$NC_PASS" -T "$file" "$BASE/$NC_DIR/$name")
  if [ "$code" = "201" ] || [ "$code" = "204" ]; then
    echo "✓ Đã đăng: $name  ($code, $(du -h "$file" | cut -f1))"
  else
    echo "✗ Lỗi đăng ($code): $name"; return 1
  fi
}

ROOT="$(cd "$(dirname "$0")" && pwd)"
ensure_dir

if [ "${1:-}" = "--all" ]; then
  shopt -s nullglob
  for f in "$ROOT"/output/preview/*FULLHD*.mp4 "$ROOT"/output/preview/*chunho*.mp4 "$ROOT"/output/preview/*canhnhip*.mp4; do
    put_one "$f"
  done
else
  put_one "${1:?Thiếu đường dẫn file cần đăng}" "${2:-}"
fi

echo "→ Xem trên web: $NC_URL/index.php/apps/files/?dir=/$NC_DIR"
