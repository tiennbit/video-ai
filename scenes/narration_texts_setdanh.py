"""
Lời thoại — "Sét đánh xa bao nhiêu?" — đếm giây từ lúc thấy chớp đến lúc nghe sấm.
Vật lý 11 (tốc độ truyền sóng âm v = s chia t; so sánh tốc độ âm và ánh sáng).
Ứng dụng đời thực · SHORT DỌC 9:16, ~1 phút 50 · KHÔNG intro.

NGUỒN DUY NHẤT cho: clone_narration_setdanh.py + karaoke (setdanh_video.py).
Số liệu (nêu rõ trong video): ánh sáng ~300.000 km/s (gần như tức thời);
âm thanh ~343 m/s; khoảng cách = v_âm × t; 6 giây ~2 km; quy tắc "chia 3 ra km".
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để karaoke chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Trời nổi giông. "
        "Bạn thấy một tia chớp loé lên thật sáng. "
        "Rồi đếm thầm: một, hai, ba, bốn, năm, sáu. "
        "Đúng giây thứ sáu mới nghe tiếng sấm rền vang. "
        "Vậy tia sét vừa rồi cách bạn bao xa? "
        "Tin hay không, chỉ cần đếm giây là bạn tính được ngay."
    ),
    "02_vande": (
        "Chớp và sấm sinh ra cùng một lúc, từ cùng một tia sét. "
        "Nhưng tai bạn lại nghe sấm trễ hơn mắt thấy chớp. "
        "Vì sao hai thứ ra đời cùng nhau lại đến với bạn lệch nhau? "
        "Bí mật nằm ở tốc độ."
    ),
    "03_tocdo": (
        "Ánh sáng đi cực nhanh, khoảng ba trăm nghìn ki lô mét mỗi giây. "
        "Với vài cây số, nó đến mắt bạn gần như tức thời. "
        "Còn âm thanh thì chậm hơn rất nhiều. "
        "Trong không khí, sóng âm chỉ đi được khoảng ba trăm bốn ba mét mỗi giây. "
        "Chính khoảng chênh lệch tốc độ này tạo ra độ trễ bạn nghe được."
    ),
    "04_congthuc": (
        "Giờ ta tính. "
        "Quãng đường bằng tốc độ nhân thời gian. "
        "Tốc độ âm thanh là ba trăm bốn ba mét mỗi giây, thời gian trễ là sáu giây. "
        "Nhân lại ta được khoảng hai nghìn mét, tức là hai ki lô mét. "
        "Vậy tia sét vừa rồi cách bạn chừng hai cây số."
    ),
    "05_ynghia": (
        "Từ đây có một mẹo dân gian rất dễ nhớ. "
        "Cứ ba giây giữa chớp và sấm là sét cách bạn khoảng một ki lô mét. "
        "Đếm được mấy giây thì chia cho ba, ra ngay số cây số. "
        "Số giây càng ít, sét càng gần, bạn càng phải cẩn thận. "
        "Nếu chớp và sấm gần như cùng lúc, cơn giông đang ở ngay trên đầu."
    ),
    "06_cta": (
        "Cùng một quy tắc tốc độ nhân thời gian, tàu ngầm dùng sóng âm để dò đáy biển, "
        "và các trạm đo cũng dựa vào nó để định vị tâm động đất. "
        "Lần tới gặp giông, hãy thử đếm giây xem sét cách mình bao xa. "
        "Theo dõi để hiểu Toán Lý đang âm thầm vận hành quanh ta."
    ),
}
