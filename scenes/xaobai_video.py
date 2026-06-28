"""
"Xáo bài 52! — thứ tự chưa ai từng cầm" — hoán vị, quy tắc nhân, giai thừa.
Toán 11 · SHORT DỌC 9:16 · ~1 phút 40 · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_xaobai.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/xaobai_video.py XaoBaiVideo
"""
import os

from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_xaobai import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def mini_card(accent=DEBT, w=0.46, h=0.66):
    """Lá bài tối giản: nền trắng + sọc màu trên (không dùng glyph để khỏi lỗi font)."""
    card = RoundedRectangle(corner_radius=0.06, width=w, height=h).set_fill("#F4F6FB", 1).set_stroke("#C8CDD8", 1.5)
    stripe = RoundedRectangle(corner_radius=0.04, width=w * 0.62, height=h * 0.17).set_fill(accent, 1).set_stroke(width=0)
    stripe.move_to(card.get_top() + DOWN * 0.16)
    pip = Dot(radius=0.05).set_fill(accent, 1).set_stroke(width=0).move_to(card.get_center() + DOWN * 0.08)
    return VGroup(card, stripe, pip)


def cmp_row(label_text, frac, color, y, width=3.0):
    """1 hàng so sánh: nhãn nhỏ + thanh bar canh trái theo tỉ lệ frac."""
    bar_bg = Rectangle(width=width, height=0.26).set_fill("#222A3C", 1).set_stroke(width=0).move_to([0, y, 0])
    bar = Rectangle(width=max(0.1, width * frac), height=0.26).set_fill(color, 1).set_stroke(width=0)
    bar.align_to(bar_bg, LEFT).set_y(y)
    lab = fit_w(Text(label_text, font=FONT, weight=BOLD, color=color).scale(SZ_SMALL), CW)
    lab.next_to(bar_bg, UP, buff=0.08).align_to(bar_bg, LEFT)
    return VGroup(lab, bar_bg, bar)


class XaoBaiVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_xaobai")
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
        title = fit_w(Text("Xáo 1 bộ bài 52 lá", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.55, 0])
        deck = VGroup()
        n = 7
        for i in range(n):
            off = i - (n - 1) / 2
            c = mini_card(DEBT if i % 2 == 0 else "#2B3040")
            c.rotate(-off * 0.16).move_to([off * 0.30, 0.85 - abs(off) * 0.07, 0])
            deck.add(c)
        fit_w(deck, CW)
        punch = fit_w(Text("Thứ tự CHƯA AI từng cầm!", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, -1.7, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(LaggedStartMap(FadeIn, deck, lag_ratio=0.12, scale=0.6), run_time=1.0)
            self.cue(D * 0.35); self.play(Write(title), run_time=0.8)
            self.cue(D * 0.72); self.play(Write(punch), Flash(punch.get_center(), color=ACCENT, line_length=0.4, num_lines=12), run_time=0.9)
            self._b = VGroup(title, deck, punch)
        self._clear()

    # 2. VẤN ĐỀ ---------------------------------------------------------
    def beat_vande(self):
        q = fit_w(Text("Có bao nhiêu cách xếp?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.6, 0])
        big = Text("?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO * 1.6).move_to([0, -0.2, 0])
        note = fit_w(Text("trực giác: \"chắc nhiều lắm\"", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.1); self.play(Write(q), run_time=0.8)
            self.cue(D * 0.5); self.play(FadeIn(big, scale=0.4), run_time=0.7)
            self.cue(D * 0.8); self.play(FadeIn(note, shift=UP * 0.15), run_time=0.6)
            self._b = VGroup(q, big, note)
        self._clear()

    # 3. QUY TẮC NHÂN ---------------------------------------------------
    def beat_logic(self):
        t = fit_w(Text("Quy tắc nhân", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        l1 = fit_w(Text("Lá 1: 52 cách chọn", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.4, 0])
        l2 = fit_w(Text("Lá 2: còn 51 cách", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 0.6, 0])
        l3 = fit_w(Text("… giảm dần tới lá cuối", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -0.15, 0])
        chain = fit_w(Text("52 × 51 × 50 × … × 1", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, -1.5, 0])
        with self.voice("03_logic") as D:
            self._kara("03_logic", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.22); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.45); self.play(FadeIn(l2, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.65); self.play(FadeIn(l3, shift=UP * 0.12), run_time=0.5)
            self.cue(D * 0.82); self.play(Write(chain), run_time=0.8)
            self._b = VGroup(t, l1, l2, l3, chain)
        self._clear()

    # 4. TÍNH RA ---------------------------------------------------------
    def beat_tinh(self):
        eq = Text("= 52 !", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE).move_to([0, 2.2, 0])
        hero = Text("≈ 8 × 10⁶⁷", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO).move_to([0, 0.7, 0])
        sub = fit_w(Text("số 8 và 67 chữ số phía sau", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -0.6, 0])
        bignum = fit_w(Text("80 658 175 170 943 878 …", font=FONT, weight=BOLD, color="#3C4760").scale(SZ_SMALL), CW).move_to([0, -1.9, 0])
        with self.voice("04_tinh") as D:
            self._kara("04_tinh", D)
            self.cue(D * 0.0); self.play(Write(eq), run_time=0.7)
            self.cue(D * 0.45); self.play(Write(hero), Flash(hero.get_center(), color=GROW, line_length=0.5, num_lines=18), run_time=1.0)
            self.cue(D * 0.78); self.play(FadeIn(sub), FadeIn(bignum), run_time=0.6)
            self._b = VGroup(eq, hero, sub, bignum)
        self._clear()

    # 5. WOW: LỚN CỠ NÀO ------------------------------------------------
    def beat_wow(self):
        t = fit_w(Text("Lớn cỡ nào?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.55, 0])
        rowA = cmp_row("Xáo bài 52!  ~ 10⁶⁷", 1.0, ACCENT, 1.35)
        rowB = cmp_row("Nguyên tử Trái Đất ~ 10⁵⁰", 50 / 67, PURPLE, 0.35)
        rowC = cmp_row("Giây từ Big Bang ~ 10¹⁷", 17 / 67, MUTED, -0.65)
        punch = fit_w(Text("Xáo mỗi giây vẫn chưa lặp lại!", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, -1.95, 0])
        with self.voice("05_wow") as D:
            self._kara("05_wow", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.18); self.play(FadeIn(rowA, shift=RIGHT * 0.2), run_time=0.6)
            self.cue(D * 0.4); self.play(FadeIn(rowB, shift=RIGHT * 0.2), run_time=0.6)
            self.cue(D * 0.58); self.play(FadeIn(rowC, shift=RIGHT * 0.2), run_time=0.6)
            self.cue(D * 0.8); self.play(Write(punch), Indicate(punch, color=ACCENT, scale_factor=1.08), run_time=0.9)
            self._b = VGroup(t, rowA, rowB, rowC, punch)
        self._clear()

    # 6. CTA ------------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Mỗi lần xáo = độc nhất", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.8, 0])
        l2 = fit_w(Text("Toán đếm ở khắp nơi", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.05, 0])
        tags = fit_w(Text("lịch thi · mật khẩu · mã hoá", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.35, 0])
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
