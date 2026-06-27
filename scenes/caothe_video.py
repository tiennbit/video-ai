"""
"Vì sao lưới điện 220V?" — truyền tải điện năng đi xa bằng cao thế + máy biến áp.
Vật lý 12 (máy biến áp, hao phí I^2 R) · SHORT DỌC 9:16 · ~1.8 phút · KHÔNG intro.

Dùng bộ cỡ chữ chuẩn SZ_* (brand.py) + CANH NHỊP self.cue(): mỗi bước hiện hình được
rải trải đều theo lời đọc của cả đoạn (không dồn ở đầu beat).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_caothe.py
Căn chỉnh:   .venv/bin/python scenes/align_narration.py output/narration_caothe
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/caothe_video.py CaoTheVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_caothe import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ORANGE = "#FB923C"   # cao thế / nhiệt hao
BLUE = "#60A5FA"     # điện áp


def pdot(color, r=0.11):
    return Dot(radius=r).set_fill(color, 1).set_stroke(width=0)


def pylon(scale=1.0):
    """Cột điện cao thế đơn giản: tháp tam giác + 2 thanh ngang."""
    legs = VGroup(
        Line([-0.5, -0.9, 0], [0, 0.9, 0]),
        Line([0.5, -0.9, 0], [0, 0.9, 0]),
        Line([-0.34, -0.3, 0], [0.34, -0.3, 0]),
        Line([-0.18, 0.3, 0], [0.18, 0.3, 0]),
    ).set_stroke("#7A8699", 4)
    arm1 = Line([-0.62, 0.55, 0], [0.62, 0.55, 0]).set_stroke("#7A8699", 4)
    arm2 = Line([-0.46, 0.15, 0], [0.46, 0.15, 0]).set_stroke("#7A8699", 4)
    ins = VGroup(*[pdot(ACCENT, 0.05).move_to(p) for p in
                   ([-0.62, 0.55, 0], [0.62, 0.55, 0], [-0.46, 0.15, 0], [0.46, 0.15, 0])])
    return VGroup(legs, arm1, arm2, ins).scale(scale)


def coil(n_turns, color, w=0.7, h=0.95):
    """Cuộn dây máy biến áp: vẽ bằng các vòng tròn nhỏ chồng dọc."""
    g = VGroup()
    for i in range(n_turns):
        y = h / 2 - (i + 0.5) * (h / n_turns)
        g.add(Arc(radius=w * 0.5, start_angle=-PI / 2, angle=PI).rotate(PI).move_to([0, y, 0]))
    g.set_stroke(color, 4)
    return g


class CaoTheVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_caothe")
    SEGMENTS = SEGMENTS
    TOPIC = "VẬT LÝ 12"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_vande()
        self.beat_mohinh()
        self.beat_conso()
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

    # 1. HOOK — cột cao thế 500kV -> ổ cắm 220V --------------------------
    def beat_hook(self):
        tower = pylon(1.0).move_to([0, 2.1, 0])
        hv = Text("500 000 V", font=FONT, weight=BOLD, color=ORANGE).scale(SZ_TITLE).next_to(tower, DOWN, buff=0.25)
        arrow = Arrow([0, 0.3, 0], [0, -0.7, 0], color=MUTED, stroke_width=5, buff=0.1).move_to([0, -0.35, 0])
        socket = RoundedRectangle(corner_radius=0.12, width=1.0, height=1.0).set_fill(BG_CARD, 1).set_stroke("#7A8699", 3).move_to([0, -1.45, 0])
        holes = VGroup(pdot(MUTED, 0.07).shift(LEFT * 0.18), pdot(MUTED, 0.07).shift(RIGHT * 0.18)).move_to(socket)
        lv = Text("220 V", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY).next_to(socket, DOWN, buff=0.18)
        q = fit_w(Text("Vì sao phải đẩy lên rồi hạ xuống?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -2.6, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(tower, shift=DOWN * 0.2), run_time=0.7)
            self.cue(D * 0.2); self.play(Write(hv), run_time=0.7)
            self.cue(D * 0.45); self.play(GrowArrow(arrow), run_time=0.5)
            self.cue(D * 0.6); self.play(FadeIn(VGroup(socket, holes), shift=UP * 0.2), Write(lv), run_time=0.8)
            self.cue(D * 0.82); self.play(FadeIn(q, shift=UP * 0.15), run_time=0.6)
            self._b = VGroup(tower, hv, arrow, socket, holes, lv, q)
        self._clear()

    # 2. VẤN ĐỀ — dây dài có điện trở -> sinh nhiệt hao ------------------
    def beat_vande(self):
        title = fit_w(Text("Điện đi cả nghìn km", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.4, 0])
        line = Line([-1.7, 1.2, 0], [1.7, 1.2, 0]).set_stroke(BLUE, 5)
        p1 = pdot("#7A8699", 0.13).move_to([-1.7, 1.2, 0])
        p2 = pdot("#7A8699", 0.13).move_to([1.7, 1.2, 0])
        rlbl = Text("dây có điện trở R", font=FONT, color=MUTED).scale(SZ_LABEL).next_to(line, DOWN, buff=0.25)
        heat = VGroup(*[Text("≈", font=FONT, color=ORANGE).scale(0.5).move_to([x, 0.1, 0]) for x in (-1.1, -0.2, 0.7)])
        heatlbl = fit_w(Text("Dòng qua R → sinh NHIỆT → hao điện", font=FONT, weight=BOLD, color=ORANGE).scale(SZ_LABEL), CW).move_to([0, -0.8, 0])
        ask = fit_w(Text("Làm sao cắt phần điện mất dọc đường?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.8, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.2); self.play(Create(line), FadeIn(p1), FadeIn(p2), run_time=0.7)
            self.cue(D * 0.38); self.play(FadeIn(rlbl), run_time=0.5)
            self.cue(D * 0.55); self.play(LaggedStart(*[FadeIn(h, shift=UP * 0.2) for h in heat], lag_ratio=0.3), FadeIn(heatlbl), run_time=1.0)
            self.cue(D * 0.82); self.play(FadeIn(ask, shift=UP * 0.15), run_time=0.6)
            self._b = VGroup(title, line, p1, p2, rlbl, heat, heatlbl, ask)
        self._clear()

    # 3. MÔ HÌNH HOÁ — 2 công thức then chốt ----------------------------
    def beat_mohinh(self):
        title = fit_w(Text("Hai công thức then chốt", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        f1 = fit_w(Text("Hao phí  =  I² · R", font=FONT, weight=BOLD, color=ORANGE).scale(0.62), CW).move_to([0, 1.4, 0])
        f1n = Text("hao phí trên dây", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(f1, DOWN, buff=0.18)
        f2 = fit_w(Text("P  =  U · I", font=FONT, weight=BOLD, color=BLUE).scale(0.62), CW).move_to([0, -0.2, 0])
        f2n = Text("công suất truyền đi", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(f2, DOWN, buff=0.18)
        key = fit_w(Text("Hao phí phụ thuộc DÒNG bình phương", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, -1.5, 0])
        key2 = fit_w(Text("→ giảm dòng I = hao tụt rất nhanh", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), CW).move_to([0, -2.2, 0])
        with self.voice("03_mohinh") as D:
            self._kara("03_mohinh", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.18); self.play(Write(f1), FadeIn(f1n), run_time=0.9)
            self.cue(D * 0.42); self.play(Write(f2), FadeIn(f2n), run_time=0.9)
            self.cue(D * 0.66); self.play(FadeIn(key, shift=UP * 0.15), Indicate(f1, color=ACCENT, scale_factor=1.1), run_time=0.8)
            self.cue(D * 0.84); self.play(FadeIn(key2, shift=UP * 0.15), run_time=0.6)
            self._b = VGroup(title, f1, f1n, f2, f2n, key, key2)
        self._clear()

    # 4. RA CON SỐ — U x10 -> I /10 -> hao /100 -------------------------
    def beat_conso(self):
        title = fit_w(Text("Tăng áp 10 lần thì sao?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        r1 = fit_w(VGroup(
            Text("U", font=FONT, weight=BOLD, color=BLUE).scale(SZ_BODY),
            Text("× 10", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY),
        ).arrange(RIGHT, buff=0.25), CW).move_to([0, 1.4, 0])
        a1 = Arrow([0, 1.05, 0], [0, 0.55, 0], color=MUTED, stroke_width=4, buff=0.05)
        r2 = fit_w(VGroup(
            Text("I", font=FONT, weight=BOLD, color=ORANGE).scale(SZ_BODY),
            Text("÷ 10", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY),
        ).arrange(RIGHT, buff=0.25), CW).move_to([0, 0.25, 0])
        a2 = Arrow([0, -0.1, 0], [0, -0.6, 0], color=MUTED, stroke_width=4, buff=0.05)
        because = Text("hao phí ~ I²", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(a2, RIGHT, buff=0.2)
        res = fit_w(VGroup(
            Text("hao phí", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY),
            Text("÷ 100", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO),
        ).arrange(RIGHT, buff=0.3), CW).move_to([0, -1.1, 0])
        punch = fit_w(Text("Cắt 99% lượng điện bị mất!", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, -2.1, 0])
        with self.voice("04_conso") as D:
            self._kara("04_conso", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.2); self.play(FadeIn(r1, shift=DOWN * 0.15), run_time=0.6)
            self.cue(D * 0.36); self.play(GrowArrow(a1), FadeIn(r2, shift=DOWN * 0.15), run_time=0.7)
            self.cue(D * 0.56); self.play(GrowArrow(a2), FadeIn(because), run_time=0.6)
            self.cue(D * 0.72); self.play(Write(res), Flash(res.get_center(), color=ACCENT, line_length=0.4, num_lines=16), run_time=1.0)
            self.cue(D * 0.9); self.play(FadeIn(punch, shift=UP * 0.15), run_time=0.6)
            self._b = VGroup(title, r1, a1, r2, a2, because, res, punch)
        self._clear()

    # 5. Ý NGHĨA — máy biến áp: U1/U2 = N1/N2 ---------------------------
    def beat_ynghia(self):
        title = fit_w(Text("Bí quyết: MÁY BIẾN ÁP", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        core = Rectangle(width=1.4, height=1.5).set_stroke("#7A8699", 6).move_to([0, 1.05, 0])
        c1 = coil(5, ORANGE).move_to([-0.7, 1.05, 0])
        c2 = coil(3, BLUE).move_to([0.7, 1.05, 0])
        n1 = Text("N1", font=FONT, weight=BOLD, color=ORANGE).scale(SZ_SMALL).next_to(c1, DOWN, buff=0.12)
        n2 = Text("N2", font=FONT, weight=BOLD, color=BLUE).scale(SZ_SMALL).next_to(c2, DOWN, buff=0.12)
        f = fit_w(Text("U1 / U2  =  N1 / N2", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, -0.7, 0])
        bullets = VGroup(
            Text("• Nâng cao thế đi xuyên Bắc Nam", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("• Hạ dần qua từng trạm về nhà", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("• Cục sạc = máy biến áp tí hon", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).move_to([0, -2.2, 0])
        for b in bullets:
            fit_w(b, CW)
        with self.voice("05_ynghia") as D:
            self._kara("05_ynghia", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.16); self.play(Create(core), Create(c1), Create(c2), FadeIn(n1), FadeIn(n2), run_time=1.0)
            self.cue(D * 0.42); self.play(Write(f), run_time=0.8)
            self.cue(D * 0.6)
            for b, fr in zip(bullets, (0.6, 0.72, 0.84)):
                self.cue(D * fr); self.play(FadeIn(b, shift=RIGHT * 0.2), run_time=0.5)
            self._b = VGroup(title, core, c1, c2, n1, n2, f, bullets)
        self._clear()

    # 6. CTA -----------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Một con số tưởng ngược đời", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.7, 0])
        l2 = fit_w(Text("là cả một hệ thống tinh tế", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.5, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("THEO DÕI", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.3, 0])
        with self.voice("06_cta", gap=0.4) as D:
            self._kara("06_cta", D)
            self.cue(D * 0.0); self.play(Write(l1), run_time=0.7)
            self.cue(D * 0.3); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.08), run_time=0.8)
            self.cue(D * 0.6); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, sub)
        self._clear()
