"""
Lời thoại — "Cây búa giấu lực 8000 Newton" (định lý động năng / công của lực cản).
Vật lý 10 (công - động năng) · ứng dụng đời thực · SHORT DỌC 9:16, ~1 phút 50 · KHÔNG intro.

NGUỒN DUY NHẤT cho: clone_narration_bua.py + karaoke (bua_video.py).
Số liệu (minh hoạ, nêu rõ trong video): đầu búa nửa kí, tốc độ tám mét trên giây,
đinh lún hai mi-li-mét → động năng mười sáu jun → lực cản tám nghìn Newton (~800 kg).
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Một cây búa chỉ nặng nửa kí. "
        "Bạn vung tay khá nhẹ nhàng. "
        "Vậy mà nó đóng được chiếc đinh xuyên sâu vào gỗ cứng. "
        "Lực ép lên đầu đinh lúc đó lớn tới tám nghìn Newton. "
        "Tức là gần bằng đặt cả một chiếc ô tô con lên mũi đinh. "
        "Sức mạnh khổng lồ đó giấu ở đâu trong cú vung tay nhẹ tênh?"
    ),
    "02_vande": (
        "Hãy nhìn kỹ khoảnh khắc va chạm. "
        "Đầu búa nửa kí lao tới với tốc độ khoảng tám mét trên giây. "
        "Nó chạm vào đinh, rồi đinh lún vào gỗ chỉ chừng hai mi-li-mét thì dừng hẳn. "
        "Câu hỏi là, làm sao một quãng đường bé xíu lại sinh ra lực lớn đến thế?"
    ),
    "03_mohinh": (
        "Bí mật nằm ở động năng. "
        "Khi đang bay, cây búa mang một năng lượng chuyển động bằng một phần hai khối lượng nhân bình phương vận tốc. "
        "Toàn bộ năng lượng ấy không tự biến mất. "
        "Nó bị tiêu hết bởi lực cản của gỗ, đúng trên đoạn lún hai mi-li-mét đó. "
        "Theo định lý động năng, công của lực cản bằng động năng của búa."
    ),
    "04_conso": (
        "Giờ thay số vào. "
        "Động năng bằng một phần hai nhân nửa kí nhân tám bình phương, ra mười sáu jun. "
        "Công của lực cản bằng lực nhân quãng đường dừng. "
        "Vậy lực bằng động năng chia cho quãng đường, tức mười sáu jun chia hai phần nghìn mét. "
        "Kết quả là tám nghìn Newton."
    ),
    "05_ynghia": (
        "Hãy nhìn lại công thức: lực bằng động năng chia cho quãng đường dừng. "
        "Quãng đường dừng càng ngắn, lực sinh ra càng khổng lồ. "
        "Đinh lún hai mi-li-mét cho lực tám nghìn Newton. "
        "Đó cũng là lý do mũi đinh phải thật nhọn, và vì sao một cú va chạm chỉ vài centimet trong tai nạn lại nguy hiểm chết người."
    ),
    "06_cta": (
        "Cùng một năng lượng, dừng càng gấp thì lực càng lớn. "
        "Một con số nhỏ có thể giấu một sức mạnh khổng lồ. "
        "Theo dõi để hiểu Toán Lý đang âm thầm vận hành quanh ta."
    ),
}
