# tiktok_publish — Đăng TikTok qua Content Posting API (chính thức)

Đẩy video của kênh (đang ở Nextcloud `/VideoAI`) lên TikTok bằng **API chính thức của TikTok**,
mặc định **SELF_ONLY** (riêng tư) để chạy ngay **không cần audit**. Đổi 1 tham số sang public sau khi audit.

> Chỉ dùng API chính thức: **không** browser automation, **không** giả chữ ký. Mọi bí mật nằm NGOÀI repo.

## Cài & dùng nhanh
```bash
pip install -r tiktok_publish/requirements.txt
# (làm theo SETUP.md để tạo app + điền key vào ~/.config/toanly/tiktok.env)
python tiktok_publish/publish.py login      # lấy token OAuth (1 lần)
python tiktok_publish/publish.py gps         # đăng 1 tập
python tiktok_publish/publish.py --queue     # đăng mọi tập chưa đăng
python tiktok_publish/publish.py --list      # xem tình trạng
```
👉 Từng bước tạo app: **[SETUP.md](SETUP.md)**. Hồ sơ audit: **[AUDIT/](AUDIT/)**.

## Cấu trúc
| File | Vai trò |
|------|---------|
| `config.py` | endpoint API + nạp/ghi token env (`~/.config/toanly/tiktok.env`, ngoài repo) |
| `oauth.py` | OAuth: authorize URL, local callback server, đổi code → token, tự refresh |
| `nextcloud_src.py` | lấy video (local `media/` hoặc tải Nextcloud) + caption (`/VideoAI/thongtin/<slug>.txt`) |
| `tiktok_api.py` | creator_info → video/init → upload theo Content-Range → poll status |
| `publish.py` | CLI: `login` / `<slug>` / `--queue` / `--list`; chống trùng qua log |
| `tests/test_logic.py` | test THUẦN LOGIC (chunk, Content-Range, parse, caption) — không cần key |

## Luồng đăng (direct post)
1. `creator_info/query` → lấy quyền (privacy options, comment/duet/stitch, thời lượng max).
2. `video/init` → gửi `post_info` (title=caption, privacy=SELF_ONLY, tôn trọng cài đặt account) +
   `source_info` (FILE_UPLOAD, video_size, chunk_size, total_chunk_count) → nhận `publish_id` + `upload_url`.
3. `PUT upload_url` → tải file theo `Content-Range` (video kênh ~3–5MB → 1 chunk; file >64MB tự chia 10MB).
4. `status/fetch` → poll tới `PUBLISH_COMPLETE`.
5. Ghi `~/.config/toanly/tiktok_posted.log` để không đăng trùng.

## Bí mật & an toàn
- Client Key/Secret + token: `~/.config/toanly/tiktok.env` (`.gitignore` chặn `*.env`). **Không commit.**
- Tái dùng credential Nextcloud (`nextcloud.env`) để lấy video/caption.

## Đổi sang PUBLIC (sau audit)
Sửa `TIKTOK_PRIVACY_LEVEL=PUBLIC_TO_EVERYONE` trong `tiktok.env` — không sửa code.

## Chạy test
```bash
cd tiktok_publish && python -m pytest -q
```
