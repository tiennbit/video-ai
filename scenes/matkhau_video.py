"""
"Mật khẩu của bạn bị bẻ trong bao lâu?" — quy tắc đếm / tổ hợp (95^l).
Toán 11 · SHORT DỌC 9:16 · ~1.8 phút · KHÔNG intro.

Dùng bộ cỡ chữ chuẩn SZ_* (brand.py) + CANH NHỊP self.cue(): mỗi bước hiện hình được
rải trải đều theo lời đọc của cả đoạn (không dồn ở đầu beat).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_matkhau.py
Căn chỉnh:   .venv/bin/python scenes/align_narration.py output/narration_matkhau
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/matkhau_video.py MatKhauVideo
"""
import os

from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_matkhau import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ORANGE = "#FB923C"


def key_cell(ch, color=WHITE, fill=BG_CARD, w=0.5, h=0.62):
    box = RoundedRectangle(corner_radius=0.08, width=w, height=h).set_fill(fill, 1).set_stroke("#3A4254", 2)
    t = Text(ch, font=FONT, weight=BOLD, color=color).scale(SZ_LABEL).move_to(box)
    return VGroup(box, t)


def password_row(chars, color=WHITE, fill=BG_CARD, buff=0.1):
    return VGroup(*[key_cell(c, color, fill) for c in chars]).arrange(RIGHT, buff=buff)


class MatKhauVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_matkhau")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 11"

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

    # 1. HOOK — 8 ký tự vs 10 ký tự: giờ vs nghìn năm ------------------
    def beat_hook(self):
        title = fit_w(Text("Mật khẩu của bạn", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        row8 = fit_w(password_row("Tr0ng#9x", color=ACCENT), CW).move_to([0, 1.5, 0])
        lbl8 = Text("8 ký tự", font=FONT, weight=BOLD, color=MUTED).scale(SZ_LABEL).next_to(row8, DOWN, buff=0.18)
        t8 = Text("bị bẻ:  vài GIỜ", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY).next_to(lbl8, DOWN, buff=0.22)

        row10 = fit_w(password_row("Tr0ng#9xQ!", color=ACCENT), CW).move_to([0, -1.0, 0])
        lbl10 = Text("10 ký tự", font=FONT, weight=BOLD, color=MUTED).scale(SZ_LABEL).next_to(row10, DOWN, buff=0.18)
        t10 = Text("bị bẻ:  HÀNG NGHÌN NĂM", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY)
        fit_w(t10, CW).next_to(lbl10, DOWN, buff=0.22)
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.18); self.play(FadeIn(row8, shift=UP * 0.15), FadeIn(lbl8), run_time=0.7)
            self.cue(D * 0.4); self.play(FadeIn(row10, shift=UP * 0.15), FadeIn(lbl10), run_time=0.7)
            self.cue(D * 0.6); self.play(Write(t8), run_time=0.7)
            self.cue(D * 0.78); self.play(Write(t10), Flash(t10.get_center(), color=GROW, line_length=0.3, num_lines=14), run_time=0.9)
            self._b = VGroup(title, row8, lbl8, t8, row10, lbl10, t10)
        self._clear()

    # 2. VẤN ĐỀ — kẻ tấn công thử cạn -> bài toán đếm ------------------
    def beat_vande(self):
        robot = VGroup(
            RoundedRectangle(corner_radius=0.12, width=1.1, height=0.95).set_fill(BG_CARD, 1).set_stroke(DEBT, 3),
            Dot(radius=0.1).set_fill(DEBT, 1).set_stroke(width=0).shift(LEFT * 0.25 + UP * 0.12),
            Dot(radius=0.1).set_fill(DEBT, 1).set_stroke(width=0).shift(RIGHT * 0.25 + UP * 0.12),
            Line([-0.25, -0.18, 0], [0.25, -0.18, 0]).set_stroke(MUTED, 3),
        ).move_to([0, 2.0, 0])
        rlbl = Text("Máy dò mật khẩu", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL).next_to(robot, DOWN, buff=0.22)
        tries = VGroup(
            Text("aaaa  →  sai", font=FONT, color=MUTED).scale(SZ_LABEL),
            Text("aaab  →  sai", font=FONT, color=MUTED).scale(SZ_LABEL),
            Text("aaac  →  sai ...", font=FONT, color=MUTED).scale(SZ_LABEL),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT).move_to([0, 0.1, 0])
        q = fit_w(Text("Có bao nhiêu mật khẩu phải thử?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, -1.3, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.0); self.play(FadeIn(robot, shift=DOWN * 0.2), FadeIn(rlbl), run_time=0.8)
            self.cue(D * 0.3); self.play(LaggedStart(*[FadeIn(t, shift=RIGHT * 0.2) for t in tries], lag_ratio=0.3), run_time=1.2)
            self.cue(D * 0.66); self.play(Write(q), run_time=0.8)
            self._b = VGroup(robot, rlbl, tries, q)
        self._clear()

    # 3. MÔ HÌNH — quy tắc nhân: 95 cách/ô -> 95^l --------------------
    def beat_mohinh(self):
        title = fit_w(Text("Quy tắc nhân", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        slots = password_row("? ? ? ?".split(), color=ACCENT).move_to([0, 1.6, 0])
        each = Text("mỗi ô:  ~95 ký tự", font=FONT, weight=BOLD, color=MUTED).scale(SZ_LABEL).next_to(slots, DOWN, buff=0.3)
        chars = VGroup(
            Text("a b c ... z", font=FONT, color=GROW).scale(SZ_SMALL),
            Text("A B C ... Z", font=FONT, color=GROW).scale(SZ_SMALL),
            Text("0 1 2 ... 9", font=FONT, color=GROW).scale(SZ_SMALL),
            Text("! @ # $ ...", font=FONT, color=GROW).scale(SZ_SMALL),
        ).arrange(DOWN, buff=0.12).next_to(each, DOWN, buff=0.22)
        mult = Text("95 × 95 × 95 ...", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to([0, -1.6, 0])
        formula = Text("= 95 mũ l", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO).next_to(mult, DOWN, buff=0.25)
        with self.voice("03_mohinh") as D:
            self._kara("03_mohinh", D)
            self.cue(D * 0.0); self.play(Write(title), FadeIn(slots, shift=UP * 0.15), run_time=0.8)
            self.cue(D * 0.22); self.play(FadeIn(each), run_time=0.5)
            self.cue(D * 0.34); self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.15) for c in chars], lag_ratio=0.25), run_time=1.1)
            self.cue(D * 0.62); self.play(Write(mult), run_time=0.7)
            self.cue(D * 0.8); self.play(Write(formula), Flash(formula.get_center(), color=ACCENT, line_length=0.35, num_lines=16), run_time=0.9)
            self._b = VGroup(title, slots, each, chars, mult, formula)
        self._clear()

    # 4. CON SỐ — 95^8 vs 95^10, gấp ~9000 lần ------------------------
    def beat_conso(self):
        title = fit_w(Text("Thay số vào", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        l8 = VGroup(
            Text("8 ký tự:", font=FONT, weight=BOLD, color=MUTED).scale(SZ_LABEL),
            Text("95 mũ 8  ≈  6,6 triệu tỉ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY),
        ).arrange(DOWN, buff=0.14)
        l10 = VGroup(
            Text("10 ký tự:", font=FONT, weight=BOLD, color=MUTED).scale(SZ_LABEL),
            Text("95 mũ 10", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY),
        ).arrange(DOWN, buff=0.14)
        stack = VGroup(l8, l10).arrange(DOWN, buff=0.55).move_to([0, 1.0, 0])
        for m in stack:
            fit_w(m, CW)
        arrow = Arrow(l8.get_bottom(), l10.get_top(), color=ACCENT, stroke_width=4, buff=0.12)
        note = Text("+2 ký tự", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL).next_to(arrow, RIGHT, buff=0.1)
        gap = fit_w(Text("gấp 95 bình phương", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -1.2, 0])
        big = Text("≈ 9000 lần", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO).next_to(gap, DOWN, buff=0.25)
        with self.voice("04_conso") as D:
            self._kara("04_conso", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.5)
            self.cue(D * 0.15); self.play(FadeIn(l8, shift=UP * 0.15), run_time=0.7)
            self.cue(D * 0.4); self.play(FadeIn(l10, shift=UP * 0.15), GrowArrow(arrow), FadeIn(note), run_time=0.8)
            self.cue(D * 0.62); self.play(Write(gap), run_time=0.6)
            self.cue(D * 0.8); self.play(Write(big), Flash(big.get_center(), color=GROW, line_length=0.4, num_lines=18), run_time=1.0)
            self._b = VGroup(title, stack, arrow, note, gap, big)
        self._clear()

    # 5. Ý NGHĨA — 1 tỉ/giây: giờ -> nghìn năm (cột bùng nổ) ----------
    def beat_ynghia(self):
        title = fit_w(Text("Máy dò ~1 tỉ / giây", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        # 2 cột so sánh, đáy chung
        baseY = -1.7
        bar8 = Rectangle(width=0.95, height=0.45).set_fill(DEBT, 1).set_stroke(width=0)
        bar8.move_to([-0.85, baseY + 0.225, 0])
        bar10 = Rectangle(width=0.95, height=3.6).set_fill(GROW, 1).set_stroke(width=0)
        bar10.move_to([0.85, baseY + 1.8, 0])
        cap8 = Text("vài GIỜ", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL).next_to(bar8, DOWN, buff=0.18)
        n8 = Text("8 ký tự", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(bar8, UP, buff=0.12)
        cap10 = fit_w(Text("HÀNG NGHÌN NĂM", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), 1.7).next_to(bar10, UP, buff=0.14)
        n10 = Text("10 ký tự", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(cap8, DOWN, buff=0.0).move_to([0.85, baseY - 0.3, 0])
        rule = fit_w(Text("Mỗi ký tự thêm = × 95", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, 2.0, 0])
        with self.voice("05_ynghia") as D:
            self._kara("05_ynghia", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.2); self.play(GrowFromEdge(bar8, DOWN), FadeIn(cap8), FadeIn(n8), run_time=0.7)
            self.cue(D * 0.42); self.play(GrowFromEdge(bar10, DOWN), run_time=1.1)
            self.cue(D * 0.66); self.play(FadeIn(cap10), FadeIn(n10), run_time=0.6)
            self.cue(D * 0.82); self.play(Write(rule), Indicate(rule, color=ACCENT, scale_factor=1.08), run_time=0.8)
            self._b = VGroup(title, bar8, bar10, cap8, cap10, n8, n10, rule)
        self._clear()

    # 6. CTA -----------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Độ DÀI thắng độ phức tạp", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.8, 0])
        l2 = fit_w(Text("Thêm vài ký tự = thêm thế kỷ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.5, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("ĐĂNG KÝ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.3, 0])
        with self.voice("06_cta", gap=0.4) as D:
            self._kara("06_cta", D)
            self.cue(D * 0.0); self.play(Write(l1), run_time=0.7)
            self.cue(D * 0.3); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.08), run_time=0.8)
            self.cue(D * 0.6); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, sub)
        self._clear()
