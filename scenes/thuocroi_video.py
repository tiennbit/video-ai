"""
"Bắt cây thước rơi: bài test phản xạ chỉ cần một công thức" — rơi tự do (h = ½gt²).
Vật lý 10 · SHORT DỌC 9:16 · ~1 phút 50 · KHÔNG intro.

Dùng bộ cỡ chữ chuẩn SZ_* (brand.py) + CANH NHỊP self.cue(): mỗi bước hiện hình được
rải trải đều theo lời đọc của cả đoạn (không dồn ở đầu beat).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_thuocroi.py
Căn chỉnh:   .venv/bin/python scenes/align_narration.py output/narration_thuocroi
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/thuocroi_video.py ThuocRoiVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_thuocroi import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WOOD = "#E2B07A"      # màu gỗ cây thước
WOOD_D = "#B9854F"    # viền thước


def ruler(height=3.4, width=0.5, n_ticks=10):
    """Cây thước thẳng đứng có vạch chia. Vạch 0 ở ĐỈNH, số tăng dần xuống dưới."""
    body = Rectangle(width=width, height=height).set_fill(WOOD, 1).set_stroke(WOOD_D, 3)
    top = body.get_top()[1]
    ticks = VGroup()
    for i in range(n_ticks + 1):
        y = top - height * (i / n_ticks)
        ln = Line([-width / 2, y, 0], [-width / 2 + width * 0.42, y, 0]).set_stroke(WOOD_D, 2)
        ticks.add(ln)
    return VGroup(body, ticks)


class ThuocRoiVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_thuocroi")
    SEGMENTS = SEGMENTS
    TOPIC = "VẬT LÝ 10"

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

    # 1. HOOK — thước rơi, bàn tay bắt ở vạch 20cm, kết quả 0,2s -------
    def beat_hook(self):
        rul = ruler(3.2, 0.5, 10).move_to([-0.55, 1.0, 0])
        # vạch 20cm: 2/10 từ đỉnh thước
        top = rul.get_top()[1]
        y20 = top - 3.2 * 0.2
        # ngón tay = 2 chấm kẹp quanh vạch 20
        grip = VGroup(
            Dot(radius=0.13).set_fill(ACCENT, 1).set_stroke(width=0).move_to([-0.95, y20, 0]),
            Dot(radius=0.13).set_fill(ACCENT, 1).set_stroke(width=0).move_to([-0.18, y20, 0]),
        )
        lbl20 = Text("vạch 20 cm", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL).next_to([0.3, y20, 0], RIGHT, buff=0.2)
        catch = fit_w(Text("Bắt được cây thước rơi", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -1.0, 0])
        res = Text("phản xạ = 0,2 giây", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO)
        res = fit_w(res, CW).move_to([0, -1.85, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(rul, shift=DOWN * 0.3), run_time=0.7)
            self.cue(D * 0.3); self.play(FadeIn(grip, scale=0.5), Write(lbl20), run_time=0.8)
            self.cue(D * 0.5); self.play(FadeIn(catch, shift=UP * 0.2), run_time=0.7)
            self.cue(D * 0.7); self.play(Write(res), Flash(res.get_center(), color=ACCENT, line_length=0.35, num_lines=16), run_time=1.0)
            self._b = VGroup(rul, grip, lbl20, catch, res)
        self._clear()

    # 2. VẤN ĐỀ — đoạn rơi là dấu vết của thời gian -------------------
    def beat_vande(self):
        q = fit_w(Text("Sao thước lại đo được thời gian?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        rul = ruler(2.4, 0.42, 8).move_to([-0.7, 0.1, 0])
        top = rul.get_top()[1]
        bot = rul.get_bottom()[1]
        a_drop = Arrow([0.05, top, 0], [0.05, bot + 0.1, 0], color=DEBT, stroke_width=5, buff=0.05)
        brace = Text("đoạn rơi", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL).next_to([0.35, (top + bot) / 2, 0], RIGHT, buff=0.25)
        note = fit_w(Text("= dấu vết của thời gian phản ứng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, -1.7, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.0); self.play(Write(q), run_time=0.9)
            self.cue(D * 0.3); self.play(FadeIn(rul, shift=DOWN * 0.2), run_time=0.7)
            self.cue(D * 0.55); self.play(GrowArrow(a_drop), FadeIn(brace), run_time=0.8)
            self.cue(D * 0.78); self.play(FadeIn(note, shift=UP * 0.15), run_time=0.7)
            self._b = VGroup(q, rul, a_drop, brace, note)
        self._clear()

    # 3. MÔ HÌNH — rơi tự do, công thức h = ½ g t² -------------------
    def beat_mohinh(self):
        title = fit_w(Text("Thước rơi TỰ DO", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        obj = Dot(radius=0.16).set_fill(WOOD, 1).set_stroke(WOOD_D, 2).move_to([-1.3, 1.7, 0])
        gtrail = VGroup(*[Dot(radius=0.06).set_fill(MUTED, 1).set_stroke(width=0).move_to([-1.3, 1.7 - 0.45 * (k ** 1.3), 0]) for k in range(1, 5)])
        garr = Arrow([-1.3, 1.6, 0], [-1.3, -0.1, 0], color=DEBT, stroke_width=4, buff=0.05)
        glbl = Text("g", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY).next_to(garr, LEFT, buff=0.12)
        formula = fit_w(Text("h = ½ · g · t²", font=FONT, weight=BOLD, color=ACCENT).scale(0.62), CW).move_to([0.55, 0.2, 0])
        gval = fit_w(Text("g ≈ 9,8 m/s²", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -1.1, 0])
        more = fit_w(Text("rơi càng dài → phản ứng càng chậm", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), CW).move_to([0, -1.75, 0])
        with self.voice("03_mohinh") as D:
            self._kara("03_mohinh", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.7)
            self.cue(D * 0.2); self.play(FadeIn(obj), GrowArrow(garr), Write(glbl), run_time=0.8)
            self.cue(D * 0.38); self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in gtrail], lag_ratio=0.2), run_time=0.9)
            self.cue(D * 0.55); self.play(Write(formula), run_time=1.0)
            self.cue(D * 0.74); self.play(FadeIn(gval), run_time=0.5)
            self.cue(D * 0.86); self.play(FadeIn(more, shift=UP * 0.15), run_time=0.6)
            self._b = VGroup(title, obj, gtrail, garr, glbl, formula, gval, more)
        self._clear()

    # 4. RA CON SỐ — giải ngược t = căn(2h/g) ≈ 0,20 s ---------------
    def beat_conso(self):
        title = fit_w(Text("Giải ngược ra thời gian", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        f1 = fit_w(Text("t = √(2h / g)", font=FONT, weight=BOLD, color=WHITE).scale(0.6), CW).move_to([0, 1.5, 0])
        sub = fit_w(Text("h = 20 cm = 0,2 m", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.5, 0])
        f2 = fit_w(Text("t = √(2 × 0,2 / 9,8)", font=FONT, weight=BOLD, color=ACCENT).scale(0.55), CW).move_to([0, -0.35, 0])
        res = Text("t ≈ 0,20 giây", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO)
        res = fit_w(res, CW).move_to([0, -1.6, 0])
        box = SurroundingRectangle(res, color=ACCENT, buff=0.2, corner_radius=0.12).set_stroke(width=3)
        with self.voice("04_conso") as D:
            self._kara("04_conso", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.22); self.play(Write(f1), run_time=0.9)
            self.cue(D * 0.45); self.play(FadeIn(sub), run_time=0.5)
            self.cue(D * 0.6); self.play(TransformFromCopy(f1, f2), run_time=0.9)
            self.cue(D * 0.82); self.play(Write(res), Create(box), Flash(res.get_center(), color=ACCENT, line_length=0.35, num_lines=16), run_time=1.0)
            self._b = VGroup(title, f1, sub, f2, res, box)
        self._clear()

    # 5. Ý NGHĨA — não-tay 0,2s; ứng dụng thực ------------------------
    def beat_ynghia(self):
        big = fit_w(Text("Não → tay mất 0,2 giây", font=FONT, weight=BOLD, color=ACCENT), CW).move_to([0, 2.5, 0])
        rule = fit_w(Text("bắt ở vạch thấp hơn → phản xạ nhanh hơn", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, 1.75, 0])
        bullets = VGroup(
            Text("• Đo độ tỉnh táo tài xế", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("• Kiểm tra phản xạ vận động viên", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("• Thắng thua trong game tốc độ", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("  ẩn sau công thức rơi tự do", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL),
        ).arrange(DOWN, buff=0.34, aligned_edge=LEFT).move_to([0, -0.3, 0])
        for b in bullets:
            fit_w(b, CW)
        bcues = [0.32, 0.5, 0.66, 0.82]
        with self.voice("05_ynghia") as D:
            self._kara("05_ynghia", D)
            self.cue(D * 0.0); self.play(Write(big), run_time=0.9)
            self.cue(D * 0.2); self.play(FadeIn(rule), run_time=0.5)
            for b, f in zip(bullets, bcues):
                self.cue(D * f); self.play(FadeIn(b, shift=RIGHT * 0.2), run_time=0.55)
            self._b = VGroup(big, rule, bullets)
        self._clear()

    # 6. CTA ----------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Cầm thước lên và thử ngay", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.7, 0])
        l2 = fit_w(Text("Thế giới chạy bằng công thức đơn giản", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.5, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("ĐĂNG KÝ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.3, 0])
        with self.voice("06_cta", gap=0.4) as D:
            self._kara("06_cta", D)
            self.cue(D * 0.0); self.play(Write(l1), run_time=0.7)
            self.cue(D * 0.35); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.06), run_time=0.8)
            self.cue(D * 0.65); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, sub)
        self._clear()
