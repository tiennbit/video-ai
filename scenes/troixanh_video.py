"""
"Vì sao trời xanh, hoàng hôn đỏ?" — tán xạ Rayleigh.
Vật lý 11–12 · SHORT DỌC 9:16 · ~2 phút · KHÔNG intro · KHÔNG karaoke · canh nhịp cue().

Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_troixanh.py
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/troixanh_video.py TroiXanhVideo
Xem trước:   .venv/bin/manim -ql --resolution 540,960 --fps 12 scenes/troixanh_video.py TroiXanhVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, ACCENT, GROW, DEBT, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_troixanh import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKY = "#4DA6FF"      # xanh trời
ORANGE = "#FB923C"   # cam hoàng hôn


def sun(scale=1.0):
    core = Circle(radius=0.4).set_fill(ACCENT, 1).set_stroke(width=0)
    rays = VGroup()
    for k in range(8):
        d = np.array([np.cos(k * np.pi / 4), np.sin(k * np.pi / 4), 0])
        rays.add(Line(d * 0.5, d * 0.72, color=ACCENT, stroke_width=4))
    return VGroup(rays, core).scale(scale)


def eye(scale=1.0):
    outline = Ellipse(width=0.64, height=0.36).set_stroke(WHITE, 3).set_fill(BG, 1)
    iris = Dot(radius=0.1).set_fill(SKY, 1).set_stroke(width=0)
    pupil = Dot(radius=0.05).set_fill(BG, 1).set_stroke(width=0)
    return VGroup(outline, iris, pupil).scale(scale)


def spectrum(width=2.6, height=0.5):
    cols = ["#FF4D4D", "#FB923C", "#FFD93D", "#4ADE80", "#4DA6FF", "#A78BFA"]
    n = len(cols); w = width / n
    g = VGroup()
    for i, c in enumerate(cols):
        g.add(Rectangle(width=w, height=height).set_fill(c, 1).set_stroke(width=0).move_to([-width / 2 + w / 2 + i * w, 0, 0]))
    return g


def wave(color, cycles, width=2.0, amp=0.16, sw=4):
    return FunctionGraph(lambda x: amp * np.sin(2 * np.pi * cycles * (x / width)),
                         x_range=[0, width, 0.02], color=color, stroke_width=sw)


def scatter_arrows(center, color, n=7, r0=0.14, r1=0.5):
    g = VGroup()
    for k in range(n):
        a = k * 2 * np.pi / n + 0.3
        d = np.array([np.cos(a), np.sin(a), 0])
        g.add(Arrow(np.array(center) + d * r0, np.array(center) + d * r1, buff=0, color=color, stroke_width=3, tip_length=0.1))
    return g


def bluedots(coords, r=0.08, color=SKY, op=1.0):
    return VGroup(*[Dot(radius=r).set_fill(color, op).set_stroke(width=0).move_to([x, y, 0]) for (x, y) in coords])


class TroiXanhVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_troixanh")
    SEGMENTS = SEGMENTS
    TOPIC = "VẬT LÝ · ÁNH SÁNG"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_trang()
        self.beat_tanxa()
        self.beat_ngay()
        self.beat_chieu()
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

    # 1. HOOK ----------------------------------------------------------
    def beat_hook(self):
        s = sun(0.95).move_to([0, 2.3, 0])
        l1 = VGroup(Text("Ban ngày:", font=FONT, color=MUTED).scale(SZ_LABEL),
                    Text("TRỜI XANH", font=FONT, weight=BOLD, color=SKY).scale(SZ_TITLE)).arrange(RIGHT, buff=0.2)
        l2 = VGroup(Text("Hoàng hôn:", font=FONT, color=MUTED).scale(SZ_LABEL),
                    Text("ĐỎ RỰC", font=FONT, weight=BOLD, color=ORANGE).scale(SZ_TITLE)).arrange(RIGHT, buff=0.2)
        lines = VGroup(l1, l2).arrange(DOWN, buff=0.4).move_to([0, 0.3, 0])
        q = Text("?  cùng 1 Mặt Trời", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY).move_to([0, -1.5, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(s, scale=0.6), run_time=0.7)
            self.cue(D * 0.28); self.play(FadeIn(l1, shift=UP * 0.15), run_time=0.7)
            self.cue(D * 0.5); self.play(FadeIn(l2, shift=UP * 0.15), run_time=0.7)
            self.cue(D * 0.72); self.play(Write(q), run_time=0.7)
            self._b = VGroup(s, lines, q)
        self._clear()

    # 2. ÁNH SÁNG TRẮNG = MỌI MÀU -------------------------------------
    def beat_trang(self):
        white = VGroup(Dot(radius=0.13).set_fill(WHITE, 1).set_stroke(width=0),
                       Text("ánh sáng trắng", font=FONT, color=MUTED).scale(SZ_SMALL)).arrange(DOWN, buff=0.15).move_to([0, 2.2, 0])
        prism = Triangle().set_fill("#2A3142", 0.6).set_stroke(MUTED, 2).scale(0.55).move_to([0, 1.0, 0])
        spec = spectrum(2.7, 0.5).move_to([0, -0.5, 0])
        a1 = Arrow(white.get_bottom(), prism.get_top(), buff=0.1, color=WHITE, stroke_width=3)
        a2 = Arrow(prism.get_bottom(), spec.get_top(), buff=0.1, color="#888", stroke_width=3)
        lbl = fit_w(Text("= tất cả các màu (cầu vồng)", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).next_to(spec, DOWN, buff=0.35)
        with self.voice("02_trang") as D:
            self._kara("02_trang", D)
            self.cue(D * 0.0); self.play(FadeIn(white, shift=DOWN * 0.15), run_time=0.7)
            self.cue(D * 0.3); self.play(GrowArrow(a1), FadeIn(prism), run_time=0.7)
            self.cue(D * 0.55); self.play(GrowArrow(a2), LaggedStart(*[FadeIn(r, scale=0.5) for r in spec], lag_ratio=0.1), run_time=1.1)
            self.cue(D * 0.82); self.play(FadeIn(lbl, shift=UP * 0.15), run_time=0.6)
            self._b = VGroup(white, prism, spec, a1, a2, lbl)
        self._clear()

    # 3. TÁN XẠ: bước sóng ngắn -> mạnh -------------------------------
    def beat_tanxa(self):
        title = fit_w(Text("Khí quyển TÁN XẠ ánh sáng", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        bw = wave(SKY, cycles=9, width=1.7).move_to([-0.5, 1.5, 0])
        mol = Dot(radius=0.08).set_fill(MUTED, 1).set_stroke(width=0).next_to(bw, RIGHT, buff=0.1)
        scat = scatter_arrows(mol.get_center(), SKY, n=7)
        blbl = fit_w(Text("XANH · bước sóng ngắn → tán xạ MẠNH", font=FONT, weight=BOLD, color=SKY).scale(SZ_LABEL), CW).move_to([0, 0.7, 0])
        rw = wave(DEBT, cycles=3, width=1.7).move_to([-0.5, -0.3, 0])
        rstr = Arrow(rw.get_right(), rw.get_right() + RIGHT * 0.55, buff=0.08, color=DEBT, stroke_width=3, tip_length=0.12)
        rlbl = fit_w(Text("ĐỎ · bước sóng dài → tán xạ yếu", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, -1.1, 0])
        factor = Text("Xanh tán xạ  ~5×  đỏ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY).move_to([0, -1.9, 0])
        with self.voice("03_tanxa") as D:
            self._kara("03_tanxa", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.7)
            self.cue(D * 0.22); self.play(Create(bw), FadeIn(mol), run_time=0.7)
            self.cue(D * 0.4); self.play(LaggedStart(*[GrowArrow(a) for a in scat], lag_ratio=0.08), FadeIn(blbl), run_time=1.0)
            self.cue(D * 0.62); self.play(Create(rw), GrowArrow(rstr), FadeIn(rlbl), run_time=0.9)
            self.cue(D * 0.84); self.play(FadeIn(factor, shift=UP * 0.15), run_time=0.6)
            self._b = VGroup(title, bw, mol, scat, blbl, rw, rstr, rlbl, factor)
        self._clear()

    # 4. BAN NGÀY -> trời xanh ----------------------------------------
    def beat_ngay(self):
        s = sun(0.55).move_to([0, 2.7, 0])
        atmo = Rectangle(width=4.3, height=0.55).set_fill(SKY, 0.12).set_stroke(SKY, 1.5, opacity=0.4).move_to([0, 1.7, 0])
        amlbl = Text("khí quyển MỎNG", font=FONT, color=MUTED).scale(SZ_SMALL).move_to(atmo)
        coords = [(-1.7, 1.0), (-1.0, 0.5), (-0.3, 1.05), (0.4, 0.4), (1.1, 1.0), (1.7, 0.5),
                  (-1.3, 0.0), (0.0, 0.1), (1.3, -0.05), (-0.6, -0.45), (0.7, -0.4), (0.1, 0.7)]
        dots = bluedots(coords, r=0.09, color=SKY)
        ey = eye(1.1).move_to([0, -1.6, 0])
        lbl = Text("BAN NGÀY → trời XANH", font=FONT, weight=BOLD, color=SKY).scale(SZ_BODY).move_to([0, -2.4, 0])
        with self.voice("04_ngay") as D:
            self._kara("04_ngay", D)
            self.cue(D * 0.0); self.play(FadeIn(s, scale=0.6), FadeIn(atmo), FadeIn(amlbl), run_time=0.8)
            self.cue(D * 0.35); self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.1), run_time=1.4)
            self.cue(D * 0.65); self.play(FadeIn(ey, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.82); self.play(FadeIn(lbl, shift=UP * 0.15), run_time=0.6)
            self._b = VGroup(s, atmo, amlbl, dots, ey, lbl)
        self._clear()

    # 5. HOÀNG HÔN -> trời đỏ -----------------------------------------
    def beat_chieu(self):
        s = sun(0.5).move_to([-1.7, 0.4, 0])
        ey = eye(1.0).move_to([1.7, 0.4, 0])
        band = Rectangle(width=3.2, height=0.8).set_fill(ORANGE, 0.12).set_stroke(ORANGE, 1.5, opacity=0.4).move_to([0, 0.4, 0])
        amlbl = Text("khí quyển DÀY", font=FONT, color=ORANGE).scale(SZ_SMALL).next_to(band, UP, buff=0.12)
        red_ray = Arrow(s.get_right(), ey.get_left(), buff=0.12, color=DEBT, stroke_width=5)
        # xanh bị tán xạ bay đi (mờ, hướng lên)
        scattered = bluedots([(-0.8, 1.2), (-0.2, 1.5), (0.4, 1.25), (-1.1, 1.45)], r=0.08, color=SKY, op=0.5)
        lbl = Text("HOÀNG HÔN → trời ĐỎ", font=FONT, weight=BOLD, color=ORANGE).scale(SZ_BODY).move_to([0, -1.7, 0])
        sub = Text("(xanh đã tán xạ hết dọc đường)", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(lbl, DOWN, buff=0.2)
        with self.voice("05_chieu") as D:
            self._kara("05_chieu", D)
            self.cue(D * 0.0); self.play(FadeIn(s, scale=0.6), FadeIn(ey), run_time=0.7)
            self.cue(D * 0.25); self.play(FadeIn(band), FadeIn(amlbl), run_time=0.7)
            self.cue(D * 0.5); self.play(LaggedStart(*[FadeIn(d) for d in scattered], lag_ratio=0.12), run_time=0.9)
            self.cue(D * 0.7); self.play(GrowArrow(red_ray), run_time=0.8)
            self.cue(D * 0.86); self.play(FadeIn(lbl), FadeIn(sub), run_time=0.7)
            self._b = VGroup(s, ey, band, amlbl, red_ray, scattered, lbl, sub)
        self._clear()

    # 6. Ý NGHĨA -------------------------------------------------------
    def beat_ynghia(self):
        big = fit_w(Text("CÙNG MỘT ĐỊNH LUẬT TÁN XẠ", font=FONT, weight=BOLD, color=ACCENT), CW).move_to([0, 2.3, 0])
        bullets = VGroup(
            Text("• Vì sao mặt biển màu xanh", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("• Sao Hoả: trời ban ngày ngả ĐỎ", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("• Vẽ nên màu sắc cả thế giới", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to([0, 0.0, 0])
        for b in bullets:
            fit_w(b, CW)
        bcues = [0.25, 0.5, 0.72]
        with self.voice("06_ynghia") as D:
            self._kara("06_ynghia", D)
            self.cue(D * 0.0); self.play(Write(big), run_time=0.9)
            for b, f in zip(bullets, bcues):
                self.cue(D * f); self.play(FadeIn(b, shift=RIGHT * 0.2), run_time=0.6)
            self._b = VGroup(big, bullets)
        self._clear()

    # 7. CTA -----------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Ngắm hoàng hôn =", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.7, 0])
        l2 = fit_w(Text("nhìn xuyên cả bầu khí quyển", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.5, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("ĐĂNG KÝ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.3, 0])
        with self.voice("07_cta", gap=0.4) as D:
            self._kara("07_cta", D)
            self.cue(D * 0.0); self.play(Write(l1), run_time=0.7)
            self.cue(D * 0.3); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.06), run_time=0.8)
            self.cue(D * 0.62); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, sub)
        self._clear()
