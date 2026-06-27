"""
Lời thoại — "Điện thoại biết bạn đi bao xa mà không cần GPS — bằng cách nào?"
(Quãng đường từ đồ thị vận tốc = diện tích dưới đường cong = tích phân của vận tốc).
Toán 12 (Tích phân: ứng dụng tính quãng đường) · ứng dụng đời thực · SHORT DỌC 9:16, ~1 phút 50 · KHÔNG intro.

NGUỒN DUY NHẤT cho: clone_narration_quangduong.py + karaoke (quangduong_video.py).
Số liệu minh hoạ: chạy 12 phút = 0,2 giờ; tăng tốc lên 12 km/h trong 0,05 h, chạy đều 12 km/h, giảm tốc về 0.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Bạn chạy bộ buổi sáng và để điện thoại trong túi. "
        "Khi về, app báo bạn vừa chạy đúng hai phẩy bốn ki lô mét. "
        "Lạ ở chỗ, lúc đó bạn còn chẳng bật định vị. "
        "Vậy chiếc điện thoại biết bạn đi bao xa bằng cách nào?"
    ),
    "02_vande": (
        "Cảm biến trong điện thoại không đo quãng đường. "
        "Nó chỉ đo được vận tốc của bạn ở từng khoảnh khắc. "
        "Mà khi chạy, vận tốc thay đổi liên tục: lúc tăng tốc, lúc chạy đều, lúc chậm lại. "
        "Vậy làm sao gộp một mớ vận tốc lộn xộn đó thành một con số quãng đường?"
    ),
    "03_dothi": (
        "Hãy vẽ vận tốc theo thời gian thành một đồ thị. "
        "Trục ngang là thời gian, trục đứng là vận tốc. "
        "Đường này đi lên khi bạn tăng tốc, nằm ngang khi bạn chạy đều, rồi đi xuống khi bạn dừng. "
        "Toàn bộ hành trình của bạn nằm gọn trong một đường cong."
    ),
    "04_dientich": (
        "Và đây là chìa khoá. "
        "Quãng đường bạn đi chính bằng diện tích nằm dưới đường cong vận tốc. "
        "Vì vận tốc nhân thời gian thì ra quãng đường, mà đó đúng là cách tính diện tích một mảnh dưới đồ thị. "
        "Cộng tất cả những mảnh nhỏ đó lại, ta được tích phân của vận tốc theo thời gian."
    ),
    "05_conso": (
        "Thử tính với buổi chạy của bạn. "
        "Phần tăng tốc là một tam giác, phần chạy đều là một hình chữ nhật, phần giảm tốc lại là một tam giác. "
        "Cộng diện tích ba mảnh đó lại, ra đúng hai phẩy bốn ki lô mét. "
        "Không cần định vị, chỉ cần diện tích dưới một đường cong."
    ),
    "06_cta": (
        "Đây cũng là nguyên lý mà tên lửa, máy bay và xe tự lái dùng để biết mình đang ở đâu. "
        "Tất cả gói gọn trong một ý tưởng: diện tích dưới đồ thị vận tốc. "
        "Theo dõi để hiểu Toán Lý đang âm thầm vận hành quanh ta."
    ),
}
