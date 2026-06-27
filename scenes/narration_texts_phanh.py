"""
Lời thoại — "Chạy nhanh gấp đôi, phanh gấp 4 lần đường" (quãng phanh ∝ v²).
Vật lý 10 · ứng dụng đời thực · SHORT DỌC 9:16, ~2 phút (giải thích logic chi tiết).

NGUỒN DUY NHẤT cho: sinh giọng clone (clone_narration_phanh.py) + karaoke (phanh_video.py).
Giả định số liệu: thời gian phản xạ ~1s; giảm tốc khi phanh a≈7 m/s² (đường khô).
Quy ước TTS: số/công thức viết theo CÁCH ĐỌC; mỗi câu kết . ? ! để karaoke chia cụm.
"""

SEGMENTS = {
    "01_hook": (
        "Một đứa trẻ bất ngờ chạy ra đường, cách xe bạn bốn mươi mét. "
        "Bạn đạp phanh ngay lập tức. "
        "Nếu đang chạy bốn mươi km một giờ, bạn dừng lại kịp. "
        "Nhưng nếu chạy tám mươi, xe bạn vẫn đang lao tới khi chạm vạch đó. "
        "Chỉ nhanh gấp đôi, vì sao hậu quả lại khác hẳn?"
    ),
    "02_haiphan": (
        "Quãng đường để dừng một chiếc xe gồm hai phần. "
        "Phần một là quãng phản xạ: từ lúc mắt thấy nguy hiểm, đến lúc chân kịp đạp phanh. "
        "Phần hai là quãng phanh: từ lúc phanh bắt đầu ăn, đến khi xe dừng hẳn. "
        "Trực giác mách bảo: nhanh gấp đôi thì tốn gấp đôi. Nhưng toán học nói khác."
    ),
    "03_phanxa": (
        "Xét phần phản xạ trước. "
        "Con người mất khoảng một giây để phản ứng. "
        "Trong một giây đó, xe vẫn chạy đều, chưa hề giảm tốc. "
        "Quãng đường đi được bằng vận tốc nhân thời gian, nên phần này tỉ lệ thuận với tốc độ. "
        "Gấp đôi vận tốc thì gấp đôi quãng phản xạ: từ mười một mét lên hai mươi hai mét."
    ),
    "04_phanh": (
        "Giờ đến phần quan trọng nhất: quãng phanh. "
        "Khi phanh, lực ma sát phải triệt tiêu toàn bộ động năng của xe. "
        "Mà động năng bằng một phần hai khối lượng nhân vận tốc bình phương. "
        "Chính vì có vận tốc bình phương ở đây, quãng phanh tỉ lệ với bình phương tốc độ. "
        "Gấp đôi vận tốc, động năng gấp bốn, nên quãng phanh cũng gấp bốn lần. "
        "Ở bốn mươi km một giờ chỉ khoảng chín mét, nhưng ở tám mươi đã là ba mươi lăm mét."
    ),
    "05_rapso": (
        "Cộng hai phần lại. "
        "Ở bốn mươi km một giờ: mười một cộng chín, tổng cộng khoảng hai mươi mét. "
        "Ở tám mươi: hai mươi hai cộng ba mươi lăm, gần sáu mươi mét. "
        "Quay lại đứa trẻ cách bốn mươi mét. "
        "Đi bốn mươi, bạn dừng cách bé tới hai mươi mét, an toàn. "
        "Nhưng ở tám mươi, bạn còn chưa kịp dừng khi đã vượt qua điểm đó."
    ),
    "06_ynghia": (
        "Đó là lý do vì sao khu dân cư luôn giới hạn tốc độ thấp. "
        "Không phải nhanh hơn một chút thì nguy hiểm hơn một chút, "
        "mà nguy hiểm tăng theo bình phương. "
        "Và quy luật vận tốc bình phương này có mặt trong mọi va chạm, vì nó chính là động năng."
    ),
    "07_cta": (
        "Tốc độ gấp đôi, quãng phanh gấp bốn. "
        "Một công thức nhỏ trong vật lý, nhưng là ranh giới giữa an toàn và tai nạn. "
        "Theo dõi để hiểu Toán Lý đang âm thầm vận hành cuộc sống của bạn."
    ),
}
