# TẬP 1 — "Bí mật của Cấp số nhân" · SHORT DỌC 9:16

> **Trạng thái:** đã code xong & verify. Mã nguồn là nguồn chính:
> `scenes/laikep_video.py` (class `LaiKepVideo`) + template `scenes/brand.py`.
> Lời thoại: `scenes/narration_texts_laikep.py` (KHÔNG viết lại lời ở scene).

## Thông số kỹ thuật
| Mục | Giá trị |
|---|---|
| Định dạng | **DỌC 9:16 (1080×1920)** — Reels / TikTok / YouTube Shorts |
| Khung Manim | `config.frame_width = 4.5`, `frame_height = 8` (ép trong brand.py) → x ∈ [−2.25, 2.25], y ∈ [−4, 4] |
| Lệnh render | `.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/laikep_video.py LaiKepVideo` |
| Xem trước | `.venv/bin/manim -ql --resolution 540,960 --fps 12 scenes/laikep_video.py LaiKepVideo` (im lặng, fallback thời lượng) |
| Font | `Arial` (Pango). Chỉ `Text`, KHÔNG `MathTex` (chưa cài LaTeX) |
| Giọng | clone của user → `output/narration_laikep/<id>.wav`; sinh bằng `~/voxcpm-venv/bin/python scenes/clone_narration_laikep.py` |
| Thời lượng | ~50–60s (4 segment). Bản preview fallback ≈ 1:04 — sẽ khớp lại khi có giọng thật |

## 4 beat (xếp DỌC, chữ to)
| Beat | Segment | Nội dung hình |
|---|---|---|
| 1 · Hook | `01_hook` | "1đ" khổng lồ + "×2 mỗi ngày" + "×30 ngày" + "= ?" xếp dọc |
| 2 · Build | `02_build` | badge "mỗi bước ×2" + dãy `1 2 4 8 16 32` + đồ thị mũ vọt "dựng đứng!" |
| 3 · Payoff | `03_payoff` | đếm số → **1.073.741.823đ** + "= LÃI KÉP" + 2 chip xếp dọc: TIẾT KIỆM ↑×7 / NỢ ↑ phình to |
| 4 · CTA | `04_cta` | "Lặp lại > Bắt đầu lớn" + nút ĐĂNG KÝ |

Mỗi video bọc sẵn: **intro vẹt "Vẹc-tơ" + "Bạn là một con vẹt à?"** (đầu) và **brand stinger** (cuối) từ `brand.py`. Khung template: thanh chủ đề trên-trái, thanh tiến trình trên cùng, watermark vẹt nhỏ trên-phải.

## Checklist khớp tiếng
- [ ] Sinh đủ 4 file `output/narration_laikep/<id>.wav` trước khi render full.
- [ ] Mỗi beat bọc `with self.voice("<id>")`; karaoke `make_karaoke(..., self.beat_t0)`.
- [ ] `add_sound` dùng `time_offset=0` (relative — đã xử lý trong `voice()`).
- [ ] Nếu có giọng mà tổng > 60s → rút bớt lời trong `narration_texts_laikep.py`.

## Cắt thêm (tùy chọn)
- Phiên bản 15–20s "siêu ngắn": chỉ beat Hook + Payoff (con số 1 tỉ) — để test hook trên TikTok.
