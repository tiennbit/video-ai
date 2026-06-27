"""
"Xét nghiệm dương tính 99% — bạn có thật mắc bệnh?" — nghịch lý dương tính giả (Bayes).
Toán 11 · SHORT DỌC 9:16 · ~1.6 phút · KHÔNG intro.

Dùng bộ cỡ chữ chuẩn SZ_* (brand.py) + CANH NHỊP self.cue(): mỗi bước hiện hình được
rải trải đều theo lời đọc của cả đoạn (không dồn ở đầu beat).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_xetnghiem.py
Căn chỉnh:   .venv/bin/python scenes/align_narration.py output/narration_xetnghiem
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/xetnghiem_video.py XetNghiemVideo
"""
import os

from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_xetnghiem import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ORANGE = "#FB923C"   # dương tính GIẢ


def pdot(color, r=0.11):
    return Dot(radius=r).set_fill(color, 1).set_stroke(width=0)


def test_strip(positive=True, scale=1.0):
    body = RoundedRectangle(corner_radius=0.1, width=0.55, height=1.25).set_fill("#E8ECF2", 1).set_stroke("#7A8699", 2)
    win = RoundedRectangle(corner_radius=0.05, width=0.36, height=0.8).set_fill("#FFFFFF", 1).set_stroke(width=0).move_to(body).shift(UP * 0.08)
    cline = Line([-0.14, 0, 0], [0.14, 0, 0]).set_stroke(DEBT, 5).move_to(win.get_center() + UP * 0.18)
    g = VGroup(body, win, cline)
    if positive:
        tline = Line([-0.14, 0, 0], [0.14, 0, 0]).set_stroke(DEBT, 5).move_to(win.get_center() + DOWN * 0.05)
        g.add(tline)
    return g.scale(scale)


def dots_row(n, color, r=0.11, buff=0.1):
    return VGroup(*[pdot(color, r) for _ in range(n)]).arrange(RIGHT, buff=buff)


class XetNghiemVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_xetnghiem")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 11 · XÁC SUẤT"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_vande()
        self.beat_danso()
        self.beat_test()
        self.beat_dem()
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
        strip = test_strip(True, 1.15).move_to([0, 2.0, 0])
        pos = Text("DƯƠNG TÍNH", font=FONT, weight=BOLD, color=DEBT).scale(SZ_TITLE).next_to(strip, DOWN, buff=0.3)
        acc = Text("que thử chính xác 99%", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(pos, DOWN, buff=0.15)
        guess = fit_w(Text("Mắc bệnh thật? Ai cũng đoán 99%", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -0.85, 0])
        real = Text("Thật ra:  ~9%", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO).move_to([0, -1.7, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(strip, shift=DOWN * 0.2), run_time=0.7)
            self.cue(D * 0.22); self.play(Write(pos), FadeIn(acc), run_time=0.8)
            self.cue(D * 0.48); self.play(FadeIn(guess, shift=UP * 0.2), run_time=0.8)
            self.cue(D * 0.64); self.play(Write(real), Flash(real.get_center(), color=ACCENT, line_length=0.35, num_lines=16), run_time=1.0)
            self._b = VGroup(strip, pos, acc, guess, real)
        self._clear()

    # 2. VẤN ĐỀ --------------------------------------------------------
    def beat_vande(self):
        secret = Text("Bí mật:", font=FONT, color=MUTED).scale(SZ_BODY).move_to([0, 1.7, 0])
        rare = Text("BỆNH HIẾM", font=FONT, weight=BOLD, color=DEBT).scale(0.72).next_to(secret, DOWN, buff=0.2)
        rule = VGroup(
            Text("Đừng nghĩ bằng  %", font=FONT, weight=BOLD, color=MUTED).scale(SZ_BODY),
            Text("→  Đếm bằng NGƯỜI", font=FONT, weight=BOLD, color=GROW).scale(SZ_TITLE),
        ).arrange(DOWN, buff=0.3).move_to([0, -0.7, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.0); self.play(FadeIn(secret), Write(rare), run_time=0.9)
            self.cue(D * 0.28); self.play(Indicate(rare, color=DEBT, scale_factor=1.12), run_time=0.6)
            self.cue(D * 0.52); self.play(FadeIn(rule, shift=UP * 0.2), run_time=0.9)
            self._b = VGroup(secret, rare, rule)
        self._clear()

    # 3. DÂN SỐ: 1000 -> 1 bệnh / 999 khoẻ ----------------------------
    def beat_danso(self):
        top = Text("1000 người", font=FONT, weight=BOLD, color=WHITE).scale(0.62).move_to([0, 2.3, 0])
        left = VGroup(pdot(DEBT, 0.22), Text("1 BỆNH", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL)).arrange(DOWN, buff=0.18).move_to([-1.1, 0.4, 0])
        right = VGroup(pdot(MUTED, 0.22), Text("999 KHOẺ", font=FONT, weight=BOLD, color=MUTED).scale(SZ_LABEL)).arrange(DOWN, buff=0.18).move_to([1.1, 0.4, 0])
        aL = Arrow(top.get_bottom(), left.get_top(), color="#3A4254", stroke_width=3, buff=0.18)
        aR = Arrow(top.get_bottom(), right.get_top(), color="#3A4254", stroke_width=3, buff=0.18)
        note = Text("(bệnh chỉ gặp 1 / 1000)", font=FONT, color=MUTED).scale(SZ_SMALL).move_to([0, -1.3, 0])
        with self.voice("03_danso") as D:
            self._kara("03_danso", D)
            self.cue(D * 0.0); self.play(Write(top), run_time=0.7)
            self.cue(D * 0.25); self.play(FadeIn(note), run_time=0.5)
            self.cue(D * 0.45); self.play(GrowArrow(aL), GrowArrow(aR), run_time=0.6)
            self.cue(D * 0.62); self.play(FadeIn(left, scale=0.6), FadeIn(right, scale=0.6), run_time=0.8)
            self._b = VGroup(top, left, right, aL, aR, note)
        self._clear()

    # 4. TEST: dương tính thật vs giả ---------------------------------
    def beat_test(self):
        title = fit_w(Text("Cho tất cả đi xét nghiệm", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        sick = fit_w(VGroup(pdot(DEBT, 0.15), Text("1 bệnh → DƯƠNG TÍNH (đúng)", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL)).arrange(RIGHT, buff=0.18), CW).move_to([0, 1.5, 0])
        hl = fit_w(Text("999 khoẻ · xét nghiệm sai 1%", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.7, 0])
        ten = dots_row(10, ORANGE, r=0.11).move_to([0, 0.05, 0])
        tenlbl = Text("≈ 10 DƯƠNG TÍNH GIẢ", font=FONT, weight=BOLD, color=ORANGE).scale(SZ_BODY).next_to(ten, DOWN, buff=0.2)
        neg = Text("(989 người còn lại: âm tính)", font=FONT, color=MUTED).scale(SZ_SMALL).move_to([0, -1.35, 0])
        with self.voice("04_test") as D:
            self._kara("04_test", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.7)
            self.cue(D * 0.2); self.play(FadeIn(sick, shift=RIGHT * 0.2), run_time=0.8)
            self.cue(D * 0.4); self.play(FadeIn(hl, shift=UP * 0.15), run_time=0.7)
            self.cue(D * 0.58); self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in ten], lag_ratio=0.12), FadeIn(tenlbl), run_time=1.4)
            self.cue(D * 0.85); self.play(FadeIn(neg), run_time=0.5)
            self._b = VGroup(title, sick, hl, ten, tenlbl, neg)
        self._clear()

    # 5. ĐẾM -> 1/11 ≈ 9% (payoff) ------------------------------------
    def beat_dem(self):
        title = fit_w(Text("Tất cả ca DƯƠNG TÍNH:", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.4, 0])
        red = pdot(DEBT, 0.12)
        row = VGroup(red, *[pdot(ORANGE, 0.12) for _ in range(10)]).arrange(RIGHT, buff=0.08).move_to([0, 1.3, 0])
        count = Text("= 11 người", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).next_to(row, DOWN, buff=0.28)
        ring = Circle(radius=0.2, color=ACCENT, stroke_width=5).move_to(red)
        rlbl = Text("chỉ 1 thật sự bệnh", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL).next_to(count, DOWN, buff=0.3)
        frac = Text("1 / 11  ≈  9%", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO).move_to([0, -1.4, 0])
        with self.voice("05_dem") as D:
            self._kara("05_dem", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.2); self.play(FadeIn(row, shift=UP * 0.15), run_time=0.8)
            self.cue(D * 0.36); self.play(FadeIn(count), run_time=0.5)
            self.cue(D * 0.5); self.play(Create(ring), FadeIn(rlbl), run_time=0.8)
            self.cue(D * 0.68); self.play(Write(frac), Flash(frac.get_center(), color=ACCENT, line_length=0.4, num_lines=18), run_time=1.1)
            self._b = VGroup(title, row, count, ring, rlbl, frac)
        self._clear()

    # 6. Ý NGHĨA -------------------------------------------------------
    def beat_ynghia(self):
        big = fit_w(Text("NGHỊCH LÝ DƯƠNG TÍNH GIẢ", font=FONT, weight=BOLD, color=DEBT), CW).move_to([0, 2.3, 0])
        bullets = VGroup(
            Text("• Bệnh càng hiếm → càng nhiều báo giả", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("• Bác sĩ luôn cho xét nghiệm lại", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("• Đây là ĐỊNH LÝ BAYES", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL),
            Text("  (lọc spam, chẩn đoán AI...)", font=FONT, color=MUTED).scale(SZ_SMALL),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to([0, -0.2, 0])
        for b in bullets:
            fit_w(b, CW)
        bcues = [0.25, 0.45, 0.62, 0.78]
        with self.voice("06_ynghia") as D:
            self._kara("06_ynghia", D)
            self.cue(D * 0.0); self.play(Write(big), run_time=0.9)
            for b, f in zip(bullets, bcues):
                self.cue(D * f); self.play(FadeIn(b, shift=RIGHT * 0.2), run_time=0.55)
            self._b = VGroup(big, bullets)
        self._clear()

    # 7. CTA -----------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Đừng tin 1 con số đơn lẻ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.7, 0])
        l2 = fit_w(Text("Hãy hỏi: trên nền BAO NHIÊU?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.5, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("ĐĂNG KÝ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.3, 0])
        with self.voice("07_cta", gap=0.4) as D:
            self._kara("07_cta", D)
            self.cue(D * 0.0); self.play(Write(l1), run_time=0.7)
            self.cue(D * 0.3); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.08), run_time=0.8)
            self.cue(D * 0.6); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, sub)
        self._clear()
