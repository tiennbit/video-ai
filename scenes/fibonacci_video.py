"""
"Xoắn ốc Fibonacci trong tự nhiên" — dãy truy hồi, giới hạn tỉ số, tỉ lệ vàng.
Toán 11 · SHORT DỌC 9:16 · ~2 phút · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_fibonacci.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/fibonacci_video.py FibonacciVideo
"""
import math
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_fibonacci import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def flower(scale=1.0):
    """Hoa hướng dương tối giản: tâm nâu + cánh vàng quanh."""
    petals = VGroup()
    for k in range(12):
        p = Ellipse(width=0.26, height=0.66).set_fill(ACCENT, 1).set_stroke(width=0)
        p.move_to([0, 0.42, 0]).rotate(k * TAU / 12, about_point=ORIGIN)
        petals.add(p)
    core = Circle(radius=0.36).set_fill("#8A5A2B", 1).set_stroke("#5E3D1C", 2)
    return VGroup(petals, core).scale(scale)


def phyllotaxis(n=130, spread=0.135, dot_r=0.052):
    """Đặt n hạt theo GÓC VÀNG 137,5° -> mô hình đài hoa hướng dương."""
    g = VGroup()
    ga = math.radians(137.5)
    for i in range(n):
        r = spread * math.sqrt(i)
        th = i * ga
        col = interpolate_color(ManimColor(ACCENT), ManimColor(DEBT), i / max(1, n - 1))
        g.add(Dot([r * math.cos(th), r * math.sin(th), 0], radius=dot_r).set_fill(col, 1).set_stroke(width=0))
    return g


class FibonacciVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_fibonacci")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 11"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_day()
        self.beat_truyhoi()
        self.beat_tiso()
        self.beat_phi()
        self.beat_gocvang()
        self.beat_xoanoc()
        self.beat_ungdung()
        self.beat_cta()
        self.brand_stinger()
        self.wait(0.3)

    def _kara(self, seg, D):
        self._kar = self.make_karaoke(SEGMENTS[seg], D, self.beat_t0)
        self.add(self._kar)

    def _clear(self):
        self.end_karaoke(self._kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 1. HOOK -----------------------------------------------------------
    def beat_hook(self):
        fl = flower(1.0).move_to([0, 1.0, 0])
        title = fit_w(Text("Đếm xoắn hoa hướng dương", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -0.7, 0])
        q = fit_w(Text("21 ?  34 ?  55 ?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, -1.8, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(fl, scale=0.6), run_time=0.8)
            self.cue(D * 0.45); self.play(Write(title), run_time=0.8)
            self.cue(D * 0.75); self.play(Write(q), Flash(q.get_center(), color=ACCENT, line_length=0.4, num_lines=12), run_time=0.9)
            self._b = VGroup(fl, title, q)
        self._clear()

    # 2. DÃY FIBONACCI --------------------------------------------------
    def beat_day(self):
        t = fit_w(Text("Dãy Fibonacci", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        nums = [1, 1, 2, 3, 5, 8, 13, 21]
        row = VGroup(*[Text(str(x), font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY) for x in nums])
        row.arrange(RIGHT, buff=0.28)
        fit_w(row, CW).move_to([0, 0.9, 0])
        rule = fit_w(Text("mỗi số = tổng hai số trước", font=FONT, weight=BOLD, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -0.5, 0])
        ex = fit_w(Text("8 + 13 = 21", font=FONT, weight=BOLD, color=GROW).scale(SZ_TITLE), CW).move_to([0, -1.7, 0])
        with self.voice("02_day") as D:
            self._kara("02_day", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.2); self.play(LaggedStartMap(FadeIn, row, shift=UP * 0.2, lag_ratio=0.18), run_time=1.4)
            self.cue(D * 0.62); self.play(FadeIn(rule, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.82); self.play(Write(ex), Indicate(row[-1], color=GROW), run_time=0.9)
            self._b = VGroup(t, row, rule, ex)
        self._clear()

    # 3. CÔNG THỨC TRUY HỒI ---------------------------------------------
    def beat_truyhoi(self):
        t = fit_w(Text("Công thức truy hồi", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.2, 0])
        f = fit_w(Text("u(n) = u(n-1) + u(n-2)", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 0.5, 0])
        note = fit_w(Text("một quy tắc cộng — vô vàn trật tự", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -1.0, 0])
        with self.voice("03_truyhoi") as D:
            self._kara("03_truyhoi", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.35); self.play(Write(f), run_time=1.0)
            self.cue(D * 0.78); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, f, note)
        self._clear()

    # 4. TỈ SỐ HAI SỐ LIÊN TIẾP -----------------------------------------
    def beat_tiso(self):
        t = fit_w(Text("Tỉ số 2 số liên tiếp", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        r1 = fit_w(Text("8 / 5 = 1,600", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.3, 0])
        r2 = fit_w(Text("13 / 8 = 1,625", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 0.45, 0])
        r3 = fit_w(Text("21 / 13 = 1,615", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -0.4, 0])
        conv = fit_w(Text("→ sát về 1 con số cố định", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, -1.6, 0])
        with self.voice("04_tiso") as D:
            self._kara("04_tiso", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.25); self.play(FadeIn(r1, shift=UP * 0.12), run_time=0.5)
            self.cue(D * 0.45); self.play(FadeIn(r2, shift=UP * 0.12), run_time=0.5)
            self.cue(D * 0.62); self.play(FadeIn(r3, shift=UP * 0.12), run_time=0.5)
            self.cue(D * 0.82); self.play(Write(conv), run_time=0.7)
            self._b = VGroup(t, r1, r2, r3, conv)
        self._clear()

    # 5. TỈ LỆ VÀNG PHI -------------------------------------------------
    def beat_phi(self):
        hero = Text("φ ≈ 1,618", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO).move_to([0, 1.0, 0])
        lbl = fit_w(Text("TỈ LỆ VÀNG", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, -0.2, 0])
        sub = fit_w(Text("= giới hạn dãy tỉ số Fibonacci", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -1.4, 0])
        with self.voice("05_phi") as D:
            self._kara("05_phi", D)
            self.cue(D * 0.0); self.play(Write(hero), Flash(hero.get_center(), color=GROW, line_length=0.6, num_lines=20), run_time=1.1)
            self.cue(D * 0.45); self.play(Write(lbl), run_time=0.7)
            self.cue(D * 0.75); self.play(FadeIn(sub, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(hero, lbl, sub)
        self._clear()

    # 6. GÓC VÀNG -------------------------------------------------------
    def beat_gocvang(self):
        t = fit_w(Text("Góc vàng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        circle = Circle(radius=1.0).set_stroke(MUTED, 3).move_to([0, 0.5, 0])
        a0 = Line(circle.get_center(), circle.get_center() + RIGHT * 1.0).set_stroke(WHITE, 4)
        ang = math.radians(137.5)
        a1 = Line(circle.get_center(), circle.get_center() + np.array([math.cos(ang), math.sin(ang), 0])).set_stroke(ACCENT, 4)
        arc = Arc(radius=0.42, start_angle=0, angle=ang, arc_center=circle.get_center(), color=ACCENT, stroke_width=6)
        deg = Text("137,5°", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY).move_to([0, -1.4, 0])
        note = fit_w(Text("hạt mới lệch đúng góc này → phủ kín, không che nắng", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -2.2, 0])
        with self.voice("06_gocvang") as D:
            self._kara("06_gocvang", D)
            self.cue(D * 0.0); self.play(Write(t), Create(circle), run_time=0.7)
            self.cue(D * 0.3); self.play(Create(a0), Create(a1), Create(arc), run_time=0.8)
            self.cue(D * 0.55); self.play(Write(deg), run_time=0.6)
            self.cue(D * 0.78); self.play(FadeIn(note), run_time=0.6)
            self._b = VGroup(t, circle, a0, a1, arc, deg, note)
        self._clear()

    # 7. XOẮN ỐC PHYLLOTAXIS (điểm nhấn) --------------------------------
    def beat_xoanoc(self):
        spiral = phyllotaxis(140).move_to([0, 0.45, 0])
        if spiral.width > CW:
            spiral.set_width(CW)
        lbl = fit_w(Text("số đường xoắn = số Fibonacci", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, -2.2, 0])
        with self.voice("07_xoanoc") as D:
            self._kara("07_xoanoc", D)
            self.cue(D * 0.0)
            self.play(LaggedStartMap(GrowFromCenter, spiral, lag_ratio=0.012), run_time=min(D * 0.7, 2.6))
            self.cue(D * 0.8); self.play(Write(lbl), run_time=0.7)
            self._b = VGroup(spiral, lbl)
        self._clear()

    # 8. ỨNG DỤNG -------------------------------------------------------
    def beat_ungdung(self):
        t = fit_w(Text("Cùng tỉ lệ vàng ở khắp nơi", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.3, 0])
        items = ["vỏ ốc anh vũ", "lá cây mọc so le", "kiến trúc cân đối", "bố cục hội hoạ"]
        rows = VGroup()
        for s in items:
            dot = Dot(radius=0.07).set_fill(ACCENT, 1).set_stroke(width=0)
            txt = Text(s, font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY)
            rows.add(VGroup(dot, txt).arrange(RIGHT, buff=0.2))
        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        fit_w(rows, CW).move_to([0, -0.2, 0])
        with self.voice("08_ungdung") as D:
            self._kara("08_ungdung", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            for i, r in enumerate(rows):
                self.cue(D * (0.2 + i * 0.18)); self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.45)
            self._b = VGroup(t, rows)
        self._clear()

    # 9. CTA ------------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("1 quy tắc cộng đơn giản", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.8, 0])
        l2 = fit_w(Text("nặn nên hình dáng sự sống", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("dãy số · giới hạn · tỉ lệ vàng", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.3, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.7, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("THEO DÕI", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.6, 0])
        with self.voice("09_cta", gap=0.4) as D:
            self._kara("09_cta", D)
            self.cue(D * 0.0); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.3); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.08), run_time=0.8)
            self.cue(D * 0.55); self.play(FadeIn(tags, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.75); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, tags, sub)
        self._clear()
