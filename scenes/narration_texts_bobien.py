"""
Lời thoại — "Bờ biển dài vô hạn" (bông tuyết Koch, cấp số nhân, giới hạn).
Toán 11 · SHORT DỌC 9:16 · ~1 phút 40 · KHÔNG intro.
NGUỒN DUY NHẤT cho: clone_narration_bobien.py + render.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Bờ biển nước ta dài bao nhiêu ki lô mét? "
        "Câu hỏi tưởng chừng đơn giản, nhưng câu trả lời chính xác nhất lại là: dài vô hạn."
    ),
    "02_vande": (
        "Đo bằng thước một trăm ki lô mét, bạn được một con số. "
        "Đổi sang thước một ki lô mét, bờ biển bỗng dài hơn hẳn, "
        "vì thước nhỏ lọt được vào từng vũng, từng mũi đá. "
        "Thước càng nhỏ, con số càng phình to."
    ),
    "03_logic": (
        "Các nhà toán học mô hình hoá bằng bông tuyết Koch. "
        "Mỗi bước, ta thay một đoạn thẳng bằng bốn đoạn nhỏ, mỗi đoạn dài một phần ba. "
        "Đường viền ngày càng gấp khúc, càng chi tiết."
    ),
    "04_tinh": (
        "Sau mỗi bước, chu vi được nhân với bốn phần ba. "
        "Đây là cấp số nhân với công bội lớn hơn một. "
        "Lặp lại mãi, chu vi tiến tới vô hạn."
    ),
    "05_wow": (
        "Nhưng kỳ lạ thay, diện tích bên trong chỉ nhích thêm một chút rồi dừng ở một giá trị hữu hạn. "
        "Một hình có chu vi vô hạn mà diện tích lại hữu hạn. "
        "Đó là lý do mỗi tấm bản đồ ghi độ dài bờ biển một khác."
    ),
    "06_cta": (
        "Những hình lặp lại vô tận như thế được gọi là fractal. "
        "Chúng có trong nén ảnh, ăng ten điện thoại, mạch máu và cả địa hình trong game. "
        "Theo dõi để cùng khám phá thêm nhé."
    ),
}
