"""
Lời thoại — "Xét nghiệm dương tính 99% — bạn có thật mắc bệnh?" (nghịch lý dương tính giả / Bayes).
Toán 11 (xác suất có điều kiện) · ứng dụng đời thực · SHORT DỌC 9:16, ~2 phút · KHÔNG intro.

NGUỒN DUY NHẤT cho: clone_narration_xetnghiem.py + karaoke (xetnghiem_video.py).
Số liệu (giả định minh hoạ, nêu rõ trong video): bệnh hiếm 1/1000; test sai 1% → ~10 dương tính giả/999 người khoẻ.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để karaoke chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Bạn đi xét nghiệm một căn bệnh hiếm. "
        "Que thử có độ chính xác chín mươi chín phần trăm. "
        "Kết quả trả về: dương tính. "
        "Vậy khả năng bạn thật sự mắc bệnh là bao nhiêu? "
        "Hầu hết mọi người, kể cả nhiều bác sĩ, đoán chín mươi chín phần trăm. "
        "Nhưng sự thật chỉ khoảng chín phần trăm. Vì sao lại vô lý đến vậy?"
    ),
    "02_vande": (
        "Bí mật nằm ở hai chữ: bệnh hiếm. "
        "Khi một căn bệnh rất hiếm gặp, ngay cả xét nghiệm chính xác cũng tạo ra rất nhiều báo động giả. "
        "Để thấy rõ, ta đừng nghĩ bằng phần trăm. Hãy đếm bằng người thật."
    ),
    "03_danso": (
        "Lấy một nghìn người bất kỳ. "
        "Giả sử bệnh này chỉ gặp ở một trên một nghìn người. "
        "Vậy trung bình, chỉ có đúng một người thật sự mắc bệnh. "
        "Chín trăm chín mươi chín người còn lại hoàn toàn khoẻ mạnh."
    ),
    "04_test": (
        "Giờ cho cả nghìn người đi xét nghiệm. "
        "Một người bệnh kia gần như chắc chắn dương tính. Đúng. "
        "Nhưng còn chín trăm chín mươi chín người khoẻ thì sao? "
        "Xét nghiệm sai một phần trăm, nghĩa là khoảng mười người khoẻ vẫn bị báo dương tính. "
        "Đây chính là những ca dương tính giả."
    ),
    "05_dem": (
        "Giờ đếm tất cả những người có kết quả dương tính. "
        "Một người bệnh thật, cộng mười người khoẻ bị báo nhầm, là mười một người. "
        "Nhưng trong mười một người đó, chỉ một người thật sự mắc bệnh. "
        "Một trên mười một, tức là khoảng chín phần trăm. Đúng bằng con số ở đầu video."
    ),
    "06_ynghia": (
        "Đây gọi là nghịch lý dương tính giả. "
        "Bệnh càng hiếm, thì một kết quả dương tính càng dễ là báo động giả. "
        "Đó là lý do bác sĩ luôn cho xét nghiệm lại trước khi kết luận. "
        "Cách suy luận này có tên: định lý Bayes, và nó vận hành cả bộ lọc thư rác lẫn trí tuệ nhân tạo."
    ),
    "07_cta": (
        "Một con số, đừng bao giờ tin nó một mình. "
        "Hãy luôn hỏi: trên nền của bao nhiêu. "
        "Theo dõi để hiểu Toán Lý đang âm thầm vận hành cuộc sống của bạn."
    ),
}
