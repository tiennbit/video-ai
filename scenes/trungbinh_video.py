"""
"Lương trung bình 53 triệu — nhưng 90% nhân viên không hề có?" — số trung bình vs trung vị,
ảnh hưởng của một giá trị ngoại lệ (Thống kê Toán 10).
Toán 10 · SHORT DỌC 9:16 · ~1.8 phút · KHÔNG intro.

Dùng bộ cỡ chữ chuẩn SZ_* (brand.py) + CANH NHỊP self.cue(): mỗi bước hiện hình được
rải trải đều theo lời đọc của cả đoạn (không dồn ở đầu beat).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_trungbinh.py
Căn chỉnh:   .venv/bin/python scenes/align_narration.py output/narration_trungbinh
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/trungbinh_video.py TrungBinhVideo
"""
import os

from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_trungbinh import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BLUE = "#60A5FA"     # nhân viên thường
GOLD = ACCENT        # con số "đinh"


def pdot(color, r=0.11):
    return Dot(radius=r).set_fill(color, 1).set_stroke(width=0)


def person(color, h=0.5):
    """Biểu tượng người đơn giản: đầu tròn + thân thang."""
    head = Circle(radius=h * 0.26).set_fill(color, 1).set_stroke(width=0)
    body = Polygon(
        [-h * 0.34, -h * 0.7, 0], [h * 0.34, -h * 0.7, 0],
        [h * 0.24, h * 0.02, 0], [-h * 0.24, h * 0.02, 0],
    ).set_fill(color, 1).set_stroke(width=0)
    head.next_to(body, UP, buff=h * 0.06)
    return VGroup(body, head)


def money_bar(value, max_value, color, width_full=2.2, height=0.34):
    """Thanh ngang tỉ lệ theo value."""
    w = max(0.06, width_full * value / max_value)
    bar = RoundedRectangle(corner_radius=0.06, width=w, height=height)
    bar.set_fill(color, 1).set_stroke(width=0)
    return bar


class TrungBinhVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_trungbinh")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 10"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_vande()
        self.beat_mohinh()
        self.beat_consso()
        self.beat_ynghia()
        self.beat_cta()
        self.brand_stinger()
        self.wait(0.3)

    def _kara(self, seg, D):
        self._kar = self.make_karaoke(SEGMENTS[seg], D, self.beat_t0)
        self.add(self._kar)

    def _clear(self):
        self.end_karaoke(self._kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 1. HOOK — quảng cáo tuyển dụng khoe lương trung bình -------------
    def beat_hook(self):
        card = RoundedRectangle(corner_radius=0.2, width=3.2, height=1.7).set_fill(BG_CARD, 1).set_stroke(BLUE, 2.5)
        card.move_to([0, 1.7, 0])
        head = Text("TUYỂN DỤNG", font=FONT, weight=BOLD, color=BLUE).scale(SZ_LABEL).move_to(card.get_top() + DOWN * 0.32)
        lbl = Text("Lương trung bình", font=FONT, color=MUTED).scale(SZ_SMALL).move_to(card.get_center() + UP * 0.18)
        big = Text("53 triệu/tháng", font=FONT, weight=BOLD, color=GOLD).scale(SZ_TITLE).move_to(card.get_center() + DOWN * 0.32)
        twist = fit_w(Text("90% nhân viên KHÔNG có mức đó", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY), CW).move_to([0, -0.35, 0])
        q = fit_w(Text("Con số không sai. Vậy sao?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -1.4, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(card, shift=DOWN * 0.2), Write(head), run_time=0.7)
            self.cue(D * 0.2); self.play(FadeIn(lbl), Write(big), run_time=0.8)
            self.cue(D * 0.5); self.play(FadeIn(twist, shift=UP * 0.2), Flash(twist.get_center(), color=DEBT, line_length=0.3, num_lines=14), run_time=0.9)
            self.cue(D * 0.75); self.play(FadeIn(q, shift=UP * 0.15), run_time=0.6)
            self._b = VGroup(card, head, lbl, big, twist, q)
        self._clear()

    # 2. VẤN ĐỀ — bảng lương thật: 9 người 15tr + 1 sếp 400tr ---------
    def beat_vande(self):
        title = fit_w(Text("Bảng lương thật (10 người)", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        staff = VGroup(*[person(BLUE, 0.5) for _ in range(9)]).arrange_in_grid(rows=3, cols=3, buff=0.22).move_to([-0.55, 0.9, 0])
        slbl = Text("9 người × 15 triệu", font=FONT, weight=BOLD, color=BLUE).scale(SZ_LABEL).next_to(staff, DOWN, buff=0.28)
        boss = person(DEBT, 0.95).move_to([1.35, 0.95, 0])
        blbl = VGroup(
            Text("1 SẾP", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL),
            Text("400 triệu", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL),
        ).arrange(DOWN, buff=0.08).next_to(boss, DOWN, buff=0.2)
        note = fit_w(Text("Tất cả đều THẬT — không ai nói dối", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.6, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.7)
            self.cue(D * 0.22); self.play(LaggedStart(*[FadeIn(p, scale=0.6) for p in staff], lag_ratio=0.06), FadeIn(slbl), run_time=1.2)
            self.cue(D * 0.55); self.play(FadeIn(boss, scale=0.6), FadeIn(blbl), run_time=0.9)
            self.cue(D * 0.8); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(title, staff, slbl, boss, blbl, note)
        self._clear()

    # 3. MÔ HÌNH — cách tính trung bình, ngoại lệ kéo lệch ------------
    def beat_mohinh(self):
        title = fit_w(Text("Số TRUNG BÌNH", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        f1 = fit_w(Text("= (tổng lương) ÷ (số người)", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 1.9, 0])
        l1 = Text("9 × 15  +  400", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to([0, 1.0, 0])
        l2 = Text("= 535 triệu", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to([0, 0.3, 0])
        l3 = Text("535 ÷ 10", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to([0, -0.4, 0])
        res = Text("≈ 53,5 triệu", font=FONT, weight=BOLD, color=GOLD).scale(SZ_HERO).move_to([0, -1.3, 0])
        warn = fit_w(Text("1 số khổng lồ kéo cả trung bình lên", font=FONT, color=DEBT).scale(SZ_SMALL), CW).move_to([0, -2.15, 0])
        with self.voice("03_mohinh") as D:
            self._kara("03_mohinh", D)
            self.cue(D * 0.0); self.play(Write(title), FadeIn(f1), run_time=0.7)
            self.cue(D * 0.28); self.play(FadeIn(l1, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.45); self.play(FadeIn(l2, shift=UP * 0.15), run_time=0.5)
            self.cue(D * 0.6); self.play(FadeIn(l3, shift=UP * 0.15), run_time=0.5)
            self.cue(D * 0.75); self.play(Write(res), Flash(res.get_center(), color=GOLD, line_length=0.35, num_lines=16), run_time=0.9)
            self.cue(D * 0.92); self.play(FadeIn(warn), run_time=0.4)
            self._b = VGroup(title, f1, l1, l2, l3, res, warn)
        self._clear()

    # 4. CON SỐ — trung vị: xếp & lấy giá trị giữa = 15tr ------------
    def beat_consso(self):
        title = fit_w(Text("Đổi thước đo: TRUNG VỊ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        sub = fit_w(Text("Xếp lương thấp → cao, lấy giá trị GIỮA", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, 2.0, 0])
        # 10 thanh: 9 thanh nhỏ (15) + 1 thanh dài (400)
        vals = [15] * 9 + [400]
        bars = VGroup()
        for i, v in enumerate(vals):
            col = DEBT if v > 15 else BLUE
            b = money_bar(v, 400, col, width_full=2.4, height=0.22)
            bars.add(b)
        bars.arrange(DOWN, buff=0.12, aligned_edge=LEFT).move_to([0, 0.2, 0])
        # đánh dấu cặp ở giữa (vị trí 5 và 6 trong 10 thanh -> chỉ số 4,5)
        midpair = VGroup(bars[4], bars[5])
        ring = SurroundingRectangle(midpair, color=GOLD, buff=0.1, corner_radius=0.05).set_stroke(GOLD, 3)
        mark = Text("ở giữa = 15 triệu", font=FONT, weight=BOLD, color=GOLD).scale(SZ_LABEL).next_to(ring, RIGHT, buff=0.18)
        fit_w(VGroup(ring, mark), CW)
        res = fit_w(Text("Trung vị = 15 triệu", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO), CW).move_to([0, -2.05, 0])
        with self.voice("04_consso") as D:
            self._kara("04_consso", D)
            self.cue(D * 0.0); self.play(Write(title), FadeIn(sub), run_time=0.7)
            self.cue(D * 0.25); self.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.07), run_time=1.3)
            self.cue(D * 0.55); self.play(Create(ring), FadeIn(mark, shift=LEFT * 0.15), run_time=0.8)
            self.cue(D * 0.78); self.play(Write(res), run_time=0.9)
            self._b = VGroup(title, sub, bars, ring, mark, res)
        self._clear()

    # 5. Ý NGHĨA — ngoại lệ, trung bình vs trung vị ------------------
    def beat_ynghia(self):
        big = fit_w(Text("GIÁ TRỊ NGOẠI LỆ", font=FONT, weight=BOLD, color=DEBT), CW).move_to([0, 2.5, 0])
        # so sánh 2 con số cạnh nhau
        mean_col = VGroup(
            Text("Trung bình", font=FONT, color=MUTED).scale(SZ_LABEL),
            Text("53,5 tr", font=FONT, weight=BOLD, color=GOLD).scale(SZ_TITLE),
            Text("bị KÉO LỆCH", font=FONT, color=DEBT).scale(SZ_SMALL),
        ).arrange(DOWN, buff=0.14)
        med_col = VGroup(
            Text("Trung vị", font=FONT, color=MUTED).scale(SZ_LABEL),
            Text("15 tr", font=FONT, weight=BOLD, color=GROW).scale(SZ_TITLE),
            Text("ĐỨNG YÊN", font=FONT, color=GROW).scale(SZ_SMALL),
        ).arrange(DOWN, buff=0.14)
        cmp = VGroup(mean_col, med_col).arrange(RIGHT, buff=0.6).move_to([0, 1.0, 0])
        fit_w(cmp, CW)
        rule = fit_w(Text("Dữ liệu LỆCH → tin TRUNG VỊ", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, -0.65, 0])
        note = fit_w(Text("Dữ liệu cân đối → trung bình vẫn tốt", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.5, 0])
        with self.voice("05_ynghia") as D:
            self._kara("05_ynghia", D)
            self.cue(D * 0.0); self.play(Write(big), run_time=0.8)
            self.cue(D * 0.3); self.play(FadeIn(mean_col, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.5); self.play(FadeIn(med_col, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.68); self.play(FadeIn(rule, shift=UP * 0.2), Indicate(rule, color=GROW, scale_factor=1.08), run_time=0.8)
            self.cue(D * 0.88); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(big, cmp, rule, note)
        self._clear()

    # 6. CTA ----------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Thấy chữ \"trung bình\"?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.9, 0])
        l2 = fit_w(Text("Hỏi thêm: TRUNG VỊ bao nhiêu?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.1, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.5, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("ĐĂNG KÝ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.2, 0])
        with self.voice("06_cta", gap=0.4) as D:
            self._kara("06_cta", D)
            self.cue(D * 0.0); self.play(Write(l1), run_time=0.7)
            self.cue(D * 0.3); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.08), run_time=0.8)
            self.cue(D * 0.6); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, sub)
        self._clear()
