# Đăng video + mô tả lên Nextcloud

Tự động đẩy **video render xong** kèm **file mô tả riêng từng tập** lên Nextcloud,
rồi **dọn bản staging** khi upload thành công.

## 0. Kiến trúc "ĐÊM CODE / NGÀY RENDER" (tự động)

Tách bạch việc tốn token (code) và việc thuần máy (render):

```
ĐÊM  (phiên Claude): code tập (animation + lời thoại + script giọng) + QA preview + commit
                     → THÊM tập vào hàng đợi:  echo "<slug> <SceneClass>" >> noidung/render_queue.txt
NGÀY (thuần máy):    1 lệnh  →  render + tự đăng từng tập tới khi HẾT hàng đợi:
```

```bash
docker compose up -d                            # 1 lần (container có sẵn manim + giọng + creds)
docker compose exec videoai bash render_queue.sh   # render-drain: chạy tới khi hết video thì DỪNG
```

**Hàng đợi** `noidung/render_queue.txt` — mỗi dòng `<slug> <SceneClass>`; bỏ qua dòng trống/`#`.

`render_queue.sh` cho mỗi tập:
- Đã có trên Nextcloud rồi → bỏ qua + gỡ khỏi queue (idempotent).
- Chưa có → `render_pipeline.sh` (sinh giọng nếu thiếu + render HD + **tự đăng**).
  - Thành công → gỡ khỏi queue, ghi `output/render_done.log`.
  - Lỗi → **GIỮ trong queue**, ghi `output/render_fail.log`, sang tập kế (1 tập lỗi không kẹt cả hàng đợi).
- Hết tập xử lý được → in "HẾT HÀNG ĐỢI" và **thoát** (không phải daemon).
- Có **lock file** chống chạy 2 drain chồng nhau.

> Tự đăng dựa trên `render_pipeline.sh` (PUBLISH=1, xem §2). Container đã mount sẵn các script
> (LF), thư mục `noidung/`, và credential Nextcloud (qua `.env` → `${NC_ENV_FILE}`, KHÔNG commit).

## 1. Cấu hình (1 lần, NẰM NGOÀI repo — không commit)

Credential đọc từ `~/.config/toanly/nextcloud.env`:

```
NC_URL=http://tiennb.com
NC_USER=news1
NC_PASS=********
NC_DIR=VideoAI          # thư mục đích trên Nextcloud (sửa tuỳ ý)
```

> File này KHÔNG nằm trong repo (`.gitignore` đã chặn `*.env`). Mật khẩu KHÔNG
> bao giờ xuất hiện trong code hay git.

## 2. Tự đăng khi render (mặc định BẬT)

`render_pipeline.sh` đã tích hợp bước đăng ở cuối:

```bash
bash render_pipeline.sh gacha GachaVideo        # render HD -> tự đăng Nextcloud
PUBLISH=0 bash render_pipeline.sh gacha GachaVideo   # render mà KHÔNG đăng
```

- Upload **thất bại** thì render vẫn coi là xong và **GIỮ video cục bộ** để đăng lại.
- Bản preview (qua GUI) **không** tự đăng; chỉ bản HD mới đăng.

## 3. Đăng lại thủ công (không render lại)

```bash
bash publish_nextcloud.sh gacha media/videos/gacha_video/1920p60/GachaVideo.mp4
CLEAN_MEDIA=1 bash publish_nextcloud.sh gacha <mp4>   # đăng xong xoá luôn bản render gốc
```

Từ GUI/back-end: `app_backend.run_publish(slug)` (tự lấy MP4 HD mới nhất).

## 4. File thông tin từng tập (CHỈ 2 phần)

Lưu tại `noidung/mota/<slug>.txt`, đúng format:

```
<Title SEO TikTok — gợi tò mò>

#toan #ly #thpt #hsa #tsa
```

- **Title tự seed** từ **câu hỏi gợi tò mò** trong lời thoại hook (câu kết bằng `?`);
  không có `?` → câu đầu; không có lời thoại → `TITLES`/slug.
- Đã có file rồi thì **giữ nguyên** bản bạn tinh chỉnh, không ghi đè.
- Sinh khung thủ công: `python scenes/make_description.py <slug>` (rồi sửa title cho hay).

## 5. Cấu trúc trên Nextcloud

```
<NC_DIR>/                 (mặc định: VideoAI)
├── video/<slug>.mp4      ← chỉ chứa VIDEO
└── thongtin/<slug>.txt   ← chỉ chứa THÔNG TIN (title + hashtag)
```

Đổi tên thư mục con: `NC_VIDEO_DIR=...`, `NC_INFO_DIR=...`. Script tự `MKCOL` nếu chưa có.

## 6. Luồng & an toàn

1. Copy MP4 → `output/upload/<slug>/<slug>.mp4` (staging, đã gitignore).
2. Bảo đảm file thông tin → copy `<slug>.txt` vào staging.
3. Upload video → `video/`, thông tin → `thongtin/`.
4. **Chỉ khi cả hai OK** → xoá staging. Lỗi → giữ nguyên mọi thứ, thoát != 0.
5. Bản render gốc trong `media/` mặc định **được giữ** (đặt `CLEAN_MEDIA=1` để xoá).
