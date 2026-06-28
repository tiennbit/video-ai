"""
Lời thoại — "Xoắn ốc Fibonacci trong tự nhiên" (dãy truy hồi, giới hạn tỉ số, tỉ lệ vàng).
Toán 11 · SHORT DỌC 9:16 · ~2 phút · KHÔNG intro.
NGUỒN DUY NHẤT cho: clone_narration_fibonacci.py + render.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Hãy đếm số đường xoắn trên đài một bông hoa hướng dương. "
        "Gần như chắc chắn bạn sẽ ra hai mươi mốt, ba mươi tư, hoặc năm mươi lăm. "
        "Vì sao thiên nhiên, từ vỏ ốc tới quả thông, cứ lặp đi lặp lại đúng một dãy số kỳ lạ?"
    ),
    "02_day": (
        "Dãy số đó tên là Fibonacci. Bắt đầu từ một và một. "
        "Mỗi số tiếp theo bằng tổng hai số liền trước. "
        "Một cộng một là hai, hai cộng một là ba, rồi năm, tám, mười ba, hai mươi mốt."
    ),
    "03_truyhoi": (
        "Đây là một dãy số cho bởi công thức truy hồi: "
        "số hạng thứ n bằng số hạng thứ n trừ một, cộng số hạng thứ n trừ hai. "
        "Chỉ một quy tắc cộng đơn giản, nhưng nó giấu cả một trật tự ẩn của tự nhiên."
    ),
    "04_tiso": (
        "Bí mật nằm ở tỉ số của hai số liên tiếp. "
        "Tám chia năm bằng một phẩy sáu. Mười ba chia tám bằng một phẩy sáu hai lăm. "
        "Càng đi xa, tỉ số này càng dao động sát về một con số cố định."
    ),
    "05_phi": (
        "Con số đó là tỉ lệ vàng, ký hiệu là phi, xấp xỉ một phẩy sáu một tám. "
        "Nói theo ngôn ngữ toán, đây chính là giới hạn của dãy tỉ số Fibonacci khi n tiến ra vô cùng."
    ),
    "06_gocvang": (
        "Từ tỉ lệ vàng, người ta suy ra góc vàng, khoảng một trăm ba mươi bảy độ rưỡi. "
        "Khi mỗi hạt mới mọc lệch đúng góc này so với hạt trước, "
        "chúng xếp kín mặt hoa mà không hạt nào che nắng hạt nào."
    ),
    "07_xoanoc": (
        "Chính cách xếp theo góc vàng đã vẽ nên những đường xoắn ốc trên đài hoa. "
        "Và kỳ diệu thay, số đường xoắn mỗi chiều luôn rơi đúng vào một số Fibonacci. "
        "Toán học lặng lẽ nặn nên hình dáng của bông hoa."
    ),
    "08_ungdung": (
        "Cùng tỉ lệ vàng ấy hiện ra trong vỏ ốc anh vũ, trong cách lá cây mọc so le để đón nắng, "
        "và được kiến trúc sư, hoạ sĩ mượn làm bố cục cân đối, dễ chịu cho mắt người."
    ),
    "09_cta": (
        "Một quy tắc cộng tưởng như tầm thường, một con số vô tỉ, "
        "vậy mà điều khiển hình dáng của sự sống quanh ta. "
        "Theo dõi để cùng thấy toán học ẩn trong từng cánh hoa."
    ),
}
