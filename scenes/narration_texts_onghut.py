"""
Lời thoại — "Ống hút cao tối đa 10 mét" (áp suất khí quyển, h = p/(rho.g)).
Lý 10 · SHORT DỌC 9:16 · ~2 phút (12 đoạn) · KHÔNG intro.
NGUỒN DUY NHẤT cho: clone_narration_onghut.py + render.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Thử tưởng tượng bạn đứng trên ban công tầng bốn, "
        "thả một chiếc ống hút siêu dài xuống ly nước dưới sân. "
        "Dù phổi bạn khoẻ như vận động viên, bạn sẽ không bao giờ hút được ngụm nước nào. Vì sao?"
    ),
    "02_hut": (
        "Trước hết phải hỏi. Hút thật ra là gì? "
        "Ai cũng tưởng miệng mình đang kéo nước lên như kéo một sợi dây. "
        "Nhưng sự thật thì miệng bạn chẳng hề chạm được vào nước để mà kéo."
    ),
    "03_giamap": (
        "Khi bạn hút, bạn chỉ làm được đúng một việc. "
        "Đó là rút bớt không khí trong ống, khiến áp suất bên trong giảm xuống. "
        "Còn ai đẩy nước lên? Là một thứ vô hình ngay quanh bạn."
    ),
    "04_khiquyen": (
        "Cả bầu khí quyển dày hàng chục cây số đang đè lên mặt nước trong ly. "
        "Mỗi mét vuông gánh khoảng mười tấn không khí. "
        "Chính sức đè khổng lồ đó ép nước chui vào ống, dâng lên chỗ áp suất thấp."
    ),
    "05_canbang": (
        "Nhưng nước không dâng lên mãi. "
        "Cột nước trong ống càng cao thì càng nặng, càng ghì xuống. "
        "Nước ngừng dâng đúng lúc sức nặng của cột nước cân bằng với sức đẩy của khí quyển."
    ),
    "06_congthuc": (
        "Từ đó, vật lý cho ta một công thức gọn gàng. "
        "Chiều cao tối đa bằng áp suất khí quyển chia cho khối lượng riêng nhân gia tốc trọng trường. "
        "Tức là h bằng p chia rô nhân g."
    ),
    "07_tinh": (
        "Thay số vào là thấy ngay giới hạn. "
        "Áp suất khí quyển khoảng một trăm linh một nghìn Pascal, "
        "chia cho một nghìn nhân chín phẩy tám, ra đúng mười phẩy ba mét."
    ),
    "08_chankhong": (
        "Con số này là trần tuyệt đối. "
        "Kể cả bạn hút mạnh đến mức trong ống là chân không hoàn toàn, "
        "nước vẫn dừng ở mười phẩy ba mét, vì khí quyển chỉ đẩy nổi đến thế."
    ),
    "09_gieng": (
        "Đây cũng là lý do máy bơm hút đặt trên miệng giếng chịu thua giếng sâu. "
        "Giếng sâu quá mười mét thì hút kiểu gì nước cũng không lên tới nơi. "
        "Muốn lấy nước, người ta phải thả bơm đẩy xuống tận đáy giếng."
    ),
    "10_thuyngan": (
        "Giờ đổi nước thành thuỷ ngân, thứ chất lỏng nặng gấp mười ba phẩy sáu lần. "
        "Khí quyển chỉ nâng nổi cột thuỷ ngân cao bảy mươi sáu xăng ti mét. "
        "Và đó chính là chiếc máy đo áp suất đầu tiên của nhân loại."
    ),
    "11_ung": (
        "Hiểu chuyện đẩy thay vì kéo, bạn giải thích được cả loạt thứ quen thuộc. "
        "Xi phông chuyển nước qua thành bể, máy hút bụi gom rác vào trong, "
        "và giác hút chân không treo được cả chục ký lô lên tấm kính."
    ),
    "12_cta": (
        "Vậy thứ nâng ly trà sữa lên miệng bạn không phải là phổi. "
        "Mà là cả bầu khí quyển của Trái Đất đang đè xuống giúp bạn. "
        "Theo dõi kênh để hiểu vật lý ẩn sau những điều quen thuộc quanh ta."
    ),
}
