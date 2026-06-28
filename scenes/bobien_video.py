"""
"Bờ biển dài vô hạn" — bông tuyết Koch, cấp số nhân, giới hạn.
Toán 11 · SHORT DỌC 9:16 · ~1 phút 40 · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_bobien.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/bobien_video.py BoBienVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_bobien import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SEA = "#5EC8F2"


def _koch_points(level, a, b):
    """Danh sách điểm của đường Koch cấp `level` giữa a và b (đỉnh nhô LÊN)."""
    pts = [np.array(a, dtype=float), np.array(b, dtype=float)]
    for _ in range(level):
        new = []
        for p, q in zip(pts[:-1], pts[1:]):
            d = (q - p) / 3.0
            p1 = p + d
            p2 = p + 2 * d
            peak = p1 + rotate_vector(d, PI / 3)   # tam giác đều nhô lên
            new += [p, p1, peak, p2]
        new.append(pts[-1])
        pts = new
    return pts


def koch_curve(level, a=(-1.85, -0.15, 0), b=(1.85, -0.15, 0), color=SEA, width=3.5, w=CW):
    m = VMobject().set_points_as_corners(_koch_points(level, a, b)).set_stroke(color, width)
    if m.width > w:
        m.set_width(w)
    return m


def fact_card(title, value, color, w=2.7):
    box = RoundedRectangle(corner_radius=0.16, width=w, height=1.05).set_fill(BG_CARD, 1).set_stroke(color, 2.5)
    tt = Text(title, font=FONT, weight=BOLD, color=MUTED).scale(SZ_LABEL)
    vv = Text(value, font=FONT, weight=BOLD, color=color).scale(SZ_TITLE)
    inner = VGroup(tt, vv).arrange(DOWN, buff=0.12).move_to(box)
    return VGroup(box, inner)


class BoBienVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_bobien")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 11"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_vande()
        self.beat_logic()
        self.beat_tinh()
        self.beat_wow()
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
        title = fit_w(Text("Bờ biển dài bao nhiêu?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.55, 0])
        coast = koch_curve(2, color=SEA, width=4).move_to([0, 0.55, 0])
        ans = Text("VÔ HẠN ?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO).move_to([0, -1.5, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Create(coast), run_time=1.1)
            self.cue(D * 0.4); self.play(Write(title), run_time=0.8)
            self.cue(D * 0.72); self.play(FadeIn(ans, scale=0.5), Flash(ans.get_center(), color=ACCENT, line_length=0.45, num_lines=14), run_time=0.9)
            self._b = VGroup(title, coast, ans)
        self._clear()

    # 2. VẤN ĐỀ: thước càng nhỏ càng dài --------------------------------
    def beat_vande(self):
        t = fit_w(Text("Thước càng nhỏ…", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        r1 = fit_w(Text("Thước 100 km  →  L₁", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.2, 0])
        r2 = fit_w(Text("Thước 1 km  →  L₂ ≫ L₁", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 0.2, 0])
        big = fit_w(Text("…con số càng PHÌNH TO", font=FONT, weight=BOLD, color=DEBT).scale(SZ_TITLE), CW).move_to([0, -1.2, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.05); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(r1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.55); self.play(FadeIn(r2, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.82); self.play(Write(big), run_time=0.7)
            self._b = VGroup(t, r1, r2, big)
        self._clear()

    # 3. DỰNG KOCH ------------------------------------------------------
    def beat_logic(self):
        t = fit_w(Text("Bông tuyết Koch", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        k = koch_curve(0).move_to([0, 0.35, 0])
        lab = fit_w(Text("1 đoạn  →  4 đoạn (mỗi đoạn 1/3)", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.5, 0])
        step = Text("bước 0", font=FONT, weight=BOLD, color=MUTED).scale(SZ_LABEL).move_to([0, -2.25, 0])
        with self.voice("03_logic") as D:
            self._kara("03_logic", D)
            self.cue(D * 0.0); self.play(Create(k), Write(t), run_time=0.7)
            self.cue(D * 0.3); self.play(FadeIn(lab, shift=UP * 0.12), FadeIn(step), run_time=0.5)
            for lvl in (1, 2, 3):
                self.cue(D * (0.3 + lvl * 0.18))
                self.play(
                    Transform(k, koch_curve(lvl).move_to([0, 0.35, 0])),
                    Transform(step, Text(f"bước {lvl}", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL).move_to([0, -2.25, 0])),
                    run_time=0.6,
                )
            self._b = VGroup(t, k, lab, step)
        self._clear()

    # 4. CHU VI → VÔ HẠN ------------------------------------------------
    def beat_tinh(self):
        icon = koch_curve(4, color=SEA, width=2).move_to([0, 2.2, 0])
        if icon.width > 2.4:
            icon.set_width(2.4)
        l1 = fit_w(Text("Mỗi bước: chu vi × 4/3", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 0.8, 0])
        l2 = fit_w(Text("công bội 4/3 > 1", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -0.05, 0])
        hero = Text("→  ∞", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO * 1.2).move_to([0, -1.5, 0])
        with self.voice("04_tinh") as D:
            self._kara("04_tinh", D)
            self.cue(D * 0.0); self.play(FadeIn(icon, shift=DOWN * 0.1), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.55); self.play(FadeIn(l2), run_time=0.5)
            self.cue(D * 0.78); self.play(Write(hero), Flash(hero.get_center(), color=ACCENT, line_length=0.5, num_lines=16), run_time=0.9)
            self._b = VGroup(icon, l1, l2, hero)
        self._clear()

    # 5. WOW: nghịch lý chu vi/diện tích --------------------------------
    def beat_wow(self):
        t = fit_w(Text("Nghịch lý", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        c1 = fact_card("CHU VI", "VÔ HẠN", DEBT).move_to([0, 1.2, 0])
        c2 = fact_card("DIỆN TÍCH", "HỮU HẠN", GROW).move_to([0, -0.2, 0])
        punch = fit_w(Text("→ mỗi bản đồ ghi một khác", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        with self.voice("05_wow") as D:
            self._kara("05_wow", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.5)
            self.cue(D * 0.2); self.play(GrowFromCenter(c1), run_time=0.6)
            self.cue(D * 0.5); self.play(GrowFromCenter(c2), run_time=0.6)
            self.cue(D * 0.8); self.play(Write(punch), run_time=0.7)
            self._b = VGroup(t, c1, c2, punch)
        self._clear()

    # 6. CTA ------------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Hình lặp vô tận = fractal", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.8, 0])
        l2 = fit_w(Text("ẩn ngay quanh ta", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.05, 0])
        tags = fit_w(Text("nén ảnh · ăng-ten · mạch máu", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.35, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.7, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("THEO DÕI", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.55, 0])
        with self.voice("06_cta", gap=0.4) as D:
            self._kara("06_cta", D)
            self.cue(D * 0.0); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.3); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.08), run_time=0.8)
            self.cue(D * 0.55); self.play(FadeIn(tags, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.75); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, tags, sub)
        self._clear()
