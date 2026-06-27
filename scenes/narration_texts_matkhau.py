"""
Lời thoại — "Mật khẩu của bạn bị bẻ trong bao lâu?" (quy tắc đếm / tổ hợp).
Toán 11 (quy tắc đếm, tổ hợp) · ứng dụng đời thực · SHORT DỌC 9:16, ~2 phút · KHÔNG intro.

NGUỒN DUY NHẤT cho: clone_narration_matkhau.py + karaoke (matkhau_video.py).
Số liệu (minh hoạ, nêu rõ trong video): bảng ~95 ký tự in được; số khả năng = 95^(độ dài);
thêm 2 ký tự → số khả năng gấp 95^2 ≈ 9000 lần; máy dò ~tỉ phép/giây.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để karaoke chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Mật khẩu của bạn có bao nhiêu ký tự? "
        "Tám, hay mười? "
        "Nghe thì chỉ hơn nhau có hai ký tự. "
        "Nhưng với một cỗ máy dò mật khẩu, "
        "một cái bị bẻ trong vài giờ, còn cái kia phải mất hàng nghìn năm. "
        "Toán tổ hợp giải thích khoảng cách khổng lồ đó."
    ),
    "02_vande": (
        "Hãy hình dung kẻ tấn công không hề thông minh. "
        "Nó chỉ thử mọi mật khẩu có thể, từng cái một, cho tới khi trúng. "
        "Vậy câu hỏi thật sự là: có tất cả bao nhiêu mật khẩu khác nhau cần thử? "
        "Đây chính là một bài toán đếm."
    ),
    "03_mohinh": (
        "Mỗi ô trong mật khẩu được chọn từ một bảng ký tự. "
        "Chữ thường, chữ hoa, chữ số và ký hiệu, "
        "cộng lại khoảng chín mươi lăm ký tự in được. "
        "Theo quy tắc nhân: ô thứ nhất có chín mươi lăm cách, "
        "ô thứ hai cũng chín mươi lăm cách, và cứ thế nhân lên. "
        "Mật khẩu dài l ký tự sẽ có chín mươi lăm mũ l khả năng."
    ),
    "04_conso": (
        "Giờ thay số vào. "
        "Mật khẩu tám ký tự cho chín mươi lăm mũ tám, "
        "khoảng sáu nghìn sáu trăm nghìn tỉ khả năng. "
        "Mật khẩu mười ký tự cho chín mươi lăm mũ mười. "
        "Chỉ thêm đúng hai ký tự, số khả năng đã gấp chín mươi lăm bình phương, "
        "tức là khoảng chín nghìn lần."
    ),
    "05_ynghia": (
        "Hãy thử với một cỗ máy dò khoảng một tỉ mật khẩu mỗi giây. "
        "Loại tám ký tự có thể bị quét cạn trong vài giờ. "
        "Nhưng loại mười ký tự, gấp chín nghìn lần, "
        "thì kéo dài thành hàng nghìn năm. "
        "Mỗi ký tự bạn thêm vào là một lần nhân với chín mươi lăm, "
        "khiến công sức của kẻ tấn công bùng nổ theo cấp số nhân."
    ),
    "06_cta": (
        "Vậy nên độ dài quan trọng hơn bạn tưởng rất nhiều. "
        "Thêm vài ký tự, bạn biến vài giờ thành nhiều thế kỷ. "
        "Theo dõi để hiểu Toán Lý đang âm thầm vận hành quanh ta."
    ),
}
