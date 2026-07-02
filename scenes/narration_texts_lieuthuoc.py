"""
Lời thoại — "Liều thuốc và giới hạn an toàn" (cấp số nhân lùi vô hạn, giới hạn dãy số).
Toán 11 · SHORT DỌC 9:16 · ~2 phút (12 đoạn) · KHÔNG intro.
NGUỒN DUY NHẤT cho: clone_narration_lieuthuoc.py + render.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Toa thuốc ghi: uống một viên mỗi tám tiếng, liên tục cả tuần. "
        "Khoan đã. Thuốc cũ chưa thải hết, thuốc mới đã vào, cứ thế cộng dồn mãi. "
        "Vậy tại sao uống đến viên thứ hai mươi bạn vẫn không bị ngộ độc?"
    ),
    "02_mohinh": (
        "Hãy nhìn vào máu của bạn như một chiếc bình chứa. "
        "Mỗi viên thuốc làm nồng độ trong bình vọt lên một nấc. "
        "Rồi suốt tám tiếng sau đó, gan và thận cần mẫn rút bớt thuốc ra."
    ),
    "03_conlai": (
        "Để dễ tính, giả sử cứ hết một chu kỳ tám tiếng, "
        "cơ thể thải được đúng một nửa lượng thuốc đang có. "
        "Tức là mỗi vòng, phần còn sót lại bị nhân với một phần hai."
    ),
    "04_cong": (
        "Giờ theo dõi từng viên nhé. "
        "Viên một: trong máu có một liều. Đến giờ uống, còn nửa liều, cộng viên mới thành một phẩy năm. "
        "Vòng sau còn không phẩy bảy lăm, cộng thêm một, thành một phẩy bảy lăm."
    ),
    "05_dayso": (
        "Con số cứ nhích lên: một, rồi một rưỡi, rồi một phẩy bảy lăm, một phẩy tám bảy lăm. "
        "Nhìn kỹ mà xem, đây chính là tổng của một cộng một phần hai, "
        "cộng một phần tư, cộng một phần tám. Một cấp số nhân đang lùi dần."
    ),
    "06_gioihan": (
        "Toán lớp mười một cho bạn công thức tuyệt đẹp. "
        "Tổng cấp số nhân lùi vô hạn bằng số hạng đầu chia cho một trừ công bội. "
        "Một chia cho một trừ một phần hai, ra đúng hai. Không phải vô cùng. Chỉ là HAI liều."
    ),
    "07_tran": (
        "Nghĩa là dù bạn uống thuốc cả đời, "
        "nồng độ trong máu chỉ leo lên sát một mức trần cố định bằng hai liều, "
        "rồi dừng ở đó mãi mãi, không bao giờ vượt qua."
    ),
    "08_bacsi": (
        "Và đây là lúc bác sĩ chơi cờ với con số. "
        "Họ chọn liều lượng và giờ uống sao cho mức trần ấy nằm dưới ngưỡng gây độc, "
        "nhưng vẫn cao hơn ngưỡng đủ để thuốc có tác dụng."
    ),
    "09_caphe": (
        "Cơ thể bạn cũng đang chạy phép tính này với cà phê. "
        "Ly cà phê sáng nay cộng vào phần cà-phê-in còn sót từ hôm qua. "
        "Uống đều mỗi ngày, mức tích luỹ cũng tiến về một trần ổn định, nên bạn không run tay mãi."
    ),
    "10_canhbao": (
        "Nhưng công thức cũng cảnh báo điều ngược lại. "
        "Nếu sốt ruột uống gấp đôi liều, mức trần mới cũng cao gấp đôi, "
        "và nó có thể chọc thủng ngưỡng gây độc. Vì thế đừng bao giờ tự ý tăng liều."
    ),
    "11_ung": (
        "Cùng một phép tính giới hạn ấy xuất hiện ở nhiều nơi. "
        "Kháng sinh phải uống đúng giờ để giữ mức thuốc trong cửa sổ an toàn, "
        "và chất ô nhiễm xả đều đặn vào một dòng sông cũng tích luỹ về một mức trần."
    ),
    "12_cta": (
        "Vậy toa thuốc mỗi tám tiếng không phải con số tuỳ hứng. "
        "Nó là một bài toán giới hạn được giải sẵn để bảo vệ bạn. "
        "Theo dõi kênh để thấy toán học ẩn sau những điều quen thuộc quanh ta."
    ),
}
