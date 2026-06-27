"""
"Kim tốc độ trên xe đang đo cái gì?" — Tốc độ kế chính là ĐẠO HÀM (vận tốc tức thời).
Toán 11 · SHORT DỌC 9:16 · ~1 phút 50 · KHÔNG intro.

Dùng bộ cỡ chữ chuẩn SZ_* (brand.py) + CANH NHỊP self.cue(): mỗi bước hiện hình được
rải trải đều theo lời đọc của cả đoạn (không dồn ở đầu beat).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_tocdoke.py
Căn chỉnh:   .venv/bin/python scenes/align_narration.py output/narration_tocdoke
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/tocdoke_video.py TocDoKeVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_tocdoke import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CYAN = "#38BDF8"   # vận tốc / kim tốc độ


def speedo(scale=1.0, frac=0.62):
    """Mặt đồng hồ tốc độ bán nguyệt + kim chỉ theo frac (0..1)."""
    R = 1.0
    arc = Arc(radius=R, start_angle=PI, angle=-PI).set_stroke("#3A4254", 6)
    ticks = VGroup()
    for i in range(9):
        a = PI - PI * i / 8.0
        p_out = np.array([np.cos(a), np.sin(a), 0]) * R
        p_in = p_out * 0.82
        col = ACCENT if i >= 6 else "#5A6472"
        ticks.add(Line(p_in, p_out).set_stroke(col, 4))
    hub = Dot(radius=0.08).set_fill(WHITE, 1).set_stroke(width=0)
    a = PI - PI * frac
    needle = Line([0, 0, 0], [np.cos(a) * 0.78, np.sin(a) * 0.78, 0]).set_stroke(DEBT, 7)
    return VGroup(arc, ticks, needle, hub).scale(scale)


class TocDoKeVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_tocdoke")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 11"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_haidongho()
        self.beat_trungbinh()
        self.beat_gioihan()
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

    # 1. HOOK — đồng hồ tốc độ, kim nhảy ------------------------------
    def beat_hook(self):
        gauge = speedo(1.05, 0.55).move_to([0, 1.7, 0])
        q = fit_w(Text("Kim này đang đo CÁI GÌ?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, -0.2, 0])
        ans = fit_w(Text("ĐẠO HÀM", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO), CW).move_to([0, -1.3, 0])
        sub = Text("(toán lớp 11)", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(ans, DOWN, buff=0.2)
        needle = gauge[2]
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(gauge, shift=DOWN * 0.2), run_time=0.7)
            self.cue(D * 0.22); self.play(Rotate(needle, -0.5, about_point=gauge[3].get_center()),
                                          rate_func=there_and_back, run_time=0.7)
            self.cue(D * 0.42); self.play(Write(q), run_time=0.8)
            self.cue(D * 0.7); self.play(Write(ans), FadeIn(sub),
                                         Flash(ans.get_center(), color=ACCENT, line_length=0.35, num_lines=16), run_time=1.0)
            self._b = VGroup(gauge, q, ans, sub)
        self._clear()

    # 2. HAI ĐỒNG HỒ — odometer (tổng) vs kim tốc độ (tức thời) -------
    def beat_haidongho(self):
        title = fit_w(Text("Xe có HAI đồng hồ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        # trái: odometer (ô số)
        od_box = RoundedRectangle(corner_radius=0.1, width=2.0, height=0.6).set_fill("#0E1426", 1).set_stroke(GROW, 3)
        od_num = Text("042 318", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY).move_to(od_box)
        od = VGroup(od_box, od_num).move_to([0, 1.5, 0])
        od_l = fit_w(Text("Cây số: TỔNG đã đi", font=FONT, color=MUTED).scale(SZ_LABEL), CW).next_to(od, DOWN, buff=0.22)
        # phải: kim tốc độ
        g = speedo(0.78, 0.6).move_to([0, -0.9, 0])
        g_l = fit_w(Text("Kim tốc độ: NHANH thế nào BÂY GIỜ", font=FONT, weight=BOLD, color=CYAN).scale(SZ_LABEL), CW).move_to([0, -2.2, 0])
        with self.voice("02_haidongho") as D:
            self._kara("02_haidongho", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.2); self.play(FadeIn(od, shift=UP * 0.15), FadeIn(od_l), run_time=0.8)
            self.cue(D * 0.5); self.play(FadeIn(g, shift=UP * 0.15), run_time=0.8)
            self.cue(D * 0.72); self.play(FadeIn(g_l, shift=UP * 0.15), run_time=0.7)
            self._b = VGroup(title, od, od_l, g, g_l)
        self._clear()

    # 3. TRUNG BÌNH — Δs/Δt = độ dốc cát tuyến ------------------------
    def beat_trungbinh(self):
        title = fit_w(Text("Tốc độ trung bình", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.7, 0])
        ax = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=3.0, y_length=3.0,
                  axis_config={"include_tip": False, "color": "#5A6472", "stroke_width": 3}).move_to([0, 0.55, 0])
        xl = Text("thời gian", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(ax.x_axis, DOWN, buff=0.1)
        yl = Text("quãng đường", font=FONT, color=MUTED).scale(SZ_SMALL).rotate(PI / 2).next_to(ax.y_axis, LEFT, buff=0.1)
        curve = ax.plot(lambda t: 0.18 * t ** 2 + 0.2 * t, x_range=[0, 4.6], color=CYAN, stroke_width=5)
        p1 = ax.c2p(1, 0.18 + 0.2); p2 = ax.c2p(4, 0.18 * 16 + 0.8)
        d1 = Dot(p1, radius=0.07).set_fill(WHITE, 1); d2 = Dot(p2, radius=0.07).set_fill(WHITE, 1)
        sec = Line(p1, p2).set_stroke(ACCENT, 5)
        frac = fit_w(Text("trung bình = quãng đường / thời gian", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, -1.7, 0])
        note = Text("= độ dốc đoạn nối 2 điểm", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(frac, DOWN, buff=0.18)
        with self.voice("03_trungbinh") as D:
            self._kara("03_trungbinh", D)
            self.cue(D * 0.0); self.play(Write(title), Create(ax), FadeIn(xl), FadeIn(yl), run_time=0.9)
            self.cue(D * 0.25); self.play(Create(curve), run_time=0.9)
            self.cue(D * 0.5); self.play(FadeIn(d1, scale=0.5), FadeIn(d2, scale=0.5), Create(sec), run_time=0.8)
            self.cue(D * 0.72); self.play(FadeIn(frac, shift=UP * 0.15), FadeIn(note), run_time=0.8)
            self._b = VGroup(title, ax, xl, yl, curve, d1, d2, sec, frac, note)
        self._clear()

    # 4. GIỚI HẠN — Δt→0: cát tuyến xoay thành tiếp tuyến = đạo hàm ---
    def beat_gioihan(self):
        title = fit_w(Text("Cho Δt tiến về 0", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.7, 0])
        ax = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1], x_length=3.0, y_length=3.0,
                  axis_config={"include_tip": False, "color": "#5A6472", "stroke_width": 3}).move_to([0, 0.55, 0])
        f = lambda t: 0.18 * t ** 2 + 0.2 * t
        curve = ax.plot(f, x_range=[0, 4.6], color=CYAN, stroke_width=5)
        x0 = 1.0
        p0 = ax.c2p(x0, f(x0))
        d0 = Dot(p0, radius=0.08).set_fill(ACCENT, 1)

        def secant(x2):
            p2 = ax.c2p(x2, f(x2))
            m = (f(x2) - f(x0)) / (x2 - x0)
            xa, xb = 0.0, 4.6
            return Line(ax.c2p(xa, f(x0) + m * (xa - x0)), ax.c2p(xb, f(x0) + m * (xb - x0))).set_stroke(ACCENT, 5)

        sec = secant(4.0)
        # tiếp tuyến (đạo hàm tại x0): m = 0.36*x0 + 0.2
        mt = 0.36 * x0 + 0.2
        tang = Line(ax.c2p(0.0, f(x0) + mt * (0.0 - x0)), ax.c2p(4.6, f(x0) + mt * (4.6 - x0))).set_stroke(GROW, 6)
        tlbl = Text("TIẾP TUYẾN", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL).move_to([1.0, -1.35, 0])
        res = fit_w(Text("độ dốc tiếp tuyến = VẬN TỐC TỨC THỜI", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), CW).move_to([0, -2.0, 0])
        eq = Text("= s'(t)  (đạo hàm)", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY).next_to(res, DOWN, buff=0.2)
        with self.voice("04_gioihan") as D:
            self._kara("04_gioihan", D)
            self.cue(D * 0.0); self.play(Write(title), Create(ax), Create(curve), FadeIn(d0, scale=0.5), run_time=0.9)
            self.cue(D * 0.22); self.play(Create(sec), run_time=0.6)
            self.cue(D * 0.4)
            for xn in (3.0, 2.0, 1.4):
                self.play(Transform(sec, secant(xn)), run_time=0.45)
            self.cue(D * 0.62); self.play(Transform(sec, tang), FadeIn(tlbl), run_time=0.7)
            self.cue(D * 0.8); self.play(FadeIn(res, shift=UP * 0.15), Write(eq),
                                         Flash(eq.get_center(), color=ACCENT, line_length=0.3, num_lines=14), run_time=1.0)
            self._b = VGroup(title, ax, curve, d0, sec, tlbl, res, eq)
        self._clear()

    # 5. Ý NGHĨA — máy lấy đạo hàm 24/7 + gia tốc kế -----------------
    def beat_ynghia(self):
        g = speedo(0.72, 0.58).move_to([0, 2.0, 0])
        cap = fit_w(Text("Tốc độ kế = máy lấy ĐẠO HÀM", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).next_to(g, DOWN, buff=0.3)
        chain = VGroup(
            Text("quãng đường", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("→  s'  →  vận tốc", font=FONT, weight=BOLD, color=CYAN).scale(SZ_LABEL),
            Text("→  v'  →  GIA TỐC", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL),
        ).arrange(DOWN, buff=0.22).move_to([0, -0.65, 0])
        for c in chain:
            fit_w(c, CW)
        phone = fit_w(Text("(điện thoại: đếm bước, xoay màn hình)", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.9, 0])
        with self.voice("05_ynghia") as D:
            self._kara("05_ynghia", D)
            self.cue(D * 0.0); self.play(FadeIn(g, shift=DOWN * 0.15), Write(cap), run_time=0.9)
            self.cue(D * 0.35); self.play(FadeIn(chain[0], shift=RIGHT * 0.2), FadeIn(chain[1], shift=RIGHT * 0.2), run_time=0.7)
            self.cue(D * 0.6); self.play(FadeIn(chain[2], shift=RIGHT * 0.2), run_time=0.6)
            self.cue(D * 0.8); self.play(FadeIn(phone), run_time=0.6)
            self._b = VGroup(g, cap, chain, phone)
        self._clear()

    # 6. CTA ----------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Đạo hàm không nằm yên trong sách", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.8, 0])
        g = speedo(0.62, 0.6).move_to([0, 0.55, 0])
        l2 = fit_w(Text("Nó là cái kim nhảy trước mắt bạn", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, -0.7, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.5, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("THEO DÕI", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -1.7, 0])
        with self.voice("06_cta", gap=0.4) as D:
            self._kara("06_cta", D)
            self.cue(D * 0.0); self.play(Write(l1), run_time=0.7)
            self.cue(D * 0.3); self.play(FadeIn(g, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.55); self.play(Write(l2), Indicate(l2, color=CYAN, scale_factor=1.06), run_time=0.8)
            self.cue(D * 0.78); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, g, l2, sub)
        self._clear()
