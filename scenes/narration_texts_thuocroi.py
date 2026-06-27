"""
Lời thoại — "Bắt cây thước rơi: bài test phản xạ chỉ cần một công thức" (rơi tự do).
Vật lý 10 (rơi tự do, h = một phần hai g t bình, suy ra t = căn của hai h chia g) · ứng dụng đời thực
SHORT DỌC 9:16, ~1 phút 50 · KHÔNG intro.

NGUỒN DUY NHẤT cho: clone_narration_thuocroi.py + karaoke (thuocroi_video.py).
Số liệu: g = chín phẩy tám mét trên giây bình phương; bắt ở hai mươi xen-ti-mét -> t = căn(2×0,2/9,8) ≈ 0,20 giây.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Một người thả thẳng cây thước, bạn chỉ việc bắt nó bằng hai ngón tay. "
        "Bạn bắt được ở vạch hai mươi xen-ti-mét. "
        "Chỉ con số đó thôi đã đo đúng tốc độ phản xạ của bạn: hai phần mười giây. "
        "Không cần máy móc gì cả, chỉ cần một cây thước và một công thức."
    ),
    "02_vande": (
        "Vấn đề là: làm sao một cây thước lại đo được thời gian phản xạ? "
        "Từ lúc thước được buông cho tới lúc bạn kịp bóp tay lại, một khoảng thời gian đã trôi qua. "
        "Trong khoảng đó, thước không đứng yên mà rơi xuống được một đoạn. "
        "Chính đoạn rơi này là dấu vết của thời gian."
    ),
    "03_mohinh": (
        "Khi buông tay, cây thước rơi tự do, chỉ có trọng lực kéo nó xuống. "
        "Vật lý lớp mười cho ta một công thức: quãng đường rơi bằng một phần hai nhân g nhân thời gian bình phương. "
        "Trong đó g là gia tốc rơi tự do, khoảng chín phẩy tám mét trên giây bình phương. "
        "Quãng đường thước rơi càng dài, nghĩa là bạn càng phản ứng chậm."
    ),
    "04_conso": (
        "Giờ ta giải ngược lại để tìm thời gian. "
        "Từ công thức, thời gian bằng căn bậc hai của hai lần quãng đường chia cho g. "
        "Thay quãng đường bằng hai mươi xen-ti-mét, tức là không phẩy hai mét. "
        "Bấm máy ra: thời gian xấp xỉ không phẩy hai mươi giây."
    ),
    "05_ynghia": (
        "Vậy bắt thước ở hai mươi xen-ti-mét nghĩa là não và tay bạn mất đúng hai phần mười giây để phản ứng. "
        "Bắt được ở vạch thấp hơn thì phản xạ của bạn càng nhanh. "
        "Cùng một nguyên lý này đo độ tỉnh táo của tài xế, kiểm tra phản xạ vận động viên, và quyết định thắng thua trong game tốc độ. "
        "Một bài kiểm tra cơ thể, ẩn sau công thức rơi tự do."
    ),
    "06_cta": (
        "Lần tới cầm thước, hãy thử bắt và đọc ngay tốc độ phản xạ của mình. "
        "Cả thế giới quanh bạn đang chạy bằng những công thức đơn giản như thế. "
        "Theo dõi để hiểu Toán Lý đang âm thầm vận hành quanh ta."
    ),
}
