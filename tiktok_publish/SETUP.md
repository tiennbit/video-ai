# Hướng dẫn tạo app TikTok & chạy đăng video (Content Posting API)

> Mục tiêu: đăng video lên TikTok bằng **API chính thức**, chạy ngay ở chế độ **riêng tư SELF_ONLY**
> (không cần audit). Sau khi app qua audit thì đổi 1 tham số sang `PUBLIC_TO_EVERYONE`.
>
> ⚠️ Giao diện developers.tiktok.com có thể đổi tên nút theo thời gian — bám theo **ý** từng bước.
> Tài liệu gốc: https://developers.tiktok.com/doc/content-posting-api-get-started

---

## 0. Cần có trước
- 1 tài khoản **TikTok** (chính là kênh sẽ đăng).
- **Python 3.10+** trên máy. Cài thư viện: `pip install -r tiktok_publish/requirements.txt`.

## 1. Đăng ký tài khoản nhà phát triển
1. Vào **https://developers.tiktok.com** → góc phải bấm **Log in** → đăng nhập bằng chính tài khoản TikTok của bạn.
2. Lần đầu sẽ yêu cầu đăng ký developer: điền tên, email, đồng ý điều khoản → xác nhận email.

## 2. Tạo app
1. Menu trên cùng: **Manage apps** → **Connect an app** (hoặc **Create an app**).
2. Điền:
   - **App name**: ví dụ `Toan Ly Doi Thuc Poster`
   - **Category / Description**: mô tả ngắn (giáo dục, tự đăng video của chính chủ).
   - **Terms of Service URL** và **Privacy Policy URL**: dùng link bạn sẽ host (xem `AUDIT/PRIVACY_POLICY.md`,
     ví dụ `https://tiennb.com/tiktok/privacy.html`). *Có thể điền tạm rồi sửa sau.*
3. Lưu.

## 3. Bật sản phẩm "Content Posting API" + quyền
1. Trong trang app → mục **Products** / **Add products** → thêm **Content Posting API**.
2. Trong cấu hình Content Posting API, **bật Direct Post** (đăng thẳng lên hồ sơ; khác với "Upload" chỉ đẩy vào hộp thư nháp).
3. Mục **Scopes** → tick:
   - `video.publish`  ← BẮT BUỘC để đăng trực tiếp
   - `user.info.basic` (khuyến nghị)

## 4. Cấu hình Redirect URI (PHẢI khớp script)
1. Trong app (mục **Login Kit** hoặc **Redirect URI**) → thêm đúng:
   ```
   http://localhost:8723/callback
   ```
2. Đây chính là giá trị `TIKTOK_REDIRECT_URI` script dùng. Nếu bạn đổi cổng, phải sửa cả 2 nơi cho khớp.

## 5. Thêm tài khoản test (Sandbox) — để đăng được khi CHƯA audit
- App chưa audit chỉ đăng được **SELF_ONLY** và chỉ cho **tài khoản đã thêm làm target user**.
- Vào mục **Sandbox / Target users / Testers** của app → **thêm chính tài khoản TikTok của bạn**
  (thường phải xác nhận trên app TikTok điện thoại).

## 6. Lấy Client Key & Client Secret
- Trong trang app, mục **App details / Credentials**: copy **Client key** và **Client secret**.
- ⚠️ **KHÔNG dán vào code, KHÔNG commit.** Chỉ đưa vào file env ở bước 7.

## 7. Tạo file cấu hình (NGOÀI repo — không commit)
Tạo file `~/.config/toanly/tiktok.env` (Windows: `C:\Users\TienNB\.config\toanly\tiktok.env`)
với nội dung — **điền 2 dòng key/secret bằng giá trị thật ở bước 6**:
```
TIKTOK_CLIENT_KEY=<DÁN Client key>
TIKTOK_CLIENT_SECRET=<DÁN Client secret>
TIKTOK_REDIRECT_URI=http://localhost:8723/callback
TIKTOK_PRIVACY_LEVEL=SELF_ONLY
```
Các dòng token (ACCESS/REFRESH...) **để trống** — script tự ghi sau khi login.
> Tạo nhanh bằng lệnh (thay `<...>` rồi chạy trong Git Bash):
> ```bash
> mkdir -p ~/.config/toanly && cat > ~/.config/toanly/tiktok.env <<'EOF'
> TIKTOK_CLIENT_KEY=<DÁN Client key>
> TIKTOK_CLIENT_SECRET=<DÁN Client secret>
> TIKTOK_REDIRECT_URI=http://localhost:8723/callback
> TIKTOK_PRIVACY_LEVEL=SELF_ONLY
> EOF
> chmod 600 ~/.config/toanly/tiktok.env
> ```

## 8. Đăng nhập OAuth lần đầu
```bash
python tiktok_publish/publish.py login
```
- Script mở trình duyệt tới trang TikTok → bấm **Authorize**.
- Trình duyệt chuyển về `localhost:8723/callback` (trang báo "Đã nhận phản hồi").
- Token lưu vào `~/.config/toanly/tiktok.env`. Script tự **refresh** khi hết hạn (không cần login lại).

## 9. Đăng video
```bash
python tiktok_publish/publish.py gps        # đăng 1 tập (video + caption lấy từ Nextcloud)
python tiktok_publish/publish.py --queue    # đăng mọi video trên Nextcloud chưa đăng TikTok
python tiktok_publish/publish.py --list     # xem tình trạng
```
- Video ở chế độ **riêng tư (SELF_ONLY)** — chỉ bạn thấy trong app TikTok, để kiểm tra trước.

## 10. Sau khi app QUA AUDIT → mở public
- Nộp audit theo hồ sơ trong `AUDIT/` (privacy policy + mô tả dữ liệu + video demo).
- Khi được duyệt: sửa 1 dòng trong `tiktok.env`:
  ```
  TIKTOK_PRIVACY_LEVEL=PUBLIC_TO_EVERYONE
  ```
- Chạy lại `--queue`, video sẽ đăng công khai. **Không cần sửa code.**

---

## Việc BẠN cần tự làm (script không làm thay được)
| # | Việc | Ở đâu |
|---|------|-------|
| 1 | Đăng ký developer + tạo app | developers.tiktok.com |
| 2 | Bật Content Posting API + scope `video.publish` + Direct Post | trang app |
| 3 | Thêm Redirect URI `http://localhost:8723/callback` | trang app |
| 4 | Thêm tài khoản TikTok của bạn làm target user (sandbox) | trang app |
| 5 | Copy Client Key/Secret → điền vào `~/.config/toanly/tiktok.env` | máy bạn |
| 6 | Host Privacy Policy lên tiennb.com (lấy URL điền vào app) | site của bạn |
| 7 | Quay video demo + nộp audit (khi muốn public) | trang app |
