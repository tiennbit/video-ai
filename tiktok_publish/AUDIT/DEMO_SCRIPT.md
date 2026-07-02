# Kịch bản video DEMO cho audit TikTok (luồng OAuth + đăng video)

> TikTok yêu cầu 1 **video demo** cho thấy app dùng scope `video.publish` đúng mục đích & tuân thủ.
> Quay màn hình (screen record) ~2–4 phút, không cần lời, có thể thêm chú thích chữ. Nộp link (YouTube unlisted / Drive).
> Quay **rõ ràng, không cắt ghép gây hiểu nhầm**; cho thấy người dùng **chủ động bấm Authorize**.

## Chuẩn bị trước khi quay
- Đã tạo app, điền Client Key/Secret vào `~/.config/toanly/tiktok.env`, thêm tài khoản test (sandbox).
- Có sẵn 1 video ngắn của kênh (vd `gps`) trên Nextcloud `/VideoAI/video/gps.mp4` + `/thongtin/gps.txt`.
- Mở sẵn: cửa sổ terminal + trình duyệt + app TikTok trên điện thoại (để cho thấy video riêng tư đã lên).

---

## Tiếng Việt — phân cảnh

**Cảnh 1 (0:00–0:20) — Giới thiệu.**
Chú thích: "App cá nhân tự đăng video giáo dục của chính mình lên TikTok qua API chính thức."
Cho thấy thư mục dự án + màn hình `python tiktok_publish/publish.py --help`.

**Cảnh 2 (0:20–0:50) — Đăng nhập OAuth.**
Gõ: `python tiktok_publish/publish.py login`. Trình duyệt mở trang **TikTok Authorize**.
Quay rõ: màn hình TikTok liệt kê quyền `video.publish`; người dùng **bấm Authorize**.
Trình duyệt chuyển về `localhost:8723/callback` (trang "Đã nhận phản hồi"). Terminal in "Đăng nhập OK".

**Cảnh 3 (0:50–1:40) — Đăng 1 video.**
Gõ: `python tiktok_publish/publish.py gps`.
Quay log: lấy caption + video → `creator_info` → `video/init` (publish_id) → upload chunk → `status/fetch` → `PUBLISH_COMPLETE`.
Nhấn mạnh: **privacy = SELF_ONLY** (riêng tư).

**Cảnh 4 (1:40–2:20) — Kết quả trên TikTok.**
Mở app TikTok của tài khoản đã cấp quyền → vào hồ sơ → cho thấy video vừa đăng ở chế độ **Chỉ mình tôi (private)**.
Chú thích: "App chưa audit → đăng riêng tư. Sau audit sẽ đổi sang công khai bằng 1 tham số."

**Cảnh 5 (2:20–2:40) — Bảo mật.**
Cho thấy token nằm trong file cục bộ `~/.config/toanly/tiktok.env` (che giá trị), không gửi đi đâu.
Cho thấy trang **TikTok → Ứng dụng đã cấp quyền** để chứng minh người dùng có thể thu hồi bất cứ lúc nào.

---

## English — shot list

**Scene 1 (0:00–0:20) — Intro.** Caption: "Personal app that self-publishes the owner's own educational
videos to TikTok via the official API." Show project folder + `publish.py --help`.

**Scene 2 (0:20–0:50) — OAuth login.** Run `python tiktok_publish/publish.py login`. Browser opens TikTok
**Authorize** screen showing `video.publish`; user **clicks Authorize**. Redirect back to `localhost:8723/callback`;
terminal prints login success.

**Scene 3 (0:50–1:40) — Post one video.** Run `python tiktok_publish/publish.py gps`. Show logs:
fetch caption+video → `creator_info` → `video/init` → chunked upload → `status/fetch` → `PUBLISH_COMPLETE`.
Emphasize **privacy = SELF_ONLY**.

**Scene 4 (1:40–2:20) — Result on TikTok.** Open the TikTok app for the authorized account → profile →
show the newly posted video set to **Only me (private)**. Caption: "Unaudited app → private. After audit,
switch to public via one parameter."

**Scene 5 (2:20–2:40) — Security.** Show tokens in local `~/.config/toanly/tiktok.env` (mask values), never
transmitted. Show **TikTok → Apps with access** proving the user can revoke anytime.
