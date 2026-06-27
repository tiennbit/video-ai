"""
Lời thoại — "Đo chiều cao toà nhà mà không cần trèo" (lượng giác / hệ thức lượng, tan).
Toán 10 (tỉ số lượng giác trong tam giác vuông) · ứng dụng đời thực · SHORT DỌC 9:16, ~1 phút 50 · KHÔNG intro.

NGUỒN DUY NHẤT cho: clone_narration_docao.py + karaoke (docao_video.py).
Số liệu minh hoạ (nêu rõ trong video): đứng cách chân toà nhà năm mươi mét, đo góc nhìn lên đỉnh là sáu mươi độ
→ chiều cao = năm mươi nhân tan sáu mươi độ ≈ tám mươi sáu mét.
Quy ước TTS: số đọc bằng chữ; mỗi câu kết . ? ! để karaoke chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Trước mặt bạn là một toà nhà cao chọc trời. "
        "Làm sao đo được chiều cao của nó mà không cần trèo lên, "
        "không thước dây, không máy bay? "
        "Chỉ cần đứng dưới đất và một góc nhìn, bạn sẽ ra con số chính xác."
    ),
    "02_vande": (
        "Đây là tình huống thật. "
        "Bạn đứng cách chân toà nhà năm mươi mét. "
        "Ngẩng đầu nhìn lên đỉnh, bạn đo được góc nhìn lên là sáu mươi độ. "
        "Chỉ có vậy thôi. Vậy mà đủ để tìm ra chiều cao."
    ),
    "03_mohinh": (
        "Hãy vẽ lại tình huống thành một tam giác vuông. "
        "Cạnh nằm ngang là khoảng cách năm mươi mét. "
        "Cạnh đứng chính là chiều cao toà nhà mà ta cần tìm. "
        "Góc giữa tia nhìn và mặt đất là sáu mươi độ."
    ),
    "04_consonu": (
        "Trong tam giác vuông, tang của góc bằng cạnh đối chia cạnh kề. "
        "Tức là tang sáu mươi độ bằng chiều cao chia cho năm mươi. "
        "Suy ra chiều cao bằng năm mươi nhân tang sáu mươi độ. "
        "Bấm máy ra khoảng tám mươi sáu mét."
    ),
    "05_ynghia": (
        "Chỉ một góc và một khoảng cách, ta đo được cả toà nhà. "
        "Hơn hai nghìn năm trước, Thales đã đo kim tự tháp bằng đúng cách này, chỉ nhờ cái bóng của nó. "
        "Ngày nay cũng chính tang của góc giúp ta đo chiều cao của cây, của núi, và cả đỉnh Everest từ xa."
    ),
    "06_cta": (
        "Một tam giác nhỏ trên giấy mở khoá được cả những thứ khổng lồ ngoài đời. "
        "Lượng giác chính là cây thước vô hình của thiên văn, trắc địa và định vị. "
        "Theo dõi để hiểu Toán Lý đang âm thầm vận hành quanh ta."
    ),
}
