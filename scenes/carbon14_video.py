"""
"Định tuổi xác ướp bằng Carbon-14" — phóng xạ, chu kỳ bán rã, định luật phân rã.
Vật lý 12 · SHORT DỌC 9:16 · ~1 phút 50 · KHÔNG intro.

Dùng bộ cỡ chữ chuẩn SZ_* (brand.py) + CANH NHỊP self.cue(): mỗi bước hiện hình được
rải trải đều theo lời đọc của cả đoạn (không dồn ở đầu beat).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_carbon14.py
Căn chỉnh:   .venv/bin/python scenes/align_narration.py output/narration_carbon14
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/carbon14_video.py Carbon14Video
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_carbon14 import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CARBON = "#34D399"   # xanh — C-14 còn lại / sự sống
GONE = "#3A4254"     # xám — C-14 đã phân rã


def pdot(color, r=0.11):
    return Dot(radius=r).set_fill(color, 1).set_stroke(width=0)


def carbon_grid(n_full, n_decay, color_full=CARBON, color_gone=GONE, cols=5, r=0.13, buff=0.16):
    """Lưới 5×4 = 20 chấm; n_full chấm đầu là C-14 còn lại, phần còn lại đã phân rã."""
    dots = []
    for i in range(20):
        c = color_full if i < n_full else color_gone
        dots.append(pdot(c, r))
    g = VGroup(*dots).arrange_in_grid(rows=4, cols=cols, buff=buff)
    return g


class Carbon14Video(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_carbon14")
    SEGMENTS = SEGMENTS
    TOPIC = "VẬT LÝ 12"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_dongho()
        self.beat_phanra()
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

    # 1. HOOK — di vật cổ + dấu hỏi tuổi ------------------------------
    def beat_hook(self):
        # "di vật": mảnh gỗ / xương cổ — gợi bằng khối nâu xám có vân
        relic = RoundedRectangle(corner_radius=0.18, width=1.7, height=1.05).set_fill("#8A6B4A", 1).set_stroke("#5E4730", 3).move_to([0, 2.0, 0])
        grain = VGroup(
            Line([-0.6, 0.2, 0], [0.6, 0.18, 0]).set_stroke("#5E4730", 2),
            Line([-0.6, -0.05, 0], [0.6, -0.02, 0]).set_stroke("#5E4730", 2),
            Line([-0.6, -0.28, 0], [0.6, -0.3, 0]).set_stroke("#5E4730", 2),
        ).move_to(relic)
        relic_g = VGroup(relic, grain)
        cap = Text("mảnh gỗ / xương cổ", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(relic_g, DOWN, buff=0.22)
        q = fit_w(Text("Bao nhiêu tuổi?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, -0.2, 0])
        clock = fit_w(Text("Đồng hồ phóng xạ tích tắc", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, -1.4, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(relic_g, shift=DOWN * 0.2), run_time=0.7)
            self.cue(D * 0.2); self.play(FadeIn(cap), run_time=0.5)
            self.cue(D * 0.45); self.play(Write(q), run_time=0.8)
            self.cue(D * 0.72); self.play(FadeIn(clock, shift=UP * 0.2), Flash(clock.get_center(), color=ACCENT, line_length=0.3, num_lines=14), run_time=1.0)
            self._b = VGroup(relic_g, cap, q, clock)
        self._clear()

    # 2. ĐỒNG HỒ — sống thì nạp đều, chết thì dừng nạp ----------------
    def beat_dongho(self):
        title = fit_w(Text("Khi còn SỐNG", font=FONT, weight=BOLD, color=CARBON).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        # cơ thể (vòng tròn) hấp thụ C-14 từ không khí (mũi tên vào)
        body = Circle(radius=0.7, color=CARBON, stroke_width=4).set_fill(CARBON, 0.12).move_to([0, 1.2, 0])
        c14 = Text("C-14", font=FONT, weight=BOLD, color=CARBON).scale(SZ_LABEL).move_to(body)
        arrs = VGroup(
            Arrow([-1.7, 1.9, 0], [-0.75, 1.4, 0], color=CARBON, stroke_width=3, buff=0.05),
            Arrow([1.7, 1.9, 0], [0.75, 1.4, 0], color=CARBON, stroke_width=3, buff=0.05),
            Arrow([-1.7, 0.5, 0], [-0.75, 1.0, 0], color=CARBON, stroke_width=3, buff=0.05),
        )
        air = Text("nạp đều từ không khí", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(body, DOWN, buff=0.3)
        # ĐẾN KHI CHẾT
        dead = fit_w(Text("Khi CHẾT → ngừng nạp", font=FONT, weight=BOLD, color=DEBT).scale(SZ_TITLE), CW).move_to([0, -1.0, 0])
        tick = fit_w(Text("Đồng hồ bắt đầu chạy", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, -1.7, 0])
        with self.voice("02_dongho") as D:
            self._kara("02_dongho", D)
            self.cue(D * 0.0); self.play(Write(title), Create(body), FadeIn(c14), run_time=0.8)
            self.cue(D * 0.28); self.play(LaggedStart(*[GrowArrow(a) for a in arrs], lag_ratio=0.2), FadeIn(air), run_time=1.0)
            self.cue(D * 0.62); self.play(FadeIn(dead, shift=UP * 0.2), run_time=0.8)
            self.cue(D * 0.82); self.play(FadeIn(tick), Indicate(tick, color=ACCENT, scale_factor=1.1), run_time=0.7)
            self._b = VGroup(title, body, c14, arrs, air, dead, tick)
        self._clear()

    # 3. PHÂN RÃ — mỗi 5730 năm còn một nửa + công thức ---------------
    def beat_phanra(self):
        title = fit_w(Text("Cứ 5730 năm → còn một nửa", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        # ba thanh giảm dần: 100% → 50% → 25%
        def bar(frac, label, color):
            full = Rectangle(width=2.6, height=0.5).set_stroke(MUTED, 1.5)
            fill = Rectangle(width=2.6 * frac, height=0.5).set_fill(color, 1).set_stroke(width=0)
            fill.align_to(full, LEFT)
            lab = Text(label, font=FONT, weight=BOLD, color=color).scale(SZ_LABEL)
            grp = VGroup(full, fill)
            return grp, lab
        b0, l0 = bar(1.0, "100%", CARBON)
        b1, l1 = bar(0.5, "50%", CARBON)
        b2, l2 = bar(0.25, "25%", CARBON)
        rows = VGroup(
            VGroup(b0, l0).arrange(RIGHT, buff=0.3),
            VGroup(b1, l1).arrange(RIGHT, buff=0.3),
            VGroup(b2, l2).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to([0, 0.9, 0])
        ar1 = Text("÷2", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL).next_to(rows[0], RIGHT, buff=0.05).shift(DOWN * 0.4 + RIGHT * 0.15)
        ar2 = Text("÷2", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL).next_to(rows[1], RIGHT, buff=0.05).shift(DOWN * 0.4 + RIGHT * 0.15)
        # công thức (Text để tránh tofu, không dùng MathTex)
        formula = fit_w(Text("N = N0 × (1/2)^(t/T)", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, -1.3, 0])
        sub = Text("T = chu kỳ bán rã = 5730 năm", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(formula, DOWN, buff=0.2)
        with self.voice("03_phanra") as D:
            self._kara("03_phanra", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.7)
            self.cue(D * 0.22); self.play(FadeIn(rows[0]), run_time=0.6)
            self.cue(D * 0.36); self.play(FadeIn(rows[1], shift=DOWN * 0.1), FadeIn(ar1), run_time=0.6)
            self.cue(D * 0.5); self.play(FadeIn(rows[2], shift=DOWN * 0.1), FadeIn(ar2), run_time=0.6)
            self.cue(D * 0.7); self.play(Write(formula), run_time=0.8)
            self.cue(D * 0.88); self.play(FadeIn(sub), run_time=0.5)
            self._b = VGroup(title, rows, ar1, ar2, formula, sub)
        self._clear()

    # 4. RA CON SỐ — còn 25% → 2 chu kỳ → 11.460 năm ------------------
    def beat_conso(self):
        title = fit_w(Text("Đo mẫu: chỉ còn 1/4", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        grid = carbon_grid(5, 15).move_to([0, 1.4, 0])
        glbl = Text("5 / 20 còn lại  =  25%", font=FONT, weight=BOLD, color=CARBON).scale(SZ_LABEL).next_to(grid, DOWN, buff=0.25)
        steps = VGroup(
            Text("1/2 rồi lại 1/2  →  2 chu kỳ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL),
            Text("2 × 5730", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY),
        ).arrange(DOWN, buff=0.25).move_to([0, -0.55, 0])
        for s in steps:
            fit_w(s, CW)
        ans = fit_w(Text("≈ 11.460 năm", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO), CW).move_to([0, -1.7, 0])
        with self.voice("04_conso") as D:
            self._kara("04_conso", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.18); self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in grid], lag_ratio=0.04), run_time=1.0)
            self.cue(D * 0.42); self.play(FadeIn(glbl), run_time=0.5)
            self.cue(D * 0.58); self.play(FadeIn(steps, shift=UP * 0.15), run_time=0.8)
            self.cue(D * 0.8); self.play(Write(ans), Flash(ans.get_center(), color=ACCENT, line_length=0.4, num_lines=18), run_time=1.1)
            self._b = VGroup(title, grid, glbl, steps, ans)
        self._clear()

    # 5. Ý NGHĨA — đồ thị phân rã + ứng dụng --------------------------
    def beat_ynghia(self):
        axes = Axes(
            x_range=[0, 3, 1], y_range=[0, 1, 0.5],
            x_length=2.9, y_length=2.0,
            axis_config={"include_tip": True, "stroke_color": MUTED, "stroke_width": 2},
            tips=True,
        ).move_to([0, 1.6, 0])
        curve = axes.plot(lambda t: 0.5 ** t, x_range=[0, 3], color=CARBON, stroke_width=5)
        xlab = Text("số chu kỳ (t/T)", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(axes, DOWN, buff=0.12)
        ylab = Text("C-14 còn lại", font=FONT, color=MUTED).scale(SZ_SMALL).rotate(PI / 2).next_to(axes, LEFT, buff=0.05)
        bullets = VGroup(
            Text("• Cọc gỗ Bạch Đằng, xác ướp", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("• Lật tẩy tranh giả, nước ngầm", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("• Pháp y, khảo cổ, địa chất", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([0, -1.4, 0])
        for b in bullets:
            fit_w(b, CW)
        bcues = [0.5, 0.66, 0.8]
        with self.voice("05_ynghia") as D:
            self._kara("05_ynghia", D)
            self.cue(D * 0.0); self.play(Create(axes), FadeIn(xlab), FadeIn(ylab), run_time=0.8)
            self.cue(D * 0.22); self.play(Create(curve), run_time=1.0)
            for b, f in zip(bullets, bcues):
                self.cue(D * f); self.play(FadeIn(b, shift=RIGHT * 0.2), run_time=0.55)
            self._b = VGroup(axes, curve, xlab, ylab, bullets)
        self._clear()

    # 6. CTA -----------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Thời gian không xoá hết", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.7, 0])
        l2 = fit_w(Text("chỉ giảm một nửa, rồi một nửa", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, 1.0, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.5, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("ĐĂNG KÝ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.3, 0])
        with self.voice("06_cta", gap=0.4) as D:
            self._kara("06_cta", D)
            self.cue(D * 0.0); self.play(Write(l1), run_time=0.7)
            self.cue(D * 0.3); self.play(FadeIn(l2, shift=UP * 0.15), Indicate(l2, color=GROW, scale_factor=1.06), run_time=0.8)
            self.cue(D * 0.62); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, sub)
        self._clear()
