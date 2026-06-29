"""
"Một viên uranium bằng tấn than" — E=mc², khối lượng hụt, phân hạch.
Lý 12 · SHORT DỌC 9:16 · ~2 phút (12 beat) · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_uranium.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/uranium_video.py UraniumVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_uranium import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def nucleus(center, color=PURPLE, r=0.42, label="U"):
    c = Circle(radius=r).set_fill(color, 0.85).set_stroke(WHITE, 2).move_to(center)
    g = VGroup(c)
    if label:
        g.add(Text(label, font=FONT, weight=BOLD, color=WHITE).scale(min(0.34, r)).move_to(center))
    return g


class UraniumVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_uranium")
    SEGMENTS = SEGMENTS
    TOPIC = "LÝ 12"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_hoahoc()
        self.beat_hatnhan()
        self.beat_emc2()
        self.beat_c2()
        self.beat_huthut()
        self.beat_chuyenhoa()
        self.beat_sosanh()
        self.beat_gram()
        self.beat_haimat()
        self.beat_mattroi()
        self.beat_cta()
        self.brand_stinger()
        self.wait(0.3)

    def _kara(self, seg, D):
        self._kar = self.make_karaoke(SEGMENTS[seg], D, self.beat_t0)
        self.add(self._kar)

    def _clear(self):
        self.end_karaoke(self._kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 1. HOOK
    def beat_hook(self):
        pellet = RoundedRectangle(corner_radius=0.05, width=0.32, height=0.4).set_fill(GROW, 1).set_stroke(WHITE, 1.5).move_to([-1.0, 0.7, 0])
        plbl = Text("1 viên", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL).next_to(pellet, DOWN, buff=0.15)
        coal = VGroup(*[RoundedRectangle(corner_radius=0.06, width=0.34, height=0.28).set_fill("#3A3A40", 1).set_stroke("#555", 1.5) for _ in range(6)])
        coal.arrange_in_grid(rows=2, cols=3, buff=0.08).move_to([1.0, 0.7, 0])
        clbl = Text("1 tấn than", font=FONT, weight=BOLD, color=MUTED).scale(SZ_SMALL).next_to(coal, DOWN, buff=0.15)
        eq = Text("=", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE).move_to([0, 0.7, 0])
        q = fit_w(Text("Vì sao nhỏ xíu mà mạnh khủng khiếp?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, -1.4, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(pellet, scale=0.5), FadeIn(plbl), run_time=0.6)
            self.cue(D * 0.3); self.play(Write(eq), LaggedStartMap(FadeIn, coal, lag_ratio=0.1), FadeIn(clbl), run_time=0.8)
            self.cue(D * 0.7); self.play(Write(q), run_time=0.8)
            self._b = VGroup(pellet, plbl, coal, clbl, eq, q)
        self._clear()

    # 2. HOÁ HỌC
    def beat_hoahoc(self):
        t = fit_w(Text("Đốt than = phản ứng HOÁ HỌC", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        nuc = Dot([0, 0.6, 0], radius=0.16).set_fill(DEBT, 1).set_stroke(width=0)
        orbit = Ellipse(width=2.4, height=1.2).set_stroke(MUTED, 2).move_to([0, 0.6, 0])
        elec = Dot(orbit.get_right(), radius=0.08).set_fill(WATER if False else "#5EC8F2", 1).set_stroke(width=0)
        note = fit_w(Text("chỉ xáo lớp vỏ electron → ít năng lượng", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.6, 0])
        with self.voice("02_hoahoc") as D:
            self._kara("02_hoahoc", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(nuc), Create(orbit), run_time=0.8)
            self.cue(D * 0.35); self.play(FadeIn(elec), Rotate(VGroup(elec), about_point=orbit.get_center(), angle=-TAU, run_time=min(D * 0.4, 1.6)))
            self.cue(D * 0.82); self.play(FadeIn(note), run_time=0.6)
            self._b = VGroup(t, nuc, orbit, elec, note)
        self._clear()

    # 3. HẠT NHÂN
    def beat_hatnhan(self):
        t = fit_w(Text("Hạt nhân thì KHÁC HẲN", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.4, 0])
        nuc = nucleus([0, 0.6, 0], PURPLE, 0.55, "U")
        note = fit_w(Text("năng lượng nằm trong LÕI — lực cực mạnh", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.2, 0])
        with self.voice("03_hatnhan") as D:
            self._kara("03_hatnhan", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.35); self.play(GrowFromCenter(nuc), run_time=0.8)
            self.cue(D * 0.7); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.7)
            self._b = VGroup(t, nuc, note)
        self._clear()

    # 4. E = mc²
    def beat_emc2(self):
        hero = Text("E = m c²", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO * 1.15).move_to([0, 0.8, 0])
        note = fit_w(Text("năng lượng = khối lượng × (tốc độ ánh sáng)²", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -0.8, 0])
        with self.voice("04_emc2") as D:
            self._kara("04_emc2", D)
            self.cue(D * 0.0); self.play(Write(hero), Flash(hero.get_center(), color=GROW, line_length=0.6, num_lines=20), run_time=1.2)
            self.cue(D * 0.6); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.7)
            self._b = VGroup(hero, note)
        self._clear()

    # 5. c²
    def beat_c2(self):
        t = fit_w(Text("Đáng sợ ở chữ c²", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.8, 0])
        hero = Text("c² ≈ 9 × 10¹⁶", font=FONT, weight=BOLD, color=DEBT).scale(SZ_HERO * 0.95).move_to([0, 0.3, 0])
        note = fit_w(Text("nhân với con số khổng lồ này", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -1.1, 0])
        with self.voice("05_c2") as D:
            self._kara("05_c2", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.4); self.play(Write(hero), Flash(hero.get_center(), color=DEBT, line_length=0.5, num_lines=16), run_time=1.0)
            self.cue(D * 0.8); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, hero, note)
        self._clear()

    # 6. KHỐI LƯỢNG HỤT (phân hạch)
    def beat_huthut(self):
        t = fit_w(Text("Uranium vỡ ra", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.4, 0])
        nuc = nucleus([0, 0.7, 0], PURPLE, 0.5, "U")
        f1 = nucleus([-0.8, 0.7, 0], "#A78BFA", 0.34, "")
        f2 = nucleus([0.8, 0.7, 0], "#7C5CD6", 0.34, "")
        neus = VGroup(*[Dot([0.2 * i, 0.7 + 0.25 * (i - 1), 0], radius=0.06).set_fill(ACCENT, 1).set_stroke(width=0) for i in (-1, 0, 1)])
        res = fit_w(Text("tổng các mảnh NHẸ hơn 1 chút = Δm", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.4, 0])
        with self.voice("06_huthut") as D:
            self._kara("06_huthut", D)
            self.cue(D * 0.0); self.play(Write(t), GrowFromCenter(nuc), run_time=0.7)
            self.cue(D * 0.4); self.play(FadeOut(nuc), FadeIn(f1), FadeIn(f2),
                                         f1.animate.shift(LEFT * 0.45), f2.animate.shift(RIGHT * 0.45),
                                         LaggedStartMap(FadeIn, neus, lag_ratio=0.2),
                                         Flash([0, 0.7, 0], color=ACCENT, line_length=0.5, num_lines=16), run_time=0.9)
            self.cue(D * 0.78); self.play(Write(res), run_time=0.7)
            self._b = VGroup(t, f1, f2, neus, res)
        self._clear()

    # 7. CHUYỂN HOÁ
    def beat_chuyenhoa(self):
        dm = Text("Δm", font=FONT, weight=BOLD, color=PURPLE).scale(SZ_HERO).move_to([-1.0, 0.6, 0])
        arr = Arrow([-0.45, 0.6, 0], [0.35, 0.6, 0], color=ACCENT, buff=0, stroke_width=7)
        e = Text("E", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO * 1.1).move_to([1.0, 0.6, 0])
        note = fit_w(Text("khối lượng hụt → chuyển THẲNG thành năng lượng", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -1.2, 0])
        with self.voice("07_chuyenhoa") as D:
            self._kara("07_chuyenhoa", D)
            self.cue(D * 0.0); self.play(Write(dm), run_time=0.6)
            self.cue(D * 0.35); self.play(GrowArrow(arr), Write(e), Flash(e.get_center(), color=GROW, line_length=0.4, num_lines=14), run_time=0.9)
            self.cue(D * 0.72); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.7)
            self._b = VGroup(dm, arr, e, note)
        self._clear()

    # 8. SO SÁNH
    def beat_sosanh(self):
        t = fit_w(Text("1 viên uranium vs 1 tấn than", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.0, 0])
        r1 = fit_w(Text("than: năng lượng hoá học", font=FONT, weight=BOLD, color=MUTED).scale(SZ_BODY), CW).move_to([0, 0.8, 0])
        r2 = fit_w(Text("uranium: nhờ khối lượng hụt", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -0.2, 0])
        big = fit_w(Text("→ hiệu quả gấp TRIỆU lần", font=FONT, weight=BOLD, color=GROW).scale(SZ_TITLE), CW).move_to([0, -1.4, 0])
        with self.voice("08_sosanh") as D:
            self._kara("08_sosanh", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(r1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.55); self.play(FadeIn(r2, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.8); self.play(Write(big), Indicate(big, color=ACCENT), run_time=0.8)
            self._b = VGroup(t, r1, r2, big)
        self._clear()

    # 9. 1 GRAM
    def beat_gram(self):
        hero = fit_w(Text("biến 1 gram → năng lượng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.3, 0])
        big = fit_w(Text("đủ thắp sáng cả 1 thành phố nhỏ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 0.0, 0])
        sub = fit_w(Text("trong nhiều ngày liền", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, -1.1, 0])
        with self.voice("09_gram") as D:
            self._kara("09_gram", D)
            self.cue(D * 0.0); self.play(Write(hero), run_time=0.8)
            self.cue(D * 0.45); self.play(FadeIn(big, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.75); self.play(Write(sub), run_time=0.6)
            self._b = VGroup(hero, big, sub)
        self._clear()

    # 10. HAI MẶT
    def beat_haimat(self):
        t = fit_w(Text("1 phương trình, 2 số phận", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.2, 0])
        c1 = RoundedRectangle(corner_radius=0.16, width=3.0, height=0.95).set_fill(BG_CARD, 1).set_stroke(GROW, 2.5).move_to([0, 0.8, 0])
        c1t = fit_w(Text("nhà máy điện hạt nhân", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), 2.6).move_to(c1)
        c2 = RoundedRectangle(corner_radius=0.16, width=3.0, height=0.95).set_fill(BG_CARD, 1).set_stroke(DEBT, 2.5).move_to([0, -0.5, 0])
        c2t = fit_w(Text("bom nguyên tử", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY), 2.6).move_to(c2)
        with self.voice("10_haimat") as D:
            self._kara("10_haimat", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(GrowFromCenter(VGroup(c1, c1t)), run_time=0.7)
            self.cue(D * 0.6); self.play(GrowFromCenter(VGroup(c2, c2t)), run_time=0.7)
            self._b = VGroup(t, c1, c1t, c2, c2t)
        self._clear()

    # 11. MẶT TRỜI
    def beat_mattroi(self):
        t = fit_w(Text("Cùng công thức ấy", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.3, 0])
        sun = Circle(radius=0.55).set_fill(ACCENT, 1).set_stroke(width=0).move_to([0, 0.9, 0])
        rays = VGroup(*[Line([0, 0.9, 0] + 0.6 * np.array([np.cos(a), np.sin(a), 0]), [0, 0.9, 0] + 0.85 * np.array([np.cos(a), np.sin(a), 0])).set_stroke(ACCENT, 4) for a in np.linspace(0, TAU, 12, endpoint=False)])
        l1 = fit_w(Text("Mặt Trời cháy sáng hàng tỉ năm", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -0.8, 0])
        l2 = fit_w(Text("nhiệt hạch — giấc mơ năng lượng loài người", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.7, 0])
        with self.voice("11_mattroi") as D:
            self._kara("11_mattroi", D)
            self.cue(D * 0.0); self.play(Write(t), GrowFromCenter(sun), Create(rays), run_time=0.8)
            self.cue(D * 0.4); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.72); self.play(FadeIn(l2), run_time=0.6)
            self._b = VGroup(t, sun, rays, l1, l2)
        self._clear()

    # 12. CTA
    def beat_cta(self):
        l1 = fit_w(Text("Khối lượng = năng lượng", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.8, 0])
        l2 = fit_w(Text("2 mặt của 1 thứ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("E = mc² · phân hạch · nhiệt hạch", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.3, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.7, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("THEO DÕI", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.6, 0])
        with self.voice("12_cta", gap=0.4) as D:
            self._kara("12_cta", D)
            self.cue(D * 0.0); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.3); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.06), run_time=0.8)
            self.cue(D * 0.55); self.play(FadeIn(tags, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.75); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, tags, sub)
        self._clear()
