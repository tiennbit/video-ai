#!/usr/bin/env bash
# =============================================================================
# render_queue.sh — DRAIN hàng đợi render (chạy BAN NGÀY, thuần máy, KHÔNG Claude).
#
# Kiến trúc "đêm code / ngày render":
#   - ĐÊM: phiên Claude code tập (animation + lời thoại + script giọng) + QA preview,
#          rồi GHI tập vào hàng đợi:  echo "<slug> <SceneClass>" >> noidung/render_queue.txt
#   - NGÀY: chạy script này. Nó đọc hàng đợi, render + tự đăng từng tập tới khi HẾT thì thoát.
#
# Mỗi tập:
#   1) Đã có trên Nextcloud rồi  -> bỏ qua (idempotent) + gỡ khỏi queue.
#   2) Chưa có -> render_pipeline.sh <slug> <Scene> (PUBLISH=1: sinh giọng nếu thiếu +
#      render HD + tự đăng). Thành công -> gỡ khỏi queue + ghi render_done.log.
#      Lỗi -> GIỮ trong queue + ghi render_fail.log, sang tập kế (không kẹt cả hàng đợi).
#   3) Hết tập xử lý được -> in "HẾT HÀNG ĐỢI" và THOÁT (không phải daemon).
#
# Chạy (1 lệnh):  docker compose exec videoai bash render_queue.sh
#
# Biến môi trường (tuỳ chọn):
#   NEXTCLOUD_ENV=...  ghi đè đường dẫn file cấu hình (mặc định ~/.config/toanly/nextcloud.env)
# =============================================================================
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

QUEUE="noidung/render_queue.txt"
DONE_LOG="output/render_done.log"
FAIL_LOG="output/render_fail.log"
LOCK_FILE="output/.render_queue.lock"
LOCK_DIR="output/.render_queue.lock.d"
NC_ENV="${NEXTCLOUD_ENV:-$HOME/.config/toanly/nextcloud.env}"

ts() { date '+%Y-%m-%d %H:%M:%S'; }

# ---------- LOCK: chống chạy 2 tiến trình drain chồng nhau ----------
mkdir -p output
if command -v flock >/dev/null 2>&1; then
  exec 9>"$LOCK_FILE"
  if ! flock -n 9; then
    echo "Đã có tiến trình render-drain khác đang chạy — thoát."
    exit 0
  fi
else
  if ! mkdir "$LOCK_DIR" 2>/dev/null; then
    echo "Đã có tiến trình render-drain khác đang chạy — thoát."
    exit 0
  fi
  trap 'rmdir "$LOCK_DIR" 2>/dev/null || true' EXIT
fi

# ---------- kiểm tra 1 tập đã có trên Nextcloud chưa ----------
already_published() {  # trả 0 nếu /<NC_DIR>/<video>/<slug>.mp4 đã tồn tại
  local slug="$1"
  [ -f "$NC_ENV" ] || return 1
  local code
  code=$(
    set -a; . "$NC_ENV"; set +a
    local vdir="${NC_VIDEO_DIR:-video}"
    curl -s -o /dev/null -w "%{http_code}" --max-time 30 \
      -u "$NC_USER:$NC_PASS" -X PROPFIND -H "Depth: 0" \
      "$NC_URL/remote.php/dav/files/$NC_USER/$NC_DIR/$vdir/$slug.mp4"
  )
  [ "$code" = "207" ] || [ "$code" = "200" ]
}

# ---------- gỡ MỌI dòng có slug khớp khỏi queue ----------
remove_from_queue() {
  local slug="$1"
  awk -v s="$slug" '{ l=$0; sub(/#.*/,"",l); n=split(l,a," "); if (n>0 && a[1]==s) next; print }' \
    "$QUEUE" > "$QUEUE.tmp" && mv "$QUEUE.tmp" "$QUEUE"
}

# ---------- lấy dòng hợp lệ ĐẦU TIÊN chưa nằm trong danh sách đã-lỗi-phiên-này ----------
PROCESSED_FAIL=" "
pick_next() {
  local raw l s
  while IFS= read -r raw || [ -n "$raw" ]; do
    l="${raw%%#*}"                       # bỏ comment
    l="$(printf '%s' "$l" | awk '{$1=$1};1')"   # trim + gom khoảng trắng
    [ -z "$l" ] && continue
    s="$(printf '%s' "$l" | awk '{print $1}')"
    case "$PROCESSED_FAIL" in *" $s "*) continue;; esac
    printf '%s' "$l"
    return 0
  done < "$QUEUE"
  return 1
}

# ---------- MAIN ----------
if [ ! -f "$QUEUE" ]; then
  echo "Không thấy hàng đợi $QUEUE — không có việc. Thoát."
  exit 0
fi

echo "==> RENDER-DRAIN bắt đầu — $(ts)"
n_done=0; n_skip=0; n_fail=0

while line="$(pick_next || true)"; [ -n "$line" ]; do
  slug="$(printf '%s' "$line" | awk '{print $1}')"
  scene="$(printf '%s' "$line" | awk '{print $2}')"
  echo "================ $slug / ${scene:-?} — $(ts) ================"

  if [ -z "$scene" ]; then
    echo "  ✗ Dòng thiếu SceneClass -> bỏ qua (giữ trong queue)."
    echo "$(ts) FAIL(no_scene) $slug" >> "$FAIL_LOG"
    PROCESSED_FAIL="$PROCESSED_FAIL$slug "; n_fail=$((n_fail+1)); continue
  fi

  if already_published "$slug"; then
    echo "  ↪ ĐÃ ĐĂNG trước đó -> gỡ khỏi queue, bỏ qua."
    remove_from_queue "$slug"
    echo "$(ts) SKIP(already) $slug $scene" >> "$DONE_LOG"
    n_skip=$((n_skip+1)); continue
  fi

  echo "  ▶ render_pipeline.sh $slug $scene (PUBLISH=1)…"
  if PUBLISH=1 bash render_pipeline.sh "$slug" "$scene"; then
    if already_published "$slug"; then
      remove_from_queue "$slug"
      echo "$(ts) DONE $slug $scene" >> "$DONE_LOG"
      echo "  ✓ XONG + ĐÃ ĐĂNG -> gỡ khỏi queue."
      n_done=$((n_done+1))
    else
      echo "  ✗ Render xong nhưng KHÔNG thấy trên Nextcloud -> giữ trong queue."
      echo "$(ts) FAIL(not_on_server) $slug $scene" >> "$FAIL_LOG"
      PROCESSED_FAIL="$PROCESSED_FAIL$slug "; n_fail=$((n_fail+1))
    fi
  else
    echo "  ✗ LỖI render/đăng -> giữ trong queue, sang tập kế."
    echo "$(ts) FAIL(render) $slug $scene" >> "$FAIL_LOG"
    PROCESSED_FAIL="$PROCESSED_FAIL$slug "; n_fail=$((n_fail+1))
  fi
done

remain=$(awk '{l=$0; sub(/#.*/,"",l); if (l ~ /[^[:space:]]/) c++} END{print c+0}' "$QUEUE")
echo "==> HẾT HÀNG ĐỢI — $(ts)"
echo "    Đã đăng mới: $n_done | Bỏ qua (đã có): $n_skip | Lỗi giữ lại: $n_fail | Còn trong queue: $remain"
exit 0
