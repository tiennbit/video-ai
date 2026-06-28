"""
Lời thoại — "Xô nước quay không đổ một giọt" (chuyển động tròn, lực hướng tâm).
Lý 10 · SHORT DỌC 9:16 · ~2 phút · KHÔNG intro.
NGUỒN DUY NHẤT cho: clone_narration_xonuoc.py + render.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Quay một xô nước thành vòng tròn qua đầu. "
        "Ở điểm cao nhất, xô lộn ngược hoàn toàn, vậy mà không một giọt nước nào rơi xuống. "
        "Phép màu gì đang giữ nước lại?"
    ),
    "02_trongluc": (
        "Bình thường, trọng lực luôn kéo nước rơi thẳng xuống đất. "
        "Đứng yên mà lật ngược xô thì nước đổ ngay lập tức. "
        "Vậy chuyển động tròn đã thay đổi điều gì?"
    ),
    "03_huongtam": (
        "Khi một vật chạy theo vòng tròn, nó luôn cần một lực kéo vào tâm, gọi là lực hướng tâm. "
        "Chính lực này bắt vật liên tục bẻ hướng, thay vì bay thẳng đi mất."
    ),
    "04_dinhcao": (
        "Tại điểm cao nhất, cả trọng lực lẫn phản lực của đáy xô đều hướng xuống, tức là cùng hướng vào tâm. "
        "Hai lực đó cùng đóng vai trò lực hướng tâm, giữ nước đi theo đường tròn."
    ),
    "05_dieukien": (
        "Mấu chốt nằm ở tốc độ. Nếu quay đủ nhanh, lực hướng tâm cần thiết sẽ lớn hơn cả trọng lực. "
        "Khi ấy trọng lực còn chưa đủ để kéo nước rời quỹ đạo, nên nước cứ bám chặt theo đáy xô."
    ),
    "06_nguong": (
        "Có một tốc độ tối thiểu. Khi lực hướng tâm vừa đúng bằng trọng lực, "
        "vận tốc tới hạn bằng căn bậc hai của g nhân bán kính. "
        "Với một xô vung cách vai khoảng một mét, con số đó chỉ vào khoảng ba mét một giây."
    ),
    "07_cham": (
        "Quay chậm hơn cái ngưỡng đó, trọng lực sẽ thắng, "
        "và nguyên xô nước đổ thẳng vào mặt bạn. "
        "Vậy nên bí mật không hề là phép màu, mà chỉ là quay cho đủ nhanh."
    ),
    "08_ungdung": (
        "Cùng nguyên lý giữ nước ấy giải thích vì sao tàu lượn siêu tốc lộn vòng mà không rơi, "
        "vì sao máy giặt vắt khô được quần áo, và vì sao khúc cua đường đua phải nghiêng vào trong."
    ),
    "09_cta": (
        "Một xô nước quay tròn dạy ta một điều lạ lùng: "
        "đôi khi muốn không bị rơi, bí quyết lại là phải đi thật nhanh. "
        "Theo dõi để hiểu vật lý quanh ta."
    ),
}
