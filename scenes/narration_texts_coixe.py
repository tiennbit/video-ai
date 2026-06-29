"""
Lời thoại — "Còi xe đổi tiếng khi vụt qua" (hiệu ứng Doppler).
Lý 12 · SHORT DỌC 9:16 · ~2 phút (12 đoạn) · KHÔNG intro.
NGUỒN DUY NHẤT cho: clone_narration_coixe.py + render.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Xe cứu thương lao về phía bạn, tiếng còi hú cao và chói. "
        "Ngay khoảnh khắc nó vượt qua, tiếng còi đột ngột tụt xuống trầm hẳn. "
        "Cùng một cái còi, vì sao tiếng lại đổi?"
    ),
    "02_vande": (
        "Người tài xế ngồi trên xe nghe còi y hệt từ đầu tới cuối, chẳng đổi gì. "
        "Vậy thứ thay đổi nằm ở tai người đứng bên đường, "
        "chứ không phải ở bản thân cái còi."
    ),
    "03_song": (
        "Âm thanh lan đi thành từng vòng sóng, hết vòng này tới vòng khác. "
        "Khoảng cách giữa hai vòng quyết định tai ta nghe cao hay thấp. "
        "Sóng càng dày thì càng cao, sóng càng thưa thì càng trầm."
    ),
    "04_dungyen": (
        "Khi nguồn âm đứng yên, các vòng sóng toả ra đều nhau về mọi phía. "
        "Người đứng bên nào cũng nghe đúng một độ cao."
    ),
    "05_laitoi": (
        "Nhưng khi xe lao về phía bạn, mỗi vòng sóng mới lại phát ra từ vị trí gần hơn vòng trước. "
        "Các vòng sóng phía trước bị dồn lại, ép sát vào nhau."
    ),
    "06_caohon": (
        "Sóng dồn dày hơn nghĩa là tần số cao hơn. "
        "Đó chính là lý do khi xe đang tiến tới, "
        "bạn nghe tiếng còi cao và gắt hơn bình thường."
    ),
    "07_vuotqua": (
        "Ngay khi xe vượt qua và chạy ra xa, điều ngược lại xảy ra. "
        "Mỗi vòng sóng mới phát ra từ vị trí xa hơn, "
        "nên các vòng sóng phía sau bị kéo giãn ra."
    ),
    "08_doppler": (
        "Sóng thưa hơn nghĩa là tần số thấp hơn, nên tiếng còi tụt xuống trầm ngay lập tức. "
        "Toàn bộ cú đổi tiếng đó được gọi là hiệu ứng Doppler."
    ),
    "09_nhanh": (
        "Hiệu ứng càng rõ khi xe chạy càng nhanh. "
        "Một chiếc xe sáu mươi ki lô mét giờ đã đủ làm độ cao tiếng còi "
        "nhảy hẳn một bậc mà tai thường nghe rất rõ."
    ),
    "10_anhsang": (
        "Điều kỳ diệu là ánh sáng cũng có Doppler. "
        "Một ngôi sao chạy ra xa thì ánh sáng của nó ngả về phía đỏ, "
        "hiện tượng gọi là dịch chuyển đỏ."
    ),
    "11_ungdung": (
        "Chính dịch chuyển đỏ giúp các nhà thiên văn phát hiện vũ trụ đang giãn nở. "
        "Doppler cũng là nguyên lý của súng bắn tốc độ giao thông "
        "và máy siêu âm đo dòng máu trong tim."
    ),
    "12_cta": (
        "Cùng một nguồn, đứng yên hay chuyển động lại cho ta nghe khác hẳn. "
        "Đó là Doppler, ẩn trong mọi tiếng còi xe vụt qua. "
        "Theo dõi để hiểu vật lý quanh ta."
    ),
}
