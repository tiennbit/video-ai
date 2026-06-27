"""
Lời thoại tiếng Việt cho video parabol — NGUỒN DUY NHẤT.
Dùng chung cho: sinh giọng (clone_narration.py) và phụ đề karaoke (parabol_video_v2.py),
để chữ trên màn hình khớp tuyệt đối với giọng đọc.
"""

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

# Bản ĐỌC (TTS) — phiên âm chữ cái/ký hiệu để máy đọc ĐÚNG.
# Máy TTS hay đọc sai chữ cái Latin đơn lẻ (x -> "xích", c -> "xê/cờ"...),
# nên ở đây viết phiên âm tiếng Việt: x -> "ích", b -> "bê", c -> "xê".
# Phụ đề karaoke vẫn dùng SEGMENTS (hiển thị "x", "b", "c" cho đúng ký hiệu toán).
SPOKEN_OVERRIDES = {
    "04_formula": (
        "Mọi parabol đều có dạng: y bằng a nhân ích bình phương, "
        "cộng bê nhân ích, cộng xê. "
        "Vì hệ số a nhỏ hơn không, nên parabol có bề lõm quay xuống dưới."
    ),
}


def tts_text(seg_id):
    """Văn bản để máy ĐỌC (ưu tiên bản phiên âm nếu có)."""
    return SPOKEN_OVERRIDES.get(seg_id, SEGMENTS[seg_id])
