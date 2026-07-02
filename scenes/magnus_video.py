"""
"Cú xoáy của Messi" — hiệu ứng Magnus, chênh áp Bernoulli quanh quả bóng xoay.
Lý 10-11 · SHORT DỌC 9:16 · ~2 phút (12 beat) · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_magnus.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/magnus_video.py MagnusVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_magnus import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DARK = "#1B2233"


def ball(center, r=0.32):
    center = np.array(center, dtype=float)
    c = Circle(radius=r).set_fill(WHITE, 1).set_stroke(DARK, 2.5).move_to(center)
    p = RegularPolygon(5, radius=r * 0.36).set_fill(DARK, 1).set_stroke(width=0).move_to(center)
    d1 = Dot(center + np.array([r * 0.62, r * 0.5, 0]), radius=r * 0.12).set_fill(DARK, 1).set_stroke(width=0)
    d2 = Dot(center + np.array([-r * 0.64, -r * 0.42, 0]), radius=r * 0.12).set_fill(DARK, 1).set_stroke(width=0)
    return VGroup(c, p, d1, d2)


def spin_arrow(center, r, color=ACCENT):
    center = np.array(center, dtype=float)
    return CurvedArrow(center + np.array([r * 1.35, r * 0.2, 0]),
                       center + np.array([-r * 1.35, r * 0.2, 0]),
                       angle=-PI * 0.9, color=color).set_stroke(width=4)


class MagnusVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_magnus")
    SEGMENTS = SEGMENTS
    TOPIC = "VẬT LÝ 10"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_thang()
        self.beat_xoay()
        self.beat_khongkhi()
        self.beat_haiben()
        self.beat_bernoulli()
        self.beat_luc()
        self.beat_huong()
        self.beat_conso()
        self.beat_khac()
        self.beat_ung()
        self.beat_cta()
        self.brand_stinger()
        self.wait(0.3)

    def _kara(self, seg, D):
        self._kar = self.make_karaoke(SEGMENTS[seg], D, self.beat_t0)
        self.add(self._kar)

    def _clear(self):
        self.end_karaoke(self._kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 1. HOOK — cú đá phạt vòng qua hàng rào
    def beat_hook(self):
        t = fit_w(Text("Cú đá phạt của Messi", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        wall = VGroup(*[RoundedRectangle(corner_radius=0.05, width=0.22, height=0.72).set_fill(MUTED, 1).set_stroke(width=0) for _ in range(4)])
        wall.arrange(RIGHT, buff=0.09).move_to([0, 0.1, 0])
        goal = Rectangle(width=1.1, height=0.8).set_stroke(WHITE, 3).move_to([1.5, 1.35, 0])
        b = ball([-1.7, -1.1, 0], 0.26)
        path = ArcBetweenPoints([-1.55, -1.0, 0], [1.35, 1.15, 0], angle=-2.1).set_stroke(ACCENT, 3)
        dpath = DashedVMobject(path, num_dashes=22).set_stroke(ACCENT, 3)
        q = fit_w(Text("Vì sao bóng bay CONG?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -2.5, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(goal), LaggedStartMap(FadeIn, wall, lag_ratio=0.12), run_time=0.9)
            self.cue(D * 0.35); self.play(FadeIn(b, scale=0.6), run_time=0.4)
            self.cue(D * 0.55); self.play(Create(dpath), run_time=1.1)
            self.cue(D * 0.85); self.play(Write(q), run_time=0.7)
            self._b = VGroup(t, wall, goal, b, dpath, q)
        self._clear()

    # 2. KHÔNG XOAY -> KHÔNG VÒNG ĐƯỢC
    def beat_thang(self):
        t = fit_w(Text("Bóng KHÔNG xoay", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        b = ball([-1.7, -0.3, 0], 0.26)
        arc = ArcBetweenPoints([-1.5, -0.2, 0], [1.7, -0.2, 0], angle=-1.0).set_stroke(MUTED, 3)
        darc = DashedVMobject(arc, num_dashes=18).set_stroke(MUTED, 3)
        note = fit_w(Text("chỉ bay theo vòng cung đều\n→ không thể lượn vào góc", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        key = fit_w(Text("Bí mật nằm ở CÁCH XOAY", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, 1.4, 0])
        with self.voice("02_thang") as D:
            self._kara("02_thang", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(b, scale=0.6), run_time=0.6)
            self.cue(D * 0.3); self.play(Create(darc), run_time=1.0)
            self.cue(D * 0.6); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.85); self.play(Write(key), run_time=0.6)
            self._b = VGroup(t, b, darc, note, key)
        self._clear()

    # 3. ĐÁ LỆCH TÂM -> BÓNG TỰ XOAY
    def beat_xoay(self):
        t = fit_w(Text("Đá LỆCH tâm bóng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        b = ball([0, 0.5, 0], 0.6)
        kick = Arrow([-1.4, -0.1, 0], [-0.55, 0.3, 0], color=DEBT, buff=0, stroke_width=7)
        klbl = Text("cú sút", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(kick, DOWN, buff=0.12)
        sp = spin_arrow([0, 0.5, 0], 0.6, ACCENT)
        note = fit_w(Text("bóng vừa lao đi vừa TỰ XOAY tít", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.7, 0])
        with self.voice("03_xoay") as D:
            self._kara("03_xoay", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(b, scale=0.7), run_time=0.6)
            self.cue(D * 0.3); self.play(GrowArrow(kick), FadeIn(klbl), run_time=0.6)
            self.cue(D * 0.55); self.play(Create(sp), Rotate(b, angle=-TAU, run_time=min(D * 0.4, 1.6)))
            self.cue(D * 0.85); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, b, kick, klbl, sp, note)
        self._clear()

    # 4. LỚP KHÍ BÁM QUANH BÓNG
    def beat_khongkhi(self):
        t = fit_w(Text("Bóng cuốn theo lớp khí", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        b = ball([0, 0.5, 0], 0.55)
        halo = Circle(radius=0.85).set_stroke(PURPLE, 3, opacity=0.8).move_to([0, 0.5, 0])
        sp = spin_arrow([0, 0.5, 0], 0.85, PURPLE)
        note = fit_w(Text("lớp không khí mỏng bám sát\nbị kéo quay CÙNG chiều bóng", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -1.8, 0])
        with self.voice("04_khongkhi") as D:
            self._kara("04_khongkhi", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(b), run_time=0.6)
            self.cue(D * 0.35); self.play(Create(halo), Create(sp), run_time=0.8)
            self.cue(D * 0.55); self.play(Rotate(VGroup(halo, sp, b), angle=-TAU, about_point=[0, 0.5, 0], run_time=min(D * 0.35, 1.6)))
            self.cue(D * 0.82); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, b, halo, sp, note)
        self._clear()

    # 5. HAI BÊN: NHANH vs CHẬM
    def beat_haiben(self):
        t = fit_w(Text("Hai bên bóng khác nhau", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        b = ball([0, 0.4, 0], 0.5)
        wind = Arrow([1.8, -1.1, 0], [-1.8, -1.1, 0], color=MUTED, buff=0, stroke_width=5)
        wlbl = Text("gió tương đối", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(wind, DOWN, buff=0.1)
        top = Arrow([-0.9, 1.15, 0], [0.9, 1.15, 0], color=GROW, buff=0, stroke_width=6)
        tlbl = Text("NHANH", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL).next_to(top, UP, buff=0.08)
        bot = Arrow([0.7, -0.35, 0], [-0.7, -0.35, 0], color=DEBT, buff=0, stroke_width=6)
        blbl = Text("CHẬM", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(bot, DOWN, buff=0.08)
        with self.voice("05_haiben") as D:
            self._kara("05_haiben", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(b), run_time=0.6)
            self.cue(D * 0.3); self.play(GrowArrow(wind), FadeIn(wlbl), run_time=0.6)
            self.cue(D * 0.55); self.play(GrowArrow(top), FadeIn(tlbl), run_time=0.6)
            self.cue(D * 0.78); self.play(GrowArrow(bot), FadeIn(blbl), run_time=0.6)
            self._b = VGroup(t, b, wind, wlbl, top, tlbl, bot, blbl)
        self._clear()

    # 6. BERNOULLI
    def beat_bernoulli(self):
        t = fit_w(Text("Nguyên lý BERNOULLI", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        r1 = fit_w(Text("khí chạy NHANH → áp suất THẤP", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, 0.9, 0])
        r2 = fit_w(Text("khí chạy CHẬM → áp suất CAO", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY), CW).move_to([0, -0.5, 0])
        note = fit_w(Text("nhanh thì loãng, chậm thì nén", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -1.8, 0])
        with self.voice("06_bernoulli") as D:
            self._kara("06_bernoulli", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.35); self.play(FadeIn(r1, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.65); self.play(FadeIn(r2, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.88); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, r1, r2, note)
        self._clear()

    # 7. CHÊNH ÁP -> LỰC MAGNUS
    def beat_luc(self):
        t = fit_w(Text("Chênh áp sinh LỰC", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        b = ball([0, 0.4, 0], 0.5)
        lo = Text("áp THẤP", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL).move_to([0, 1.5, 0])
        hi = Text("áp CAO", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).move_to([0, -0.75, 0])
        force = Arrow([0, -0.35, 0], [0, 1.05, 0], color=ACCENT, buff=0, stroke_width=9)
        flbl = fit_w(Text("lực MAGNUS", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        with self.voice("07_luc") as D:
            self._kara("07_luc", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(b), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(hi, shift=UP * 0.1), FadeIn(lo, shift=DOWN * 0.1), run_time=0.7)
            self.cue(D * 0.6); self.play(GrowArrow(force), Flash([0, 0.4, 0], color=ACCENT, line_length=0.4, num_lines=14), run_time=0.9)
            self.cue(D * 0.85); self.play(Write(flbl), run_time=0.6)
            self._b = VGroup(t, b, lo, hi, force, flbl)
        self._clear()

    # 8. LỰC VUÔNG GÓC -> QUỸ ĐẠO CONG
    def beat_huong(self):
        t = fit_w(Text("Lực bẻ cong đường bay", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        path = ArcBetweenPoints([-1.7, -1.2, 0], [1.7, 1.0, 0], angle=-1.7).set_stroke(ACCENT, 3)
        dpath = DashedVMobject(path, num_dashes=20).set_stroke(ACCENT, 3)
        b = ball([-1.7, -1.2, 0], 0.24)
        f1 = Arrow([-0.7, -0.75, 0], [-0.35, -0.25, 0], color=DEBT, buff=0, stroke_width=6)
        f2 = Arrow([0.55, 0.25, 0], [0.9, 0.75, 0], color=DEBT, buff=0, stroke_width=6)
        note = fit_w(Text("lực luôn VUÔNG GÓC hướng bay\n→ đường lượn mềm mại", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -2.2, 0])
        with self.voice("08_huong") as D:
            self._kara("08_huong", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(b, scale=0.6), run_time=0.6)
            self.cue(D * 0.3); self.play(Create(dpath), run_time=1.0)
            self.cue(D * 0.6); self.play(GrowArrow(f1), GrowArrow(f2), run_time=0.7)
            self.cue(D * 0.82); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, b, dpath, f1, f2, note)
        self._clear()

    # 9. CÀNG NHANH + CÀNG XOÁY = CÀNG CONG
    def beat_conso(self):
        t = fit_w(Text("Cong nhiều khi nào?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        hero = fit_w(Text("lực ∝ tốc độ bay × tốc độ xoáy", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.1, 0])
        r1 = fit_w(Text("sút MẠNH + xoáy NHIỀU → cong gắt", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), CW).move_to([0, -0.2, 0])
        r2 = fit_w(Text("sút nhẹ, xoáy ít → gần như thẳng", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -1.4, 0])
        with self.voice("09_conso") as D:
            self._kara("09_conso", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(Write(hero), run_time=0.9)
            self.cue(D * 0.62); self.play(FadeIn(r1, shift=UP * 0.12), Indicate(r1, color=GROW), run_time=0.7)
            self.cue(D * 0.85); self.play(FadeIn(r2, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, hero, r1, r2)
        self._clear()

    # 10. CÙNG HIỆU ỨNG TRONG THỂ THAO
    def beat_khac(self):
        t = fit_w(Text("Cùng hiệu ứng ở khắp nơi", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        rows = [("bóng bàn xoáy đổi hướng", GROW), ("bóng chày cong đánh lừa", ACCENT), ("tennis topspin cắm nhanh", PURPLE)]
        chips = VGroup()
        for txt, col in rows:
            card = RoundedRectangle(corner_radius=0.16, width=3.2, height=0.9).set_fill(BG_CARD, 1).set_stroke(col, 2.5)
            lab = fit_w(Text(txt, font=FONT, weight=BOLD, color=col).scale(SZ_LABEL), 2.9).move_to(card)
            chips.add(VGroup(card, lab))
        chips.arrange(DOWN, buff=0.35).move_to([0, -0.3, 0])
        with self.voice("10_khac") as D:
            self._kara("10_khac", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            for i, c in enumerate(chips):
                self.cue(D * (0.28 + 0.22 * i)); self.play(GrowFromCenter(c), run_time=0.55)
            self._b = VGroup(t, chips)
        self._clear()

    # 11. ỨNG DỤNG THỰC — TÀU BUỒM QUAY
    def beat_ung(self):
        t = fit_w(Text("Con người tận dụng lực này", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        sea = Rectangle(width=4.2, height=1.0).set_fill(PURPLE, 0.25).set_stroke(width=0).move_to([0, -1.6, 0])
        hull = Polygon([-1.1, -1.1, 0], [1.1, -1.1, 0], [0.8, -1.55, 0], [-0.8, -1.55, 0]).set_fill(MUTED, 1).set_stroke(width=0)
        rotor = RoundedRectangle(corner_radius=0.12, width=0.5, height=1.5).set_fill(BG_CARD, 1).set_stroke(ACCENT, 2.5).move_to([0, -0.2, 0])
        sp = spin_arrow([0, -0.2, 0], 0.55, ACCENT)
        wind = Arrow([-1.9, 0.3, 0], [-0.5, 0.3, 0], color=GROW, buff=0, stroke_width=5)
        wlbl = Text("gió", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL).next_to(wind, UP, buff=0.08)
        note = fit_w(Text("trụ xoay thay buồm → gió đẩy tàu\ntốn ít nhiên liệu hơn", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_SMALL), CW).move_to([0, 1.2, 0])
        with self.voice("11_ung") as D:
            self._kara("11_ung", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(sea), FadeIn(hull), run_time=0.7)
            self.cue(D * 0.35); self.play(GrowFromEdge(rotor, DOWN), Create(sp), run_time=0.7)
            self.cue(D * 0.6); self.play(GrowArrow(wind), FadeIn(wlbl), run_time=0.6)
            self.cue(D * 0.8); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, sea, hull, rotor, sp, wind, wlbl, note)
        self._clear()

    # 12. CTA
    def beat_cta(self):
        l1 = fit_w(Text("Cú cong không phải phép màu", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.9, 0])
        l2 = fit_w(Text("chỉ là CHÊNH ÁP SUẤT", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("Magnus · Bernoulli · xoáy bóng", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.25, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.7, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("THEO DÕI", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.75, 0])
        with self.voice("12_cta", gap=0.4) as D:
            self._kara("12_cta", D)
            self.cue(D * 0.0); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.3); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.06), run_time=0.8)
            self.cue(D * 0.55); self.play(FadeIn(tags, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.75); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, tags, sub)
        self._clear()
