"""
TẬP 1 — "Bí mật của Cấp số nhân" (lãi kép) · SHORT DỌC 9:16 (~50s).
Toán 11 · Reels / TikTok / YouTube Shorts.

Kế thừa template thương hiệu brand.py (intro vẹt + khung dọc + karaoke + outro).
Bố cục XẾP DỌC, chữ to cho màn hình điện thoại.

Sinh giọng clone của bạn trước:
    ~/voxcpm-venv/bin/python scenes/clone_narration_laikep.py
Render DỌC:
    .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/laikep_video.py LaiKepVideo
Xem trước NHANH (im lặng, fallback thời lượng):
    .venv/bin/manim -ql --resolution 540,960 --fps 12 scenes/laikep_video.py LaiKepVideo
"""
import os

from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED)
from narration_texts_laikep import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def vnd(v):
    return f"{int(round(v)):,}".replace(",", ".") + "đ"


def money_counter(tracker, pos, color, max_value):
    """Số tiền đếm nhảy, scale CỐ ĐỊNH vừa khung dọc (theo giá trị lớn nhất)."""
    probe = Text(vnd(max_value), font=FONT, weight=BOLD)
    s = min(1.0, 3.9 / probe.width)
    t = Text(vnd(tracker.get_value()), font=FONT, weight=BOLD, color=color).scale(s).move_to(pos)
    t.add_updater(lambda m: m.become(
        Text(vnd(tracker.get_value()), font=FONT, weight=BOLD, color=color).scale(s).move_to(pos)))
    return t


def chip(text, col):
    t = Text(text, font=FONT, weight=BOLD, color=col).scale(0.62)
    box = RoundedRectangle(corner_radius=0.18, width=t.width + 0.5, height=t.height + 0.35).set_stroke(col, 2.5).set_fill(BG_CARD, 0.95)
    return VGroup(box, t)


class LaiKepVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_laikep")
    SEGMENTS = SEGMENTS
    TOPIC = "CẤP SỐ NHÂN"

    def construct(self):
        self.camera.background_color = BG
        self.play_intro()
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)

        self.beat_hook()
        self.beat_build()
        self.beat_payoff()
        self.beat_cta()
        self.brand_stinger()
        self.wait(0.3)

    # ---------- 1. HOOK ----------
    def beat_hook(self):
        one = Text("1đ", font=FONT, weight=BOLD, color=ACCENT).scale(2.4)
        l1 = Text("× 2  mỗi ngày", font=FONT, color=MUTED).scale(0.9)
        l2 = Text("× 30 ngày", font=FONT, color=MUTED).scale(0.9)
        q = Text("=  ?", font=FONT, weight=BOLD, color=WHITE).scale(2.0)
        stack = VGroup(one, l1, l2, q).arrange(DOWN, buff=0.45).move_to([0, 0.4, 0])
        with self.voice("01_hook") as D:
            kar = self.make_karaoke(SEGMENTS["01_hook"], D, self.beat_t0)
            self.add(kar)
            self.play(Write(one), run_time=0.7)
            self.play(FadeIn(l1, shift=UP * 0.15), FadeIn(l2, shift=UP * 0.15), run_time=0.7)
            self.play(Write(q), Indicate(q, color=ACCENT, scale_factor=1.2), run_time=0.9)
            self._b1 = stack
        self.end_karaoke(kar)
        self.play(FadeOut(self._b1), run_time=0.35)

    # ---------- 2. BUILD: cấp số nhân ----------
    def beat_build(self):
        badge = Text("mỗi bước  × 2", font=FONT, weight=BOLD, color=ACCENT).scale(0.75).move_to([0, 2.7, 0])
        seq = VGroup(*[Text(v, font=FONT, weight=BOLD, color=GROW).scale(0.95) for v in ["1", "2", "4", "8", "16", "32"]])
        seq.arrange(RIGHT, buff=0.32)
        fit_w(seq, 4.2)
        seq.move_to([0, 1.8, 0])

        axes = Axes(x_range=[0, 6, 1], y_range=[0, 40, 10], x_length=3.7, y_length=2.6,
                    axis_config={"color": "#3A4254", "include_tip": True, "stroke_width": 3}).move_to([0, -0.7, 0])
        curve = axes.plot(lambda x: 2 ** x, x_range=[0, 5.2], stroke_width=8).set_color_by_gradient(GROW, "#A7F3D0")
        dot = Dot(color=GROW, radius=0.12).move_to(axes.c2p(0, 1))
        lbl = Text("dựng đứng!", font=FONT, weight=BOLD, color=GROW).scale(0.65).move_to([0.1, 0.9, 0])

        with self.voice("02_build") as D:
            kar = self.make_karaoke(SEGMENTS["02_build"], D, self.beat_t0)
            self.add(kar)
            self.play(FadeIn(badge), run_time=0.5)
            for m in seq:
                self.play(FadeIn(m, scale=0.6), run_time=0.2)
            self.play(Create(axes), run_time=0.8)
            self.play(Create(curve), MoveAlongPath(dot, curve), FadeIn(lbl), run_time=2.2)
            self._b2 = VGroup(badge, seq, axes, curve, dot, lbl)
        self.end_karaoke(kar)
        self.play(FadeOut(self._b2), run_time=0.35)

    # ---------- 3. PAYOFF: con số sốc + lãi kép ----------
    def beat_payoff(self):
        with self.voice("03_payoff") as D:
            kar = self.make_karaoke(SEGMENTS["03_payoff"], D, self.beat_t0)
            self.add(kar)
            # ngày 30 → hơn 536 triệu
            tr = ValueTracker(0)
            cnt = money_counter(tr, [0, 1.5, 0], GROW, 536_870_912)
            day = Text("NGÀY 30", font=FONT, weight=BOLD, color=MUTED).scale(0.6).move_to([0, 2.4, 0])
            self.add(cnt)
            self.play(FadeIn(day), tr.animate.set_value(536_870_912), run_time=1.6, rate_func=rate_functions.ease_out_cubic)
            cnt.clear_updaters()
            self.play(FadeOut(cnt, day), run_time=0.3)
            # tổng cả tháng → hơn 1 tỉ
            tr2 = ValueTracker(0)
            total = money_counter(tr2, [0, 1.5, 0], ACCENT, 1_073_741_823)
            tlbl = Text("TỔNG 30 NGÀY · từ 1đ", font=FONT, weight=BOLD, color=ACCENT).scale(0.6).move_to([0, 2.4, 0])
            self.add(total)
            self.play(FadeIn(tlbl), tr2.animate.set_value(1_073_741_823), run_time=1.6, rate_func=rate_functions.ease_out_cubic)
            total.clear_updaters()
            self.play(Flash(total.get_center(), color=ACCENT, line_length=0.5, num_lines=20),
                      Indicate(total, color=ACCENT, scale_factor=1.12), run_time=0.7)
            # lãi kép: hai chiều
            save = chip("TIẾT KIỆM   ↑ ×7", GROW)
            debt = chip("NỢ để lâu   ↑ phình to", DEBT)
            chips = VGroup(save, debt).arrange(DOWN, buff=0.35).move_to([0, -1.1, 0])
            kep = Text("= LÃI KÉP", font=FONT, weight=BOLD, color=WHITE).scale(0.7).move_to([0, 0.2, 0])
            self.play(FadeIn(kep), run_time=0.4)
            self.play(FadeIn(chips, shift=UP * 0.2), run_time=0.7)
            self._b3 = VGroup(total, tlbl, kep, chips)
        self.end_karaoke(kar)
        self.play(FadeOut(self._b3), run_time=0.35)

    # ---------- 4. CTA ----------
    def beat_cta(self):
        lesson = fit_w(Text("Lặp lại  >  Bắt đầu lớn", font=FONT, weight=BOLD, color=ACCENT).scale(1.1), 4.2).move_to([0, 1.5, 0])
        sub_btn = RoundedRectangle(corner_radius=0.22, width=3.2, height=0.95).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("ĐĂNG KÝ", font=FONT, weight=BOLD, color=WHITE).scale(0.72).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.2, 0])
        with self.voice("04_cta", gap=0.4) as D:
            kar = self.make_karaoke(SEGMENTS["04_cta"], D, self.beat_t0)
            self.add(kar)
            self.play(Write(lesson), run_time=0.8)
            self.play(Indicate(lesson, color=GROW, scale_factor=1.1), run_time=0.5)
            self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b4 = VGroup(lesson, sub)
        self.end_karaoke(kar)
        self.play(FadeOut(self._b4), run_time=0.4)
