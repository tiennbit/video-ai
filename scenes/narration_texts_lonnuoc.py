"""
Lời thoại — "Vì sao lon nước ngọt có đúng hình dạng đó?" (tối ưu diện tích, đạo hàm, cực trị).
Toán 12 · SHORT DỌC 9:16 · ~2 phút (12 đoạn) · KHÔNG intro.
NGUỒN DUY NHẤT cho: clone_narration_lonnuoc.py + render.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Mỗi năm thế giới sản xuất hàng trăm tỉ lon nước ngọt. "
        "Hình dạng của chúng trông đơn giản nhưng không hề ngẫu nhiên chút nào. "
        "Nó được toán học chọn ra để tốn ít nhôm nhất có thể."
    ),
    "02_baitoan": (
        "Bài toán của hãng nước ngọt rất rõ ràng. "
        "Mỗi lon phải chứa đúng một lượng nước cố định, chẳng hạn ba trăm ba mươi mi li lít. "
        "Nhưng phần vỏ nhôm bọc quanh thì phải càng ít càng tốt, để tiết kiệm chi phí."
    ),
    "03_bien": (
        "Một chiếc lon thực ra là một hình trụ. "
        "Nó được mô tả bằng hai con số: bán kính đáy và chiều cao. "
        "Thể tích của trụ, bằng diện tích đáy nhân chiều cao, phải luôn giữ cố định."
    ),
    "04_dientich": (
        "Lượng nhôm cần dùng chính là diện tích toàn phần của lon. "
        "Gồm hai nắp tròn ở trên và dưới, cộng với phần thân cuốn quanh thành ống. "
        "Ta muốn tổng diện tích này nhỏ nhất."
    ),
    "05_the": (
        "Vì thể tích đã cố định, chiều cao không còn tự do nữa. "
        "Ta có thể tính chiều cao theo bán kính, rồi thế vào công thức diện tích. "
        "Nhờ vậy diện tích chỉ còn phụ thuộc vào một biến duy nhất là bán kính."
    ),
    "06_hamso": (
        "Bây giờ hãy hình dung. Nếu bán kính quá nhỏ, lon gầy nhom và cao ngồng, thân tốn rất nhiều nhôm. "
        "Nếu bán kính quá to, lon bè ra, hai cái nắp lại ngốn quá nhiều nhôm. "
        "Ở đâu đó chính giữa có một điểm ngọt tiết kiệm nhất."
    ),
    "07_daoham": (
        "Và đây là lúc đạo hàm ra tay. "
        "Diện tích đạt nhỏ nhất đúng tại nơi mà đạo hàm của nó bằng không. "
        "Đó là điểm mà đồ thị diện tích chạm đáy rồi mới đi lên."
    ),
    "08_giai": (
        "Cho đạo hàm bằng không rồi giải phương trình, ta rút ra một điều kiện đẹp bất ngờ. "
        "Nó buộc thể tích phải liên hệ với bán kính theo một tỉ lệ cố định. "
        "Từ đó tính ngược lại được chiều cao lý tưởng."
    ),
    "09_ketqua": (
        "Kết quả gọn gàng đến mức khó tin: chiều cao đúng bằng đường kính của lon. "
        "Nói cách khác, chiếc lon tối ưu nhìn nghiêng sẽ vừa khít trong một hình vuông. "
        "Không cao lêu nghêu, cũng không lùn tịt."
    ),
    "10_thucte": (
        "Thế nhưng lon ngoài đời lại hơi cao hơn con số lý tưởng đó. "
        "Lý do là phần nắp lon dày và cứng hơn thân nhiều lần. "
        "Nên tối ưu thật sẽ đẩy lon cao lên một chút để thu nhỏ diện tích nắp đắt đỏ."
    ),
    "11_ungdung": (
        "Cùng một kiểu bài toán tối ưu này xuất hiện ở khắp nơi trong sản xuất. "
        "Nó quyết định kích thước thùng phuy, bể chứa, hộp sữa và bao bì đủ loại. "
        "Mỗi phần trăm vật liệu tiết kiệm được là hàng triệu đô mỗi năm."
    ),
    "12_cta": (
        "Vậy là một chiếc lon quen thuộc giấu bên trong nó một bài toán cực trị lớp mười hai. "
        "Đạo hàm không hề khô khan, nó đang lặng lẽ thiết kế mọi thứ quanh bạn. "
        "Theo dõi kênh để thấy toán học ẩn trong đời thường."
    ),
}
