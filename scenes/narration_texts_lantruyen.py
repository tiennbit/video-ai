"""
Lời thoại — "Hàm mũ — vì sao 1 video bùng nổ triệu view" (hàm mũ, cấp số nhân, R0).
Toán 11 · SHORT DỌC 9:16 · ~2 phút · KHÔNG intro.
NGUỒN DUY NHẤT cho: clone_narration_lantruyen.py + render.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Sáng ngủ dậy, một video bình thường bỗng có cả triệu lượt xem. "
        "Không quảng cáo, không người nổi tiếng nào chia sẻ. "
        "Vì sao nó bùng nổ nhanh đến mức phi lý như vậy?"
    ),
    "02_chia": (
        "Bí mật là sự lan truyền. Một người thấy hay, chia sẻ cho hai người. "
        "Hai người đó, mỗi người lại chia cho hai người nữa. "
        "Cứ thế nhân đôi sau mỗi vòng."
    ),
    "03_capso": (
        "Sau một vòng là hai người, hai vòng là bốn, ba vòng là tám. "
        "Đây không phải cộng thêm đều đặn, mà là nhân đôi liên tục, "
        "đúng định nghĩa một cấp số nhân."
    ),
    "04_hammu": (
        "Số người tiếp cận sau n vòng là hai mũ n, một hàm số mũ. "
        "Khác hẳn tăng tuyến tính cộng đều, "
        "đường cong mũ ban đầu bò sát mặt đất, rồi đột ngột dựng đứng."
    ),
    "05_no": (
        "Chỉ hai mươi vòng, hai mũ hai mươi đã hơn một triệu. "
        "Ba mươi vòng thì vượt một tỉ. "
        "Vài bước nhân đôi cuối cùng tạo ra gần như toàn bộ con số, đó chính là cú bùng nổ sau một đêm."
    ),
    "06_heso": (
        "Tốc độ phụ thuộc hệ số lan truyền, gọi là R: "
        "trung bình mỗi người kéo thêm được bao nhiêu người. "
        "R lớn hơn một thì bùng nổ, nhỏ hơn một thì tắt dần."
    ),
    "07_dich": (
        "Cùng đúng quy luật này là cách dịch bệnh lây lan, với R không là số ca mỗi người truyền đi. "
        "Đó là lý do làm phẳng đường cong sống còn đến vậy: "
        "kéo R xuống dưới một là bẻ gãy được cấp số nhân."
    ),
    "08_ungdung": (
        "Hàm mũ điều khiển cả tin đồn lan đi, lãi kép sinh sôi, "
        "lượng vi khuẩn nhân lên, và chuỗi phản ứng trong lò hạt nhân."
    ),
    "09_cta": (
        "Trực giác con người quen với cộng đều, nên luôn bị bất ngờ trước thứ nhân đôi. "
        "Theo dõi để không bao giờ đánh giá thấp sức mạnh của hàm số mũ."
    ),
}
