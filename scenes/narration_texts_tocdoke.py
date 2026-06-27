"""
Lời thoại — "Kim tốc độ trên xe đang đo cái gì mà nhảy nhạy đến vậy?" (Tốc độ kế chính là đạo hàm).
Toán 11 (đạo hàm là tốc độ biến thiên tức thời) · ứng dụng đời thực · SHORT DỌC 9:16, ~1 phút 50 · KHÔNG intro.

NGUỒN DUY NHẤT cho: clone_narration_tocdoke.py + karaoke (tocdoke_video.py).
Logic-first: hook → đặt vấn đề thực (odometer vs kim tốc độ) → mô hình hoá (Δs/Δt, cho Δt→0)
→ ra con số (độ dốc tiếp tuyến = vận tốc tức thời) → ý nghĩa (đạo hàm chạy 24/7, gia tốc kế) → CTA.
Quy ước TTS: số/công thức đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Nhìn xuống đồng hồ xe máy. "
        "Kim tốc độ rung lên rung xuống, nhạy đến từng cái nhích ga. "
        "Nó đang đo cái gì mà phản ứng nhanh đến vậy? "
        "Câu trả lời là một khái niệm bạn học ở lớp mười một: đạo hàm."
    ),
    "02_haidongho": (
        "Trên xe có hai đồng hồ rất khác nhau. "
        "Đồng hồ cây số cộng dồn tổng quãng đường bạn đã đi, từ lúc mua xe đến giờ. "
        "Còn kim tốc độ chỉ cho bạn biết một điều: ngay lúc này, bạn đang đi nhanh thế nào. "
        "Một cái là tổng tích luỹ, một cái là tốc độ ngay tại khoảnh khắc hiện tại."
    ),
    "03_trungbinh": (
        "Vậy tốc độ tức thời tính kiểu gì? "
        "Hãy bắt đầu từ tốc độ trung bình mà ai cũng biết. "
        "Lấy quãng đường đi được chia cho thời gian, ta được trung bình của cả chặng. "
        "Trên đồ thị quãng đường theo thời gian, đó chính là độ dốc của đoạn nối hai điểm."
    ),
    "04_gioihan": (
        "Nhưng trung bình cả chặng thì quá thô. "
        "Hãy thu khoảng thời gian lại: một phút, một giây, rồi nhỏ hơn nữa. "
        "Khi khoảng thời gian tiến dần về không, đoạn nối hai điểm xoay lại thành đường tiếp tuyến. "
        "Độ dốc của tiếp tuyến tại một điểm chính là vận tốc tức thời, và đó đúng là đạo hàm."
    ),
    "05_ynghia": (
        "Vậy nên tốc độ kế thật ra là một cỗ máy lấy đạo hàm, chạy không nghỉ suốt hành trình. "
        "Mỗi khoảnh khắc, nó đo độ dốc tiếp tuyến của quãng đường để báo ra con số. "
        "Cảm biến trong điện thoại còn đi xa hơn một bước: nó lấy đạo hàm của vận tốc để ra gia tốc, đếm bước chân và xoay màn hình."
    ),
    "06_cta": (
        "Đạo hàm không nằm yên trong sách. "
        "Nó là cái kim đang nhảy trước mắt bạn mỗi lần lên xe. "
        "Theo dõi để hiểu Toán Lý đang âm thầm vận hành quanh ta."
    ),
}
