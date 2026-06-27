"""
Sinh lời thoại tiếng Việt cho video parabol bằng edge-tts.

Chạy:  .venv/bin/python scenes/narration_parabol.py

Đổi giọng:  VOICE = "vi-VN-NamMinhNeural" (nam) hoặc "vi-VN-HoaiMyNeural" (nữ).
File mp3 xuất ra: output/narration/<id>.mp3
"""
import asyncio
import os

import edge_tts

VOICE = "vi-VN-HoaiMyNeural"   # nữ, rõ ràng — hợp học sinh lớp 10
RATE = "-6%"                   # chậm lại một chút cho dễ nghe
OUT = os.path.join(os.path.dirname(__file__), "..", "output", "narration")

# id -> câu thoại. id dùng làm tên file và được scene tham chiếu.
SEGMENTS = {
    "01_hook": (
        "Vì sao tia nước lại cong thành hình vòng cung đẹp mắt như thế này? "
        "Câu trả lời nằm gọn trong Toán lớp mười."
    ),
    "02_curve": (
        "Khi nước phun lên rồi rơi xuống, nó vạch ra một đường cong đặc biệt, "
        "gọi là parabol. Đó chính là đồ thị của hàm số bậc hai."
    ),
    "03_vertex": (
        "Điểm cao nhất của parabol được gọi là đỉnh. "
        "Tại đỉnh, tia nước đạt độ cao lớn nhất, rồi mới rơi xuống."
    ),
    "04_formula": (
        "Mọi parabol đều có dạng: y bằng a nhân x bình phương, cộng b nhân x, cộng c. "
        "Vì hệ số a nhỏ hơn không, nên parabol có bề lõm quay xuống dưới."
    ),
    "05_apply": (
        "Quả bóng rổ, chùm pháo hoa, hay đài phun nước, tất cả đều bay theo quỹ đạo parabol. "
        "Toán học hiện diện quanh ta mỗi ngày. "
        "Hãy theo dõi kênh để cùng khám phá thêm nhé!"
    ),
}


async def synth(text, path, retries=6):
    """edge-tts thỉnh thoảng trả NoAudioReceived (lỗi server tạm thời) -> retry."""
    last = None
    for attempt in range(1, retries + 1):
        try:
            await edge_tts.Communicate(text, VOICE, rate=RATE).save(path)
            if os.path.getsize(path) > 1000:   # file hợp lệ
                return attempt
            raise RuntimeError("file rỗng")
        except Exception as e:  # noqa: BLE001
            last = e
            await asyncio.sleep(1.2 * attempt)  # backoff tăng dần
    raise RuntimeError(f"Thất bại sau {retries} lần: {last}")


async def main():
    os.makedirs(OUT, exist_ok=True)
    for name, text in SEGMENTS.items():
        path = os.path.abspath(os.path.join(OUT, f"{name}.mp3"))
        n = await synth(text, path)
        print(f"✓ {name}.mp3  (lần thử {n})")
        await asyncio.sleep(0.4)   # nghỉ nhẹ giữa các đoạn, tránh bị chặn


if __name__ == "__main__":
    asyncio.run(main())
