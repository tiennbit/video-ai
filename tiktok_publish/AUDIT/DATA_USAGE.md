# Mô tả sử dụng dữ liệu & phạm vi quyền (cho hồ sơ audit TikTok)

> Dùng để **điền vào form audit** của TikTok ("how does your app use this scope / data").
> Copy các đoạn tương ứng khi TikTok hỏi từng scope.

## Tiếng Việt

### Bảng ánh xạ scope → mục đích → endpoint
| Scope | Vì sao cần | Endpoint gọi | Lưu gì |
|-------|-----------|--------------|--------|
| `video.publish` | Đăng trực tiếp video do chính chủ kênh sản xuất lên tài khoản của họ | `POST /v2/post/publish/video/init/`, `PUT <upload_url>`, `POST /v2/post/publish/status/fetch/` | không lưu nội dung; chỉ token cục bộ |
| `user.info.basic` | Xác nhận đúng tài khoản đã cấp quyền (open_id) | trả về cùng token; (tuỳ chọn) `creator_info/query` | open_id (cục bộ) |

### Luồng dữ liệu (không có máy chủ trung gian)
```
Máy của chủ kênh  ──OAuth──▶  TikTok (đăng nhập + cấp quyền)
                  ◀─token───
Máy của chủ kênh  ──creator_info/query─▶  TikTok  (lấy quyền đăng hợp lệ)
Máy của chủ kênh  ──video/init─────────▶  TikTok  (post_info + kích thước file)
Máy của chủ kênh  ──PUT file (Content-Range)▶ upload_url  (tải video)
Máy của chủ kênh  ──status/fetch───────▶  TikTok  (chờ PUBLISH_COMPLETE)
```
- **Không** có server bên thứ ba. Mọi lời gọi đi thẳng từ máy chủ kênh tới API TikTok qua HTTPS.
- Video & phần mô tả do **chính chủ kênh** tạo (nội dung giáo dục Toán/Lý), lấy từ kho riêng của họ (Nextcloud).

### Lưu trữ & bảo mật token
- access/refresh token lưu **cục bộ** tại `~/.config/toanly/tiktok.env` (chmod 600). Không truyền đi đâu khác.
- Token tự refresh bằng refresh_token; chủ kênh có thể thu hồi quyền bất cứ lúc nào trong cài đặt TikTok.

### Không dùng
Không thu thập/không dùng: danh bạ, tin nhắn trực tiếp, dữ liệu người dùng khác, quảng cáo, bán dữ liệu.

---

## English

### Scope → purpose → endpoint
| Scope | Why needed | Endpoints | Stored |
|-------|-----------|-----------|--------|
| `video.publish` | Directly publish the owner's own videos to their own account | `POST /v2/post/publish/video/init/`, `PUT <upload_url>`, `POST /v2/post/publish/status/fetch/` | no content stored; local token only |
| `user.info.basic` | Confirm the authorized account (open_id) | returned with token; optional `creator_info/query` | open_id (local) |

### Data flow (no intermediary server)
```
Owner's machine  ──OAuth──▶  TikTok (login + consent)
                 ◀─token───
Owner's machine  ──creator_info/query─▶ TikTok (fetch valid posting options)
Owner's machine  ──video/init────────▶ TikTok (post_info + file size)
Owner's machine  ──PUT file (Content-Range)▶ upload_url (upload video)
Owner's machine  ──status/fetch──────▶ TikTok (await PUBLISH_COMPLETE)
```
- **No** third-party server. All calls go directly from the owner's machine to TikTok over HTTPS.
- Videos & captions are created by the **owner** (educational math/physics content), taken from their own storage.

### Token storage & security
- Access/refresh tokens are stored **locally** at `~/.config/toanly/tiktok.env` (chmod 600), never transmitted elsewhere.
- Tokens auto-refresh via the refresh token; the owner can revoke access anytime in TikTok settings.

### Not used
No collection/use of: contacts, direct messages, other users' data, advertising, or data selling.
