"""
"Thang máy biến bạn thành 72kg" — định luật II Newton, trọng lượng biểu kiến.
Lý 10 · SHORT DỌC 9:16 · ~1 phút 40 · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_thangmay.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/thangmay_video.py ThangMayVideo
"""
import os

from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_thangmay import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def stick_person(color=ACCENT, s=1.0):
    head = Circle(radius=0.13).set_fill(color, 1).set_stroke(width=0).move_to([0, 0.13, 0])
    body = Line([0, 0, 0], [0, -0.4, 0]).set_stroke(color, 5)
    arms = Line([-0.2, -0.1, 0], [0.2, -0.1, 0]).set_stroke(color, 5)
    legL = Line([0, -0.4, 0], [-0.15, -0.68, 0]).set_stroke(color, 5)
    legR = Line([0, -0.4, 0], [0.15, -0.68, 0]).set_stroke(color, 5)
    return VGroup(head, body, arms, legL, legR).scale(s)


def cabin(readout, read_color=ACCENT):
    """Cabin thang máy: người đứng trên cân, kèm ô hiển thị số cân."""
    cab = RoundedRectangle(corner_radius=0.1, width=1.7, height=2.05).set_fill("#0F1830", 1).set_stroke(MUTED, 2.5)
    scale = RoundedRectangle(corner_radius=0.05, width=1.15, height=0.22).set_fill(MUTED, 1).set_stroke(width=0)
    scale.move_to(cab.get_bottom() + UP * 0.42)
    person = stick_person(ACCENT, 1.0)
    person.next_to(scale, UP, buff=-0.02)
    disp = RoundedRectangle(corner_radius=0.06, width=0.92, height=0.4).set_fill(BG, 1).set_stroke(read_color, 2)
    disp.move_to(cab.get_bottom() + UP * 0.0 + DOWN * 0.0).next_to(cab, DOWN, buff=0.18)
    dtx = Text(readout, font=FONT, weight=BOLD, color=read_color).scale(0.3).move_to(disp)
    return VGroup(cab, scale, person), VGroup(disp, dtx)


def wow_row(tag, val, color, y):
    dot = Triangle().scale(0.12).set_fill(color, 1).set_stroke(width=0).rotate(-PI / 2).move_to([-1.6, y, 0])
    lab = Text(tag, font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL)
    v = Text(val, font=FONT, weight=BOLD, color=color).scale(SZ_BODY)
    row = VGroup(lab, v).arrange(RIGHT, buff=0.18)
    row.next_to(dot, RIGHT, buff=0.2)
    g = VGroup(dot, row)
    fit_w(g, CW)
    return g.set_y(y)


class ThangMayVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_thangmay")
    SEGMENTS = SEGMENTS
    TOPIC = "LÝ 10"

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
        cab, disp = cabin("72 kg", ACCENT)
        group = VGroup(cab, disp).move_to([0, 0.55, 0])
        up = Arrow([1.5, -0.1, 0], [1.5, 0.9, 0], color=ACCENT, buff=0, stroke_width=6, max_tip_length_to_length_ratio=0.3)
        up_lbl = Text("ĐI LÊN", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL).next_to(up, UP, buff=0.1)
        note = fit_w(Text("…dù bạn chỉ nặng 60 kg", font=FONT, weight=BOLD, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -2.2, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(cab, shift=DOWN * 0.2), run_time=0.7)
            self.cue(D * 0.35); self.play(GrowArrow(up), FadeIn(up_lbl), run_time=0.6)
            self.cue(D * 0.6); self.play(FadeIn(disp, scale=0.6), Flash(disp.get_center(), color=ACCENT, line_length=0.35, num_lines=12), run_time=0.8)
            self.cue(D * 0.85); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.5)
            self._b = VGroup(group, up, up_lbl, note)
        self._clear()

    # 2. VẤN ĐỀ: cân đo gì ----------------------------------------------
    def beat_vande(self):
        q = fit_w(Text("Cân đang đo cái gì?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.4, 0])
        foot = RoundedRectangle(corner_radius=0.08, width=1.3, height=0.3).set_fill(MUTED, 1).set_stroke(width=0).move_to([0, 0.2, 0])
        down = Arrow([0, 1.2, 0], [0, 0.45, 0], color=DEBT, buff=0, stroke_width=6).shift(LEFT * 0.5)
        d_lbl = Text("lực ép", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(down, LEFT, buff=0.1)
        upr = Arrow([0, -0.8, 0], [0, -0.05, 0], color=GROW, buff=0, stroke_width=6).shift(RIGHT * 0.5)
        u_lbl = Text("phản lực N", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL).next_to(upr, RIGHT, buff=0.1)
        ans = fit_w(Text("Đo LỰC — không đo khối lượng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.1); self.play(Write(q), run_time=0.7)
            self.cue(D * 0.4); self.play(FadeIn(foot), GrowArrow(down), FadeIn(d_lbl), run_time=0.7)
            self.cue(D * 0.6); self.play(GrowArrow(upr), FadeIn(u_lbl), run_time=0.6)
            self.cue(D * 0.85); self.play(Write(ans), run_time=0.7)
            self._b = VGroup(q, foot, down, d_lbl, upr, u_lbl, ans)
        self._clear()

    # 3. ĐỊNH LUẬT II NEWTON --------------------------------------------
    def beat_logic(self):
        t = fit_w(Text("Định luật II Newton", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.55, 0])
        block = Square(side_length=0.5).set_fill(PURPLE, 1).set_stroke(WHITE, 2).move_to([0, 0.9, 0])
        nN = Arrow(block.get_top(), block.get_top() + UP * 0.95, color=GROW, buff=0, stroke_width=6)
        nN_l = Text("N", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL).next_to(nN, RIGHT, buff=0.08)
        mg = Arrow(block.get_bottom(), block.get_bottom() + DOWN * 0.7, color=DEBT, buff=0, stroke_width=6)
        mg_l = Text("mg", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL).next_to(mg, RIGHT, buff=0.08)
        eq1 = fit_w(Text("Đứng yên:  N = mg", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -1.2, 0])
        eq2 = fit_w(Text("Tăng tốc lên:  N = mg + ma", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, -2.1, 0])
        with self.voice("03_logic") as D:
            self._kara("03_logic", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(block), run_time=0.6)
            self.cue(D * 0.25); self.play(GrowArrow(nN), FadeIn(nN_l), GrowArrow(mg), FadeIn(mg_l), run_time=0.7)
            self.cue(D * 0.5); self.play(FadeIn(eq1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.78); self.play(FadeIn(eq2, shift=UP * 0.12), nN.animate.put_start_and_end_on(block.get_top(), block.get_top() + UP * 1.25), run_time=0.8)
            self._b = VGroup(t, block, nN, nN_l, mg, mg_l, eq1, eq2)
        self._clear()

    # 4. TÍNH RA ---------------------------------------------------------
    def beat_tinh(self):
        f = fit_w(Text("N = m (g + a)", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.1, 0])
        s1 = fit_w(Text("= 60 × (10 + 2)", font=FONT, weight=BOLD, color=MUTED).scale(SZ_BODY), CW).move_to([0, 0.9, 0])
        s2 = Text("= 720 N", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO).move_to([0, -0.3, 0])
        res = fit_w(Text("→ cân đọc 72 kg", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, -1.55, 0])
        pct = fit_w(Text("nặng hơn 20%", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -2.35, 0])
        with self.voice("04_tinh") as D:
            self._kara("04_tinh", D)
            self.cue(D * 0.0); self.play(Write(f), run_time=0.7)
            self.cue(D * 0.35); self.play(FadeIn(s1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.55); self.play(Write(s2), run_time=0.7)
            self.cue(D * 0.78); self.play(Write(res), Flash(res.get_center(), color=ACCENT, line_length=0.4, num_lines=14), run_time=0.9)
            self.play(FadeIn(pct), run_time=0.4)
            self._b = VGroup(f, s1, s2, res, pct)
        self._clear()

    # 5. WOW: 3 trạng thái ----------------------------------------------
    def beat_wow(self):
        t = fit_w(Text("Đổi gia tốc → đổi cân nặng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.55, 0])
        r1 = wow_row("Đi lên:", "72 kg", ACCENT, 1.4)
        r2 = wow_row("Đi xuống:", "48 kg", PURPLE, 0.5)
        r3 = wow_row("Rơi tự do:", "0 kg", DEBT, -0.4)
        punch = fit_w(Text("Không trọng lượng — như phi hành gia!", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        with self.voice("05_wow") as D:
            self._kara("05_wow", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.5)
            self.cue(D * 0.18); self.play(FadeIn(r1, shift=RIGHT * 0.2), run_time=0.55)
            self.cue(D * 0.4); self.play(FadeIn(r2, shift=RIGHT * 0.2), run_time=0.55)
            self.cue(D * 0.6); self.play(FadeIn(r3, shift=RIGHT * 0.2), run_time=0.55)
            self.cue(D * 0.82); self.play(Write(punch), Indicate(punch, color=ACCENT, scale_factor=1.06), run_time=0.9)
            self._b = VGroup(t, r1, r2, r3, punch)
        self._clear()

    # 6. CTA ------------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Nặng nhẹ = phản lực đổi", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.8, 0])
        l2 = fit_w(Text("Vật lý quanh ta", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.05, 0])
        tags = fit_w(Text("phi hành gia · tàu lượn · máy bay", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.35, 0])
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
