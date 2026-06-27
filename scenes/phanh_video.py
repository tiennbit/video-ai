"""
"Chạy nhanh gấp đôi, phanh gấp 4 lần đường" — quãng phanh ∝ v².
Vật lý 10 · SHORT DỌC 9:16 · ~2 phút · giải thích logic từng bước.

Kế thừa template brand.py. Bố cục xếp dọc, chữ vừa phải (đã giảm cỡ theo phản hồi).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_phanh.py
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/phanh_video.py PhanhVideo
Xem trước:   .venv/bin/manim -ql --resolution 540,960 --fps 12 scenes/phanh_video.py PhanhVideo
"""
import os

from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED)
from narration_texts_phanh import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def car_icon(scale=1.0, color=ACCENT):
    body = RoundedRectangle(corner_radius=0.12, width=1.0, height=0.34).set_fill(color, 1).set_stroke(width=0)
    cabin = RoundedRectangle(corner_radius=0.1, width=0.5, height=0.26).set_fill(color, 1).set_stroke(width=0).move_to([0.05, 0.22, 0])
    win = RoundedRectangle(corner_radius=0.05, width=0.32, height=0.15).set_fill(BG, 1).set_stroke(width=0).move_to([0.08, 0.22, 0])
    w1 = Dot([-0.28, -0.2, 0], radius=0.11).set_fill("#1A1A1A", 1).set_stroke(width=0)
    w2 = Dot([0.3, -0.2, 0], radius=0.11).set_fill("#1A1A1A", 1).set_stroke(width=0)
    return VGroup(body, cabin, win, w1, w2).scale(scale)


def kid(scale=1.0):
    body = Polygon([-0.13, -0.22, 0], [0.13, -0.22, 0], [0, 0.2, 0]).set_fill(DEBT, 1).set_stroke(width=0)
    head = Dot(radius=0.12).set_fill("#FFD9A0", 1).set_stroke(width=0).move_to([0, 0.3, 0])
    return VGroup(body, head).scale(scale)


def hbar(length, color, y, start_x=-1.95, h=0.34, fill=0.9):
    r = Rectangle(width=max(length, 0.02), height=h).set_fill(color, fill).set_stroke(width=0)
    r.move_to([start_x + length / 2, y, 0])
    return r


class PhanhVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_phanh")
    SEGMENTS = SEGMENTS
    TOPIC = "VẬT LÝ 10"

    def construct(self):
        self.camera.background_color = BG
        self.play_intro()
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_haiphan()
        self.beat_phanxa()
        self.beat_phanh()
        self.beat_rapso()
        self.beat_ynghia()
        self.beat_cta()
        self.brand_stinger()
        self.wait(0.3)

    # 1. HOOK ----------------------------------------------------------
    def beat_hook(self):
        road = Line([-2.05, 0.2, 0], [2.05, 0.2, 0]).set_stroke("#3A4254", 7)
        car = car_icon(0.9, ACCENT).move_to([-1.4, 0.46, 0])
        child = kid(0.95).move_to([1.7, 0.5, 0])
        dim = DoubleArrow([-0.9, -0.4, 0], [1.7, -0.4, 0], buff=0, color=MUTED, stroke_width=3, tip_length=0.18)
        dlbl = Text("40 m", font=FONT, weight=BOLD, color=MUTED).scale(0.5).next_to(dim, DOWN, buff=0.1)
        q = Text("?", font=FONT, weight=BOLD, color=ACCENT).scale(1.7).move_to([0, -1.7, 0])
        with self.voice("01_hook") as D:
            kar = self.make_karaoke(SEGMENTS["01_hook"], D, self.beat_t0)
            self.add(kar)
            self.play(Create(road), FadeIn(car, shift=RIGHT * 0.3), run_time=0.8)
            self.play(FadeIn(child, scale=0.6), run_time=0.5)
            self.play(GrowFromCenter(dim), FadeIn(dlbl), run_time=0.7)
            self.play(Write(q), Indicate(q, color=ACCENT, scale_factor=1.3), run_time=0.9)
            self._b = VGroup(road, car, child, dim, dlbl, q)
        self.end_karaoke(kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 2. HAI PHẦN ------------------------------------------------------
    def beat_haiphan(self):
        title = fit_w(Text("QUÃNG ĐƯỜNG DỪNG", font=FONT, weight=BOLD, color=ACCENT).scale(0.66), 3.5).move_to([0, 2.7, 0])
        refl = hbar(1.4, ACCENT, 1.3, start_x=-1.8)
        brk = hbar(2.1, DEBT, 1.3, start_x=-1.8 + 1.4)
        l1 = Text("phản xạ", font=FONT, weight=BOLD, color=ACCENT).scale(0.44).next_to(refl, DOWN, buff=0.15)
        l2 = Text("phanh", font=FONT, weight=BOLD, color=DEBT).scale(0.44).next_to(brk, DOWN, buff=0.15)
        guess = VGroup(
            Text("Trực giác:", font=FONT, color=MUTED).scale(0.52),
            fit_w(Text("×2 tốc độ → ×2 đường?", font=FONT, weight=BOLD, color=WHITE).scale(0.55), 3.7),
        ).arrange(DOWN, buff=0.2).move_to([0, -0.8, 0])
        with self.voice("02_haiphan") as D:
            kar = self.make_karaoke(SEGMENTS["02_haiphan"], D, self.beat_t0)
            self.add(kar)
            self.play(Write(title), run_time=0.7)
            self.play(GrowFromEdge(refl, LEFT), FadeIn(l1), run_time=0.7)
            self.play(GrowFromEdge(brk, LEFT), FadeIn(l2), run_time=0.7)
            self.play(FadeIn(guess, shift=UP * 0.2), run_time=0.8)
            self._b = VGroup(title, refl, brk, l1, l2, guess)
        self.end_karaoke(kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 3. PHẢN XẠ (∝ v) -------------------------------------------------
    def beat_phanxa(self):
        f = fit_w(Text("quãng phản xạ = v × t", font=FONT, weight=BOLD, color=WHITE).scale(0.7), 3.6).move_to([0, 2.6, 0])
        t1 = Text("t ≈ 1 giây  (chưa giảm tốc)", font=FONT, color=MUTED).scale(0.48).next_to(f, DOWN, buff=0.2)
        b1 = hbar(0.9, ACCENT, 0.9); n1 = Text("40 km/h → 11 m", font=FONT, weight=BOLD, color=ACCENT).scale(0.44).next_to(b1, UP, buff=0.08).align_to(b1, LEFT)
        b2 = hbar(1.8, ACCENT, -0.2); n2 = Text("80 km/h → 22 m", font=FONT, weight=BOLD, color=ACCENT).scale(0.44).next_to(b2, UP, buff=0.08).align_to(b2, LEFT)
        badge = Text("×2  (tỉ lệ thuận)", font=FONT, weight=BOLD, color=GROW).scale(0.52).move_to([0, -1.3, 0])
        with self.voice("03_phanxa") as D:
            kar = self.make_karaoke(SEGMENTS["03_phanxa"], D, self.beat_t0)
            self.add(kar)
            self.play(Write(f), FadeIn(t1), run_time=1.0)
            self.play(GrowFromEdge(b1, LEFT), FadeIn(n1), run_time=0.7)
            self.play(GrowFromEdge(b2, LEFT), FadeIn(n2), run_time=0.7)
            self.play(FadeIn(badge, shift=UP * 0.2), run_time=0.6)
            self._b = VGroup(f, t1, b1, n1, b2, n2, badge)
        self.end_karaoke(kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 4. PHANH (∝ v²) — CỐT LÕI ---------------------------------------
    def beat_phanh(self):
        e1 = fit_w(Text("Động năng = ½·m·v²", font=FONT, weight=BOLD, color=WHITE).scale(0.68), 3.5).move_to([0, 2.8, 0])
        e2 = fit_w(Text("Lực phanh × d  =  ½·m·v²", font=FONT, color=MUTED).scale(0.55), 3.5).move_to([0, 2.2, 0])
        res = fit_w(Text("→  d = k · v²", font=FONT, weight=BOLD, color=ACCENT).scale(0.78), 3.3).move_to([0, 1.5, 0])
        b1 = hbar(0.62, DEBT, 0.5); n1 = Text("40 → 9 m", font=FONT, weight=BOLD, color=DEBT).scale(0.44).next_to(b1, UP, buff=0.08).align_to(b1, LEFT)
        b2 = hbar(2.45, DEBT, -0.3); n2 = Text("80 → 35 m", font=FONT, weight=BOLD, color=DEBT).scale(0.44).next_to(b2, UP, buff=0.08).align_to(b2, LEFT)
        badge = Text("× 4 !", font=FONT, weight=BOLD, color=ACCENT).scale(0.85).move_to([0, -1.4, 0])
        with self.voice("04_phanh") as D:
            kar = self.make_karaoke(SEGMENTS["04_phanh"], D, self.beat_t0)
            self.add(kar)
            self.play(Write(e1), run_time=0.9)
            self.play(FadeIn(e2, shift=UP * 0.15), run_time=0.7)
            self.play(Write(res), Indicate(res, color=ACCENT, scale_factor=1.15), run_time=0.9)
            self.play(GrowFromEdge(b1, LEFT), FadeIn(n1), run_time=0.6)
            self.play(GrowFromEdge(b2, LEFT), FadeIn(n2), run_time=0.9)
            self.play(FadeIn(badge, scale=0.5), Flash(badge.get_center(), color=ACCENT, line_length=0.4, num_lines=14), run_time=0.8)
            self._b = VGroup(e1, e2, res, b1, n1, b2, n2, badge)
        self.end_karaoke(kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 5. RÁP SỐ — payoff ----------------------------------------------
    def beat_rapso(self):
        SC = 0.062  # đơn vị / mét (để 57m ~ vừa khung)
        sx = -1.95
        line40 = -1.95 + 40 * SC
        marker = DashedLine([line40, 1.4, 0], [line40, -1.6, 0], color=WHITE, stroke_width=2.5)
        mlbl = VGroup(kid(0.65), Text("40 m", font=FONT, weight=BOLD, color=WHITE).scale(0.4)).arrange(DOWN, buff=0.05)
        mlbl.next_to([line40, 1.4, 0], UP, buff=0.1)

        r40 = hbar(11 * SC, ACCENT, 0.6, start_x=sx); k40 = hbar(9 * SC, DEBT, 0.6, start_x=sx + 11 * SC)
        t40 = Text("40 km/h: ~20 m", font=FONT, weight=BOLD, color=GROW).scale(0.44).next_to(VGroup(r40, k40), UP, buff=0.12).align_to([sx, 0, 0], LEFT)
        safe = Text("DỪNG KỊP", font=FONT, weight=BOLD, color=GROW).scale(0.44).next_to(k40, RIGHT, buff=0.2)
        r80 = hbar(22 * SC, ACCENT, -0.7, start_x=sx); k80 = hbar(35 * SC, DEBT, -0.7, start_x=sx + 22 * SC)
        t80 = Text("80 km/h: ~57 m", font=FONT, weight=BOLD, color=DEBT).scale(0.44).next_to(VGroup(r80, k80), UP, buff=0.12).align_to([sx, 0, 0], LEFT)
        with self.voice("05_rapso") as D:
            kar = self.make_karaoke(SEGMENTS["05_rapso"], D, self.beat_t0)
            self.add(kar)
            self.play(GrowFromEdge(r40, LEFT), GrowFromEdge(k40, LEFT), FadeIn(t40), run_time=1.0)
            self.play(GrowFromEdge(r80, LEFT), GrowFromEdge(k80, LEFT), FadeIn(t80), run_time=1.2)
            self.play(Create(marker), FadeIn(mlbl, shift=DOWN * 0.15), run_time=0.8)
            self.play(FadeIn(safe), run_time=0.5)
            crash = Text("ĐÂM!", font=FONT, weight=BOLD, color=DEBT).scale(0.65).move_to([line40 + 0.55, -1.35, 0])
            self.play(Flash(k80.get_right(), color=DEBT, line_length=0.4, num_lines=14), FadeIn(crash, scale=0.5), run_time=0.9)
            self._b = VGroup(marker, mlbl, r40, k40, t40, safe, r80, k80, t80, crash)
        self.end_karaoke(kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 6. Ý NGHĨA -------------------------------------------------------
    def beat_ynghia(self):
        big = Text("v²", font=FONT, weight=BOLD, color=ACCENT).scale(1.55).move_to([0, 2.2, 0])
        bullets = VGroup(
            Text("• Khu dân cư: giới hạn tốc độ thấp", font=FONT, color=WHITE).scale(0.48),
            Text("• Nguy hiểm tăng theo v² (không phải v)", font=FONT, color=WHITE).scale(0.48),
            Text("• = động năng trong MỌI va chạm", font=FONT, weight=BOLD, color=GROW).scale(0.48),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).move_to([0, -0.4, 0])
        for b in bullets:
            fit_w(b, 3.7)
        with self.voice("06_ynghia") as D:
            kar = self.make_karaoke(SEGMENTS["06_ynghia"], D, self.beat_t0)
            self.add(kar)
            self.play(Write(big), run_time=0.7)
            for b in bullets:
                self.play(FadeIn(b, shift=RIGHT * 0.2), run_time=0.7)
            self._b = VGroup(big, bullets)
        self.end_karaoke(kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 7. CTA -----------------------------------------------------------
    def beat_cta(self):
        lesson = fit_w(Text("Tốc độ ×2  →  Phanh ×4", font=FONT, weight=BOLD, color=ACCENT).scale(0.9), 3.6).move_to([0, 1.5, 0])
        sub_btn = RoundedRectangle(corner_radius=0.22, width=2.8, height=0.85).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("ĐĂNG KÝ", font=FONT, weight=BOLD, color=WHITE).scale(0.6).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.2, 0])
        with self.voice("07_cta", gap=0.4) as D:
            kar = self.make_karaoke(SEGMENTS["07_cta"], D, self.beat_t0)
            self.add(kar)
            self.play(Write(lesson), run_time=0.8)
            self.play(Indicate(lesson, color=GROW, scale_factor=1.1), run_time=0.5)
            self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(lesson, sub)
        self.end_karaoke(kar)
        self.play(FadeOut(self._b), run_time=0.4)
