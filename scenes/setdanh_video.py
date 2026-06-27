"""
"Sét đánh xa bao nhiêu?" — đếm giây từ chớp đến sấm để biết khoảng cách.
Vật lý 11 · tốc độ truyền sóng âm v = s/t · SHORT DỌC 9:16 · ~1 phút 50 · KHÔNG intro.

Dùng bộ cỡ chữ chuẩn SZ_* (brand.py) + CANH NHỊP self.cue(): mỗi bước hiện hình được
rải trải đều theo lời đọc của cả đoạn (không dồn ở đầu beat).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_setdanh.py
Căn chỉnh:   .venv/bin/python scenes/align_narration.py output/narration_setdanh
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/setdanh_video.py SetDanhVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_setdanh import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LIGHT = "#FDE68A"    # ánh chớp (vàng sáng)
SOUND = "#60A5FA"    # sóng âm (xanh dương)


def lightning_bolt(scale=1.0, color=LIGHT):
    """Tia chớp zig-zag đơn giản (Polygon)."""
    pts = [
        [0.10, 1.00, 0], [-0.18, 0.18, 0], [0.08, 0.18, 0],
        [-0.22, -0.55, 0], [0.05, -0.55, 0], [-0.30, -1.30, 0],
        [0.18, -0.30, 0], [-0.06, -0.30, 0], [0.30, 0.45, 0], [0.04, 0.45, 0],
    ]
    return Polygon(*pts).set_fill(color, 1).set_stroke(ACCENT, 2).scale(scale)


def cloud(scale=1.0, color="#475569"):
    g = VGroup(
        Circle(radius=0.45).move_to([-0.5, 0, 0]),
        Circle(radius=0.6).move_to([0.05, 0.12, 0]),
        Circle(radius=0.45).move_to([0.6, 0, 0]),
        RoundedRectangle(corner_radius=0.3, width=1.7, height=0.55).move_to([0.05, -0.2, 0]),
    )
    g.set_fill(color, 1).set_stroke(width=0)
    return g.scale(scale)


class SetDanhVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_setdanh")
    SEGMENTS = SEGMENTS
    TOPIC = "VẬT LÝ 11"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_vande()
        self.beat_tocdo()
        self.beat_congthuc()
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

    # 1. HOOK: chớp -> đếm 6 giây -> sấm ------------------------------
    def beat_hook(self):
        cl = cloud(0.9).move_to([0, 2.5, 0])
        bolt = lightning_bolt(0.95).next_to(cl, DOWN, buff=0.05).shift(LEFT * 0.2)
        dots = VGroup(*[
            VGroup(
                Circle(radius=0.16).set_stroke(ACCENT, 3).set_fill(BG_CARD, 1),
                Text(str(i + 1), font=FONT, weight=BOLD, color=ACCENT).scale(0.32),
            ) for i in range(6)
        ])
        for grp in dots:
            grp[1].move_to(grp[0])
        dots.arrange(RIGHT, buff=0.12).move_to([0, 0.5, 0])
        countlbl = Text("đếm thầm...", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(dots, UP, buff=0.22)
        thunder = Text("...rồi nghe SẤM", font=FONT, weight=BOLD, color=SOUND).scale(SZ_BODY).move_to([0, -0.5, 0])
        q = fit_w(Text("Sét cách bạn bao xa?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, -1.45, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(cl, shift=DOWN * 0.2), run_time=0.6)
            self.cue(D * 0.12); self.play(Create(bolt), Flash(bolt.get_center(), color=LIGHT, line_length=0.5, num_lines=16), run_time=0.6)
            self.cue(D * 0.30); self.play(FadeIn(countlbl), run_time=0.4)
            self.cue(D * 0.38); self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.18), run_time=1.5)
            self.cue(D * 0.70); self.play(FadeIn(thunder, shift=RIGHT * 0.2), run_time=0.6)
            self.cue(D * 0.84); self.play(FadeIn(q, shift=UP * 0.2), run_time=0.6)
            self._b = VGroup(cl, bolt, dots, countlbl, thunder, q)
        self._clear()

    # 2. VẤN ĐỀ: cùng nguồn, đến lệch nhau ----------------------------
    def beat_vande(self):
        title = fit_w(Text("Chớp và sấm: cùng 1 tia sét", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        eye = VGroup(
            Text("MẮT thấy chớp", font=FONT, weight=BOLD, color=LIGHT).scale(SZ_LABEL),
            Text("ngay lập tức", font=FONT, color=MUTED).scale(SZ_SMALL),
        ).arrange(DOWN, buff=0.12).move_to([0, 1.3, 0])
        ear = VGroup(
            Text("TAI nghe sấm", font=FONT, weight=BOLD, color=SOUND).scale(SZ_LABEL),
            Text("trễ vài giây", font=FONT, color=MUTED).scale(SZ_SMALL),
        ).arrange(DOWN, buff=0.12).move_to([0, 0.1, 0])
        vs = Text("vì sao lệch nhau?", font=FONT, color=MUTED).scale(SZ_BODY).move_to([0, -0.9, 0])
        key = fit_w(Text("Bí mật ở TỐC ĐỘ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, -1.7, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.7)
            self.cue(D * 0.20); self.play(FadeIn(eye, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.38); self.play(FadeIn(ear, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.58); self.play(FadeIn(vs), run_time=0.5)
            self.cue(D * 0.78); self.play(FadeIn(key, shift=UP * 0.2), Indicate(key, color=ACCENT, scale_factor=1.1), run_time=0.8)
            self._b = VGroup(title, eye, ear, vs, key)
        self._clear()

    # 3. TỐC ĐỘ: ánh sáng vs âm thanh ---------------------------------
    def beat_tocdo(self):
        title = fit_w(Text("So tốc độ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        # thanh ánh sáng (dài, gần như tức thời)
        l_lbl = Text("ÁNH SÁNG", font=FONT, weight=BOLD, color=LIGHT).scale(SZ_LABEL).move_to([-1.4, 1.6, 0]).align_to([-1.55, 0, 0], LEFT)
        l_bar = RoundedRectangle(corner_radius=0.08, width=3.0, height=0.42).set_fill(LIGHT, 1).set_stroke(width=0).next_to(l_lbl, DOWN, buff=0.18).align_to(l_lbl, LEFT)
        l_val = Text("~300.000 km/s", font=FONT, weight=BOLD, color=BG).scale(SZ_SMALL).move_to(l_bar)
        # thanh âm thanh (ngắn xíu)
        s_lbl = Text("ÂM THANH", font=FONT, weight=BOLD, color=SOUND).scale(SZ_LABEL).move_to([-1.4, 0.1, 0]).align_to([-1.55, 0, 0], LEFT)
        s_bar = RoundedRectangle(corner_radius=0.06, width=0.5, height=0.42).set_fill(SOUND, 1).set_stroke(width=0).next_to(s_lbl, DOWN, buff=0.18).align_to(s_lbl, LEFT)
        s_val = Text("~343 m/s", font=FONT, weight=BOLD, color=SOUND).scale(SZ_SMALL).next_to(s_bar, RIGHT, buff=0.18)
        concl = fit_w(Text("Âm chậm hơn → bạn nghe TRỄ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, -1.55, 0])
        with self.voice("03_tocdo") as D:
            self._kara("03_tocdo", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.5)
            self.cue(D * 0.12); self.play(FadeIn(l_lbl), GrowFromEdge(l_bar, LEFT), run_time=0.7)
            self.cue(D * 0.30); self.play(FadeIn(l_val), run_time=0.4)
            self.cue(D * 0.48); self.play(FadeIn(s_lbl), GrowFromEdge(s_bar, LEFT), run_time=0.7)
            self.cue(D * 0.66); self.play(FadeIn(s_val), run_time=0.4)
            self.cue(D * 0.82); self.play(FadeIn(concl, shift=UP * 0.2), run_time=0.7)
            self._b = VGroup(title, l_lbl, l_bar, l_val, s_lbl, s_bar, s_val, concl)
        self._clear()

    # 4. CÔNG THỨC: s = v × t -> 2 km ---------------------------------
    def beat_congthuc(self):
        formula = fit_w(Text("s = v × t", font=FONT, weight=BOLD, color=WHITE).scale(SZ_HERO), CW).move_to([0, 2.4, 0])
        sub = fit_w(Text("quãng đường = tốc độ × thời gian", font=FONT, color=MUTED).scale(SZ_SMALL), CW).next_to(formula, DOWN, buff=0.22)
        plug = VGroup(
            Text("v = 343 m/s", font=FONT, weight=BOLD, color=SOUND).scale(SZ_BODY),
            Text("t = 6 giây", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY),
        ).arrange(DOWN, buff=0.22).move_to([0, 0.5, 0])
        calc = fit_w(Text("343 × 6 ≈ 2000 m", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -0.55, 0])
        result = Text("≈ 2 km", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO).move_to([0, -1.55, 0])
        with self.voice("04_congthuc") as D:
            self._kara("04_congthuc", D)
            self.cue(D * 0.0); self.play(Write(formula), FadeIn(sub), run_time=0.8)
            self.cue(D * 0.28); self.play(FadeIn(plug, shift=UP * 0.15), run_time=0.8)
            self.cue(D * 0.55); self.play(FadeIn(calc, shift=UP * 0.15), run_time=0.7)
            self.cue(D * 0.78); self.play(Write(result), Flash(result.get_center(), color=GROW, line_length=0.4, num_lines=18), run_time=1.0)
            self._b = VGroup(formula, sub, plug, calc, result)
        self._clear()

    # 5. Ý NGHĨA: mẹo "chia 3 ra km" ----------------------------------
    def beat_ynghia(self):
        big = fit_w(Text("MẸO: chia 3 ra km", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        rule = fit_w(Text("3 giây  ≈  1 km", font=FONT, weight=BOLD, color=WHITE).scale(SZ_HERO), CW).move_to([0, 1.5, 0])
        # thước số giây -> cảnh báo gần/xa
        bar = Line([-1.5, 0.2, 0], [1.5, 0.2, 0]).set_stroke("#3A4254", 6)
        near = Text("ít giây → GẦN", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL).move_to([-0.85, -0.4, 0])
        far = Text("nhiều giây → xa", font=FONT, color=MUTED).scale(SZ_LABEL).move_to([0.85, -0.4, 0])
        warn = fit_w(Text("Chớp & sấm cùng lúc = ngay trên đầu!", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY), CW).move_to([0, -1.5, 0])
        with self.voice("05_ynghia") as D:
            self._kara("05_ynghia", D)
            self.cue(D * 0.0); self.play(Write(big), run_time=0.7)
            self.cue(D * 0.20); self.play(FadeIn(rule, shift=UP * 0.15), Indicate(rule, color=ACCENT, scale_factor=1.08), run_time=0.8)
            self.cue(D * 0.45); self.play(Create(bar), run_time=0.5)
            self.cue(D * 0.56); self.play(FadeIn(near, shift=LEFT * 0.1), FadeIn(far, shift=RIGHT * 0.1), run_time=0.6)
            self.cue(D * 0.80); self.play(FadeIn(warn, shift=UP * 0.2), run_time=0.7)
            self._b = VGroup(big, rule, bar, near, far, warn)
        self._clear()

    # 6. CTA ----------------------------------------------------------
    def beat_cta(self):
        title = fit_w(Text("Cùng quy tắc s = v × t", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.4, 0])
        uses = VGroup(
            Text("• Tàu ngầm dò đáy biển (sonar)", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("• Trạm đo định vị động đất", font=FONT, color=WHITE).scale(SZ_LABEL),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to([0, 1.3, 0])
        for u in uses:
            fit_w(u, CW)
        l2 = fit_w(Text("Lần tới gặp giông: đếm giây thử!", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, 0.0, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.5, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("ĐĂNG KÝ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -1.1, 0])
        with self.voice("06_cta", gap=0.4) as D:
            self._kara("06_cta", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.7)
            self.cue(D * 0.22); self.play(FadeIn(uses[0], shift=RIGHT * 0.2), run_time=0.55)
            self.cue(D * 0.38); self.play(FadeIn(uses[1], shift=RIGHT * 0.2), run_time=0.55)
            self.cue(D * 0.58); self.play(Write(l2), run_time=0.7)
            self.cue(D * 0.78); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(title, uses, l2, sub)
        self._clear()
