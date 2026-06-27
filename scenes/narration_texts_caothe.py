"""
Lời thoại — "Vì sao lưới điện 220V?" (truyền tải điện năng đi xa bằng cao thế / máy biến áp).
Vật lý 12 (máy biến áp, hao phí I bình R) · ứng dụng đời thực · SHORT DỌC 9:16, ~1.8 phút · KHÔNG intro.

NGUỒN DUY NHẤT cho: clone_narration_caothe.py + karaoke (caothe_video.py).
Số liệu minh hoạ (nêu rõ trong video): hao phí trên dây tỉ lệ I^2·R; cùng công suất P=U·I,
tăng áp 10 lần -> dòng giảm 10 lần -> hao phí giảm 100 lần. Đường dây 500kV Bắc-Nam.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để chia cụm tự nhiên.
"""

SEGMENTS = {
    "01_hook": (
        "Điện từ nhà máy về tới ổ cắm nhà bạn là hai trăm hai mươi vôn. "
        "Vậy mà trên đường đi, người ta đẩy nó lên tới năm trăm nghìn vôn, "
        "rồi mới hạ dần xuống. "
        "Nghe thì ngược đời, nhưng chính cú tăng áp đó giúp điện đi xa mà gần như không hao. "
        "Vì sao lại như thế?"
    ),
    "02_vande": (
        "Vấn đề là thế này. "
        "Điện phải chạy qua hàng nghìn cây số dây dẫn, mà dây nào cũng có điện trở. "
        "Dòng điện chạy qua điện trở thì sinh nhiệt, làm hao mất một phần năng lượng. "
        "Truyền càng xa, hao phí càng lớn. "
        "Câu hỏi đặt ra: làm sao cắt giảm phần điện bị mất dọc đường này?"
    ),
    "03_mohinh": (
        "Vật lý cho ta hai công thức then chốt. "
        "Thứ nhất, công suất hao trên dây bằng cường độ dòng bình phương, nhân với điện trở. "
        "Thứ hai, công suất truyền đi bằng điện áp nhân cường độ dòng. "
        "Nhìn kỹ: hao phí phụ thuộc vào dòng điện bình phương. "
        "Vậy chỉ cần làm cho dòng nhỏ đi, hao phí sẽ tụt rất nhanh."
    ),
    "04_conso": (
        "Mà muốn giữ nguyên công suất truyền thì điện áp với dòng điện tỉ lệ nghịch. "
        "Tăng điện áp lên mười lần, dòng điện tự động giảm đúng mười lần. "
        "Nhưng hao phí lại tỉ lệ với dòng bình phương. "
        "Dòng giảm mười lần, thì hao phí giảm tới một trăm lần. "
        "Chỉ một cú tăng áp mà cắt được chín mươi chín phần trăm lượng điện bị mất."
    ),
    "05_ynghia": (
        "Bí quyết để tăng rồi hạ điện áp chính là máy biến áp. "
        "Tỉ số điện áp đúng bằng tỉ số số vòng dây ở hai cuộn. "
        "Nhờ nó, điện được nâng lên cao thế để đi xuyên Bắc Nam, "
        "rồi hạ dần qua từng trạm cho tới mức an toàn về nhà. "
        "Đó cũng là lý do cục sạc nào cũng có một máy biến áp tí hon bên trong."
    ),
    "06_cta": (
        "Một con số tưởng ngược đời, hoá ra là cả một hệ thống tính toán cực kỳ tinh tế. "
        "Lần tới nhìn cột điện cao thế, bạn sẽ thấy vật lý đang làm việc. "
        "Theo dõi để hiểu Toán Lý đang âm thầm vận hành quanh ta."
    ),
}
