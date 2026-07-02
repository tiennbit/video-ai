# Privacy Policy — Toán Lý Đời Thực Poster

_Cập nhật lần cuối / Last updated: 2026-07-02_
_Liên hệ / Contact: ngbatienth@gmail.com — https://tiennb.com_

> Bản này dùng để **host lên site của bạn** (ví dụ `https://tiennb.com/tiktok/privacy.html`)
> và điền URL đó vào phần **Privacy Policy URL** khi tạo app TikTok. Sửa tên/email/domain cho khớp.

---

## Tiếng Việt

**1. Ứng dụng này là gì.** "Toán Lý Đời Thực Poster" là công cụ cá nhân giúp chủ kênh **tự đăng video giáo dục
do chính mình sản xuất** lên tài khoản TikTok của chính mình, thông qua Content Posting API chính thức của TikTok.

**2. Dữ liệu chúng tôi truy cập.** Khi bạn cấp quyền qua TikTok, ứng dụng nhận:
- **Access token / refresh token** (để đăng video thay bạn) và **open_id** (định danh tài khoản).
- Thông tin cơ bản hồ sơ (qua `user.info.basic`) và **cài đặt đăng** (qua `creator_info`: mức riêng tư cho phép,
  bật/tắt bình luận, duet, stitch, thời lượng tối đa) — chỉ để dựng bài đăng hợp lệ.
Ứng dụng **không** thu thập danh bạ, tin nhắn, mật khẩu, hay dữ liệu người dùng khác.

**3. Cách dùng dữ liệu.** Token chỉ được dùng để gọi các endpoint đăng video của TikTok
(`creator_info/query`, `video/init`, upload, `status/fetch`). Nội dung đăng (video + phần mô tả) là do chính
chủ tài khoản tạo ra.

**4. Lưu trữ.** Token được lưu **cục bộ trên máy của chủ kênh** trong file cấu hình có quyền hạn chế
(`~/.config/toanly/tiktok.env`, chmod 600). **Không** gửi lên máy chủ bên thứ ba, **không** chia sẻ với ai.

**5. Chia sẻ với bên thứ ba.** Không. Dữ liệu chỉ trao đổi trực tiếp giữa máy của bạn và API của TikTok.

**6. Lưu giữ & xoá.** Token tồn tại tới khi bạn thu hồi quyền hoặc xoá file cấu hình. Bạn có thể thu hồi quyền
bất cứ lúc nào tại **Cài đặt TikTok → Bảo mật → Ứng dụng đã cấp quyền**, và xoá file `tiktok.env` để xoá token cục bộ.

**7. Trẻ em.** Ứng dụng không hướng tới người dưới 13 tuổi và không cố ý thu thập dữ liệu của trẻ em.

**8. Thay đổi.** Nếu chính sách thay đổi, bản cập nhật sẽ đăng tại cùng URL kèm ngày cập nhật mới.

**9. Liên hệ.** Mọi câu hỏi: ngbatienth@gmail.com.

---

## English

**1. What this app is.** "Toán Lý Đời Thực Poster" is a personal tool that lets the channel owner
**self-publish their own educational videos** to their own TikTok account via TikTok's official Content Posting API.

**2. Data we access.** With your authorization, the app receives:
- an **access/refresh token** (to post videos on your behalf) and your **open_id** (account identifier);
- basic profile info (`user.info.basic`) and **posting settings** (`creator_info`: allowed privacy levels,
  comment/duet/stitch toggles, max duration) — solely to build a valid post.
The app does **not** collect contacts, messages, passwords, or any other user data.

**3. How we use it.** Tokens are used only to call TikTok's posting endpoints
(`creator_info/query`, `video/init`, upload, `status/fetch`). The posted content (video + description)
is created by the account owner.

**4. Storage.** Tokens are stored **locally on the owner's machine** in a restricted config file
(`~/.config/toanly/tiktok.env`, chmod 600). They are **not** sent to any third-party server and **not** shared.

**5. Third-party sharing.** None. Data flows only between your machine and TikTok's API.

**6. Retention & deletion.** Tokens persist until you revoke access or delete the config file. You may revoke
access anytime in **TikTok Settings → Security → Apps that have access**, and delete `tiktok.env` to remove
local tokens.

**7. Children.** The app is not directed to children under 13 and does not knowingly collect their data.

**8. Changes.** Updates will be posted at the same URL with a new "last updated" date.

**9. Contact.** ngbatienth@gmail.com.
