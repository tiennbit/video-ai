"""
"Liều thuốc và giới hạn an toàn" — cấp số nhân lùi vô hạn, nồng độ tiệm cận mức trần.
Toán 11 · SHORT DỌC 9:16 · ~2 phút (12 beat) · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_lieuthuoc.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/lieuthuoc_video.py LieuThuocVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_lieuthuoc import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def pill(center, scale=1.0, c1=DEBT, c2=WHITE):
    """Viên thuốc con nhộng nằm ngang."""
    c = np.array([center[0], center[1], 0.0])
    body = RoundedRectangle(corner_radius=0.14 * scale, width=0.62 * scale, height=0.28 * scale)
    body.set_fill(c2, 1).set_stroke(MUTED, 1.5).move_to(c)
    half = Rectangle(width=0.31 * scale, height=0.28 * scale).set_fill(c1, 1).set_stroke(width=0)
    half.move_to(c + np.array([-0.155 * scale, 0, 0]))
    return VGroup(body, half)


def saw_chart(n=5, x0=-1.7, dx=0.85, y0=-1.4, ky=1.2, color=GROW):
    """Đồ thị răng cưa nồng độ: nhảy +1 liều mỗi chu kỳ, giữa 2 liều giảm còn 1/2.
    Trả về (VGroup các đoạn, mức sau liều cuối, hàm đổi level->y)."""
    def Y(level):
        return y0 + level * ky
    segs = VGroup()
    lv = 0.0
    for i in range(n):
        x = x0 + i * dx
        lv_new = lv + 1.0
        segs.add(Line([x, Y(lv), 0], [x, Y(lv_new), 0]).set_stroke(color, 3.5))
        if i < n - 1:
            segs.add(Line([x, Y(lv_new), 0], [x + dx, Y(lv_new / 2), 0]).set_stroke(color, 3.5))
        lv = lv_new / 2 if i < n - 1 else lv_new
    return segs, lv, Y


class LieuThuocVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_lieuthuoc")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 11"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_mohinh()
        self.beat_conlai()
        self.beat_cong()
        self.beat_dayso()
        self.beat_gioihan()
        self.beat_tran()
        self.beat_bacsi()
        self.beat_caphe()
        self.beat_canhbao()
        self.beat_ung()
        self.beat_cta()
        self.brand_stinger()
        self.wait(0.3)

    def _kara(self, seg, D):
        self._kar = self.make_karaoke(SEGMENTS[seg], D, self.beat_t0)
        self.add(self._kar)

    def _clear(self):
        self.end_karaoke(self._kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 1. HOOK — uống mãi sao không ngộ độc?
    def beat_hook(self):
        t = fit_w(Text("1 viên mỗi 8 tiếng, cả tuần", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        pills = VGroup(*[pill([-1.3 + 0.65 * i, 0.9, 0], 1.0) for i in range(5)])
        dots = Text("...", font=FONT, weight=BOLD, color=MUTED).scale(SZ_BODY).move_to([1.95, 0.9, 0])
        note = fit_w(Text("thuốc cũ chưa thải hết\nthuốc mới đã vào — CỘNG DỒN mãi", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -0.6, 0])
        q = fit_w(Text("Sao viên thứ 20 vẫn KHÔNG ngộ độc?", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, -2.1, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.7)
            self.cue(D * 0.2); self.play(LaggedStartMap(FadeIn, pills, lag_ratio=0.12), FadeIn(dots), run_time=1.0)
            self.cue(D * 0.5); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.82); self.play(Write(q), run_time=0.8)
            self._b = VGroup(t, pills, dots, note, q)
        self._clear()

    # 2. MÔ HÌNH — bình chứa, gan thận rút bớt
    def beat_mohinh(self):
        t = fit_w(Text("Máu bạn = chiếc bình chứa", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        tank = VGroup(
            Line([-0.8, 1.3, 0], [-0.8, -0.9, 0]),
            Line([-0.8, -0.9, 0], [0.8, -0.9, 0]),
            Line([0.8, -0.9, 0], [0.8, 1.3, 0]),
        ).set_stroke(MUTED, 3.5)
        lvl = Rectangle(width=1.52, height=0.8).set_fill(DEBT, 0.5).set_stroke(width=0).move_to([0, -0.46, 0])
        up = Arrow([0, 1.9, 0], [0, 1.0, 0], color=DEBT, buff=0, stroke_width=6)
        ulbl = Text("mỗi viên: vọt lên 1 nấc", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).move_to([0, 2.05, 0])
        dn = Arrow([1.35, -0.2, 0], [1.35, -1.1, 0], color=GROW, buff=0, stroke_width=6)
        dlbl = fit_w(Text("gan + thận: rút bớt ra suốt 8 tiếng", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL), CW).move_to([0, -1.75, 0])
        lvl_low = Rectangle(width=1.52, height=0.45).set_fill(DEBT, 0.5).set_stroke(width=0).move_to([0, -0.635, 0])
        with self.voice("02_mohinh") as D:
            self._kara("02_mohinh", D)
            self.cue(D * 0.0); self.play(Write(t), Create(tank), run_time=0.8)
            self.cue(D * 0.3); self.play(GrowArrow(up), FadeIn(ulbl), GrowFromEdge(lvl, DOWN), run_time=0.9)
            self.cue(D * 0.65); self.play(GrowArrow(dn), FadeIn(dlbl), Transform(lvl, lvl_low), run_time=0.9)
            self._b = VGroup(t, tank, lvl, up, ulbl, dn, dlbl)
        self._clear()

    # 3. CÒN LẠI 1/2 SAU MỖI CHU KỲ
    def beat_conlai(self):
        t = fit_w(Text("Quy ước đơn giản", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        b1 = Rectangle(width=0.9, height=1.6).set_fill(DEBT, 0.7).set_stroke(width=0).move_to([-1.0, 0.3, 0])
        l1 = Text("đang có", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL).next_to(b1, DOWN, buff=0.15)
        arr = Arrow([-0.35, 0.3, 0], [0.45, 0.3, 0], color=ACCENT, buff=0, stroke_width=6)
        albl = Text("8 tiếng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL).next_to(arr, UP, buff=0.1)
        b2 = Rectangle(width=0.9, height=0.8).set_fill(DEBT, 0.7).set_stroke(width=0).move_to([1.1, -0.1, 0])
        l2 = Text("còn 1/2", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL).next_to(b2, DOWN, buff=0.15)
        rule = fit_w(Text("mỗi vòng: lượng sót × 1/2", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, -1.9, 0])
        with self.voice("03_conlai") as D:
            self._kara("03_conlai", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(GrowFromEdge(b1, DOWN), FadeIn(l1), run_time=0.7)
            self.cue(D * 0.5); self.play(GrowArrow(arr), FadeIn(albl), run_time=0.6)
            self.cue(D * 0.65); self.play(GrowFromEdge(b2, DOWN), FadeIn(l2), run_time=0.7)
            self.cue(D * 0.85); self.play(Write(rule), run_time=0.7)
            self._b = VGroup(t, b1, l1, arr, albl, b2, l2, rule)
        self._clear()

    # 4. CỘNG TỪNG VIÊN — 1 → 1,5 → 1,75
    def beat_cong(self):
        t = fit_w(Text("Theo dõi từng viên", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        rows = [
            ("viên 1:  trong máu = 1 liều", WHITE),
            ("trước viên 2: còn 0,5", MUTED),
            ("+ viên mới  →  1,5", GROW),
            ("vòng sau  →  1,75", GROW),
        ]
        labs = VGroup()
        for txt, col in rows:
            labs.add(fit_w(Text(txt, font=FONT, weight=BOLD, color=col).scale(SZ_LABEL), CW))
        labs.arrange(DOWN, buff=0.42, aligned_edge=LEFT).move_to([0, 0.2, 0])
        note = fit_w(Text("mỗi lần chỉ nhích thêm một chút", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.9, 0])
        with self.voice("04_cong") as D:
            self._kara("04_cong", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            for i, lab in enumerate(labs):
                self.cue(D * (0.2 + 0.17 * i)); self.play(FadeIn(lab, shift=UP * 0.1), run_time=0.55)
            self.cue(D * 0.9); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, labs, note)
        self._clear()

    # 5. NHẬN RA DÃY SỐ — cấp số nhân lùi
    def beat_dayso(self):
        t = fit_w(Text("Nhìn kỹ dãy số này", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        seq = fit_w(Text("1 → 1,5 → 1,75 → 1,875 → ...", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.2, 0])
        card = RoundedRectangle(corner_radius=0.2, width=3.5, height=1.15).set_fill(BG_CARD, 1).set_stroke(PURPLE, 2.5).move_to([0, -0.15, 0])
        sum_t = fit_w(Text("= 1 + 1/2 + 1/4 + 1/8 + ...", font=FONT, weight=BOLD, color=PURPLE).scale(SZ_BODY), 3.1).move_to(card)
        name = fit_w(Text("CẤP SỐ NHÂN đang lùi dần", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), CW).move_to([0, -1.55, 0])
        with self.voice("05_dayso") as D:
            self._kara("05_dayso", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.25); self.play(Write(seq), run_time=1.0)
            self.cue(D * 0.55); self.play(GrowFromCenter(card), Write(sum_t), run_time=1.0)
            self.cue(D * 0.85); self.play(Write(name), run_time=0.6)
            self._b = VGroup(t, seq, card, sum_t, name)
        self._clear()

    # 6. GIỚI HẠN — S = 1/(1-q) = 2
    def beat_gioihan(self):
        t = fit_w(Text("Công thức Toán 11", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        f1 = fit_w(Text("S = u1 / (1 − q)", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.3, 0])
        f2 = fit_w(Text("= 1 / (1 − 1/2)", font=FONT, weight=BOLD, color=MUTED).scale(SZ_BODY), CW).move_to([0, 0.55, 0])
        card = RoundedRectangle(corner_radius=0.2, width=3.0, height=1.2).set_fill(BG_CARD, 1).set_stroke(GROW, 3).move_to([0, -0.75, 0])
        hero = fit_w(Text("= 2 liều", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO), 2.6).move_to(card)
        note = fit_w(Text("KHÔNG phải vô cùng!", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, -1.95, 0])
        with self.voice("06_gioihan") as D:
            self._kara("06_gioihan", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(Write(f1), run_time=0.8)
            self.cue(D * 0.52); self.play(Write(f2), run_time=0.8)
            self.cue(D * 0.72); self.play(GrowFromCenter(card), Write(hero), Flash(card.get_center(), color=GROW, line_length=0.4, num_lines=14), run_time=1.0)
            self.cue(D * 0.92); self.play(Write(note), run_time=0.5)
            self._b = VGroup(t, f1, f2, card, hero, note)
        self._clear()

    # 7. ĐỒ THỊ RĂNG CƯA TIỆM CẬN TRẦN
    def beat_tran(self):
        t = fit_w(Text("Uống cả đời cũng chỉ tới TRẦN", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.5, 0])
        segs, lv, Y = saw_chart()
        axis = Line([-1.85, -1.4, 0], [1.95, -1.4, 0]).set_stroke(MUTED, 2.5)
        ceil = DashedLine([-1.85, Y(2.0), 0], [1.95, Y(2.0), 0]).set_stroke(ACCENT, 3)
        clbl = Text("trần = 2 liều", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL).next_to(ceil, UP, buff=0.1).shift(RIGHT * 0.9)
        note = fit_w(Text("leo sát trần rồi dừng mãi ở đó\nkhông bao giờ vượt qua", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -2.35, 0])
        with self.voice("07_tran") as D:
            self._kara("07_tran", D)
            self.cue(D * 0.0); self.play(Write(t), Create(axis), run_time=0.7)
            self.cue(D * 0.22); self.play(LaggedStartMap(Create, segs, lag_ratio=0.1), run_time=1.8)
            self.cue(D * 0.6); self.play(Create(ceil), FadeIn(clbl), run_time=0.8)
            self.cue(D * 0.82); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.7)
            self._b = VGroup(t, axis, segs, ceil, clbl, note)
        self._clear()

    # 8. BÁC SĨ CHỌN LIỀU — cửa sổ điều trị
    def beat_bacsi(self):
        t = fit_w(Text("Bác sĩ chơi cờ với con số", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        toxic = DashedLine([-1.8, 1.35, 0], [1.8, 1.35, 0]).set_stroke(DEBT, 3)
        tlbl = Text("ngưỡng GÂY ĐỘC", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(toxic, UP, buff=0.1)
        eff = DashedLine([-1.8, -0.9, 0], [1.8, -0.9, 0]).set_stroke(PURPLE, 3)
        elbl = Text("ngưỡng CÓ TÁC DỤNG", font=FONT, weight=BOLD, color=PURPLE).scale(SZ_SMALL).next_to(eff, DOWN, buff=0.1)
        band = Rectangle(width=3.6, height=2.25).set_fill(GROW, 0.13).set_stroke(width=0).move_to([0, 0.225, 0])
        ceil = Line([-1.6, 0.75, 0], [1.6, 0.75, 0]).set_stroke(GROW, 4)
        clbl = Text("mức trần của toa thuốc", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL).next_to(ceil, DOWN, buff=0.12)
        note = fit_w(Text("trần dưới mức độc, trên mức tác dụng", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -2.15, 0])
        with self.voice("08_bacsi") as D:
            self._kara("08_bacsi", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.28); self.play(Create(toxic), FadeIn(tlbl), run_time=0.7)
            self.cue(D * 0.45); self.play(Create(eff), FadeIn(elbl), FadeIn(band), run_time=0.7)
            self.cue(D * 0.68); self.play(Create(ceil), FadeIn(clbl), run_time=0.8)
            self.cue(D * 0.88); self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
            self._b = VGroup(t, toxic, tlbl, eff, elbl, band, ceil, clbl, note)
        self._clear()

    # 9. CÀ PHÊ CŨNG VẬY
    def beat_caphe(self):
        t = fit_w(Text("Cà phê của bạn cũng thế", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        cup = VGroup(
            RoundedRectangle(corner_radius=0.1, width=0.9, height=1.0).set_fill(BG_CARD, 1).set_stroke(ACCENT, 3),
            Arc(radius=0.28, start_angle=-PI / 2, angle=PI).set_stroke(ACCENT, 3).move_to([0.62, 0.85, 0]),
        ).move_to([0, 0.85, 0])
        steam = VGroup(*[Line([sx, 1.55, 0], [sx, 1.95, 0]).set_stroke(MUTED, 2.5) for sx in [-0.2, 0.05, 0.3]])
        note = fit_w(Text("ly sáng nay + phần sót hôm qua\nuống đều → tích luỹ cũng CÓ TRẦN", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -0.9, 0])
        sub = fit_w(Text("nên bạn không run tay mãi", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -2.0, 0])
        with self.voice("09_caphe") as D:
            self._kara("09_caphe", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(cup, scale=0.8), FadeIn(steam), run_time=0.8)
            self.cue(D * 0.45); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.8)
            self.cue(D * 0.85); self.play(FadeIn(sub), run_time=0.5)
            self._b = VGroup(t, cup, steam, note, sub)
        self._clear()

    # 10. CẢNH BÁO — tự tăng liều là trần nhảy vọt
    def beat_canhbao(self):
        t = fit_w(Text("Công thức cũng CẢNH BÁO", font=FONT, weight=BOLD, color=DEBT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        l1 = fit_w(Text("liều × 2  →  trần × 2", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.2, 0])
        toxic = DashedLine([-1.7, 0.3, 0], [1.7, 0.3, 0]).set_stroke(DEBT, 3)
        tlbl = Text("ngưỡng gây độc", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(toxic, UP, buff=0.08).shift(LEFT * 0.9)
        bar1 = Rectangle(width=0.75, height=1.1).set_fill(GROW, 0.8).set_stroke(width=0).move_to([-0.75, -1.05, 0])
        bar2 = Rectangle(width=0.75, height=2.2).set_fill(DEBT, 0.8).set_stroke(width=0).move_to([0.75, -0.5, 0])
        b1l = Text("đúng liều", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL).next_to(bar1, DOWN, buff=0.12)
        b2l = Text("gấp đôi", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(bar2, DOWN, buff=0.12)
        note = fit_w(Text("ĐỪNG tự ý tăng liều", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY), CW).move_to([0, -2.55, 0])
        with self.voice("10_canhbao") as D:
            self._kara("10_canhbao", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.25); self.play(Write(l1), run_time=0.8)
            self.cue(D * 0.45); self.play(Create(toxic), FadeIn(tlbl), GrowFromEdge(bar1, DOWN), FadeIn(b1l), run_time=0.8)
            self.cue(D * 0.65); self.play(GrowFromEdge(bar2, DOWN), FadeIn(b2l), run_time=0.8)
            self.cue(D * 0.87); self.play(Write(note), run_time=0.6)
            self._b = VGroup(t, l1, toxic, tlbl, bar1, bar2, b1l, b2l, note)
        self._clear()

    # 11. ỨNG DỤNG
    def beat_ung(self):
        t = fit_w(Text("Cùng phép tính giới hạn", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        rows = [("kháng sinh phải uống đúng giờ", GROW), ("insulin giữ mức đường ổn định", ACCENT), ("ô nhiễm xả đều cũng tích về trần", PURPLE)]
        chips = VGroup()
        for txt, col in rows:
            card = RoundedRectangle(corner_radius=0.16, width=3.2, height=0.9).set_fill(BG_CARD, 1).set_stroke(col, 2.5)
            lab = fit_w(Text(txt, font=FONT, weight=BOLD, color=col).scale(SZ_LABEL), 2.9).move_to(card)
            chips.add(VGroup(card, lab))
        chips.arrange(DOWN, buff=0.35).move_to([0, -0.3, 0])
        with self.voice("11_ung") as D:
            self._kara("11_ung", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            for i, ch in enumerate(chips):
                self.cue(D * (0.28 + 0.22 * i)); self.play(GrowFromCenter(ch), run_time=0.55)
            self._b = VGroup(t, chips)
        self._clear()

    # 12. CTA
    def beat_cta(self):
        l1 = fit_w(Text("Toa thuốc mỗi 8 tiếng", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.9, 0])
        l2 = fit_w(Text("là BÀI TOÁN GIỚI HẠN giải sẵn", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("cấp số nhân · giới hạn · S = u1/(1−q)", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.25, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.7, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("THEO DÕI", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.75, 0])
        with self.voice("12_cta", gap=0.4) as D:
            self._kara("12_cta", D)
            self.cue(D * 0.0); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.3); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.06), run_time=0.8)
            self.cue(D * 0.55); self.play(FadeIn(tags, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.75); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale