# 🗂️ KHO Ý TƯỞNG — Toán & Lý đời thực (video ~2 phút, dọc 9:16)

> Mỗi mục = 1 video 2 phút theo template **logic-first**: Hook → Đặt vấn đề thực →
> Mô hình hoá (giải thích VÌ SAO từng bước) → Giải ra con số → Ý nghĩa/tổng quát → CTA.
> Tag: 🎯 độ hấp dẫn · 🎨 độ dễ dựng hình (Manim) · ⚠️ số liệu cần kiểm chứng web.
> Trạng thái: bản nháp v1 (logic đã vet); con số ⚠️ sẽ tra web khi hệ thống search hoạt động lại.

---


## 📐 TOÁN

### T1. Lãi kép — "1 đồng thành 1 tỉ" ✅ ĐÃ LÀM (Tập 1)
Cấp số nhân/lãi kép. (Đã có `laikep_video.py`.)

### T2. Hàm mũ — "Vì sao 1 video bùng nổ triệu view sau 1 sáng?"
- 🎯 cao · 🎨 dễ · Lớp 11–12 (hàm mũ, cấp số nhân)
- **Thực:** 1 người chia sẻ cho 2 người, mỗi vòng lặp lại.
- **Logic:** số người tiếp cận sau n vòng = 2ⁿ (hoặc Rⁿ với R = hệ số lan truyền). Vẽ đường cong mũ vọt đứng; so với tăng tuyến tính.
- **Wow:** chỉ ~20–30 vòng là phủ cả triệu người. Cùng quy luật với dịch bệnh (R₀) → vì sao "làm phẳng đường cong" quan trọng.
- **Còn dùng:** lãi kép [[T1]], tin đồn, marketing.

### T3. Logarit — "Động đất 7 độ mạnh hơn 6 độ bao nhiêu?"
- 🎯 cao · 🎨 trung bình · Lớp 11 (logarit)
- **Thực:** tin báo động đất 6.0 và 7.0 — chênh "1 độ" nghe như nhau?
- **Logic:** thang Richter là thang LOG. Mỗi 1 độ → biên độ ×10, **năng lượng ×~31.6** (=10¹·⁵). ⚠️ kiểm chứng hệ số 31.6.
- **Wow:** 9.0 so với 6.0 = 3 bậc → năng lượng gấp ~32.000 lần. Giải thích vì sao 9 độ là thảm hoạ.
- **Còn dùng:** decibel (âm thanh), pH (hoá), độ sáng sao.

### T4. Lượng giác — "Đo chiều cao toà nhà mà không cần trèo"
- 🎯 cao · 🎨 dễ · Lớp 10–11 (hệ thức lượng, tan)
- **Thực:** đứng cách chân toà nhà 50m, đo góc nhìn lên đỉnh.
- **Logic:** tan(góc) = chiều cao / khoảng cách → chiều cao = 50·tan(góc). Minh hoạ tam giác vuông động.
- **Wow:** Thales đo kim tự tháp bằng cái bóng; cách đo Everest, đo cây, đo núi từ xa.
- **Còn dùng:** GPS [[T8]], thiên văn, trắc địa.

### T5. Xác suất (Bayes) — "Xét nghiệm dương tính 99% — bạn có thật sự mắc bệnh?"
- 🎯 rất cao (phản trực giác) · 🎨 trung bình · Lớp 11–12 (xác suất có điều kiện)
- **Thực:** bệnh hiếm (1/1000 người), test chính xác 99%. Bạn dương tính.
- **Logic:** trong 1000 người: 1 bệnh thật (gần chắc +), nhưng ~10 người khoẻ cũng "+" giả (1% của 999). → P(bệnh thật | dương tính) ≈ 1/11 ≈ **9%**.
- **Wow:** dương tính ≠ chắc chắn bệnh — vì tỉ lệ nền thấp. ⚠️ trình bày bằng số nguyên người cho dễ hiểu.
- **Còn dùng:** lọc spam, chẩn đoán AI, pháp y.

### T6. Tổ hợp — "Mật khẩu của bạn bị bẻ trong bao lâu?"
- 🎯 cao · 🎨 dễ · Lớp 11 (quy tắc đếm, tổ hợp)
- **Thực:** mật khẩu 8 ký tự so với 10 ký tự.
- **Logic:** số khả năng = (số ký tự)^(độ dài). Với ~95 ký tự in được: 95⁸ vs 95¹⁰. Chia cho tốc độ dò của máy.
- **Wow:** thêm 2 ký tự → số khả năng gấp ~9.000 lần → thời gian bẻ từ "giờ" thành "năm". ⚠️ tra tốc độ dò GPU thực tế (tỷ phép/giây).
- **Còn dùng:** an ninh mạng, mã PIN, biển số xe.

### T7. Đạo hàm (tối ưu) — "Vì sao lon nước ngọt có đúng hình dạng đó?"
- 🎯 cao · 🎨 trung bình · Lớp 12 (ứng dụng đạo hàm, GTNN)
- **Thực:** hãng muốn chứa 330ml nhưng tốn ít nhôm nhất.
- **Logic:** cố định thể tích V, tối thiểu diện tích vỏ S(r) → S'(r)=0 → ra điều kiện **chiều cao = đường kính** (h=2r).
- **Wow:** tiết kiệm hàng triệu đô vật liệu mỗi năm; vì sao lon thực tế hơi khác (chi phí nắp dày hơn).
- **Còn dùng:** thùng, bể, bao bì, logistics.

### T8. Vector & toạ độ — "GPS định vị bạn đến từng mét bằng cách nào?"
- 🎯 rất cao · 🎨 trung bình · Lớp 12 (toạ độ không gian, mặt cầu)
- **Thực:** điện thoại biết vị trí dù vệ tinh cách 20.000 km.
- **Logic:** mỗi vệ tinh cho 1 khoảng cách → bạn nằm trên 1 mặt cầu. Giao 3–4 mặt cầu = 1 điểm. Khoảng cách suy từ thời gian tín hiệu × tốc độ ánh sáng.
- **Wow:** sai 1 phần triệu giây → lệch 300m → **phải hiệu chỉnh cả thuyết tương đối** (đồng hồ vệ tinh nhanh hơn ⚠️ ~38 µs/ngày).
- **Còn dùng:** bản đồ, drone, game 3D.

### T9. Tích phân — "Tính lượng nước một con đập chứa được"
- 🎯 trung bình · 🎨 trung bình · Lớp 12 (tích phân, diện tích/thể tích)
- **Thực:** mặt hồ cong, đáy lồi lõm — làm sao biết thể tích?
- **Logic:** "chia nhỏ vô hạn" thành lát mỏng, cộng tất cả lại = tích phân. Minh hoạ Riemann → đường cong.
- **Wow:** cùng ý tưởng tính quãng đường từ đồ thị vận tốc, lượng thuốc trong máu, diện tích logo bất kỳ.
- **Còn dùng:** kỹ thuật, kinh tế (tổng tích luỹ).

### T10. Bí mật phòng thì thầm — "Tại sao thì thầm ở góc này, người đứng tận góc kia nghe rõ mồn một?"
- 🎯 cao · 🎨 dễ · Lớp 10 (Conic - elip và tính chất phản xạ qua hai tiêu điểm; định nghĩa elip MF1+MF2=2a) ⚠️ Khoảng cách hai tiêu điểm phòng thì thầm St Paul's và mức âm nghe được
- **Thực:** Phòng vòm hình elip (whispering gallery) ở nhà thờ St Paul's: hai người đứng cách nhau 30m vẫn nghe tiếng thì thầm của nhau, dù xung quanh ồn ào.
- **Logic:** Mô hình trần phòng là một elip với hai tiêu điểm F1, F2. Tính chất conic: mọi tia âm xuất phát từ F1 phản xạ trên thành elip đều đi qua F2, và quãng đường F1->thành->F2 luôn bằng 2a nên âm tới cùng pha. Đặt người nói ở F1, người nghe ở F2.
- **Wow:** Âm thanh hội tụ y như ánh sáng: 100% tia âm dù đi hướng nào cũng dồn về đúng 1 điểm.
- **Còn dùng:** Đèn pha ô tô (parabol), chảo vệ tinh, máy tán sỏi thận bằng sóng xung kích, kính thiên văn phản xạ.

### T11. Đường việt vị của VAR — "Một đầu gối nhô ra 5cm cũng đủ huỷ bàn thắng - VAR vẽ đường đó bằng cái gì?"
- 🎯 cao · 🎨 trung bình · Lớp 10 (Vectơ - phép chiếu và tích vô hướng để so sánh vị trí theo một trục) ⚠️ Số điểm dữ liệu mỗi cầu thủ và thời gian tiết kiệm của SAOT
- **Thực:** Công nghệ việt vị bán tự động (SAOT) ở Ngoại hạng Anh kẻ đường thẳng qua hậu vệ thứ 2 và tiền đạo để xác định ai đứng trước ai.
- **Logic:** Dựng vectơ pháp tuyến của đường biên ngang làm hướng chuẩn. Chiếu vị trí hậu vệ và tiền đạo lên trục dọc sân bằng tích vô hướng; so sánh hình chiếu để biết cầu thủ nào ở gần khung thành đối phương hơn. Khác biệt vài cm = chênh lệch hình chiếu.
- **Wow:** Hệ thống bám 10.000 điểm lưới trên thân mỗi cầu thủ, ra quyết định việt vị nhanh hơn trọng tài tới 30 giây.
- **Còn dùng:** Định vị trong game, xe tự lái xác định làn đường, robot cảm biến khoảng cách, đồ hoạ 3D.

### T12. Bắn pháo hoa trúng đỉnh — "Pháo hoa nổ đúng đỉnh cao nhất, không sớm không muộn - làm sao tính được giây đó?"
- 🎯 cao · 🎨 dễ · Lớp 10 (Hàm số bậc hai - đỉnh parabol, giá trị lớn nhất tại x = -b/2a)
- **Thực:** Người đốt pháo hoa lễ hội muốn quả pháo nổ ngay lúc lên cao nhất để bông hoa xoè đều, biết tốc độ bắn lên ban đầu.
- **Logic:** Độ cao theo thời gian là hàm bậc hai h(t) = -5t^2 + v0·t. Đây là parabol quay xuống; đỉnh parabol tại t = -b/2a chính là thời điểm cao nhất, h cực đại = giá trị tại đỉnh. Hẹn giờ ngòi nổ bằng đúng t đỉnh.
- **Wow:** Cùng một quả pháo, chỉ cần chỉnh ngòi lệch 0,3 giây là bông hoa nổ lệch vài chục mét và méo hẳn.
- **Còn dùng:** Tính tầm xa vòi phun nước, đường bay quả bóng rổ, tối ưu doanh thu/lợi nhuận, thiết kế cầu vòm.

### T13. Cú nhảy ba bước vàng — "Vận động viên nhảy xa nên lao nhanh hay nhảy cao? Toán bảo: phải cân bằng."
- 🎯 trung bình · 🎨 trung bình · Lớp 10 (Hệ thức lượng - giá trị lượng giác và cực trị của biểu thức sin·cos) ⚠️ Góc giậm nhảy thực tế của kỷ lục gia nhảy xa
- **Thực:** Tuyển thủ điền kinh muốn tối đa tầm nhảy xa, chọn góc giậm nhảy với tốc độ chạy đà cố định để chân tiếp cát xa nhất.
- **Logic:** Tầm xa L phụ thuộc góc qua biểu thức chứa sin và cos của góc giậm. Dùng hệ thức lượng và tính chất tích sin·cos đạt cực đại khi hai góc bù trợ bằng nhau, suy ra góc tối ưu lý thuyết 45 độ; rồi giải thích vì sao người thật chọn ~20-22 độ do hạn chế cơ thể.
- **Wow:** Kỷ lục thế giới nhảy xa dùng góc chỉ ~20 độ chứ không phải 45 - vì người không phải viên đạn, chân không bật được lực ngang lớn như vậy.
- **Còn dùng:** Ném lao, đá phạt bóng đá, vòi tưới cây, thiết kế đường trượt ván.

### T14. Tam giác cứu hộ trên biển — "Tàu cá kêu cứu nhưng không có GPS - hai trạm radar tìm ra nó trong 1 phút."
- 🎯 cao · 🎨 dễ · Lớp 10 (Hệ thức lượng trong tam giác - định lý sin)
- **Thực:** Hai trạm ven biển cách nhau 40km cùng bắt được tín hiệu cấp cứu, mỗi trạm chỉ đo được góc hướng về tàu, cần tìm khoảng cách để điều tàu cứu hộ.
- **Logic:** Tam giác tạo bởi hai trạm và tàu có cạnh đáy đã biết và hai góc đo được. Dùng định lý sin: cạnh chia sin góc đối bằng nhau, suy ra khoảng cách từ mỗi trạm tới tàu, rồi định vị chính xác toạ độ tàu.
- **Wow:** Chỉ cần hai cái máy đo góc, không cần đến gần, đã khoanh đúng vị trí tàu lạc giữa biển khơi.
- **Còn dùng:** Định vị nguồn phát sóng, đo khoảng cách thiên văn (thị sai sao), trắc địa đo đất, dẫn đường máy bay.

### T15. Cú xoáy của Messi — "Quả đá phạt vòng qua hàng rào rồi cắm vào góc xa - lực nào bẻ cong nó?"
- 🎯 cao · 🎨 trung bình · Lớp 10 (Vectơ - phép cộng vectơ và quy tắc hình bình hành) ⚠️ Độ lệch ngang tối đa của quả sút xoáy chuối
- **Thực:** Cầu thủ sút phạt, bóng xoáy tạo lực Magnus đẩy ngang. Người phân tích cần cộng vận tốc bay thẳng với độ lệch ngang để vẽ đường cong tới khung thành.
- **Logic:** Biểu diễn chuyển động bằng vectơ: vectơ vận tốc tới khung thành cộng vectơ độ lệch ngang do xoáy. Tổng hai vectơ theo quy tắc hình bình hành cho hướng và độ lớn vận tốc thực; độ lệch tích luỹ vẽ nên quỹ đạo cong.
- **Wow:** Bóng có thể lệch ngang hơn 1 mét trên quãng đường 20m - đủ để lách qua hàng rào người rồi đổi hướng vào lưới.
- **Còn dùng:** Đường bay quả tennis/bóng chuyền, mô phỏng gió tạt máy bay, cộng lực kéo trong cơ học, dòng chảy sông và thuyền.

