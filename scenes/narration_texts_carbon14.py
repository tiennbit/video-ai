"""
Lời thoại — "Định tuổi xác ướp bằng Carbon-14" (phóng xạ, chu kỳ bán rã, định luật phân rã).
Vật lý 12 · ứng dụng đời thực · SHORT DỌC 9:16, ~1 phút 50 · KHÔNG intro.

NGUỒN DUY NHẤT cho: clone_narration_carbon14.py + karaoke (carbon14_video.py).
Số liệu (đã vet, ý tưởng L49): T(C-14) = 5730 năm; N = N0·(1/2)^(t/T);
còn 25% → 2 chu kỳ bán rã → khoảng 11.460 năm.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm tự nhiên.
"""

SEGMENTS = {
    "01_hook": (
        "Làm sao biết một mảnh gỗ cổ hay một bộ xương đã bao nhiêu tuổi? "
        "Không có giấy khai sinh, không ai chứng kiến. "
        "Vậy mà nhà khoa học vẫn đọc ra con số hàng nghìn năm, sai lệch chỉ vài chục năm. "
        "Bí mật: mọi cơ thể từng sống đều mang trong mình một chiếc đồng hồ phóng xạ vẫn đang tích tắc."
    ),
    "02_dongho": (
        "Trong không khí luôn có một lượng nhỏ Carbon mười bốn phóng xạ. "
        "Khi còn sống, cây cối và con người liên tục hấp thụ nó qua thức ăn và hơi thở. "
        "Nhờ vậy, tỉ lệ Carbon mười bốn trong cơ thể luôn giữ ổn định, đúng bằng ngoài môi trường. "
        "Nhưng đến khoảnh khắc chết đi, nguồn nạp dừng hẳn. Chiếc đồng hồ bắt đầu chạy."
    ),
    "03_phanra": (
        "Từ lúc đó, Carbon mười bốn chỉ còn phân rã, mỗi lúc một ít. "
        "Quy luật rất gọn: cứ sau năm nghìn bảy trăm ba mươi năm, lượng Carbon mười bốn lại giảm đúng một nửa. "
        "Khoảng thời gian đó gọi là chu kỳ bán rã. "
        "Viết thành công thức: lượng còn lại bằng lượng ban đầu nhân một phần hai mũ t chia T."
    ),
    "04_conso": (
        "Giờ ta đo mẫu vật và thấy Carbon mười bốn chỉ còn một phần tư so với ban đầu. "
        "Một nửa, rồi lại một nửa, là hai lần giảm, tức hai chu kỳ bán rã. "
        "Hai nhân năm nghìn bảy trăm ba mươi, ra mười một nghìn bốn trăm sáu mươi. "
        "Vậy mẫu vật đã ngủ yên khoảng mười một nghìn năm trăm năm."
    ),
    "05_ynghia": (
        "Chỉ cần đo tỉ lệ phóng xạ còn lại, ta đọc được tuổi của quá khứ. "
        "Đây chính là cách người ta định tuổi cọc gỗ Bạch Đằng, xác ướp và những tấm vải liệm cổ. "
        "Cùng một định luật phân rã còn dùng để vạch trần tranh giả, đoán tuổi nước ngầm và phá án pháp y. "
        "Một hàm số mũ đơn giản, biến mọi vật từng sống thành cuốn lịch sử biết tự kể chuyện."
    ),
    "06_cta": (
        "Thời gian không xoá sạch dấu vết, nó chỉ giảm đi một nửa, rồi lại một nửa. "
        "Và toán học giúp ta đọc ngược dòng thời gian ấy. "
        "Theo dõi để hiểu Toán Lý đang âm thầm vận hành quanh ta."
    ),
}
