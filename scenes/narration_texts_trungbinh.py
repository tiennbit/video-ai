"""
Lời thoại — "Lương trung bình 50 triệu nhưng 90% nhân viên không hề có?" (số trung bình vs trung vị, ảnh hưởng của giá trị ngoại lệ).
Toán 10 (Thống kê: số trung bình, trung vị, ngoại lệ) · ứng dụng đời thực · SHORT DỌC 9:16, ~1.8 phút · KHÔNG intro.

NGUỒN DUY NHẤT cho: clone_narration_trungbinh.py + karaoke (trungbinh_video.py).
Số liệu (minh hoạ, nêu rõ trong video): công ty 10 người, 9 người lương 15 triệu, 1 sếp 400 triệu
→ trung bình ~ 53,5 triệu; trung vị 15 triệu.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Một công ty đăng tin tuyển dụng: lương trung bình năm mươi ba triệu một tháng. "
        "Nghe quá hấp dẫn, bạn nộp hồ sơ ngay. "
        "Nhưng vào làm rồi mới biết: chín trên mười người ở đây không hề có mức lương đó. "
        "Con số không sai. Vậy nó đã đánh lừa bạn bằng cách nào?"
    ),
    "02_vande": (
        "Hãy nhìn vào bảng lương thật của công ty mười người này. "
        "Chín nhân viên, mỗi người mười lăm triệu một tháng. "
        "Còn người thứ mười là sếp, lương bốn trăm triệu. "
        "Tất cả đều thật, không ai nói dối. Vấn đề nằm ở cách ta gộp chúng lại thành một con số."
    ),
    "03_mohinh": (
        "Số trung bình được tính bằng cách cộng hết tất cả lương rồi chia cho số người. "
        "Cộng chín người mười lăm triệu với một người bốn trăm triệu, ta được năm trăm ba mươi lăm triệu. "
        "Chia cho mười, ra trung bình khoảng năm mươi ba triệu rưỡi mỗi người. "
        "Chỉ một con số khổng lồ đã kéo cả trung bình vọt lên."
    ),
    "04_consso": (
        "Giờ ta thử một thước đo khác: trung vị. "
        "Xếp mười mức lương từ thấp đến cao, rồi lấy giá trị nằm ở chính giữa. "
        "Người ở giữa nhận đúng mười lăm triệu. "
        "Trung vị bằng mười lăm triệu, gần gấp bốn lần nhỏ hơn con số trung bình hào nhoáng kia."
    ),
    "05_ynghia": (
        "Đây là sức mạnh của một giá trị ngoại lệ. "
        "Lương sếp là điểm bất thường, nó kéo lệch hẳn số trung bình nhưng gần như không động tới trung vị. "
        "Khi dữ liệu bị lệch bởi vài con số quá lớn, trung vị mới phản ánh đúng người ở giữa. "
        "Trung bình hợp với dữ liệu cân đối, còn trung vị mạnh khi có ngoại lệ."
    ),
    "06_cta": (
        "Lần sau thấy chữ trung bình trong quảng cáo lương, giá nhà hay điểm chuẩn, hãy hỏi thêm trung vị là bao nhiêu. "
        "Một con số có thể che giấu cả một câu chuyện. "
        "Theo dõi để hiểu Toán Lý đang âm thầm vận hành quanh ta."
    ),
}
