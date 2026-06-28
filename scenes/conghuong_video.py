"""
"Cộng hưởng làm sập cầu" — dao động, tần số riêng, cộng hưởng.
Lý 12 · SHORT DỌC 9:16 · ~2 phút · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_conghuong.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/conghuong_video.py CongHuongVideo
"""
import math
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_conghuong import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def wave(amp, k=3.0, color=ACCENT, sw=5):
    return ParametricFunction(lambda t: np.array([t, amp * math.sin(k * t), 0]),
                              t_range=[-1.7, 1.7, 0.03], color=color).set_stroke(width=sw)


def bridge(amp=0.0, color=ACCENT):
    deck = ParametricFunction(lambda t: np.array([t, amp * math.sin(PI * (t + 1.6) / 1.6), 0]),
                              t_range=[-1.6, 1.6, 0.03], color=color).set_stroke(width=6)
    sL = Triangle().scale(0.2).set_fill(MUTED, 1).set_stroke(width=0).next_to([-1.6, 0, 0], DOWN, buff=0.02)
    sR = Triangle().scale(0.2).set_fill(MUTED, 1).set_stroke(width=0).next_to([1.6, 0, 0], DOWN, buff=0.02)
    return VGroup(deck, sL, sR)


def swing(angle_deg, pivot=(0, 1.25, 0), L=1.4, color=ACCENT):
    a = math.radians(angle_deg)
    p = np.array(pivot, dtype=float)
    bob = p + np.array([L * math.sin(a), -L * math.cos(a), 0])
    rod = Line(p, bob).set_stroke(MUTED, 4)
    ball = Dot(bob, radius=0.17).set_fill(color, 1).set_stroke(width=0)
    piv = Dot(p, radius=0.07).set_fill(WHITE, 1).set_stroke(width=0)
    return VGroup(piv, rod, ball)


class CongHuongVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_conghuong")
    SEGMENTS = SEGMENTS
    TOPIC = "LÝ 12"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_tanso()
        self.beat_xichdu()
        self.beat_conghuong()
        self.beat_cong()
        self.beat_loannhip()
        self.beat_tacoma()
        self.beat_ungdung()
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
        br = bridge(0.0, MUTED).move_to([0, 0.9, 0])
        soldiers = VGroup(*[Dot(radius=0.07).set_fill(ACCENT, 1).set_stroke(width=0) for _ in range(7)])
        soldiers.arrange(RIGHT, buff=0.16).move_to([0, 1.15, 0])
        title = fit_w(Text("Lính đi đều bước qua cầu", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -0.6, 0])
        boom = Text("SẬP ?!", font=FONT, weight=BOLD, color=DEBT).scale(SZ_HERO).move_to([0, -1.8, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Create(br), FadeIn(soldiers, shift=DOWN * 0.1), run_time=0.9)
            self.cue(D * 0.45); self.play(Write(title), run_time=0.8)
            self.cue(D * 0.78); self.play(FadeIn(boom, scale=0.5), Flash(boom.get_center(), color=DEBT, line_length=0.5, num_lines=14), run_time=0.9)
            self._b = VGroup(br, soldiers, title, boom)
        self._clear()

    # 2. TẦN SỐ RIÊNG ---------------------------------------------------
    def beat_tanso(self):
        t = fit_w(Text("Mỗi vật có tần số riêng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        sw = swing(28).shift(UP * 0.2)
        note = fit_w(Text("nhịp mà nó \"thích\" rung nhất", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -2.0, 0])
        with self.voice("02_tanso") as D:
            self._kara("02_tanso", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(sw), run_time=0.6)
            self.cue(D * 0.5); self.play(Transform(sw, swing(-28).shift(UP * 0.2)), run_time=0.7)
            self.cue(D * 0.72); self.play(Transform(sw, swing(28).shift(UP * 0.2)), FadeIn(note), run_time=0.7)
            self._b = VGroup(t, sw, note)
        self._clear()

    # 3. ĐẨY XÍCH ĐU ĐÚNG NHỊP ------------------------------------------
    def beat_xichdu(self):
        t = fit_w(Text("Đẩy đúng nhịp", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        sw = swing(15).shift(UP * 0.2)
        push = Text("đẩy →", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL).move_to([-1.4, -0.6, 0])
        note = fit_w(Text("mỗi nhịp đúng lúc → biên độ LỚN DẦN", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -2.0, 0])
        with self.voice("03_xichdu") as D:
            self._kara("03_xichdu", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(sw), run_time=0.6)
            self.cue(D * 0.35); self.play(FadeIn(push), Transform(sw, swing(32).shift(UP * 0.2)), run_time=0.7)
            self.cue(D * 0.6); self.play(Transform(sw, swing(50).shift(UP * 0.2)), run_time=0.7)
            self.cue(D * 0.82); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, sw, push, note)
        self._clear()

    # 4. CỘNG HƯỞNG: biên độ tăng vọt -----------------------------------
    def beat_conghuong(self):
        t = fit_w(Text("CỘNG HƯỞNG", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        base = Line([-1.7, 0, 0], [1.7, 0, 0]).set_stroke("#2A3142", 2).move_to([0, 0.7, 0])
        w = wave(0.15).move_to([0, 0.7, 0])
        cond = fit_w(Text("lực lặp = tần số riêng", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.1, 0])
        hero = fit_w(Text("→ biên độ TĂNG VỌT", font=FONT, weight=BOLD, color=DEBT).scale(SZ_TITLE), CW).move_to([0, -2.0, 0])
        with self.voice("04_conghuong") as D:
            self._kara("04_conghuong", D)
            self.cue(D * 0.0); self.play(Write(t), Create(base), Create(w), run_time=0.8)
            self.cue(D * 0.35); self.play(Transform(w, wave(0.45).move_to([0, 0.7, 0])), FadeIn(cond), run_time=0.7)
            self.cue(D * 0.6); self.play(Transform(w, wave(0.9).move_to([0, 0.7, 0])), run_time=0.7)
            self.cue(D * 0.82); self.play(Write(hero), run_time=0.7)
            self._b = VGroup(t, base, w, cond, hero)
        self._clear()

    # 5. BƯỚC ĐỀU CỘNG DỒN → SẬP ----------------------------------------
    def beat_cong(self):
        t = fit_w(Text("Bước đều cộng dồn", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        br = bridge(0.1, ACCENT).move_to([0, 0.8, 0])
        steps = fit_w(Text("mỗi bước = 1 cú đẩy nhỏ", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -0.8, 0])
        limit = fit_w(Text("vượt giới hạn chịu lực của thép", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        with self.voice("05_cong") as D:
            self._kara("05_cong", D)
            self.cue(D * 0.0); self.play(Write(t), Create(br), run_time=0.7)
            self.cue(D * 0.3); self.play(Transform(br, bridge(0.35, ACCENT).move_to([0, 0.8, 0])), FadeIn(steps), run_time=0.7)
            self.cue(D * 0.55); self.play(Transform(br, bridge(0.8, DEBT).move_to([0, 0.8, 0])), run_time=0.7)
            self.cue(D * 0.8); self.play(Write(limit), Indicate(limit, color=DEBT), run_time=0.8)
            self._b = VGroup(t, br, steps, limit)
        self._clear()

    # 6. LOẠN NHỊP → AN TOÀN --------------------------------------------
    def beat_loannhip(self):
        t = fit_w(Text("Bước loạn nhịp?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        br = bridge(0.06, GROW).move_to([0, 0.8, 0])
        c1 = fit_w(Text("các cú đẩy lệch pha → triệt tiêu", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -0.7, 0])
        c2 = fit_w(Text("NGHỊCH LÝ: hỗn loạn lại an toàn", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), CW).move_to([0, -1.8, 0])
        with self.voice("06_loannhip") as D:
            self._kara("06_loannhip", D)
            self.cue(D * 0.0); self.play(Write(t), Create(br), run_time=0.7)
            self.cue(D * 0.4); self.play(FadeIn(c1, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.75); self.play(Write(c2), run_time=0.7)
            self._b = VGroup(t, br, c1, c2)
        self._clear()

    # 7. TACOMA ---------------------------------------------------------
    def beat_tacoma(self):
        t = fit_w(Text("Cầu Tacoma, 1940", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        br = bridge(0.0, MUTED).move_to([0, 0.9, 0])
        wind = fit_w(Text("gió thổi ĐỀU → kích đúng tần số → xoắn sập", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -0.7, 0])
        rule = fit_w(Text("→ quân đội phải bước loạn nhịp khi qua cầu", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL), CW).move_to([0, -1.8, 0])
        with self.voice("07_tacoma") as D:
            self._kara("07_tacoma", D)
            self.cue(D * 0.0); self.play(Write(t), Create(br), run_time=0.7)
            self.cue(D * 0.25); self.play(Transform(br, bridge(0.5, DEBT).move_to([0, 0.9, 0])), run_time=0.6)
            self.cue(D * 0.45); self.play(Transform(br, bridge(-0.5, DEBT).move_to([0, 0.9, 0])), run_time=0.5)
            self.cue(D * 0.6); self.play(FadeIn(wind, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.82); self.play(Write(rule), run_time=0.7)
            self._b = VGroup(t, br, wind, rule)
        self._clear()

    # 8. ỨNG DỤNG -------------------------------------------------------
    def beat_ungdung(self):
        t = fit_w(Text("Cộng hưởng không chỉ phá", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.3, 0])
        items = ["radio bắt đúng kênh", "lò vi sóng làm nóng", "nhạc cụ vang lên"]
        rows = VGroup()
        for s in items:
            dot = Dot(radius=0.07).set_fill(ACCENT, 1).set_stroke(width=0)
            txt = Text(s, font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY)
            rows.add(VGroup(dot, txt).arrange(RIGHT, buff=0.2))
        rows.arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        fit_w(rows, CW).move_to([0, -0.4, 0])
        with self.voice("08_ungdung") as D:
            self._kara("08_ungdung", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            for i, r in enumerate(rows):
                self.cue(D * (0.25 + i * 0.2)); self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.5)
            self._b = VGroup(t, rows)
        self._clear()

    # 9. CTA ------------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Cùng 1 nhịp đúng lúc", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.8, 0])
        l2 = fit_w(Text("nâng trẻ — hoặc sập cầu", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("dao động · tần số riêng · cộng hưởng", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.3, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.7, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("THEO DÕI", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.6, 0])
        with self.voice("09_cta", gap=0.4) as D:
            self._kara("09_cta", D)
            self.cue(D * 0.0); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.3); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.08), run_time=0.8)
            self.cue(D * 0.55); self.play(FadeIn(tags, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.75); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, tags, sub)
        self._clear()