### T16. Phễu chứng khoán lừa tình — "Hai quỹ cùng lãi trung bình 10%/năm - vì sao một cái khiến bạn mất ngủ?"
- 🎯 cao · 🎨 dễ · Lớp 10 (Thống kê - phương sai và độ lệch chuẩn đo độ phân tán)
- **Thực:** Nhà đầu tư chọn giữa hai quỹ: cùng lợi nhuận trung bình năm là 10%, nhưng một quỹ ổn định, một quỹ lúc +40% lúc -20%.
- **Logic:** Trung bình giống nhau không nói lên rủi ro. Tính phương sai và độ lệch chuẩn của chuỗi lợi nhuận: quỹ dao động mạnh có độ lệch chuẩn lớn hơn nhiều. Độ lệch chuẩn chính là thước đo rủi ro tài chính.
- **Wow:** Cùng lãi trung bình 10%, quỹ có độ lệch chuẩn 30% có thể khiến bạn lỗ nặng đúng năm cần rút tiền - trong khi bảng quảng cáo trông y hệt nhau.
- **Còn dùng:** So sánh điểm thi giữa các lớp, kiểm soát chất lượng nhà máy, đánh giá độ ổn định của VĐV, chỉ số biến động VN-Index.

### T17. Một KOL nói dối cả bảng số — "Lương trung bình công ty 50 triệu/tháng - nhưng 90% nhân viên không hề có?"
- 🎯 cao · 🎨 dễ · Lớp 10 (Thống kê - số trung bình, trung vị và ảnh hưởng của giá trị ngoại lệ)
- **Thực:** Công ty 10 người: 9 người lương 15 triệu, 1 sếp lương 400 triệu. Báo cáo khoe lương trung bình ~53 triệu để tuyển dụng.
- **Logic:** So sánh số trung bình và trung vị. Một giá trị ngoại lệ kéo lệch hẳn trung bình, nhưng trung vị (15 triệu) phản ánh đúng người ở giữa. Khi dữ liệu lệch, trung vị mới đáng tin.
- **Wow:** Đổi 1 con số duy nhất làm trung bình nhảy từ 15 lên 53 triệu, còn trung vị đứng yên - đó là cách số liệu đánh lừa bạn.
- **Còn dùng:** Giá nhà trung bình khu phố, thu nhập quốc gia, lượt view trung bình kênh, điểm chuẩn đại học.

### T18. Cửa hàng nên giảm giá bao nhiêu — "Giảm giá càng sâu càng đông khách - nhưng tại điểm nào thì lỗ vốn?"
- 🎯 cao · 🎨 dễ · Lớp 10 (Hàm số bậc hai - bài toán tối ưu doanh thu, đỉnh parabol)
- **Thực:** Quán trà sữa đang bán 30k/ly được 200 ly/ngày. Cứ giảm 1k thì bán thêm 20 ly. Chủ quán muốn biết giá nào cho doanh thu cao nhất.
- **Logic:** Gọi mức giảm là x nghìn. Doanh thu R(x) = (30 - x)(200 + 20x) là hàm bậc hai theo x, parabol quay xuống. Đỉnh tại x = -b/2a cho mức giảm tối ưu và doanh thu cực đại.
- **Wow:** Giảm đúng 5k cho doanh thu cao nhất; giảm tới 15k thì bán gấp đôi ly mà tiền thu về lại còn ít hơn lúc đầu.
- **Còn dùng:** Định giá vé xem phim, đặt giá quảng cáo, tối ưu diện tích chuồng trại, lợi nhuận sản xuất.

### T19. Định vị sét bằng tiếng nổ — "Sét đánh ở đâu? Hai trạm nghe tiếng nổ là vẽ ra được đường cong tìm nó."
- 🎯 trung bình · 🎨 trung bình · Lớp 10 (Conic - hypebol và định nghĩa qua hiệu khoảng cách tới hai tiêu điểm)
- **Thực:** Hai trạm quan trắc nghe tiếng sấm lệch nhau 2 giây. Vì âm thanh có tốc độ cố định, hiệu khoảng cách tới hai trạm là một hằng số.
- **Logic:** Tập hợp các điểm có hiệu khoảng cách tới hai tiêu điểm bằng hằng số chính là một nhánh hypebol: |MF1 - MF2| = 2a. Vẽ hypebol từ mỗi cặp trạm; giao của các đường cong định vị tia sét.
- **Wow:** Đây đúng là nguyên lý hệ định vị LORAN cũ dẫn đường tàu thuyền cả thế kỷ - chỉ dùng hiệu thời gian, không cần đo khoảng cách thật.
- **Còn dùng:** GPS (về bản chất cũng dùng hiệu khoảng cách), định vị nguồn nổ, dò ô nhiễm tiếng ồn, sonar tàu ngầm.

### T20. Bạn có thật sự xui không — "Mở 10 hộp gacha không ra nhân vật xịn - bạn xui, hay tỉ lệ 'hiếm' chỉ là cái bẫy?"
- 🎯 cao · 🎨 dễ · Lớp 10 (Xác suất - biến cố đối và quy tắc nhân cho biến cố độc lập)
- **Thực:** Game gacha quảng cáo tỉ lệ ra nhân vật 5 sao là 1%. Người chơi nạp tiền mở 10 lần và tin chắc kiểu gì cũng ra.
- **Logic:** Biến cố đối: xác suất KHÔNG ra mỗi lần là 0,99. Mười lần độc lập nhân lại: 0,99^10. Xác suất ra ít nhất một lần = 1 - 0,99^10. Tính ra chỉ khoảng 9,6%, không hề chắc chắn.
- **Wow:** Phải mở khoảng 69 lần mới có hơn 50% cơ hội ra được nhân vật 5 sao - tỉ lệ 1% lừa não bạn nặng đến vậy.
- **Còn dùng:** Rủi ro trúng/trật khi quay số, độ tin cậy hệ thống nhiều linh kiện, xác suất ít nhất một ca dương tính, vé số.

### T21. Ăng-ten chảo và điểm vàng — "Vì sao chảo thu sóng vệ tinh không lắp đầu thu ở đáy mà lại nhô ra giữa không trung?"
- 🎯 cao · 🎨 dễ · Lớp 10 (Conic - parabol và tính chất phản xạ qua tiêu điểm)
- **Thực:** Lắp chảo K+ thu tín hiệu vệ tinh: sóng từ trời xuống gần như song song, phải đặt đầu thu (LNB) đúng chỗ để bắt được tín hiệu mạnh nhất.
- **Logic:** Mặt cắt chảo là parabol. Tính chất phản xạ parabol: mọi tia song song với trục đối xứng sau khi phản xạ đều đi qua tiêu điểm. Đặt đầu thu đúng tiêu điểm thì toàn bộ năng lượng sóng dồn về một điểm.
- **Wow:** Cả mét vuông sóng yếu ớt từ vệ tinh cách 36.000km được gom đúng về một điểm bé bằng đầu ngón tay - sai vài cm là mất sóng.
- **Còn dùng:** Đèn pin/đèn pha (đảo ngược: nguồn ở tiêu điểm cho tia song song), kính thiên văn, bếp năng lượng mặt trời, micro parabol.

### T22. Thuật toán gợi ý bạn cùng gu — "Vì sao TikTok biết bạn và một người lạ 'hợp gu' để gợi ý theo dõi nhau?"
- 🎯 cao · 🎨 trung bình · Lớp 10 (Vectơ - tích vô hướng và góc giữa hai vectơ (cosine similarity))
- **Thực:** Mạng xã hội biểu diễn sở thích mỗi người thành một dãy số (vectơ đặc trưng), rồi đo độ giống nhau giữa hai người để gợi ý kết bạn hoặc nội dung.
- **Logic:** Mỗi người là một vectơ trong không gian sở thích. Độ tương đồng tính bằng tích vô hướng chia tích độ dài - chính là cos của góc giữa hai vectơ. Góc càng nhỏ (cos gần 1) thì hai người càng giống gu.
- **Wow:** Hai người chưa từng quen nhau được app xếp 'hợp nhau' chỉ vì góc giữa hai vectơ sở thích của họ gần 0 độ - toán quyết định bạn xem gì tiếp theo.
- **Còn dùng:** Gợi ý phim Netflix, tìm kiếm hình ảnh giống nhau, lọc thư rác, nhận dạng khuôn mặt, công cụ dịch máy.

### T23. Phím đàn và căn bậc 12 của 2 — "Vì sao 12 phím đàn piano lại 'lệch' nhau đúng kiểu đó, không hề tuỳ tiện?"
- 🎯 cao · 🎨 dễ · Lớp 11 (Cấp số nhân (công bội, số hạng tổng quát un = u1·q^(n-1))) ⚠️ q = căn bậc 12 của 2 xấp xỉ 1,05946; A4 = 440 Hz; phím 12 = nửa dây nên tần số ×2 (equal temperament)
- **Thực:** Đàn guitar/piano: từ nốt La 440 Hz, mỗi phím (nửa cung) cao hơn phím trước theo cùng một tỉ lệ; lên đúng 12 phím thì tần số gấp đôi (cao 1 quãng tám).
- **Logic:** Tần số các nốt là một CẤP SỐ NHÂN với công bội q. Đi 12 bước phải nhân thành 2 nên q^12 = 2, suy ra q = căn bậc 12 của 2 xấp xỉ 1,0595. Đặt phím đàn (phím thứ 12 nằm đúng giữa dây) chính là dựng cấp số nhân này trên gỗ.
- **Wow:** Cả nền âm nhạc hiện đại đứng trên một con số vô tỉ: 1,05946. Phím thứ 12 cắt dây làm đôi nên tần số gấp đúng 2 lần.
- **Còn dùng:** Lên dây đàn, autotune, nén âm thanh MP3, thiết kế nhạc cụ, phần mềm chỉnh nhạc.

### T24. Nghịch lý sinh nhật trong lớp học — "Lớp bạn chỉ 23 người - cá rằng có 2 bạn trùng ngày sinh, bạn dám không?"
- 🎯 cao · 🎨 trung bình · Lớp 11 (Xác suất biến cố đối + tổ hợp chập 2 (C(n,2) đếm cặp)) ⚠️ 23 người -> 50,7%; C(23,2)=253 cặp; 75 người -> 99,9% (birthday problem)
- **Thực:** Một phòng 23 người (đúng cỡ một lớp/nhóm dự án). Hỏi: xác suất có ÍT NHẤT hai người trùng ngày sinh là bao nhiêu?
- **Logic:** Đếm bằng biến cố đối: tính xác suất TẤT CẢ khác ngày = (365/365)(364/365)...(343/365), rồi lấy 1 trừ đi. Mấu chốt: số CẶP người = C(23,2) = 253 cặp, mỗi cặp một cơ hội trùng.
- **Wow:** Chỉ 23 người mà xác suất trùng đã 50,7%; 75 người là 99,9%. Trực giác nói 'phải cần ~183 người' là sai bét vì ta đếm cặp chứ không đếm người.
- **Còn dùng:** Bảo mật băm mật khẩu (birthday attack), trùng mã hoá, dò gian lận, kiểm thử dữ liệu trùng.

### T25. Bờ biển dài vô hạn — "Bờ biển Việt Nam dài bao nhiêu km? Câu trả lời đúng là... vô hạn."
- 🎯 cao · 🎨 trung bình · Lớp 11 (Giới hạn tổng cấp số nhân lùi vô hạn (|q|<1 hội tụ, |q|>=1 phân kỳ)) ⚠️ Chu vi ×4/3 mỗi bước -> vô hạn; diện tích hội tụ 8/5 tam giác gốc (Koch snowflake)
- **Thực:** Đo bờ biển bằng thước 100 km được một số; đo lại bằng thước 1 km thấy dài hơn nhiều vì lọt vào từng vũng, mũi đá. Thước càng nhỏ, số càng phình to.
- **Logic:** Mô hình bằng bông tuyết Koch: mỗi bước thay 1 cạnh bằng 4 đoạn dài 1/3 nên chu vi nhân 4/3 mỗi vòng. Chu vi là cấp số nhân công bội 4/3 > 1 nên tổng tiến tới VÔ HẠN. Nhưng diện tích lại là cấp số nhân công bội 4/9 < 1 nên tổng HỘI TỤ.
- **Wow:** Một hình có CHU VI VÔ HẠN nhưng DIỆN TÍCH HỮU HẠN. Đây là lý do bản đồ ghi độ dài bờ biển mỗi nguồn một khác.
- **Còn dùng:** Nén ảnh fractal, ăng-ten điện thoại gấp khúc, mô hình mạch máu/phổi, đồ hoạ game địa hình.

