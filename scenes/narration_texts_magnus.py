"""
Lời thoại — "Cú xoáy của Messi" (hiệu ứng Magnus, chênh áp Bernoulli).
Lý 10-11 · SHORT DỌC 9:16 · ~2 phút (12 đoạn) · KHÔNG intro.
NGUỒN DUY NHẤT cho: clone_narration_magnus.py + render.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Một quả đá phạt của Messi vòng qua cả hàng rào cầu thủ, "
        "rồi bất ngờ cắm thẳng vào góc xa khung thành. "
        "Quả bóng đang bay bỗng bẻ cong giữa không trung. Vì sao?"
    ),
    "02_thang": (
        "Nếu quả bóng bay mà không xoay, nó chỉ đi theo một đường vòng cung đều. "
        "Kiểu đó không thể nào lượn vòng qua hàng rào rồi bẻ ngoặt vào góc được. "
        "Vậy bí mật không nằm ở lực sút, mà ở cách quả bóng xoay."
    ),
    "03_xoay": (
        "Khi sút, Messi đá lệch khỏi tâm quả bóng. "
        "Cú chạm đó khiến bóng vừa lao đi vừa tự xoay tít quanh trục của mình. "
        "Chính vòng xoay này là chìa khoá của cú cong thần thánh."
    ),
    "04_khongkhi": (
        "Bề mặt quả bóng không hề nhẵn tuyệt đối. "
        "Khi nó xoay, nó kéo theo một lớp không khí mỏng sát bề mặt quay cùng chiều. "
        "Lớp khí này bị cuốn đi như một tấm chăn vô hình bám quanh bóng."
    ),
    "05_haiben": (
        "Bây giờ hãy nhìn hai bên quả bóng đang lao tới. "
        "Một bên, lớp khí xoay cùng chiều với luồng gió thổi ngược lại nên chạy rất nhanh. "
        "Bên kia, lớp khí xoay ngược chiều gió nên bị hãm lại, chạy chậm hẳn."
    ),
    "06_bernoulli": (
        "Và đây là nguyên lý Bernoulli mà bạn học trong sách Vật lý. "
        "Ở chỗ không khí chuyển động nhanh, áp suất giảm xuống thấp. "
        "Ở chỗ không khí chuyển động chậm, áp suất lại cao hơn."
    ),
    "07_luc": (
        "Thế là hai bên quả bóng có áp suất chênh lệch nhau. "
        "Bên áp suất cao ép mạnh hơn bên áp suất thấp. "
        "Kết quả là xuất hiện một lực đẩy ngang, gọi là lực Magnus."
    ),
    "08_huong": (
        "Lực Magnus luôn vuông góc với hướng bay của quả bóng. "
        "Nó liên tục kéo bóng lệch sang một bên trong suốt đường đi. "
        "Vì vậy quỹ đạo không còn thẳng nữa, mà uốn cong thành một đường lượn mềm mại."
    ),
    "09_conso": (
        "Lực này càng lớn khi bóng bay càng nhanh và xoay càng mạnh. "
        "Đó là lý do các siêu sao phải sút vừa mạnh vừa xoáy thật nhiều. "
        "Sút nhẹ mà xoáy ít thì đường bóng gần như thẳng, chẳng lừa được thủ môn."
    ),
    "10_khac": (
        "Cùng một hiệu ứng ấy có mặt khắp nơi trong thể thao. "
        "Quả bóng bàn xoáy đột ngột đổi hướng, quả bóng chày cong đánh lừa người đỡ, "
        "và cú tennis giật topspin cắm sầm xuống sân nhanh bất ngờ."
    ),
    "11_ung": (
        "Không chỉ trong thể thao, con người còn tận dụng lực Magnus để làm việc lớn. "
        "Có những con tàu gắn ống trụ xoay khổng lồ thay cho buồm, "
        "để gió thổi qua tạo lực đẩy con tàu đi mà tốn ít nhiên liệu hơn."
    ),
    "12_cta": (
        "Vậy cú cong ma thuật của Messi thật ra chẳng có phép màu nào cả. "
        "Nó chỉ là chênh lệch áp suất của không khí quanh một quả bóng đang xoay. "
        "Theo dõi kênh để hiểu vật lý ẩn sau những điều quen thuộc quanh ta."
    ),
}
