"""
"Hàm mũ — vì sao 1 video bùng nổ triệu view" — hàm mũ, cấp số nhân, hệ số R.
Toán 11 · SHORT DỌC 9:16 · ~2 phút · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_lantruyen.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/lantruyen_video.py LanTruyenVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_lantruyen import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def share_tree():
    """Cây lan truyền 1 -> 2 -> 4 (đỉnh trên, toả xuống)."""
    pos = {
        0: [(0, 1.5)],
        1: [(-0.85, 0.5), (0.85, 0.5)],
        2: [(-1.25, -0.5), (-0.45, -0.5), (0.45, -0.5), (1.25, -0.5)],
    }
    dots, edges = VGroup(), VGroup()
    node = {}
    for lvl in (0, 1, 2):
        for j, (x, y) in enumerate(pos[lvl]):
            d = Dot([x, y, 0], radius=0.13).set_fill(ACCENT if lvl == 0 else (GROW if lvl == 1 else PURPLE), 1).set_stroke(width=0)
            node[(lvl, j)] = d
            dots.add(d)
    for j in range(2):
        edges.add(Line(node[(0, 0)].get_center(), node[(1, j)].get_center()).set_stroke(MUTED, 2.5))
    for j in range(4):
        edges.add(Line(node[(1, j // 2)].get_center(), node[(2, j)].get_center()).set_stroke(MUTED, 2.5))
    return VGroup(edges, dots)


class LanTruyenVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_lantruyen")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 11"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_chia()
        self.beat_capso()
        self.beat_hammu()
        self.beat_no()
        self.beat_heso()
        self.beat_dich()
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
        thumb = RoundedRectangle(corner_radius=0.12, width=2.3, height=1.4).set_fill(BG_CARD, 1).set_stroke(MUTED, 2).move_to([0, 1.1, 0])
        play = Triangle().scale(0.32).set_fill(WHITE, 1).set_stroke(width=0).rotate(-PI / 2).move_to(thumb)
        views = Text("1.000.000 views ?!", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE)
        fit_w(views, CW).move_to([0, -0.6, 0])
        q = fit_w(Text("bùng nổ chỉ sau 1 đêm", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, -1.7, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(thumb), GrowFromCenter(play), run_time=0.7)
            self.cue(D * 0.4); self.play(Write(views), Flash(views.get_center(), color=ACCENT, line_length=0.4, num_lines=12), run_time=0.9)
            self.cue(D * 0.75); self.play(Write(q), run_time=0.7)
            self._b = VGroup(thumb, play, views, q)
        self._clear()

    # 2. CHIA SẺ NHÂN ĐÔI -----------------------------------------------
    def beat_chia(self):
        t = fit_w(Text("Mỗi người chia cho 2", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        tree = share_tree().move_to([0, 0.4, 0])
        edges, dots = tree
        note = fit_w(Text("cứ thế nhân đôi sau mỗi vòng", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -2.0, 0])
        with self.voice("02_chia") as D:
            self._kara("02_chia", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.25); self.play(FadeIn(dots[0], scale=0.5), run_time=0.4)
            self.cue(D * 0.42); self.play(Create(edges[0:2]), *[FadeIn(dots[i], scale=0.5) for i in (1, 2)], run_time=0.6)
            self.cue(D * 0.62); self.play(Create(edges[2:6]), *[FadeIn(dots[i], scale=0.5) for i in (3, 4, 5, 6)], run_time=0.7)
            self.cue(D * 0.85); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, tree, note)
        self._clear()

    # 3. CẤP SỐ NHÂN ----------------------------------------------------
    def beat_capso(self):
        t = fit_w(Text("Cấp số nhân", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.4, 0])
        seq = fit_w(Text("2  →  4  →  8  →  16 …", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 0.8, 0])
        note = fit_w(Text("không cộng đều — mà NHÂN ĐÔI liên tục", font=FONT, weight=BOLD, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -0.7, 0])
        with self.voice("03_capso") as D:
            self._kara("03_capso", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.35); self.play(Write(seq), run_time=1.0)
            self.cue(D * 0.78); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, seq, note)
        self._clear()

    # 4. HÀM MŨ vs TUYẾN TÍNH (điểm nhấn) -------------------------------
    def beat_hammu(self):
        t = fit_w(Text("Mũ vs tuyến tính", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        ox, oy, SX, SY = -1.25, -0.55, 0.46, 0.075
        P = lambda x, y: np.array([ox + x * SX, oy + min(y, 30) * SY, 0])
        xaxis = Line(P(0, 0), P(6.2, 0)).set_stroke(MUTED, 2)
        yaxis = Line(P(0, 0), P(0, 31)).set_stroke(MUTED, 2)
        lin = Line(P(0, 0), P(6, 30)).set_stroke("#6B7689", 4)
        exp = VMobject().set_points_as_corners([P(x, 2 ** x) for x in np.linspace(0, 4.96, 44)]).set_stroke(ACCENT, 6)
        l_lin = Text("tuyến tính", font=FONT, weight=BOLD, color="#8A93A6").scale(SZ_SMALL).next_to(lin.get_end(), UP, buff=0.05)
        l_exp = Text("mũ 2^n", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL).next_to(exp.get_end(), LEFT, buff=0.1)
        note = fit_w(Text("bò sát đất → rồi DỰNG ĐỨNG", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        with self.voice("04_hammu") as D:
            self._kara("04_hammu", D)
            self.cue(D * 0.0); self.play(Write(t), Create(xaxis), Create(yaxis), run_time=0.7)
            self.cue(D * 0.3); self.play(Create(lin), FadeIn(l_lin), run_time=0.7)
            self.cue(D * 0.55); self.play(Create(exp), FadeIn(l_exp), run_time=1.1)
            self.cue(D * 0.85); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, xaxis, yaxis, lin, exp, l_lin, l_exp, note)
        self._clear()

    # 5. BÙNG NỔ --------------------------------------------------------
    def beat_no(self):
        r1 = Text("2^20  >  1 triệu", font=FONT, weight=BOLD, color=GROW).scale(SZ_TITLE)
        fit_w(r1, CW).move_to([0, 1.5, 0])
        r2 = Text("2^30  >  1 tỉ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO * 0.8)
        fit_w(r2, CW).move_to([0, 0.1, 0])
        note = fit_w(Text("vài bước cuối tạo gần như toàn bộ con số", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.4, 0])
        with self.voice("05_no") as D:
            self._kara("05_no", D)
            self.cue(D * 0.0); self.play(Write(r1), run_time=0.8)
            self.cue(D * 0.4); self.play(Write(r2), Flash(r2.get_center(), color=ACCENT, line_length=0.5, num_lines=16), run_time=1.0)
            self.cue(D * 0.8); self.play(FadeIn(note), run_time=0.6)
            self._b = VGroup(r1, r2, note)
        self._clear()

    # 6. HỆ SỐ R --------------------------------------------------------
    def beat_heso(self):
        t = fit_w(Text("Hệ số lan truyền R", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.4, 0])
        d = fit_w(Text("mỗi người kéo thêm ~ R người", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, 1.1, 0])
        up = fit_w(Text("R > 1  →  BÙNG NỔ", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY), CW).move_to([0, -0.2, 0])
        dn = fit_w(Text("R < 1  →  tắt dần", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, -1.2, 0])
        with self.voice("06_heso") as D:
            self._kara("06_heso", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(d, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.55); self.play(FadeIn(up, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.78); self.play(FadeIn(dn, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, d, up, dn)
        self._clear()

    # 7. DỊCH BỆNH ------------------------------------------------------
    def beat_dich(self):
        t = fit_w(Text("Dịch bệnh: cùng quy luật", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        d = fit_w(Text("R0 = số ca mỗi người truyền đi", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, 1.1, 0])
        flat = fit_w(Text("\"làm phẳng đường cong\"", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, -0.2, 0])
        why = fit_w(Text("= kéo R xuống dưới 1, bẻ gãy cấp số nhân", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.3, 0])
        with self.voice("07_dich") as D:
            self._kara("07_dich", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(d, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.58); self.play(Write(flat), run_time=0.7)
            self.cue(D * 0.82); self.play(FadeIn(why), run_time=0.6)
            self._b = VGroup(t, d, flat, why)
        self._clear()

    # 8. ỨNG DỤNG -------------------------------------------------------
    def beat_ungdung(self):
        t = fit_w(Text("Hàm mũ điều khiển", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.3, 0])
        items = ["tin đồn lan đi", "lãi kép sinh sôi", "vi khuẩn nhân lên", "phản ứng hạt nhân"]
        rows = VGroup()
        for s in items:
            dot = Dot(radius=0.07).set_fill(ACCENT, 1).set_stroke(width=0)
            txt = Text(s, font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY)
            rows.add(VGroup(dot, txt).arrange(RIGHT, buff=0.2))
        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        fit_w(rows, CW).move_to([0, -0.2, 0])
        with self.voice("08_ungdung") as D:
            self._kara("08_ungdung", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            for i, r in enumerate(rows):
                self.cue(D * (0.2 + i * 0.18)); self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.45)
            self._b = VGroup(t, rows)
        self._clear()

    # 9. CTA ------------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Trực giác quen cộng đều", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.8, 0])
        l2 = fit_w(Text("nên luôn sốc trước cái nhân đôi", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("hàm mũ · cấp số nhân · R", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.3, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.7, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("THEO DÕI", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.6, 0])
        with self.voice("09_cta", gap=0.4) as D:
            self._kara("09_cta", D)
            self.cue(D * 0.0); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.3); self.play(Write(l2), Indicate(l2, color=GROW, scale_factor=1.06), run_time=0.8)
            self.cue(D * 0.55); self.play(FadeIn(tags, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.75); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, tags, sub)
        self._clear()