### T26. Thuỷ triều là một hàm sin — "Làm sao ngư dân biết trước con nước lên xuống chính xác... cho cả năm sau?"
- 🎯 trung bình · 🎨 dễ · Lớp 11 (Hàm số lượng giác tuần hoàn (biên độ, chu kỳ T = 2π/ω, pha)) ⚠️ Chu kỳ thuỷ triều bán nhật ~12h25' (cần ghi rõ địa phương); biên độ tuỳ cảng
- **Thực:** Mực nước biển ở cảng lên xuống đều đặn ~2 lần/ngày. Lịch thuỷ triều in sẵn giờ nước lớn, nước ròng từng ngày để tàu ra vào, người nuôi tôm canh xả nước.
- **Logic:** Mô hình mực nước h(t) = A·cos(ω·t) + h0: A là biên độ con nước, ω = 2π/chu kỳ (~12h25'). Đây là hàm lượng giác tuần hoàn nên biết chu kỳ và biên độ là dự đoán được mọi thời điểm trong tương lai bằng cách thay t.
- **Wow:** Chỉ với một hàm cos, ta tính được giờ nước lớn của 10 năm sau - vì biển 'lặp lại' tuyệt đối đều theo Mặt Trăng.
- **Còn dùng:** Cảng biển, thuỷ điện thuỷ triều, dự báo ngập đô thị, nhịp sinh học, tín hiệu điện xoay chiều.

### T27. Liều thuốc và giới hạn an toàn — "Uống thuốc mỗi 8 tiếng - vì sao thuốc không 'tích lại' đến mức ngộ độc?"
- 🎯 cao · 🎨 trung bình · Lớp 11 (Giới hạn dãy số / tổng cấp số nhân lùi vô hạn S = u1/(1-q)) ⚠️ Mô hình một ngăn (one-compartment) bán thải; r = (1/2)^(Δt/t½) - nêu là mô hình đơn giản hoá
- **Thực:** Mỗi liều thuốc đưa nồng độ trong máu tăng vọt, rồi gan thận đào thải bớt giữa hai liều. Liều mới cộng vào phần còn sót của liều cũ.
- **Logic:** Sau mỗi chu kỳ còn lại tỉ lệ r (vd r=1/2 nếu mất nửa). Nồng độ trước liều thứ n là cấp số nhân: D·(r + r^2 + ...) nên tổng cấp số nhân lùi vô hạn = D·r/(1-r). Nó HỘI TỤ về một mức ổn định chứ không lên vô hạn.
- **Wow:** Dù uống thuốc cả đời, nồng độ chỉ tiệm cận một 'trần' cố định - bác sĩ chọn liều để cái trần đó nằm dưới mức độc, trên mức có tác dụng.
- **Còn dùng:** Kê đơn kháng sinh, insulin, cà-phê-in tích trong cơ thể, sạc pin, mô hình ô nhiễm tích luỹ.

### T28. Tốc độ kế chính là đạo hàm — "Kim tốc độ trên xe máy đang đo cái gì mà nhảy nhạy đến vậy?"
- 🎯 cao · 🎨 dễ · Lớp 11 (Đạo hàm là tốc độ biến thiên tức thời (giới hạn tỉ số Δy/Δx khi Δx->0))
- **Thực:** Đồng hồ cây số (odometer) cho biết bạn đã đi tổng bao nhiêu km. Kim tốc độ lại cho 'nhanh thế nào ngay lúc này'. Hai cái khác nhau.
- **Logic:** Quãng đường s(t) là một hàm theo thời gian. Vận tốc trung bình = Δs/Δt trên một đoạn. Cho Δt -> 0 ta được vận tốc TỨC THỜI = đạo hàm s'(t). Tốc độ kế đo đúng độ dốc tiếp tuyến của đồ thị quãng đường tại đúng khoảnh khắc này.
- **Wow:** Tốc độ kế là một cỗ máy lấy đạo hàm chạy 24/7. Gia tốc kế trong điện thoại làm thêm bước nữa: đạo hàm của đạo hàm.
- **Còn dùng:** Phạt nguội tốc độ, đo gia tốc điện thoại (đếm bước, xoay màn hình), kinh tế (tốc độ tăng giá), y tế (nhịp biến đổi).

### T29. Vì sao tên lửa luôn ngỏng đúng góc — "Tên lửa, máy bay nghiêng đúng góc tối ưu - ai tính ra góc đó và bằng cách nào?"
- 🎯 trung bình · 🎨 dễ · Lớp 11 (Ứng dụng đạo hàm: tìm cực trị bằng phương trình f'(x) = 0)
- **Thực:** Một viên đạn/quả pháo hoa bay theo quỹ đạo parabol. Người ta cần biết nó đạt độ cao tối đa ở đâu, hoặc nghiêng dàn phóng góc nào để đạt độ cao mong muốn nhanh nhất.
- **Logic:** Độ cao h(t) là hàm bậc 2 theo thời gian (parabol). Tại đỉnh, vận tốc thẳng đứng = 0, tức ĐẠO HÀM h'(t) = 0. Giải h'(t)=0 ra thời điểm và độ cao cực đại - không cần thử từng giá trị.
- **Wow:** Đạo hàm bằng 0 = 'đứng yên một khoảnh khắc' = đỉnh quỹ đạo. Cùng một phép tính tìm điểm cao nhất của cú nhảy, đỉnh tia nước đài phun, giá cổ phiếu đạt đỉnh.
- **Còn dùng:** Đạn đạo, đài phun nước nghệ thuật, nhảy cao thể thao, drone, tối ưu lợi nhuận.

### T30. Xếp lịch thi không trùng giờ — "Một trường nghìn học sinh, hàng trăm môn - máy tính xếp lịch thi không trùng kiểu gì?"
- 🎯 cao · 🎨 dễ · Lớp 11 (Hoán vị, chỉnh hợp và quy tắc nhân (n! bùng nổ)) ⚠️ 10! = 3.628.800; 52! xấp xỉ 8×10^67
- **Thực:** Cần xếp lịch sao cho không ai phải thi 2 môn cùng buổi. Hoặc bài toán xếp đội tuyển: chọn 5 bạn vào 5 vị trí khác nhau từ một nhóm.
- **Logic:** Đếm số cách bằng quy tắc nhân và chỉnh hợp/hoán vị. Vị trí 1 có n cách, vị trí 2 còn n-1 cách... nên n·(n-1)·(n-2)... = chỉnh hợp Ank. Số khả năng bùng nổ giai thừa cực nhanh.
- **Wow:** Chỉ xếp 10 môn vào 10 buổi đã có 10! = hơn 3,6 triệu cách. Đó là lý do phải dùng thuật toán chứ không thử tay - và vì sao xáo bài 52 lá cho ra một thứ tự gần như CHƯA AI từng có.
- **Còn dùng:** Xếp thời khoá biểu, lịch bay, lịch trận đấu, sắp xếp dữ liệu, mã hoá hoán vị.

### T31. Bữa buffet bao nhiêu cách gắp — "Quán trà sữa '6 topping tuỳ chọn' - quảng cáo 'hàng nghìn combo' có nói phét không?"
- 🎯 cao · 🎨 dễ · Lớp 11 (Tổ hợp C(n,k) và đẳng thức tổng tổ hợp = 2^n (nhị thức Newton)) ⚠️ Tổng C(n,0)+...+C(n,n) = 2^n; 2^10 = 1024
- **Thực:** Một quán cho chọn tuỳ ý các topping/lớp nhân từ một danh sách; mỗi món chỉ có 2 trạng thái: lấy hoặc không lấy. Hỏi tổng số combo khác nhau.
- **Logic:** Mỗi món là một lựa chọn nhị phân nên quy tắc nhân cho 2·2·...·2 = 2^n. Nếu muốn 'chọn đúng k món trong n' thì là tổ hợp C(n,k); tổng mọi k chính bằng 2^n (tổng hệ số nhị thức).
- **Wow:** 10 topping nên 2^10 = 1024 combo từ chỉ 10 lựa chọn. 'Hàng nghìn combo' là thật, mà còn ít! Đây cũng là lý do n bit lưu được 2^n trạng thái.
- **Còn dùng:** Cấu hình laptop/xe, menu tuỳ chọn, bit nhớ máy tính, chọn danh mục đầu tư, khai triển nhị thức Newton.

### T32. Trò chơi điện tử và số π bí ẩn — "Vì sao đường tròn trong game lại 'răng cưa', và máy tính 'vẽ' hình tròn bằng cách nào?"
- 🎯 trung bình · 🎨 trung bình · Lớp 11 (Giới hạn của dãy số (dãy chu vi đa giác -> 2πR)) ⚠️ Chu vi n-giác đều nội tiếp -> 2πR khi n-> vô cùng (phương pháp Archimedes)
- **Thực:** Màn hình chỉ có các điểm ảnh vuông. Để vẽ đường cong mượt (vòng tròn, cung tốc độ), máy chia nhỏ thành rất nhiều đoạn thẳng/đa giác. Càng nhiều cạnh, càng giống cong.
- **Logic:** Cho đa giác đều n cạnh nội tiếp đường tròn, tính chu vi của nó. Khi n -> vô cùng, chu vi đa giác có GIỚI HẠN chính bằng chu vi đường tròn 2πR. Đây đúng là cách Archimedes 'kẹp' số π giữa hai đa giác.
- **Wow:** Hình tròn thật ra là giới hạn của đa giác vô số cạnh. Tăng độ phân giải = tăng n; đó là toàn bộ bí mật đồ hoạ mượt mà - và là cách loài người lần đầu tính ra số π.
- **Còn dùng:** Đồ hoạ 3D, độ phân giải màn hình, tính diện tích bất kỳ (tích phân), thiết kế bánh răng, robot vẽ.

### T33. Cú nảy của quả bóng dừng khi nào — "Thả quả bóng từ 1 mét, nó nảy mãi nảy mãi - tổng quãng đường nó đi là vô hạn?"
- 🎯 cao · 🎨 trung bình · Lớp 11 (Tổng cấp số nhân lùi vô hạn (hội tụ khi |q| < 1)) ⚠️ S = h0·(1+q)/(1-q) với rơi đầu; q=0,7, h0=1m -> tổng xấp xỉ 5,67m
- **Thực:** Bóng rổ/bóng tennis rơi rồi nảy lên, mỗi lần chỉ lên được một tỉ lệ độ cao lần trước (vd 70%). Số lần nảy thì 'vô hạn' nhưng bóng rõ ràng dừng sau vài giây.
- **Logic:** Độ cao mỗi lần nảy là cấp số nhân công bội q = 0,7 < 1. Tổng quãng đường = lần rơi đầu + 2 lần (mỗi lần lên rồi xuống) nên dùng công thức tổng cấp số nhân lùi vô hạn S = u1/(1-q). Vô hạn số hạng nhưng tổng HỮU HẠN.
- **Wow:** Bóng nảy vô số lần nhưng chỉ đi tổng cộng ~5,67 mét rồi nằm im (với q=0,7, h0=1m). 'Vô hạn lần' không có nghĩa là 'đi vô hạn xa' - nghịch lý Zeno được hoá giải.
- **Còn dùng:** Hệ số đàn hồi vật liệu, giảm chấn, tín hiệu tắt dần, phân rã phóng xạ, nghịch lý Zeno.

### T34. Cánh cửa dao động và hàm cosin — "Đẩy nhẹ cánh cửa, nó dao động qua lại rồi đứng yên - phương trình của chuyển động đó trông như thế nào?"
- 🎯 trung bình · 🎨 trung bình · Lớp 11 (Hàm số lượng giác (cos) mô tả dao động; chu kỳ và tần số góc ω) ⚠️ Dạng dao động tắt dần x(t)=A·e^(-kt)·cos(ωt) là mô hình chuẩn
- **Thực:** Lò xo giảm xóc xe máy, dây đàn vừa gảy, cái lưỡi gà còi xe: tất cả rung qua lại quanh vị trí cân bằng với biên độ NHỎ DẦN theo thời gian.
- **Logic:** Mô hình bằng hàm lượng giác nhân hàm tắt dần: x(t) = A·e^(-kt)·cos(ωt). Phần cos(ωt) cho dao động tuần hoàn; e^(-kt) bóp biên độ về 0. Vẽ đồ thị: sóng cos bị 'kẹp' trong hai đường cong mũ.
- **Wow:** Mọi rung động ngoài đời (dây đàn, lò xo, sóng âm tắt) đều là tích của một hàm cos và một hàm mũ giảm - một công thức gói cả tiếng đàn và giảm xóc xe bạn.
- **Còn dùng:** Giảm xóc ô tô/xe máy, cách âm, mạch điện RLC, cảm biến rung, hiệu ứng âm thanh.

### T35. Hình chiếu camera giám sát — "Một camera góc rộng treo góc trần - làm sao biết nó 'nhìn thấy' đúng vùng nào dưới sàn?"
- 🎯 trung bình · 🎨 trung bình · Lớp 11 (Hình học không gian: khoảng cách và góc giữa đường thẳng và mặt phẳng (Pythagoras 3D)) ⚠️ Đường chéo hộp 4×5×3 = căn(16+25+9)=căn50 xấp xỉ 7,07m
- **Thực:** Lắp camera an ninh hoặc đèn chiếu sân khấu ở góc trần phòng. Cần biết vùng phủ trên sàn, và khoảng cách thật từ camera tới một người đứng ở góc đối diện.
- **Logic:** Mô hình phòng thành hình hộp chữ nhật. Khoảng cách camera-người là độ dài đoạn thẳng trong KHÔNG GIAN, tính bằng định lý Pythagoras 3 chiều: d = căn(a^2+b^2+c^2). Góc nghiêng tia nhìn so với sàn tính bằng góc giữa đường thẳng và mặt phẳng.
- **Wow:** Đường chéo một căn phòng 4×5×3 m dài tới 7,07 m - xa hơn bạn tưởng. Cùng công thức cho khoảng cách máy bay, định vị 3D, và đường chéo màn hình.
- **Còn dùng:** Lắp camera/đèn, dựng phim 3D, kiến trúc, đo đường chéo TV, robot điều hướng.

### T36. Mái nhà dốc bao nhiêu là vừa — "Vì sao mái nhà miền Bắc dốc đứng còn mái miền Nam thoai thoải - toán quyết định độ dốc đó?"
- 🎯 trung bình · 🎨 trung bình · Lớp 11 (Hình học không gian: góc giữa hai mặt phẳng (góc nhị diện)) ⚠️ tan(góc dốc) = chiều cao nóc / nửa bề ngang; cần ví dụ số cụ thể khi dựng
- **Thực:** Người thợ phải đặt độ dốc mái: dốc quá thì tốn ngói và gió giật bay; thoải quá thì nước mưa đọng dột. Cần tính góc giữa mặt mái nghiêng và mặt sàn nằm ngang.
- **Logic:** Mô hình mái thành mặt phẳng nghiêng cắt mặt phẳng ngang. Góc nhị diện (góc giữa hai mặt phẳng) đo bằng cách dựng hai đường vuông góc với giao tuyến. Biết chiều cao đỉnh mái h và nửa bề ngang nhà b nên tan(góc dốc) = h/b.
- **Wow:** Cùng một ngôi nhà, chỉ cần đổi chiều cao nóc thêm 1 mét là góc dốc nhảy vọt - và lượng nước thoát nhanh hơn hẳn. Góc nhị diện chính là 'độ dốc' bạn thấy hằng ngày.
- **Còn dùng:** Thiết kế mái, lắp pin mặt trời đúng góc, đường dốc cho xe lăn, ta-luy chống sạt, kim tự tháp.

### T37. Xoắn ốc Fibonacci trong tự nhiên — "Hoa hướng dương, vỏ ốc, cách lá mọc - vì sao thiên nhiên cứ lặp đúng một dãy số?"
- 🎯 cao · 🎨 trung bình · Lớp 11 (Dãy số cho bởi công thức truy hồi và giới hạn của dãy (Fibonacci -> φ)) ⚠️ un/u(n-1) -> φ = (1+căn5)/2 xấp xỉ 1,618; góc vàng xấp xỉ 137,5 độ
- **Thực:** Đếm số xoắn trên đài hoa hướng dương, quả thông, quả dứa: gần như luôn ra 21, 34, 55... Cây xếp lá theo cùng quy luật để lá không che nắng của nhau.
- **Logic:** Đây là dãy Fibonacci: mỗi số bằng tổng hai số trước (dãy cho bởi công thức truy hồi un = u(n-1) + u(n-2)). Tỉ số hai số liên tiếp có GIỚI HẠN tiến về tỉ lệ vàng φ xấp xỉ 1,618 - góc xoắn ~137,5 độ giúp lá phủ kín tối ưu.
- **Wow:** Một dãy số cộng đơn giản điều khiển hình dáng hoa lá khắp Trái Đất, và tỉ số của nó hội tụ về con số vàng 1,618 - cùng con số kiến trúc sư dùng cho thẩm mỹ.
- **Còn dùng:** Thiết kế (tỉ lệ vàng), nông học xếp tán cây, nén/phân tích dữ liệu, nghệ thuật, kiến trúc.

### T38. Hộp giấy tối ưu — "Cùng một tấm bìa, vì sao có cách gấp đựng gấp đôi cái khác?"
- 🎯 cao · 🎨 dễ · Lớp 12 (Ứng dụng đạo hàm tìm GTLN của hàm thể tích) ⚠️ x=5cm, Vmax=2000cm3; V(2)=1352, V(10)=1000
- **Thực:** Cắt 4 góc vuông của tấm bìa carton 30x30 cm rồi gấp lên thành hộp không nắp đựng đồ ship hàng. Cắt cạnh bao nhiêu để hộp chứa nhiều nhất?
- **Logic:** Gọi cạnh cắt là x, thể tích V(x)=x(30-2x)^2. Lấy đạo hàm V'(x)=0, giải ra x=5. So sánh với cắt 'cảm tính' x=2 hay x=10 để thấy chênh lệch.
- **Wow:** Cắt đúng 5 cm cho thể tích 2000 cm3 - nhiều hơn hẳn so với cắt 10 cm chỉ được dưới 1000 cm3.
- **Còn dùng:** Thiết kế bao bì, thùng container, bể chứa, tối ưu vật liệu trong sản xuất.

### T39. Ống nước qua góc cua — "Cây sào dài nhất khiêng lọt khúc cua chữ L là bao nhiêu?"
- 🎯 cao · 🎨 trung bình · Lớp 12 (Ứng dụng đạo hàm tìm GTNN (bài toán cực tiểu khó)) ⚠️ L_min=(1+1)^1.5=2.828m tại θ=45 độ
- **Thực:** Khiêng một thanh ống nước (hoặc cái thang) qua góc cua vuông trong hành lang nhà, hai đoạn rộng đều 1 m. Thanh dài tối đa bao nhiêu mới quay lọt?
- **Logic:** Độ dài thanh chạm hai tường theo góc θ là L(θ)=1/sinθ+1/cosθ. Thanh khiêng lọt phải ngắn hơn GIÁ TRỊ NHỎ NHẤT của L. Lấy đạo hàm L'(θ)=0 ra θ=45 độ.
- **Wow:** Giá trị nhỏ nhất chỉ 2,83 m - thanh dài 3 m là kẹt cứng không cách nào quay được, dù hành lang trông rộng.
- **Còn dùng:** Chuyển nhà, thiết kế hành lang bệnh viện, robot tự hành tính đường, logistics kho hàng.

### T40. Đo tốc độ bằng camera đoạn — "Bạn không vượt tốc độ lúc nào, sao vẫn bị phạt 'tốc độ trung bình'?"
- 🎯 cao · 🎨 dễ · Lớp 12 (Giá trị trung bình của hàm số / định lý giá trị trung bình tích phân) ⚠️ 50/(25/60)=120 km/h
- **Thực:** Camera phạt nguội kiểu 'speed-section' ở cao tốc ghi giờ vào và giờ ra. Đi 50 km hết 25 phút thì hệ thống tính tốc độ trung bình bao nhiêu?
- **Logic:** Tốc độ trung bình = quãng đường / thời gian = giá trị trung bình của vận tốc trên đoạn (định lý giá trị trung bình của tích phân). 50 km / (25/60 h).
- **Wow:** Kết quả 120 km/h - vượt giới hạn 100. Định lý giá trị trung bình bảo đảm CHẮC CHẮN có ít nhất một thời điểm bạn chạy đúng 120 km/h.
- **Còn dùng:** Phạt nguội giao thông, đo mức tiêu thụ trung bình, lãi suất trung bình, nhiệt độ trung bình ngày.

### T41. Quãng đường từ đồ thị vận tốc — "Điện thoại biết bạn đi bao xa mà không cần GPS - bằng cách nào?"
- 🎯 cao · 🎨 dễ · Lớp 12 (Tích phân: quãng đường = tích phân của vận tốc)
- **Thực:** App chạy bộ vẽ đồ thị vận tốc theo thời gian từ cảm biến. Tính tổng quãng đường khi vận tốc thay đổi liên tục (tăng tốc, chạy đều, giảm tốc).
- **Logic:** Quãng đường = tích phân của vận tốc theo thời gian = diện tích dưới đường cong v(t). Chia đồ thị thành hình thang/tam giác hoặc lấy tích phân hàm v(t).
- **Wow:** Chỉ cần DIỆN TÍCH dưới đồ thị vận tốc là ra quãng đường - cùng nguyên lý mà tên lửa, ô tô tự lái và đồng hồ chạy bộ đều dùng để biết mình đi đâu.
- **Còn dùng:** App thể thao, dẫn đường quán tính (INS) máy bay, xe tự lái, đo lượng mưa từ cường độ.

### T42. Ly rượu và khối tròn xoay — "Vì sao ly rượu vang loe miệng chứa ít rượu hơn bạn tưởng?"
- 🎯 trung bình · 🎨 trung bình · Lớp 12 (Thể tích khối tròn xoay bằng tích phân)
- **Thực:** Một chiếc ly/bình hoa có thành cong được tạo bằng cách quay một đường cong quanh trục. Tính chính xác thể tích chất lỏng nó chứa.
- **Logic:** Mô tả thành ly bằng hàm x=f(y). Thể tích = tích phân π·[f(y)]^2 dy theo chiều cao - công thức thể tích khối tròn xoay. Phần loe ở miệng đóng góp ít vào dung tích thực.
- **Wow:** Ly cao gấp đôi nhưng do thành thắt ở giữa, dung tích thực có thể chỉ bằng một nửa cái ly thấp mà thẳng - mắt thường đoán sai hoàn toàn.
- **Còn dùng:** Thiết kế chai lọ, bình chứa nhiên liệu, mái vòm, thân trống, gốm sứ công nghiệp.

### T43. Điện 220V thực ra là 311V — "Ổ điện ghi 220V nhưng đỉnh điện áp lại là 311V - con số nào đúng?"
- 🎯 cao · 🎨 trung bình · Lớp 12 (Giá trị trung bình của hàm bình phương (RMS) qua tích phân) ⚠️ 220·căn2=311V
- **Thực:** Điện lưới Việt Nam là dòng xoay chiều hình sin. '220V' là giá trị hiệu dụng (RMS), còn điện áp đỉnh chạm tới đâu khi thiết kế cách điện thiết bị?
- **Logic:** Điện áp tức thời u(t)=U0·sin(ωt). Giá trị hiệu dụng = căn bậc hai của GIÁ TRỊ TRUNG BÌNH của u^2 trên một chu kỳ (tích phân). Từ đó U0 = 220·căn2.
- **Wow:** Đỉnh điện áp lên tới 311V - cao hơn 41% so với con số 220 ghi trên nhãn. Đó là lý do thiết bị phải chịu được tới hơn 300V.
- **Còn dùng:** Thiết kế nguồn điện, chọn tụ/diode chịu áp, loa âm thanh, đo công suất hiệu dụng.

### T44. Số phức quay robot — "Cánh tay robot xoay một điểm 90 độ chỉ bằng MỘT phép nhân - làm sao?"
- 🎯 cao · 🎨 dễ · Lớp 12 (Số phức: phép nhân tương ứng phép quay trong mặt phẳng) ⚠️ (3+0i)·i = 0+3i
- **Thực:** Lập trình cánh tay robot hoặc nhân vật game xoay một điểm quanh gốc tọa độ. Thay vì công thức lượng giác rối rắm, dùng số phức.
- **Logic:** Coi điểm (a,b) là số phức z=a+bi. Nhân z với (cosθ + i·sinθ) = quay z một góc θ. Ví dụ nhân với i là quay đúng 90 độ.
- **Wow:** Điểm (3,0) nhân với i biến thành (0,3) ngay lập tức - cả một phép quay phẳng gói gọn trong một phép nhân số phức, nền tảng của đồ họa máy tính.
- **Còn dùng:** Đồ họa 2D game, robot, xử lý ảnh, biến đổi Fourier, điều khiển động cơ.

### T45. Tấm pin mặt trời nghiêng bao nhiêu — "Đặt pin mặt trời nằm ngang là bạn đang mất điện miễn phí mỗi ngày."
- 🎯 cao · 🎨 trung bình · Lớp 12 (Tọa độ không gian: tích vô hướng, vector pháp tuyến, góc giữa đường và mặt) ⚠️ loss xấp xỉ (1-cos21 độ)·100=6.6%
- **Thực:** Lắp pin mặt trời trên mái nhà ở Hà Nội (vĩ độ 21 độ). Nên đặt nằm phẳng hay nghiêng, và nghiêng đúng bao nhiêu để hứng nhiều nắng nhất?
- **Logic:** Công suất hứng được tỉ lệ với cosin góc giữa tia nắng và pháp tuyến tấm pin (tích vô hướng hai vector). Tối ưu khi pháp tuyến chỉ thẳng về mặt trời, tức góc nghiêng xấp xỉ vĩ độ.
- **Wow:** Đặt phẳng làm mất khoảng 7% năng lượng giữa trưa so với nghiêng 21 độ - cả năm là hàng trăm số điện bay hơi chỉ vì đặt sai góc.
- **Còn dùng:** Điện mặt trời, định hướng ăng-ten/vệ tinh, kiến trúc lấy sáng, nông nghiệp nhà kính.

### T46. Bình gas hình con nhộng — "Vì sao bình gas, bình oxy đều bo tròn hai đầu chứ không phẳng?"
- 🎯 trung bình · 🎨 khó · Lớp 12 (Khối tròn xoay (trụ + cầu) và đạo hàm tối ưu diện tích)
- **Thực:** Bình chứa khí nén (gas, oxy y tế) thường là hình trụ gắn hai nửa cầu ở hai đầu. Với cùng một thể tích cố định, hình dạng nào tốn ít thép nhất để chế tạo?
- **Logic:** Thể tích = trụ + 2 nửa cầu (cố định). Diện tích bề mặt là hàm theo bán kính r. Lấy đạo hàm diện tích theo r với ràng buộc thể tích, tìm GTNN của lượng vật liệu.
- **Wow:** Hai đầu cầu không phải để đẹp - nó cho diện tích nhỏ nhất nên tốn ít thép nhất VÀ chịu áp lực tốt nhất, tiết kiệm chi phí và an toàn cùng lúc.
- **Còn dùng:** Bình gas/oxy, tàu ngầm, bồn xăng, tên lửa, bình áp lực công nghiệp.

### T47. Cà phê nguội bao lâu uống được — "Toán biết chính xác phút nào ly cà phê 90 độ vừa đủ ấm để uống."
- 🎯 cao · 🎨 trung bình · Lớp 12 (Nguyên hàm/tích phân giải phương trình tốc độ, hàm số mũ giảm) ⚠️ t=-ln(35/65)/0.05=12.4 phút
- **Thực:** Rót cà phê nóng 90 độ vào phòng 25 độ. Bao lâu nó nguội xuống 60 độ - mức uống ngon nhất không phỏng miệng?
- **Logic:** Tốc độ nguội tỉ lệ với chênh nhiệt độ (định luật Newton): T'(t)=-k(T-25), nghiệm T(t)=25+65·e^(-kt). Đây là phương trình vi phân giải bằng nguyên hàm, ra hàm mũ giảm.
- **Wow:** Với k=0,05 thì đúng 12,4 phút sau là chạm 60 độ - và đường nguội KHÔNG tuyến tính: nóng càng cao nguội càng nhanh rồi chậm dần.
- **Còn dùng:** Y tế (nguội thuốc/máu), bảo quản thực phẩm, pháp y ước tính thời gian tử vong, điều hòa.

### T48. Mạch RLC và số phức — "Trong mạch điện, 30 cộng 40 lại ra 50 - phép cộng này sai ở đâu?"
- 🎯 trung bình · 🎨 khó · Lớp 12 (Số phức: mô-đun và acgumen mô tả tổng trở và pha) ⚠️ Z=căn(30^2+40^2)=50, pha=atan(40/30)=53.1 độ
- **Thực:** Sạc điện thoại, loa, đèn LED đều có cuộn cảm và tụ điện. Tổng trở của mạch RLC không cộng thẳng như điện trở thường - vì sao?
- **Logic:** Mỗi linh kiện là một số phức: điện trở R thực, cảm kháng và dung kháng là phần ảo. Tổng trở Z là mô-đun của số phức R + (XL - XC)i. Pha lệch chính là acgumen.
- **Wow:** R=30, hiệu kháng=40, nhưng tổng trở không phải 70 mà là 50 ohm (vì cộng theo số phức), kèm độ lệch pha 53 độ - đó là lý do quạt điện 'ăn gian' công suất.
- **Còn dùng:** Mạch điện tử, lọc tín hiệu, sạc, loa, viễn thông, hệ số công suất hóa đơn điện.

### T49. Đường cong IQ và đường chuẩn — "Vì sao thiên tài IQ 130 chỉ chiếm 2% dân số - con số này từ đâu ra?"
- 🎯 cao · 🎨 trung bình · Lớp 12 (Thống kê 12: phân phối chuẩn, độ lệch chuẩn, quy tắc 68-95-99,7) ⚠️ P(z>2)=2.28%, P(z>3)=0.135%
- **Thực:** Điểm IQ, chiều cao, điểm thi của hàng triệu người tuân theo 'đường cong chuông' (phân phối chuẩn). IQ trung bình 100, độ lệch chuẩn 15. Có bao nhiêu người IQ trên 130?
- **Logic:** Dùng phân phối chuẩn lớp 12: IQ 130 cách trung bình 2 độ lệch chuẩn (z=2). Diện tích đuôi phải của đường cong (tích phân) cho tỉ lệ người vượt mốc đó.
- **Wow:** Chỉ 2,28% dân số đạt trên 130, và vượt mốc z=3 (IQ 145) thì còn 0,13% - hiếm tới mức 1 trên 740 người. Cả thế giới chạy theo một đường cong toán học.
- **Còn dùng:** Tuyển sinh/thi cử, kiểm soát chất lượng sản xuất, bảo hiểm, xét nghiệm y khoa, A/B testing.

### T50. Diện tích đất giữa hai con đường — "Mảnh đất cong queo giữa hai con đường - tính diện tích thế nào để mua bán?"
- 🎯 trung bình · 🎨 trung bình · Lớp 12 (Tích phân: diện tích hình phẳng giới hạn bởi hai đường cong)
- **Thực:** Một thửa đất nằm kẹp giữa hai con đường cong (hoặc bờ sông và con lộ). Không phải hình vuông tròn gì - làm sao đo diện tích chính xác để định giá, nộp thuế?
- **Logic:** Mô tả hai biên bằng hai hàm số y=f(x) và y=g(x). Diện tích = tích phân của hiệu (f-g) trên khoảng giao. Diện tích kẹp giữa hai đường cong.
- **Wow:** Một mảnh đất trông 'be bé' nhưng phần phình giữa khiến diện tích lớn hơn ước lượng bằng mắt tới 30-40% - sai một chút là lệch hàng trăm triệu tiền đất.
- **Còn dùng:** Đo đạc địa chính, quy hoạch đô thị, tính diện tích hồ/ruộng từ ảnh vệ tinh, nông nghiệp.

---

## ⚛️ VẬT LÝ

### L1. Quãng đường phanh ∝ v² — "Chạy nhanh gấp đôi, phanh gấp... 4 lần đường!"
- 🎯 rất cao (an toàn GT) · 🎨 dễ · Lớp 10 (động năng, công)
- **Thực:** 40 km/h và 80 km/h, đạp phanh cùng lúc thấy chướng ngại.
- **Logic:** động năng ½mv² phải bị công ma sát F·d triệt tiêu → d ∝ v². Gấp đôi v → gấp 4 quãng phanh. (Cộng thêm quãng phản xạ ∝ v.)
- **Wow:** vì sao vượt tốc độ nguy hiểm phi tuyến; khoảng cách an toàn. ✅ ĐÃ KIỂM CHỨNG (Wikipedia "Braking distance"): quãng phanh 80 km/h ≈ 36m với μ=0.7 (đường khô); quy luật ×2 tốc độ → ×4 quãng phanh do động năng. Giả định phản xạ 1s (tài xế tỉnh táo; chuẩn pháp lý/tái dựng tai nạn hay dùng 1.5s).
- **Còn dùng:** thiết kế đường, khoảng cách xe.

### L2. Ném xiên 45° — "Đá bóng/ném lao góc nào xa nhất?"
- 🎯 cao · 🎨 dễ (parabol) · Lớp 10 (chuyển động ném)
- **Thực:** muốn ném/đá đi xa nhất nên chọn góc nào?
- **Logic:** tầm xa R = v²·sin(2θ)/g, lớn nhất khi sin(2θ)=1 → **θ = 45°**. Vẽ nhiều quỹ đạo parabol theo góc.
- **Wow:** pháo binh, ném tạ, nhảy xa (thực tế <45° vì độ cao tay); sức cản không khí làm lệch.
- **Còn dùng:** thể thao, đạn đạo, đài phun.

### L3. Xung lực — "Vì sao túi khí & dây an toàn cứu mạng?"
- 🎯 rất cao · 🎨 trung bình · Lớp 10 (động lượng, xung lực)
- **Thực:** cùng một vụ va chạm, có/không túi khí.
- **Logic:** xung lực F·Δt = Δp (độ giảm động lượng) là cố định. Kéo dài thời gian dừng Δt → lực F tác dụng giảm.
- **Wow:** dừng trong 0.1s thay vì 0.01s → lực lên người giảm 10 lần. Cùng lý do: mũ bảo hiểm, đệm, gập gối khi tiếp đất.
- **Còn dùng:** bao bì chống sốc, thể thao.

### L4. Áp suất = F/A — "Giày cao gót tạo áp suất lớn hơn... chân voi"
- 🎯 cao (bất ngờ) · 🎨 dễ · Lớp 10 (áp suất)
- **Thực:** vì sao dao sắc cắt dễ, giày cao gót để lại vết lún.
- **Logic:** cùng một lực, diện tích tiếp xúc nhỏ → áp suất p = F/A lớn.
- **Wow:** gót nhọn + trọng lượng người → áp suất trên sàn có thể vượt cả chân voi (voi nặng nhưng chân to). ⚠️ kiểm chứng so sánh áp suất gót giày vs chân voi.
- **Còn dùng:** lặn sâu, ván trượt tuyết, đinh/dao.

### L5. Công suất điện — "Thiết bị nào ngốn điện nhất nhà bạn?"
- 🎯 rất cao (tiền điện) · 🎨 dễ · Lớp 11–12 (điện năng, công suất)
- **Thực:** hoá đơn điện tăng — thủ phạm là ai?
- **Logic:** điện năng tiêu thụ = công suất P (W) × thời gian t (h) = số kWh. Nhân giá điện bậc thang.
- **Wow:** bình nóng lạnh/điều hoà (1500–2500W) vài giờ ăn đứt đèn LED cả tháng. Tính tiền cụ thể. ⚠️ tra giá điện EVN bậc thang mới nhất (đồng/kWh).
- **Còn dùng:** tiết kiệm điện, chọn thiết bị.

### L6. Bảo toàn động lượng — "Tên lửa đẩy vào hư không sao vẫn bay?"
- 🎯 cao · 🎨 trung bình · Lớp 10 (động lượng)
- **Thực:** ngoài vũ trụ không có gì để "đạp" vào.
- **Logic:** tổng động lượng bảo toàn. Phụt khối khí về sau (m·v) → tên lửa nhận động lượng bằng & ngược chiều → tiến tới.
- **Wow:** súng giật, bi-a, mực/sứa bơi, đứng trên ván trượt ném vật.
- **Còn dùng:** hàng không vũ trụ, va chạm.

### L7. Tán xạ Rayleigh — "Vì sao trời xanh ban ngày, đỏ lúc hoàng hôn?"
- 🎯 rất cao (đẹp) · 🎨 trung bình · Lớp 11–12 (sóng ánh sáng)
- **Thực:** cùng một Mặt Trời, hai màu trời khác nhau.
- **Logic:** không khí tán xạ ánh sáng tỉ lệ ~1/λ⁴ → ánh sáng xanh (λ ngắn) tán xạ mạnh nhất → trời xanh. Hoàng hôn: ánh sáng đi qua nhiều khí quyển hơn, xanh tán hết, còn đỏ/cam.
- **Wow:** trên sao Hoả thì ngược lại; vì sao biển xanh.
- **Còn dùng:** quang học, nhiếp ảnh.

### L8. Khúc xạ & phản xạ toàn phần — "Ống hút gãy trong nước & cọng cáp quang chở cả Internet"
- 🎯 cao · 🎨 trung bình · Lớp 11 (khúc xạ ánh sáng)
- **Thực:** ống hút trông "gãy" ở mặt nước.
- **Logic:** ánh sáng đổi tốc độ khi qua môi trường → bẻ góc (định luật Snell). Khi góc đủ lớn → phản xạ toàn phần (không lọt ra).
- **Wow:** phản xạ toàn phần giữ ánh sáng chạy trong sợi cáp quang → truyền Internet xuyên đại dương. Ảo ảnh sa mạc cùng nguyên lý.
- **Còn dùng:** kính cận/viễn, lăng kính, nội soi.

### L9. Lực hướng tâm — "Vì sao khúc cua đường đua phải nghiêng?"
- 🎯 cao · 🎨 trung bình · Lớp 10 (lực hướng tâm)
- **Thực:** đường đua F1/xe đạp lòng chảo nghiêng vào trong.
- **Logic:** vào cua cần lực hướng tâm = mv²/r hướng vào tâm. Mặt nghiêng dùng thành phần phản lực cung cấp lực này, đỡ phải dựa hết vào ma sát.
- **Wow:** tàu lượn vòng lặp, vệ tinh "rơi mãi mà không chạm đất", máy giặt vắt.
- **Còn dùng:** giao thông, hàng không.

### L10. Chim đậu dây điện — "Vì sao chim không bị giật mà người thì chết?"
- 🎯 rất cao (an toàn) · 🎨 dễ · Lớp 11 (hiệu điện thế, dòng điện)
- **Thực:** chim đậu thoải mái trên dây cao thế.
- **Logic:** dòng điện chỉ chạy khi có HIỆU ĐIỆN THẾ giữa hai điểm. Chim chạm 1 dây, hai chân gần nhau → ΔU ≈ 0 → không có dòng qua người. Người chạm dây + đất → ΔU lớn → giật.
- **Wow:** vì sao không được thả diều/trèo gần đường dây; an toàn điện trong nhà.
- **Còn dùng:** sửa điện, nối đất.

### L11. Cú vẩy tay khi phanh gấp — "Liếc điện thoại 1,5 giây khi đang chạy 60km/h, bạn đã đi mù bao xa?"
- 🎯 cao · 🎨 dễ · Lớp 10 (Động học - chuyển động thẳng đều, quãng đường = v×t, phân biệt thời gian phản xạ và thời gian phanh) ⚠️ 60km/h = 16,67m/s; 16,67 × 1,5 = 25m
- **Thực:** Đang lái xe máy 60km/h, bạn liếc màn hình điện thoại để xem tin nhắn trong đúng 1,5 giây trước cả khi kịp đạp phanh.
- **Logic:** Mô hình hoá pha 'phản xạ' là chuyển động thẳng đều: quãng đường = vận tốc × thời gian, tách bạch với pha phanh (giảm tốc). Đổi 60km/h ra 16,7m/s rồi nhân với 1,5s.
- **Wow:** Bạn lao đi 25 mét hoàn toàn 'nhắm mắt' - dài hơn cả một sân bóng chuyền, trước khi tay kịp chạm phanh.
- **Còn dùng:** Thiết kế khoảng cách an toàn, hệ thống cảnh báo va chạm, luật cấm dùng điện thoại khi lái, đèn phanh xe phía trước

### L12. Nắm tay cửa và bí mật đòn bẩy — "Tại sao đẩy cửa gần bản lề lại nặng gấp 8 lần - dù bạn dùng đúng một lực?"
- 🎯 trung bình · 🎨 dễ · Lớp 10 (Moment lực M = F×d, vai trò cánh tay đòn trong chuyển động quay) ⚠️ 0,8/0,1 = 8 lần
- **Thực:** Cùng một lực đẩy, nhưng đẩy ở tay nắm cửa (cách bản lề 0,8m) so với đẩy sát bản lề (cách 0,1m).
- **Logic:** Tác dụng quay phụ thuộc moment lực = lực × cánh tay đòn, chứ không chỉ độ lớn lực. Cùng F, moment tỉ lệ với khoảng cách tới trục quay. Lấy tỉ số 0,8/0,1.
- **Wow:** Đẩy ở tay nắm cho moment lực gấp 8 lần đẩy sát bản lề - đó là lý do tay nắm luôn được đặt xa nhất khỏi bản lề.
- **Còn dùng:** Cờ lê dài để vặn ốc cứng, tay nắm cửa, bập bênh, vô lăng, kéo cắt cành dài, mở nắp chai bằng đòn bẩy

### L13. Cây búa giấu lực 8000 Newton — "Búa nặng nửa kí, vung tay nhẹ - sao đóng được đinh xuyên gỗ với lực 8000 Newton?"
- 🎯 cao · 🎨 dễ · Lớp 10 (Định lý động năng - công, công lực cản = ½mv^2, lực lớn khi quãng đường dừng nhỏ) ⚠️ F = 0,5×8^2/(2×0,002) = 8000 N
- **Thực:** Đầu búa 0,5kg đập vào đinh ở tốc độ 8m/s, đinh lún sâu vào gỗ chỉ 2mm rồi dừng.
- **Logic:** Toàn bộ động năng ½mv^2 của búa bị 'tiêu' trong quãng đường lún 2mm. Dùng công của lực cản = động năng: F×d = ½mv^2, suy ra F = mv^2/(2d). Quãng đường càng ngắn, lực càng khổng lồ.
- **Wow:** Lực ép lên đinh lên tới 8000 Newton - tương đương đặt cả một chiếc ô tô con lên đầu đinh, dù bạn chỉ vung nhẹ tay.
- **Còn dùng:** Đóng cọc, máy ép thuỷ lực, va đập trong tai nạn, vì sao mũi đinh phải nhọn, búa máy phá bê tông

### L14. Bàn học gánh 5 tấn không khí — "Ngay lúc này không khí đang ép xuống bàn học của bạn một lực bằng 5 tấn - sao bàn không sập?"
- 🎯 cao · 🎨 dễ · Lớp 10 (Áp suất khí quyển, F = p×S, cân bằng áp suất hai phía) ⚠️ 101325 × 0,5 = 50662 N xấp xỉ 5170 kg
- **Thực:** Mặt bàn 1m × 0,5m đang chịu áp suất khí quyển 101325 Pa từ phía trên.
- **Logic:** Áp suất là lực trên một đơn vị diện tích, nên lực = áp suất × diện tích. Nhân 101325 với 0,5m^2. Bàn không sập vì không khí bên dưới cũng đẩy ngược lên cân bằng.
- **Wow:** Không khí ép xuống mặt bàn một lực hơn 50000 Newton - tương đương 5 tấn, nhưng được lực đẩy từ dưới triệt tiêu hoàn hảo.
- **Còn dùng:** Giác hút treo đồ, hút giấy bằng ống hút, lon nước bị bóp khi hút hết, vì sao không bị bẹp dù khí quyển ép, bơm hút chân không

### L15. Giác hút treo 13kg bằng hư không — "Một miếng cao su nhỏ dán lên kính, hút sạch không khí - và nó giữ được 13kg chỉ nhờ... sự trống rỗng."
- 🎯 cao · 🎨 trung bình · Lớp 10 (Áp suất khí quyển tạo lực ép khi chênh lệch áp suất, F = p_atm×S) ⚠️ 101325 × π×0,02^2 = 127 N xấp xỉ 13 kg
- **Thực:** Móc giác hút bán kính 2cm dán lên tường gạch men, ép hết không khí bên trong tạo chân không một phần.
- **Logic:** Khi bên trong gần như chân không, chỉ còn áp suất khí quyển bên ngoài ép giác hút vào tường. Lực giữ = áp suất khí quyển × diện tích đĩa hút = 101325 × π×0,02^2.
- **Wow:** Một móc giác hút bé tí giữ được tới 13kg - không phải nhờ 'keo dính', mà nhờ chính bầu khí quyển đè nó vào tường.
- **Còn dùng:** Móc treo nhà tắm, tay máy hút kính trong nhà máy, robot leo tường, vận chuyển tấm kính lớn, đồ chơi phi tiêu giác hút

### L16. Ống hút cao tối đa 10 mét — "Dù phổi bạn khoẻ đến đâu, không ống hút nào hút nước lên cao quá 10,3 mét - đây là giới hạn của vũ trụ."
- 🎯 cao · 🎨 trung bình · Lớp 10 (Áp suất khí quyển nâng cột chất lỏng, h = p/(ρg)) ⚠️ 101325/(1000×9,8) = 10,34 m
- **Thực:** Bạn cố hút nước qua một ống hút dài thẳng đứng, hút mạnh đến mức tạo chân không hoàn toàn ở miệng trên.
- **Logic:** Hút không phải 'kéo' nước, mà là giảm áp suất ở trên để khí quyển đẩy nước lên. Chiều cao tối đa khi áp suất khí quyển cân bằng cột nước: h = p_atm/(ρ·g) = 101325/(1000×9,8).
- **Wow:** Ngay cả với chân không tuyệt đối, nước chỉ lên được 10,3m - đó là lý do không có giếng nào hút nước sâu hơn 10m bằng bơm hút thường.
- **Còn dùng:** Giới hạn bơm hút giếng, vì sao phải dùng bơm đẩy ở giếng sâu, cột thuỷ ngân đo áp suất, hệ thống xi phông, máy hút bụi

### L17. Lặn 30m, áp suất gấp 4 lần — "Lặn xuống chỉ 30 mét, mỗi centimet vuông da bạn gánh áp suất gấp 4 lần trên mặt nước."
- 🎯 cao · 🎨 trung bình · Lớp 10 (Áp suất chất lỏng theo độ sâu p = p0 + ρgh) ⚠️ 1 + (1000×9,8×30)/101325 = 3,9 atm
- **Thực:** Một thợ lặn xuống độ sâu 30m trong nước biển, phải biết áp suất tăng bao nhiêu để tránh chấn thương tai và phổi.
- **Logic:** Áp suất trong lòng chất lỏng tăng theo độ sâu: p = p_atm + ρ·g·h. Cứ mỗi 10m nước, áp suất tăng thêm khoảng 1 atm. Cộng áp suất khí quyển ở mặt nước.
- **Wow:** Ở 30m, tổng áp suất lên tới gần 4 atm - thể tích phổi bị nén còn 1/4, đó là lý do thợ lặn phải thở khí nén và ngoi lên thật chậm.
- **Còn dùng:** Lặn biển an toàn, bệnh giảm áp, thiết kế tàu ngầm, vì sao đập thuỷ điện dày ở đáy, ráng tai khi máy bay hạ cánh

### L18. Băng trơn gấp 120 lần đường nhựa — "Vì sao trượt băng nhẹ tênh còn đi bộ thì không? Lớp ma sát của băng nhỏ hơn 120 lần."
- 🎯 trung bình · 🎨 dễ · Lớp 10 (Lực ma sát F = μN, vai trò hệ số ma sát) ⚠️ 0,6/0,005 = 120 lần
- **Thực:** So sánh giày trượt trên băng (hệ số ma sát ~0,005) với đế cao su trên mặt đường (hệ số ~0,6) cho cùng một người.
- **Logic:** Lực ma sát = hệ số ma sát × áp lực. Cùng trọng lượng người, lực cản chuyển động chỉ khác nhau ở hệ số ma sát. Lấy tỉ số 0,6/0,005 cho thấy mức chênh.
- **Wow:** Đi trên đường, lực cản gấp 120 lần trên băng - đó là lý do một cú đẩy nhẹ trên băng đưa bạn trượt cả chục mét, còn trên đường thì dừng ngay.
- **Còn dùng:** Vì sao đường đóng băng cực nguy hiểm, lốp xe có rãnh, bôi dầu giảm ma sát máy móc, cát rải đường mùa đông, môn khúc côn cầu

### L19. Thước rơi đo phản xạ của bạn — "Bắt được cây thước rơi ở vạch 20cm? Phản xạ của bạn đúng 0,2 giây - và đó là vật lý thuần tuý."
- 🎯 cao · 🎨 dễ · Lớp 10 (Rơi tự do, h = ½gt^2, suy ra thời gian từ quãng đường) ⚠️ t = căn(2×0,2/9,8) = 0,20 s
- **Thực:** Một người thả cây thước thẳng đứng, bạn bắt nó bằng hai ngón tay. Thước rơi tự do và bạn bắt được ở vạch 20cm.
- **Logic:** Thước rơi tự do với gia tốc g, quãng đường rơi cho biết thời gian: h = ½g·t^2. Giải ngược ra t = căn(2h/g). Khoảng cách thước rơi chính là thước đo thời gian phản xạ.
- **Wow:** Bắt ở 20cm nghĩa là não - tay bạn mất đúng 0,2 giây để phản ứng - bài kiểm tra phản xạ không cần máy móc, chỉ cần một cây thước và công thức rơi tự do.
- **Còn dùng:** Test phản xạ vận động viên, đo độ tỉnh táo tài xế, ứng dụng game phản xạ, thời gian phản ứng trong phanh xe, eSports

### L20. Thang máy biến bạn thành 72kg — "Trong thang máy đang tăng tốc đi lên, cân hiện 72kg dù bạn chỉ nặng 60kg - bạn vừa 'mập' lên trong 1 giây."
- 🎯 cao · 🎨 trung bình · Lớp 10 (Định luật II Newton, trọng lượng biểu kiến N=m(g±a)) ⚠️ 60×(9,8+2)/9,8 = 72,2kg; 60×(9,8-2)/9,8 = 47,8kg
- **Thực:** Bạn 60kg đứng trên cân trong thang máy. Thang tăng tốc đi lên với gia tốc 2m/s^2, rồi tăng tốc đi xuống cũng 2m/s^2.
- **Logic:** Cân đo 'trọng lượng biểu kiến' = phản lực sàn. Theo định luật II Newton, khi đi lên có gia tốc: N = m(g+a); khi xuống: N = m(g-a). Đổi ra số kg tương đương.
- **Wow:** Tăng tốc lên bạn 'nặng' 72kg, tăng tốc xuống chỉ còn 48kg - cảm giác hẫng bụng trong thang máy chính là định luật II Newton đang tác dụng lên cơ thể.
- **Còn dùng:** Cảm giác trong tàu lượn, phi hành gia chịu gia tốc, thiết kế thang máy êm, máy bay cất cánh, cảm biến trọng lực điện thoại

### L21. Xô nước quay không đổ một giọt — "Quay xô nước vòng tròn qua đầu, nước lộn ngược mà không rơi - bí mật là một con số: 3,1 m/s."
- 🎯 cao · 🎨 trung bình · Lớp 10 (Lực hướng tâm tại đỉnh quỹ đạo, điều kiện mg=mv^2/r, v=căn(gr)) ⚠️ v = căn(9,8×1) = 3,13 m/s
- **Thực:** Bạn quay xô nước thành vòng tròn thẳng đứng bán kính 1m. Cần quay nhanh tối thiểu bao nhiêu để nước không đổ khi ở điểm cao nhất?
- **Logic:** Ở đỉnh vòng, trọng lực đóng vai lực hướng tâm giữ nước theo quỹ đạo. Điều kiện tối thiểu là trọng lực vừa đủ: mg = mv^2/r, suy ra v = căn(g·r). Nhanh hơn ngưỡng này nước bị ép vào đáy xô.
- **Wow:** Chỉ cần quay đạt 3,1 m/s ở đỉnh là nước 'dính' vào đáy xô dù lộn ngược - cùng nguyên lý giữ bạn trên ghế ở vòng lộn của tàu lượn siêu tốc.
- **Còn dùng:** Tàu lượn vòng lộn, máy giặt vắt khô, máy ly tâm tách máu, vận động viên ném tạ xoay, mô hình trọng lực nhân tạo trong phim

### L22. Vòi cứu hoả đẩy lùi 333 Newton — "Vì sao cần 2-3 lính cứu hoả mới giữ nổi một vòi nước? Nước phun ra đẩy ngược lại 333 Newton."
- 🎯 cao · 🎨 trung bình · Lớp 10 (Định luật III Newton và động lượng, lực = (dm/dt)×v) ⚠️ 1000 L/phút = 16,67 kg/s; 16,67×20 = 333 N
- **Thực:** Vòi cứu hoả phun 1000 lít nước mỗi phút ở tốc độ 20m/s. Người cầm vòi cảm nhận một lực giật ngược về phía sau.
- **Logic:** Nước được vòi đẩy về phía trước, theo định luật III Newton nước đẩy ngược lại vòi cùng độ lớn. Lực phản hồi = lưu lượng khối lượng × vận tốc = (kg/s)×v. Đổi 1000 L/phút ra 16,7 kg/s.
- **Wow:** Lực giật ngược lên tới 333 Newton - tương đương nhấc bổng 34kg, đó là lý do lính cứu hoả phải ghì chân và cầm vòi theo cặp.
- **Còn dùng:** Lực đẩy động cơ phản lực, tên lửa, vòi rửa xe áp lực, súng nước, vì sao tàu chạy được nhờ chân vịt

### L23. Leo cầu thang công suất 441W — "Chạy nhanh lên 3 tầng lầu trong 4 giây, cơ thể bạn xuất ra công suất ngang một chiếc lò vi sóng."
- 🎯 cao · 🎨 dễ · Lớp 10 (Công A=mgh và công suất P=A/t, phân biệt công và công suất) ⚠️ P = 60×9,8×3/4 = 441 W; đi bộ 12s = 147 W
- **Thực:** Người 60kg chạy lên cầu thang cao 3m hết 4 giây so với đi bộ thong thả hết 12 giây.
- **Logic:** Công nâng người = trọng lượng × độ cao (m·g·h), không đổi dù nhanh hay chậm. Nhưng công suất = công / thời gian, nên đi nhanh hơn tốn công suất lớn hơn dù cùng một lượng công.
- **Wow:** Chạy lên 4 giây cần công suất 441W, gần gấp 3 lần đi bộ - cùng một việc, nhưng làm nhanh đòi hỏi 'động cơ cơ thể' mạnh hơn hẳn.
- **Còn dùng:** Đánh giá thể lực, công suất động cơ ô tô, hoá đơn calo khi tập gym, vì sao chạy mệt hơn đi bộ, định mức công suất máy bơm

### L24. Con đội nâng cả ô tô bằng tay — "Một tay đẩy nhẹ 50 Newton mà nâng được cả tấn xe - máy ép thuỷ lực nhân lực lên 50 lần."
- 🎯 cao · 🎨 trung bình · Lớp 10 (Nguyên lý Pascal, áp suất truyền trong chất lỏng, F2=F1×(S2/S1)) ⚠️ 50 × (50/1) = 2500 N xấp xỉ 255 kg
- **Thực:** Kích thuỷ lực có pít-tông nhỏ tiết diện 1cm^2 và pít-tông lớn 50cm^2. Bạn ấn lực 50N lên pít-tông nhỏ.
- **Logic:** Theo nguyên lý Pascal, áp suất truyền đều trong chất lỏng kín: p = F/S như nhau ở hai pít-tông. Lực ra = lực vào × tỉ số diện tích. Đẩy ở pít-tông nhỏ, nhận lực khổng lồ ở pít-tông lớn.
- **Wow:** Lực 50N ở pít-tông nhỏ biến thành 2500N ở pít-tông lớn - đủ nâng một phần tư tấn, đổi lại bạn phải ấn quãng đường dài gấp 50 lần.
- **Còn dùng:** Phanh thuỷ lực ô tô, kích nâng xe sửa chữa, máy ép rác, ghế nha khoa, cánh tay máy xúc

### L25. Sạc điện thoại nhanh hay chậm — "Vì sao cùng 1 cục sạc, điện thoại bạn sạc lề rề còn máy bạn cùng phòng đầy vèo?"
- 🎯 cao · 🎨 dễ · Lớp 11 (Công và công suất của dòng điện, P = U.I, năng lượng điện W = U.q) ⚠️ 65W / 5W xấp xỉ 13 lần; 18.5Wh / 5W xấp xỉ 3.7h; 18.5Wh / 65W xấp xỉ 17 phút
- **Thực:** Sạc nhanh 65W vs sạc 'cùi' 5W cho điện thoại pin 5000mAh (3.7V xấp xỉ 18.5Wh).
- **Logic:** Năng lượng cần nạp W = U.q. Công suất sạc P = U.I quyết định thời gian t = W/P. Sạc 5W mất ~3.7h, sạc 65W lý thuyết ~17 phút. Giải thích vì sao củ sạc 'yếu' không truyền đủ dòng I.
- **Wow:** Sạc 65W nhanh gấp ~13 lần sạc 5W chỉ vì I lớn hơn, không phải vì 'pin xịn'.
- **Còn dùng:** Công suất điện P=UI, sạc laptop, trạm sạc xe điện, sụt áp dây sạc rởm

### L26. Vì sao dây điện cao thế 500kV — "Tải cùng 1 lượng điện, vì sao họ đẩy điện áp lên nửa triệu vôn thay vì hạ xuống cho an toàn?"
- 🎯 cao · 🎨 trung bình · Lớp 11 (Định luật Ohm, công suất tỏa nhiệt P = I^2.R, hao phí truyền tải) ⚠️ P_hao tỉ lệ I^2 tỉ lệ 1/U^2; tăng U 1000 lần -> hao phí giảm 10^6 lần
- **Thực:** Truyền 100MW điện đi xa: so sánh hao phí trên đường dây ở 220V và ở 500kV.
- **Logic:** Hao phí nhiệt P_hao = I^2.R. Với P = U.I cố định, tăng U thì I giảm cùng tỉ lệ, mà P_hao tỉ lệ I^2 nên giảm theo bình phương. Tăng U lên 1000 lần nên hao phí giảm 1 triệu lần.
- **Wow:** Tăng điện áp 1000 lần thì điện hao phí trên dây giảm 1.000.000 lần.
- **Còn dùng:** Định luật Joule-Lenz, máy biến áp, lưới điện quốc gia, sạc không dây

### L27. Nhạc cụ và sóng dừng — "Vì sao dây đàn guitar ngắn hơn lại cho nốt cao hơn, theo đúng một công thức?"
- 🎯 cao · 🎨 dễ · Lớp 11 (Sóng dừng trên dây, tần số họa âm f = v/(2L)) ⚠️ L giảm 1/2 -> f tăng ×2; tỉ lệ tần số octave = 2:1
- **Thực:** Bấm phím đàn guitar làm ngắn dây từ 65cm xuống 32.5cm để lên 1 quãng tám (octave).
- **Logic:** Sóng dừng trên dây 2 đầu cố định: f = v/(2L). v không đổi (cùng dây, cùng lực căng) nên f tỉ lệ nghịch L. Giảm L còn nửa nên f tăng gấp đôi = đúng 1 octave.
- **Wow:** Cắt đôi chiều dài dây đàn nên âm cao hơn đúng gấp đôi tần số, đó chính là 1 octave.
- **Còn dùng:** Sóng dừng, cộng hưởng, sáo, ống nghiệm thổi, dây thanh quản

### L28. Bịt tai khử ồn hoạt động sao — "Tai nghe chống ồn không chặn âm thanh, nó tạo thêm âm thanh để... xóa âm thanh. Bằng cách nào?"
- 🎯 cao · 🎨 trung bình · Lớp 11 (Giao thoa sóng, điều kiện triệt tiêu (lệch pha nửa bước sóng)) ⚠️ Điều kiện triệt tiêu: hiệu đường đi = (k+0.5)λ; lệch pha π
- **Thực:** Tai nghe chống ồn chủ động (ANC) trên máy bay khử tiếng động cơ ầm ầm.
- **Logic:** Hai sóng âm ngược pha (lệch pha π, tức nửa bước sóng) giao thoa triệt tiêu. Micro thu sóng ồn, loa phát sóng đảo pha nên biên độ tổng = 0. Giải thích điều kiện giao thoa triệt tiêu.
- **Wow:** Cộng hai âm thanh to lại với nhau có thể ra... im lặng hoàn toàn.
- **Còn dùng:** Giao thoa sóng, vân tối, sóng nước, kiểm tra phẳng quang học

### L29. Sét đánh xa bao nhiêu — "Đếm giây từ lúc thấy chớp đến lúc nghe sấm, bạn biết ngay sét cách mình mấy cây số."
- 🎯 cao · 🎨 dễ · Lớp 11 (Tốc độ truyền sóng âm v = s/t, so sánh tốc độ âm và ánh sáng) ⚠️ 343 m/s × 3s xấp xỉ 1029 m xấp xỉ 1 km; 6s -> ~2 km
- **Thực:** Thấy tia chớp rồi 6 giây sau mới nghe tiếng sấm - sét cách bạn bao xa?
- **Logic:** Ánh sáng đến gần như tức thời (300.000 km/s). Âm thanh đi 343 m/s. Khoảng cách = v_âm × t. 6 giây nên ~2 km. Quy tắc dân gian 'chia 3 ra km'.
- **Wow:** Cứ 3 giây giữa chớp và sấm là sét cách bạn đúng ~1 km.
- **Còn dùng:** Tốc độ truyền âm, sonar, đo độ sâu, định vị động đất

### L30. Đồng hồ quả lắc và trọng lực — "Mang đồng hồ quả lắc lên núi cao, nó chạy chậm lại mỗi ngày - vì sao?"
- 🎯 trung bình · 🎨 dễ · Lớp 11 (Con lắc đơn, chu kỳ T = 2π căn(L/g)) ⚠️ T = 2π căn(1/9.8) xấp xỉ 2.0s; g giảm 0.3% -> T tăng ~0.15%
- **Thực:** Con lắc đồng hồ dài 1m, chu kỳ ở mặt đất và ở đỉnh Everest (g giảm nhẹ).
- **Logic:** Chu kỳ con lắc đơn T = 2π căn(L/g). T chỉ phụ thuộc L và g, KHÔNG phụ thuộc khối lượng hay biên độ nhỏ. g giảm nên T tăng nên đồng hồ chạy chậm. Tính độ lệch giờ mỗi ngày.
- **Wow:** Một con lắc 1m luôn lắc đúng ~2 giây/chu kỳ, dù bạn treo quả nặng hay nhẹ.
- **Còn dùng:** Dao động điều hòa, đo g, máy đo địa chấn, giảm chấn nhà cao tầng

### L31. Bếp từ nấu mà không nóng mặt bếp — "Mặt kính bếp từ vẫn nguội, nhưng nồi thì sôi sùng sục - nhiệt ở đâu ra?"
- 🎯 cao · 🎨 trung bình · Lớp 11 (Cảm ứng điện từ, dòng điện Foucault, từ thông biến thiên) ⚠️ Hiệu suất bếp từ ~85-90% vs hồng ngoại ~60-70%; P=2000W
- **Thực:** Bếp từ 2000W đun sôi 1 lít nước, so với bếp hồng ngoại tỏa nhiệt ra ngoài.
- **Logic:** Cuộn dây tạo từ trường biến thiên nên cảm ứng dòng Foucault (dòng xoáy) trong đáy nồi sắt từ. Dòng cảm ứng sinh nhiệt Joule ngay trong nồi. Mặt kính không dẫn từ nên không nóng. Hiệu suất ~90%.
- **Wow:** Bếp từ 'đốt' nồi từ bên trong bằng dòng điện sinh ra từ hư không - không hề có lửa hay điện trở nóng.
- **Còn dùng:** Cảm ứng điện từ, dòng Foucault, sạc không dây, phanh điện từ tàu cao tốc

### L32. Loa kéo rung được nhờ nam châm — "Một nam châm cố định + cuộn dây + dòng điện nhạc = cả căn phòng rung lên. Đây là vật lý 11."
- 🎯 cao · 🎨 trung bình · Lớp 11 (Lực từ tác dụng lên dây dẫn mang dòng điện F = B.I.L.sinα) ⚠️ F = B.I.L; tần số dòng điện = tần số dao động màng loa
- **Thực:** Màng loa thùng kéo đám cưới rung 100 lần/giây tạo nốt nhạc, đẩy không khí thành sóng âm.
- **Logic:** Dòng điện biến thiên chạy qua cuộn dây đặt trong từ trường nam châm nên lực từ F = B.I.L đẩy/kéo màng loa theo nhịp dòng điện. Màng dao động nên nén/giãn không khí nên sóng âm. Tần số dòng = tần số âm.
- **Wow:** Lực từ trên một đoạn dây biến tín hiệu điện thành đúng giai điệu bạn nghe - đảo ngược thì thành micro.
- **Còn dùng:** Lực từ F = BIL, động cơ điện, micro, tai nghe, rơle

### L33. Quẹt thẻ ATM đọc dữ liệu sao — "Vạch đen sau thẻ ATM/xe buýt là cả một 'cuốn băng từ' - máy đọc nó bằng vật lý 11."
- 🎯 cao · 🎨 trung bình · Lớp 11 (Định luật Faraday, suất điện động cảm ứng e = -ΔΦ/Δt) ⚠️ e = -N.ΔΦ/Δt; tín hiệu tỉ lệ tốc độ biến thiên từ thông
- **Thực:** Quẹt thẻ từ qua khe đọc của máy POS hoặc cổng xe buýt.
- **Logic:** Vạch đen chứa các hạt từ tính sắp xếp theo mã. Khi quẹt, từ trường các hạt biến thiên qua đầu đọc (cuộn dây) nên sinh suất điện động cảm ứng e = -ΔΦ/Δt. Tín hiệu điện = dữ liệu thẻ. Quẹt nhanh/chậm vẫn đọc được vì mã hóa theo đổi chiều từ.
- **Wow:** Quẹt thẻ chính là 'tua' một đoạn nam châm qua cuộn dây để biến từ thành điện - định luật Faraday.
- **Còn dùng:** Cảm ứng điện từ, suất điện động cảm ứng, ổ cứng HDD, đàn guitar điện

### L34. Màng bọc thực phẩm tự dính — "Màng bọc dính chặt vào tô mà không cần keo - bí mật là điện tích bạn không nhìn thấy."
- 🎯 trung bình · 🎨 dễ · Lớp 11 (Nhiễm điện do ma sát và hưởng ứng, lực Coulomb F = kq1q2/r^2) ⚠️ F = k.q1q2/r^2; lực tĩnh điện > trọng lực màng mỏng
- **Thực:** Kéo màng bọc PE ra khỏi cuộn, nó tích điện và hút dính vào thành tô thủy tinh.
- **Logic:** Ma sát khi kéo (hiệu ứng ma sát điện) làm màng nhiễm điện. Màng tích điện gây phân cực vật trung hòa gần đó (hưởng ứng tĩnh điện) nên lực hút Coulomb giữa điện tích trái dấu. Cùng cơ chế tóc dựng khi cọ bóng bay.
- **Wow:** Chỉ vài nano-coulomb điện tích đủ thắng trọng lực, giữ màng bám dính vào tô.
- **Còn dùng:** Điện tích, lực Coulomb, nhiễm điện do hưởng ứng, sơn tĩnh điện, máy photocopy

### L35. Pin dự phòng mất dung lượng — "Pin dự phòng ghi 10000mAh nhưng sạc điện thoại 3000mAh chỉ được 2 lần - số liệu bay đâu?"
- 🎯 cao · 🎨 trung bình · Lớp 11 (Điện năng W = U.I.t = U.q, bảo toàn năng lượng, hiệu suất) ⚠️ 37Wh × 0.65 / (3000mAh×3.7V=11.1Wh) xấp xỉ 2.2 lần
- **Thực:** Pin sạc dự phòng 10000mAh (3.7V) sạc cho điện thoại pin 3000mAh (3.7V) qua mạch tăng áp lên 5V.
- **Logic:** Năng lượng mới là thứ bảo toàn, không phải mAh ở điện áp khác nhau. W = U.q. Pin 3.7V×10000mAh = 37Wh. Phải tăng áp 3.7V->5V (tổn hao ~10-20%) và điện thoại sạc cũng hao. Số lần thực = 37Wh × hiệu suất / năng lượng điện thoại.
- **Wow:** 10000mAh thật ra chỉ sạc đầy điện thoại ~2 lần, không phải 3, vì mAh ở 3.7V khác mAh ở 5V.
- **Còn dùng:** Năng lượng điện W=U.q, công suất, hiệu suất, định mức pin xe điện

### L36. Mạch nối tiếp đứt 1 bóng tắt cả dây — "Một bóng đèn Tết cháy, cả dây đèn tối thui - còn đèn nhà thì không. Khác nhau ở đâu?"
- 🎯 trung bình · 🎨 dễ · Lớp 11 (Đoạn mạch nối tiếp và song song, định luật Ohm cho toàn mạch) ⚠️ Nối tiếp: U mỗi bóng = 220V/50 xấp xỉ 4.4V; R_nt = ΣR; song song độc lập
- **Thực:** Dây đèn LED trang trí Tết mắc nối tiếp 50 bóng so với ổ điện nhà mắc song song.
- **Logic:** Nối tiếp: cùng 1 dòng I qua tất cả, đứt 1 chỗ nên I=0, tắt hết; mỗi bóng chia U = U_tổng/50. Song song: mỗi bóng có đủ U nguồn, 1 cái hỏng không ảnh hưởng cái khác. So sánh điện trở tương đương.
- **Wow:** Trong dây đèn nối tiếp, mỗi bóng chỉ nhận 1/50 điện áp - đứt một mắt xích là cả chuỗi 'chết'.
- **Còn dùng:** Mạch nối tiếp/song song, điện trở tương đương, hệ thống điện nhà, pin ghép

### L37. La bàn điện thoại bị làm loạn — "Để điện thoại cạnh loa hay nồi cơm điện, la bàn quay loạn xạ - từ trường vô hình đang phá nó."
- 🎯 trung bình · 🎨 trung bình · Lớp 11 (Từ trường gây bởi dòng điện, B = 2.10^-7.I/r (dây thẳng dài)) ⚠️ B = 2.10^-7×5/0.01 = 100µT vs B Trái Đất ~50µT
- **Thực:** La bàn số trên điện thoại lệch hướng khi đặt gần dây điện đang tải dòng lớn hoặc nam châm loa.
- **Logic:** Dòng điện sinh từ trường (Oersted): dây thẳng B = 2.10^-7.I/r. Kim/cảm biến la bàn định hướng theo từ trường tổng = từ Trái Đất (~50µT) + từ do dòng điện. Khi B_dòng đủ lớn so với B_đất nên la bàn lệch.
- **Wow:** Chỉ cần một dòng vài ampe cách 1cm đã tạo từ trường mạnh ngang từ trường cả Trái Đất.
- **Còn dùng:** Từ trường dòng điện, thí nghiệm Oersted, cảm biến Hall, MRI, động cơ

### L38. Còi xe đổi tiếng khi vụt qua — "Xe cứu thương lao tới hú cao chói, vừa vượt qua tiếng tụt thấp ngay - vật lý đổi cao độ thật."
- 🎯 cao · 🎨 trung bình · Lớp 11 (Hiệu ứng Doppler của sóng âm, f' = f.v/(v∓v_nguồn)) ⚠️ f' xấp xỉ 1000×343/(343-20)=1062Hz lại gần; ×343/(343+20)=945Hz đi xa
- **Thực:** Xe cứu thương chạy 72 km/h (20 m/s) hú còi 1000Hz vụt qua người đứng yên.
- **Logic:** Hiệu ứng Doppler: nguồn lại gần nên bước sóng bị nén nên tần số nghe cao hơn; ra xa nên giãn nên thấp hơn. f' = f.v_âm/(v_âm ∓ v_nguồn). Tính tần số nghe khi lại gần và khi đi xa, độ chênh.
- **Wow:** Còi 1000Hz nghe thành ~1062Hz khi xe lao tới và ~945Hz khi đi xa - chênh hơn 1 nốt nhạc, chỉ vì xe chạy.
- **Còn dùng:** Hiệu ứng Doppler, súng bắn tốc độ radar, siêu âm tim thai, đo tốc độ thiên hà

### L39. Cộng hưởng sập cầu — "Một nhóm lính đi đều bước có thể làm SẬP cả cây cầu thép. Vì sao quân đội bắt buộc phải bước loạn nhịp khi qua cầu?"
- 🎯 cao · 🎨 dễ · Lớp 12 (Dao động cưỡng bức và hiện tượng cộng hưởng cơ học) ⚠️ Tần số bước đi đều của lính ~2 Hz; tần số riêng cầu bộ hành điển hình 1.5-2.5 Hz; Millennium Bridge 2000 phải lắp 37 bộ giảm chấn
- **Thực:** Cầu treo Broughton (Anh, 1831) và cầu Angers (Pháp, 1850) sập khi lính đi đều bước; ở VN, lan can cầu rung mạnh khi đám đông cùng nhún nhịp.
- **Logic:** Mỗi cây cầu có tần số dao động riêng f0. Khi nhịp chân của đoàn người trùng f0, biên độ dao động được bơm năng lượng cộng dồn mỗi chu kỳ (cộng hưởng) và lớn dần đến mức vượt giới hạn bền của vật liệu. Mô hình hoá: dao động cưỡng bức, biên độ vọt cực đại khi tần số cưỡng bức tiến tới f0.
- **Wow:** Chỉ vài chục người nặng tổng cộng vài tấn, nhún đúng tần số riêng, có thể tạo lực dao động tương đương hàng trăm tấn - đủ phá kết cấu thiết kế chịu tải tĩnh gấp nhiều lần.
- **Còn dùng:** Thiết kế cầu (giảm chấn TMD ở cầu Millennium London), nhà chống động đất, máy giặt rung khi vắt, đung đưa toà nhà cao tầng.

### L40. Giảm xóc xe máy — "Vì sao đi qua ổ gà xe máy chỉ nảy một cái rồi êm, không rung lắc mãi như lò xo bút bi? Bí mật nằm ở 'dao động tắt dần'."
- 🎯 trung bình · 🎨 trung bình · Lớp 12 (Dao động tắt dần, lực cản và tắt dần tới hạn) ⚠️ Mô hình tắt dần A=A0·e^(-bt/2m); critically damped khi b^2=4mk
- **Thực:** Bộ giảm xóc (phuộc) xe máy/ô tô: lò xo + ống dầu thuỷ lực, khi qua gờ giảm tốc xe nảy lên rồi tắt rung gần như tức thì.
- **Logic:** Lò xo đơn thuần dao động điều hoà mãi mãi (lý tưởng), nhưng phuộc có lực cản nhớt của dầu tỉ lệ vận tốc nên dao động tắt dần, biên độ giảm theo hàm mũ A=A0·e^(-bt/2m). Kỹ sư chỉnh hệ số cản b để xe 'tắt rung tới hạn': hết nảy nhanh nhất mà không cứng đơ.
- **Wow:** Nếu phuộc thiếu dầu (b nhỏ), xe sẽ nảy 5-6 lần sau mỗi ổ gà; chỉnh đúng độ cản, biên độ giảm còn dưới 5% chỉ sau 1 chu kỳ.
- **Còn dùng:** Hệ treo ô tô, giảm chấn toà nhà, loa (màng loa tắt dần), cửa tự đóng có piston.

### L41. Váng dầu bảy màu — "Vũng nước mưa dính xăng lại lấp lánh cầu vồng, dù xăng vốn trong suốt. Màu đó từ đâu ra?"
- 🎯 cao · 🎨 trung bình · Lớp 12 (Giao thoa ánh sáng trên bản mỏng) ⚠️ Điều kiện giao thoa bản mỏng 2nd=(k+1/2)λ hay kλ tuỳ pha; bề dày màng dầu ~100-1000nm; n_dầu xấp xỉ 1.4
- **Thực:** Váng dầu/xăng loang trên mặt nước sau cơn mưa, bong bóng xà phòng, lớp phủ mắt kính chống loá.
- **Logic:** Ánh sáng phản xạ ở mặt trên và mặt dưới của lớp màng mỏng giao thoa với nhau. Tuỳ độ dày màng d và bước sóng λ, một số màu giao thoa tăng cường, số khác triệt tiêu (2nd xấp xỉ kλ). Vì màng dày mỏng khác nhau ở mỗi chỗ nên ra dải màu khác nhau.
- **Wow:** Lớp dầu mỏng chỉ vài trăm nanomet - mỏng hơn sợi tóc cả nghìn lần - lại 'lọc màu' chính xác đến mức tạo cả cầu vồng mà không cần một hạt sắc tố nào.
- **Còn dùng:** Lớp phủ chống phản xạ ống kính/pin mặt trời, cánh bướm/lông công (màu cấu trúc), kiểm tra độ dày màng công nghiệp.

### L42. Đĩa CD tán sắc — "Mặt sau đĩa CD/DVD tách ánh sáng trắng thành cầu vồng - nó là một 'cách tử nhiễu xạ' tự nhiên ngay trong nhà bạn."
- 🎯 cao · 🎨 trung bình · Lớp 12 (Nhiễu xạ qua cách tử và đo bước sóng) ⚠️ d·sinθ=kλ; bước rãnh CD xấp xỉ 1.6µm (DVD 0.74µm); 1/1.6µm xấp xỉ 625 rãnh/mm
- **Thực:** Nghiêng đĩa CD dưới đèn thấy bảy sắc; có thể tự chế quang phổ kế bằng đĩa CD và hộp giấy.
- **Logic:** Mặt đĩa có hàng nghìn rãnh dữ liệu song song cực sát nhau, hoạt động như cách tử nhiễu xạ. Ánh sáng các bước sóng khác nhau bị lệch góc khác nhau theo d·sinθ = kλ nên tách màu. Đo góc lệch của một màu, biết d, suy ra bước sóng λ.
- **Wow:** Các rãnh trên CD cách nhau chỉ 1,6 micromet - khoảng 625 rãnh trong 1 mm - nên nó tách màu tốt ngang một thiết bị phòng thí nghiệm.
- **Còn dùng:** Quang phổ kế phân tích thành phần sao/hoá chất, đo bước sóng laser, cảm biến màu, hologram chống giả tiền.

### L43. Kính râm phân cực — "Kính râm phân cực cắt được ánh chói trên mặt nước/mặt đường mà kính tối thường không làm nổi. Nó 'lọc hướng' của ánh sáng."
- 🎯 cao · 🎨 trung bình · Lớp 12 (Phân cực ánh sáng và định luật Malus) ⚠️ Định luật Malus I=I0·cos^2θ; ánh sáng phản xạ phân cực mạnh ở góc Brewster; kính phân cực chặn >90% chói mặt nước
- **Thực:** Đeo kính phân cực lái xe trưa nắng hết loá mặt đường, hoặc câu cá nhìn rõ xuống đáy nước; màn hình LCD nhìn qua kính phân cực bị tối ở vài góc.
- **Logic:** Ánh sáng phản xạ từ mặt phẳng (nước, đường) bị phân cực ngang chủ yếu. Kính phân cực chỉ cho qua dao động theo một phương; xoay nó vuông góc với ánh chói phản xạ sẽ chặn gần hết. Cường độ qua kính tuân định luật Malus I = I0·cos^2θ.
- **Wow:** Chỉ một lớp màng lọc theo đúng phương có thể cắt tới hơn 95% ánh chói phản xạ - và nếu xoay kính 90 độ, độ sáng tụt theo cos^2 xuống gần như bằng 0.
- **Còn dùng:** Màn hình LCD, kính 3D rạp phim, đo ứng suất nhựa, lọc phân cực nhiếp ảnh, kiểm tra đường thẳng quang học.

### L44. Sạc không dây — "Điện thoại sạc được mà không cắm dây - điện 'nhảy' qua không khí. Đó không phải phép thuật mà là điện xoay chiều và cảm ứng."
- 🎯 cao · 🎨 trung bình · Lớp 12 (Cảm ứng điện từ và vai trò của dòng điện xoay chiều) ⚠️ Định luật Faraday e=-dΦ/dt; sạc Qi chuẩn ~5-15W; DC không biến thiên -> dΦ/dt=0 -> không cảm ứng
- **Thực:** Đế sạc không dây điện thoại, bàn chải điện, sạc xe điện không dây.
- **Logic:** Cuộn dây trong đế cho dòng xoay chiều chạy qua nên tạo từ trường biến thiên. Cuộn dây trong điện thoại nằm trong từ trường biến thiên này nên xuất hiện suất điện động cảm ứng (Faraday), sinh dòng để sạc pin. Cần dòng XOAY CHIỀU vì từ trường phải liên tục đổi mới cảm ứng được.
- **Wow:** Hai cuộn dây không hề chạm nhau vẫn truyền được vài chục watt - và nếu bạn dùng dòng một chiều ổn định thay vì xoay chiều, công suất truyền qua sẽ tụt về đúng 0.
- **Còn dùng:** Bếp từ, máy biến áp, sạc xe điện, RFID/thẻ từ, đọc thẻ ngân hàng contactless, micro động.

### L45. Vì sao lưới 220V — "Vì sao truyền điện đi xa người ta đẩy lên hàng trăm nghìn vôn rồi mới hạ xuống 220V? Tăng áp để... đỡ mất điện."
- 🎯 cao · 🎨 dễ · Lớp 12 (Máy biến áp và truyền tải điện năng đi xa) ⚠️ P_hao=I^2R; P=UI; U×10 -> I/10 -> hao /100; tỉ số biến áp U1/U2=N1/N2; đường dây 500kV VN
- **Thực:** Đường dây cao thế 500kV Bắc-Nam, trạm biến áp khu dân cư, cục sạc laptop biến 220V xuống 19V.
- **Logic:** Công suất hao trên dây P_hao = I^2·R. Với cùng công suất truyền P = U·I, tăng điện áp U lên thì dòng I giảm tương ứng, mà hao phí tỉ lệ I^2 nên giảm cực mạnh. Máy biến áp dùng cảm ứng điện từ để tăng/hạ áp: U1/U2 = N1/N2.
- **Wow:** Tăng điện áp truyền tải lên 10 lần làm dòng giảm 10 lần, nhưng hao phí I^2R giảm tới 100 lần. Nhờ vậy điện đi cả nghìn km mà chỉ mất vài phần trăm.
- **Còn dùng:** Hệ thống điện quốc gia, adapter mọi thiết bị, sạc điện thoại, lò vi sóng, hàn điện.

### L46. Dòng điện chết người — "Cùng một ổ điện, vì sao có người bị giật bắn ra còn có người chết? Không phải vôn - chính là 'cường độ dòng' và điện trở da."
- 🎯 cao · 🎨 dễ · Lớp 12 (Định luật Ohm, tác dụng sinh lý của dòng điện) ⚠️ I=U/R; ngưỡng nguy hiểm ~30mA (co cơ), ~100mA (rung thất); R da khô ~100kΩ, da ướt ~1kΩ
- **Thực:** Tai nạn điện giật trong nhà, vì sao tay ướt nguy hiểm hơn tay khô khi chạm điện.
- **Logic:** Tác hại do dòng I qua tim quyết định, theo Ohm I = U/R. Da khô R lớn (~100kΩ) nên dòng nhỏ; da ướt R tụt (~1kΩ) nên cùng 220V dòng tăng cả trăm lần. Dòng ~10-30mA đã gây co cơ không nhả tay, ~100mA qua tim gây rung thất.
- **Wow:** Chỉ cần 0,1 ampe - bằng dòng thắp một bóng LED nhỏ - đi đúng qua tim là đủ gây tử vong; trong khi tay ướt có thể khiến cùng một ổ điện nguy hiểm gấp ~100 lần tay khô.
- **Còn dùng:** An toàn điện gia đình, thiết kế CB chống giật ELCB/RCD, máy khử rung tim, đi dây tiếp đất.

### L47. Cảm biến khoá cửa quang điện — "Cửa tự động và đèn cảm biến 'thấy' bạn bằng tia mắt thường không thấy - và đôi khi bằng đúng hiệu ứng giúp Einstein đoạt Nobel."
- 🎯 cao · 🎨 trung bình · Lớp 12 (Hiện tượng quang điện và thuyết photon (lượng tử ánh sáng)) ⚠️ Phương trình Einstein hf=A+(1/2)mv^2max; tồn tại tần số ngưỡng; h=6.626e-34; cường độ không thay ngưỡng
- **Thực:** Cảm biến đèn tự bật khi có người, cửa siêu thị tự mở, đồng hồ pin mặt trời, cảm biến ánh sáng tự chỉnh độ sáng màn hình.
- **Logic:** Hiện tượng quang điện: ánh sáng đập vào kim loại/bán dẫn, mỗi photon có năng lượng E = hf bứt electron ra tạo dòng - chỉ khi tần số f đủ lớn (vượt ngưỡng), bất kể cường độ. Ánh sáng được 'đếm' thành hạt photon chứ không phải dòng chảy liên tục.
- **Wow:** Ánh sáng đỏ dù chiếu mạnh cỡ nào cũng không bứt nổi electron của một số kim loại, nhưng ánh sáng tím dù le lói lại bứt được ngay - bằng chứng ánh sáng đi thành từng 'gói' năng lượng.
- **Còn dùng:** Pin mặt trời, cảm biến camera CCD/CMOS, máy đo ánh sáng, cảm biến khói, đèn đường tự động.

### L48. Đèn LED đổi màu — "Vì sao có đèn LED đỏ, có đèn LED xanh, và vì sao LED xanh dương lại đoạt giải Nobel 2014? Màu của LED bị 'lượng tử hoá'."
- 🎯 cao · 🎨 trung bình · Lớp 12 (Phát xạ photon, mức năng lượng và lượng tử ánh sáng) ⚠️ E_photon=hf=hc/λ; khe năng lượng bán dẫn quyết định màu; LED xanh GaN, Nobel Vật lý 2014
- **Thực:** Đèn LED chiếu sáng, màn hình điện thoại/TV, đèn giao thông, đèn flash camera, đèn pin.
- **Logic:** Trong LED, electron rơi qua khe năng lượng của bán dẫn và nhả ra một photon với E = hf đúng bằng độ rộng khe. Khe rộng nên photon năng lượng cao nên ánh sáng xanh/tím; khe hẹp nên đỏ/hồng ngoại. Màu LED do vật liệu quyết định, không pha được bằng sơn.
- **Wow:** Để làm LED xanh dương phải tạo khe năng lượng lớn hơn LED đỏ, khó đến mức nhân loại chế được LED đỏ từ 1962 nhưng phải đợi tới 1993 mới có xanh dương - và chính nó mở đường cho mọi màn hình và đèn LED trắng ngày nay.
- **Còn dùng:** Màn hình RGB, đèn chiếu sáng tiết kiệm, laser bán dẫn, cảm biến quang, đầu đọc đĩa Blu-ray.

### L49. Định tuổi xác ướp C-14 — "Làm sao biết một bộ xương hay mảnh gỗ cổ đã 'bao nhiêu tuổi'? Cơ thể từng sống là một chiếc đồng hồ phóng xạ tích tắc."
- 🎯 cao · 🎨 dễ · Lớp 12 (Phóng xạ, chu kỳ bán rã và định luật phân rã) ⚠️ N=N0·(1/2)^(t/T); T(C-14)=5730 năm; còn 25% -> 2 chu kỳ -> 11460 năm; cọc Bạch Đằng định tuổi C-14
- **Thực:** Xác định niên đại di vật khảo cổ, cọc gỗ Bạch Đằng, xác ướp, vải liệm, mẫu than củi cổ.
- **Logic:** Sinh vật sống hấp thụ Carbon-14 phóng xạ đều đặn; khi chết, C-14 ngừng nạp và phân rã theo N = N0·(1/2)^(t/T) với chu kỳ bán rã T = 5730 năm. Đo tỉ lệ C-14 còn lại so với ban đầu nên giải ra tuổi t.
- **Wow:** Cứ mỗi 5730 năm lượng C-14 lại giảm đúng một nửa - nên chỉ cần đo còn 25% là biết mẫu vật đã 'ngủ' khoảng 11.460 năm, sai số chỉ vài chục năm.
- **Còn dùng:** Khảo cổ, địa chất, kiểm tra tranh giả, định tuổi nước ngầm, pháp y.

### L50. Một viên uranium bằng tấn than — "Một viên nhiên liệu hạt nhân bé bằng đốt ngón tay cho năng lượng bằng cả tấn than đá. Bí mật nằm trong công thức E=mc^2."
- 🎯 cao · 🎨 dễ · Lớp 12 (Hệ thức Einstein E=mc^2, năng lượng liên kết và phản ứng hạt nhân) ⚠️ E=Δm·c^2; c^2 xấp xỉ 9e16 m^2/s^2; 1mg -> ~9e10 J xấp xỉ năng lượng đốt ~3 tấn than
- **Thực:** Nhà máy điện hạt nhân Ninh Thuận (đang tái khởi động), tàu ngầm/tàu sân bay chạy hạt nhân, vì sao Mặt Trời cháy mãi không hết.
- **Logic:** Khi hạt nhân nặng (U-235) phân hạch, khối lượng tổng các mảnh nhỏ hơn khối lượng ban đầu một chút (Δm). Khối lượng 'biến mất' đó hoá thành năng lượng khổng lồ theo E = Δm·c^2, với c^2 xấp xỉ 9·10^16 - một con số cực lớn.
- **Wow:** Chỉ cần một phần nghìn gam vật chất biến hoàn toàn thành năng lượng đã tương đương đốt khoảng 3 tấn than - vì c^2 nhân lên gấp gần trăm triệu tỉ lần.
- **Còn dùng:** Điện hạt nhân, năng lượng Mặt Trời/sao, y học hạt nhân, vũ khí hạt nhân, lò phản ứng nghiên cứu.

---

## 🧭 Gợi ý thứ tự đăng (đan xen Toán–Lý, ưu tiên hấp dẫn + dễ dựng)
1. **L1** Phanh xe ∝ v² (an toàn, đã làm)
2. **T1** Lãi kép (đã làm) → **T5** Xét nghiệm Bayes (phản trực giác)
3. **L7** Trời xanh/hoàng hôn đỏ (đẹp, đã làm)
4. **T10** Phòng thì thầm · **L31** Bếp từ · **T19** Nghịch lý sinh nhật — chọn theo mùa/sự kiện
5. Xoay vòng: mỗi tuần 1 Toán + 1 Lý, ưu tiên thẻ 🎯 cao + 🎨 dễ, tránh đăng 2 thẻ trùng concept liền nhau.

> Tổng kho: ~100 ý tưởng (Toán T1–T50, Lý L1–L50). Thẻ ✅ ĐÃ LÀM: T1, T5, L1, L7.

## ✅ Việc tiếp theo
- [ ] Tra web điền các số ⚠️ trước khi viết kịch bản (giá điện EVN, hằng số vật lý, số liệu thực tế).
- [ ] Chốt 1 chủ đề → viết kịch bản 2 phút (logic chi tiết) theo template dọc 9:16.
