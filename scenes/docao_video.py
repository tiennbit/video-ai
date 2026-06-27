"""
"Đo chiều cao toà nhà mà không cần trèo" — lượng giác / hệ thức lượng (tan).
Toán 10 · SHORT DỌC 9:16 · ~1 phút 50 · KHÔNG intro.

Dùng bộ cỡ chữ chuẩn SZ_* (brand.py) + CANH NHỊP self.cue(): mỗi bước hiện hình được
rải trải đều theo lời đọc của cả đoạn (không dồn ở đầu beat).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_docao.py
Căn chỉnh:   .venv/bin/python scenes/align_narration.py output/narration_docao
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/docao_video.py DoCaoVideo
"""
import os

import numpy as np

from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_docao import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKY = "#60A5FA"      # màu toà nhà / cạnh đứng (chiều cao)
GROUND = "#6B7280"   # màu mặt đất / cạnh ngang (khoảng cách)


def building(w=0.9, h=2.6, color=SKY):
    """Toà nhà đơn giản: khối chữ nhật + vài ô cửa sổ."""
    tower = Rectangle(width=w, height=h).set_fill(color, 0.85).set_stroke("#1E3A5F", 3)
    wins = VGroup()
    cols = 3
    rows = max(2, int(h / 0.45))
    for r in range(rows):
        for c in range(cols):
            win = Rectangle(width=w * 0.16, height=h * 0.05).set_fill("#0B1020", 0.9).set_stroke(width=0)
            win.move_to(tower.get_center())
            win.shift([(c - 1) * w * 0.28, (r - (rows - 1) / 2) * (h / rows) * 0.85, 0])
            wins.add(win)
    return VGroup(tower, wins)


class DoCaoVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_docao")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 10"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_vande()
        self.beat_mohinh()
        self.beat_consonu()
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

    # 1. HOOK: toà nhà cao + dấu hỏi chiều cao -------------------------
    def beat_hook(self):
        bld = building(1.0, 3.4).move_to([0.55, 0.5, 0])
        ground = Line([-1.9, -1.2, 0], [1.9, -1.2, 0]).set_stroke(GROUND, 4)
        person = VGroup(
            Circle(radius=0.1).set_fill(ACCENT, 1).set_stroke(width=0),
            Line([0, -0.1, 0], [0, -0.45, 0]).set_stroke(ACCENT, 4),
        ).arrange(DOWN, buff=0.02).move_to([-1.4, -0.95, 0])
        qmark = Text("?", font=FONT, weight=BOLD, color=ACCENT).scale(1.3).next_to(bld, UP, buff=0.15)
        title = fit_w(Text("Cao bao nhiêu mét?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, -1.7, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Create(ground), FadeIn(person, shift=UP * 0.2), run_time=0.7)
            self.cue(D * 0.22); self.play(FadeIn(bld, shift=DOWN * 0.3), run_time=0.9)
            self.cue(D * 0.5); self.play(FadeIn(qmark, scale=0.5), run_time=0.6)
            self.cue(D * 0.72); self.play(Write(title), run_time=0.8)
            self._b = VGroup(bld, ground, person, qmark, title)
        self._clear()

    # 2. VẤN ĐỀ: khoảng cách 50m + góc nhìn 60° ------------------------
    def beat_vande(self):
        A = np.array([-1.55, -1.4, 0])     # vị trí người (đỉnh góc)
        B = np.array([1.45, -1.4, 0])      # chân toà nhà
        T = np.array([1.45, 1.7, 0])       # đỉnh toà nhà
        ground = Line(A + LEFT * 0.3, B + RIGHT * 0.3, color=GROUND, stroke_width=4)
        bld = building(0.7, (T[1] - B[1])).move_to([(B[0]), (B[1] + T[1]) / 2, 0])
        sight = DashedLine(A, T, color=ACCENT, stroke_width=4)
        dist = Line(A, B).set_stroke(GROUND, 5)
        dlbl = Text("50 m", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL).next_to(dist, DOWN, buff=0.18)
        ang = Arc(radius=0.55, start_angle=0, angle=np.arctan2(T[1] - A[1], T[0] - A[0]), arc_center=A).set_stroke(ACCENT, 4)
        albl = Text("60°", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL).move_to(A + RIGHT * 0.95 + UP * 0.4)
        eye = Dot(A, radius=0.09).set_fill(ACCENT, 1).set_stroke(width=0)
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.0); self.play(Create(ground), FadeIn(bld, shift=DOWN * 0.2), run_time=0.8)
            self.cue(D * 0.3); self.play(FadeIn(eye), Create(dist), FadeIn(dlbl), run_time=0.8)
            self.cue(D * 0.58); self.play(Create(sight), run_time=0.7)
            self.cue(D * 0.78); self.play(Create(ang), Write(albl), run_time=0.7)
            self._b = VGroup(ground, bld, dist, dlbl, sight, ang, albl, eye)
        self._clear()

    # 3. MÔ HÌNH HOÁ: tam giác vuông ----------------------------------
    def beat_mohinh(self):
        A = np.array([-1.45, -1.55, 0])
        B = np.array([1.45, -1.55, 0])
        T = np.array([1.45, 1.75, 0])
        tri = Polygon(A, B, T).set_fill(BG_CARD, 0.5).set_stroke(ACCENT, 4)
        # ký hiệu góc vuông tại B
        s = 0.28
        sq = VGroup(
            Line(B + LEFT * s, B + LEFT * s + UP * s),
            Line(B + LEFT * s + UP * s, B + UP * s),
        ).set_stroke(WHITE, 3)
        horiz = Text("kề: 50 m", font=FONT, weight=BOLD, color=GROUND).scale(SZ_LABEL)
        horiz.next_to(Line(A, B), DOWN, buff=0.18)
        vert = Text("đối: chiều cao", font=FONT, weight=BOLD, color=SKY).scale(SZ_LABEL)
        vert.rotate(PI / 2).next_to(Line(B, T), RIGHT, buff=0.18)
        ang = Arc(radius=0.55, start_angle=0, angle=np.arctan2(T[1] - A[1], T[0] - A[0]), arc_center=A).set_stroke(ACCENT, 4)
        albl = Text("60°", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL).move_to(A + RIGHT * 0.95 + UP * 0.42)
        qh = Text("?", font=FONT, weight=BOLD, color=SKY).scale(0.7).next_to(Line(B, T), RIGHT, buff=0.95)
        with self.voice("03_mohinh") as D:
            self._kara("03_mohinh", D)
            self.cue(D * 0.0); self.play(Create(tri), Create(sq), run_time=0.9)
            self.cue(D * 0.3); self.play(FadeIn(horiz, shift=UP * 0.15), run_time=0.7)
            self.cue(D * 0.55); self.play(FadeIn(vert, shift=LEFT * 0.15), FadeIn(qh, scale=0.5), run_time=0.7)
            self.cue(D * 0.8); self.play(Create(ang), Write(albl), run_time=0.6)
            self._b = VGroup(tri, sq, horiz, vert, ang, albl, qh)
        self._clear()

    # 4. RA CON SỐ: tan60 = h/50 -> h ≈ 86 m --------------------------
    def beat_consonu(self):
        title = fit_w(Text("Tỉ số lượng giác", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        f1 = fit_w(Text("tan(góc) = đối / kề", font=FONT, weight=BOLD, color=MUTED).scale(SZ_BODY), CW).move_to([0, 1.7, 0])
        f2 = fit_w(Text("tan 60° = h / 50", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, 0.85, 0])
        f3 = fit_w(Text("h = 50 × tan 60°", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 0.0, 0])
        line = Line([-1.5, -0.55, 0], [1.5, -0.55, 0]).set_stroke("#3A4254", 3)
        res = Text("h ≈ 86 m", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO).move_to([0, -1.4, 0])
        with self.voice("04_consonu") as D:
            self._kara("04_consonu", D)
            self.cue(D * 0.0); self.play(Write(title), FadeIn(f1, shift=UP * 0.15), run_time=0.8)
            self.cue(D * 0.3); self.play(FadeIn(f2, shift=UP * 0.15), run_time=0.7)
            self.cue(D * 0.55); self.play(FadeIn(f3, shift=UP * 0.15), run_time=0.7)
            self.cue(D * 0.78); self.play(Create(line), Write(res), Flash(res.get_center(), color=GROW, line_length=0.4, num_lines=18), run_time=1.1)
            self._b = VGroup(title, f1, f2, f3, line, res)
        self._clear()

    # 5. Ý NGHĨA: Thales + Everest ------------------------------------
    def beat_ynghia(self):
        big = fit_w(Text("MỘT GÓC ĐO CẢ THẾ GIỚI", font=FONT, weight=BOLD, color=ACCENT), CW).move_to([0, 2.4, 0])
        # kim tự tháp + bóng (Thales)
        pyr = Polygon([-1.55, -0.4, 0], [-0.35, -0.4, 0], [-0.95, 0.5, 0]).set_fill("#D9A441", 0.85).set_stroke("#8A6A1F", 3)
        shadow = Line([-0.35, -0.4, 0], [0.5, -0.4, 0]).set_stroke(MUTED, 5)
        plbl = Text("Thales đo kim tự tháp", font=FONT, color=WHITE).scale(SZ_SMALL).move_to([-0.4, -0.85, 0])
        bullets = VGroup(
            Text("→ đo cây, đo núi từ xa", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("→ đo cả đỉnh Everest", font=FONT, weight=BOLD, color=SKY).scale(SZ_LABEL),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([0, -1.65, 0])
        for b in bullets:
            fit_w(b, CW)
        with self.voice("05_ynghia") as D:
            self._kara("05_ynghia", D)
            self.cue(D * 0.0); self.play(Write(big), run_time=0.9)
            self.cue(D * 0.28); self.play(Create(pyr), Create(shadow), FadeIn(plbl), run_time=0.9)
            self.cue(D * 0.58); self.play(FadeIn(bullets[0], shift=RIGHT * 0.2), run_time=0.6)
            self.cue(D * 0.78); self.play(FadeIn(bullets[1], shift=RIGHT * 0.2), run_time=0.6)
            self._b = VGroup(big, pyr, shadow, plbl, bullets)
        self._clear()

    # 6. CTA -----------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Tam giác nhỏ trên giấy", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.8, 0])
        l2 = fit_w(Text("mở khoá thứ khổng lồ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.05, 0])
        tags = VGroup(
            Text("thiên văn · trắc địa · GPS", font=FONT, color=MUTED).scale(SZ_LABEL),
        ).move_to([0, 0.35, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.5, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("ĐĂNG KÝ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.55, 0])
        with self.voice("06_cta", gap=0.4) as D:
            self._kara("06_cta", D)
            self.cue(D * 0.0); self.play(Write(l1), run_time=0.7)
            self.cue(D * 0.25); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.08), run_time=0.8)
            self.cue(D * 0.5); self.play(FadeIn(tags, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.7); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, tags, sub)
        self._clear()
