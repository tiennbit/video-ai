"""
Lời thoại — "GPS định vị bạn đến từng mét bằng cách nào?" (toạ độ, mặt cầu, giao điểm).
Toán 12 · SHORT DỌC 9:16 · ~2 phút (12 đoạn) · KHÔNG intro.
NGUỒN DUY NHẤT cho: clone_narration_gps.py + render.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Chiếc điện thoại trong túi biết chính xác bạn đang đứng ở đâu, sai số chỉ vài mét. "
        "Trong khi vệ tinh giúp nó định vị thì bay cách mặt đất tới hai mươi nghìn ki lô mét. "
        "Làm sao một thiết bị bé tí làm được điều phi thường đó?"
    ),
    "02_vande": (
        "Bí mật không nằm ở chỗ vệ tinh nhìn thấy bạn. "
        "Thật ra vệ tinh chẳng biết bạn ở đâu cả. "
        "Tất cả chỉ là một bài toán hình học thuần tuý về khoảng cách."
    ),
    "03_thoigian": (
        "Mỗi vệ tinh liên tục phát đi một tín hiệu, kèm theo cả thời điểm gửi. "
        "Điện thoại nhận được, đem so với thời điểm nhận, "
        "là ra khoảng thời gian tín hiệu đã đi trên đường."
    ),
    "04_tocdo": (
        "Tín hiệu chạy bằng tốc độ ánh sáng, khoảng ba trăm nghìn ki lô mét mỗi giây. "
        "Lấy tốc độ nhân với thời gian, ta được khoảng cách từ bạn tới vệ tinh đó."
    ),
    "05_motcau": (
        "Biết khoảng cách tới một vệ tinh thôi, bạn đang ở đâu? "
        "Ở bất cứ điểm nào cách nó đúng khoảng đó, "
        "tức là nằm đâu đó trên một mặt cầu khổng lồ bao quanh vệ tinh."
    ),
    "06_haicau": (
        "Một mặt cầu thì còn quá mơ hồ. "
        "Thêm vệ tinh thứ hai, bạn phải nằm trên giao của hai mặt cầu, "
        "thu lại thành một đường tròn."
    ),
    "07_bacau": (
        "Thêm vệ tinh thứ ba nữa, giao của ba mặt cầu chỉ còn lại hai điểm. "
        "Một điểm vô lý lơ lửng ngoài không gian bị loại, "
        "còn đúng một điểm trên mặt đất, chính là bạn."
    ),
    "08_bonve": (
        "Trên thực tế người ta cần tới vệ tinh thứ tư. "
        "Vì đồng hồ trong điện thoại không đủ chính xác, "
        "vệ tinh thứ tư giúp sửa lại chính cái sai lệch đồng hồ đó."
    ),
    "09_chinhxac": (
        "Và đây mới là chỗ đáng sợ. Vì nhân với tốc độ ánh sáng, "
        "chỉ cần đồng hồ sai một phần triệu giây, "
        "vị trí của bạn đã lệch đi tới ba trăm mét."
    ),
    "10_tuongdoi": (
        "Tệ hơn nữa, đồng hồ trên vệ tinh lại chạy nhanh hơn đồng hồ dưới đất một chút, "
        "đúng như thuyết tương đối của Einstein. "
        "Không hiệu chỉnh thì GPS sẽ trôi lệch hàng ki lô mét mỗi ngày."
    ),
    "11_ungdung": (
        "Cùng nguyên lý giao các mặt cầu ấy dẫn đường cho máy bay, tàu biển, drone, "
        "xe tự lái, và mọi tấm bản đồ đang chạy trong điện thoại bạn."
    ),
    "12_cta": (
        "Định vị tưởng như phép màu, thật ra chỉ là hình học toạ độ "
        "cộng thêm một chút thuyết tương đối. "
        "Theo dõi để thấy toán học chạy âm thầm ngay trong túi bạn."
    ),
}
