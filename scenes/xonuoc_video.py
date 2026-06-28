"""
"Xô nước quay không đổ một giọt" — chuyển động tròn, lực hướng tâm.
Lý 10 · SHORT DỌC 9:16 · ~2 phút · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_xonuoc.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/xonuoc_video.py XoNuocVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_xonuoc import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WATER = "#5EC8F2"


def cup(scale=1.0):
    """Xô tối giản: vành nâu hình thang hở miệng + nước xanh."""
    rim = VGroup(
        Line([-0.30, 0.24, 0], [-0.26, -0.22, 0]),
        Line([-0.26, -0.22, 0], [0.26, -0.22, 0]),
        Line([0.26, -0.22, 0], [0.30, 0.24, 0]),
    ).set_stroke("#A9742E", 6)
    water = RoundedRectangle(corner_radius=0.04, width=0.48, height=0.34).set_fill(WATER, 0.92).set_stroke(width=0).move_to([0, -0.03, 0])
    return VGroup(water, rim).scale(scale)


class XoNuocVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_xonuoc")
    SEGMENTS = SEGMENTS
    TOPIC = "LÝ 10"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_trongluc()
        self.beat_huongtam()
        self.beat_dinhcao()
        self.beat_dieukien()
        self.beat_nguong()
        self.beat_cham()
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
        path = Circle(radius=1.15).set_stroke(MUTED, 2, opacity=0.6).move_to([0, 0.55, 0])
        top_cup = cup().rotate(PI).move_to([0, 1.7, 0])
        title = fit_w(Text("Lộn ngược mà 0 giọt rơi ?!", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, -1.4, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Create(path), run_time=0.7)
            self.cue(D * 0.35); self.play(FadeIn(top_cup, shift=DOWN * 0.15), run_time=0.6)
            self.cue(D * 0.55); self.play(Rotate(VGroup(top_cup), about_point=path.get_center(), angle=-TAU, run_time=min(D * 0.4, 1.6)))
            self.cue(D * 0.85); self.play(Write(title), run_time=0.7)
            self._b = VGroup(path, top_cup, title)
        self._clear()

    # 2. TRỌNG LỰC ------------------------------------------------------
    def beat_trongluc(self):
        t = fit_w(Text("Đứng yên thì sao?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.4, 0])
        c = cup().rotate(PI).move_to([0, 1.0, 0])
        g = Arrow([0, 0.5, 0], [0, -0.6, 0], color=DEBT, buff=0, stroke_width=6)
        glb = Text("trọng lực", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(g, RIGHT, buff=0.12)
        drops = VGroup(*[Dot([(-0.2 + 0.2 * i), -0.9 - 0.15 * i, 0], radius=0.05).set_fill(WATER, 1).set_stroke(width=0) for i in range(3)])
        res = fit_w(Text("nước đổ ngay!", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -1.9, 0])
        with self.voice("02_trongluc") as D:
            self._kara("02_trongluc", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(c), run_time=0.6)
            self.cue(D * 0.35); self.play(GrowArrow(g), FadeIn(glb), run_time=0.6)
            self.cue(D * 0.62); self.play(LaggedStartMap(FadeIn, drops, shift=DOWN * 0.3, lag_ratio=0.2), run_time=0.7)
            self.cue(D * 0.82); self.play(Write(res), run_time=0.6)
            self._b = VGroup(t, c, g, glb, drops, res)
        self._clear()

    # 3. LỰC HƯỚNG TÂM --------------------------------------------------
    def beat_huongtam(self):
        t = fit_w(Text("Lực hướng tâm", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        ctr = np.array([0, 0.4, 0])
        path = Circle(radius=1.15).set_stroke(MUTED, 2, opacity=0.6).move_to(ctr)
        obj = Dot(ctr + np.array([1.15, 0, 0]), radius=0.13).set_fill(WATER, 1).set_stroke(width=0)
        arr = Arrow(obj.get_center(), ctr, color=ACCENT, buff=0.1, stroke_width=6)
        note = fit_w(Text("luôn kéo vào TÂM → vật bẻ hướng, không bay thẳng", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.9, 0])
        with self.voice("03_huongtam") as D:
            self._kara("03_huongtam", D)
            self.cue(D * 0.0); self.play(Write(t), Create(path), FadeIn(obj), run_time=0.7)
            self.cue(D * 0.4); self.play(GrowArrow(arr), run_time=0.6)
            self.cue(D * 0.6); self.play(Rotate(VGroup(obj, arr), about_point=ctr, angle=-TAU, run_time=min(D * 0.35, 1.5)))
            self.cue(D * 0.86); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, path, obj, arr, note)
        self._clear()

    # 4. TẠI ĐỈNH -------------------------------------------------------
    def beat_dinhcao(self):
        t = fit_w(Text("Tại điểm cao nhất", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        c = cup().rotate(PI).move_to([0, 1.3, 0])
        p = Arrow([-0.3, 0.85, 0], [-0.3, -0.1, 0], color=DEBT, buff=0, stroke_width=6)
        n = Arrow([0.3, 0.85, 0], [0.3, -0.1, 0], color=GROW, buff=0, stroke_width=6)
        pl = Text("P", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL).next_to(p, LEFT, buff=0.1)
        nl = Text("N", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL).next_to(n, RIGHT, buff=0.1)
        res = fit_w(Text("cả hai hướng vào tâm = lực hướng tâm", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.4, 0])
        with self.voice("04_dinhcao") as D:
            self._kara("04_dinhcao", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(c), run_time=0.6)
            self.cue(D * 0.35); self.play(GrowArrow(p), FadeIn(pl), GrowArrow(n), FadeIn(nl), run_time=0.8)
            self.cue(D * 0.75); self.play(Write(res), run_time=0.7)
            self._b = VGroup(t, c, p, n, pl, nl, res)
        self._clear()

    # 5. ĐIỀU KIỆN ------------------------------------------------------
    def beat_dieukien(self):
        t = fit_w(Text("Bí mật: quay đủ NHANH", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.2, 0])
        l1 = fit_w(Text("lực hướng tâm cần > trọng lực", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 0.8, 0])
        l2 = fit_w(Text("→ trọng lực chưa kịp kéo nước rời quỹ đạo", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -0.3, 0])
        l3 = fit_w(Text("nước bám chặt theo đáy xô", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, -1.4, 0])
        with self.voice("05_dieukien") as D:
            self._kara("05_dieukien", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.55); self.play(FadeIn(l2), run_time=0.5)
            self.cue(D * 0.78); self.play(FadeIn(l3, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, l1, l2, l3)
        self._clear()

    # 6. NGƯỠNG TỐC ĐỘ --------------------------------------------------
    def beat_nguong(self):
        t = fit_w(Text("Tốc độ tới hạn", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.4, 0])
        cond = fit_w(Text("lực hướng tâm = trọng lực", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 1.3, 0])
        hero = Text("v = √(g · R)", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO * 0.95).move_to([0, 0.1, 0])
        num = fit_w(Text("R = 1 m  →  ≈ 3 m/s", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, -1.4, 0])
        with self.voice("06_nguong") as D:
            self._kara("06_nguong", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(cond), run_time=0.6)
            self.cue(D * 0.35); self.play(Write(hero), Flash(hero.get_center(), color=GROW, line_length=0.5, num_lines=16), run_time=1.0)
            self.cue(D * 0.75); self.play(Write(num), run_time=0.7)
            self._b = VGroup(t, cond, hero, num)
        self._clear()

    # 7. QUAY CHẬM ------------------------------------------------------
    def beat_cham(self):
        t = fit_w(Text("Quay chậm hơn ngưỡng?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.3, 0])
        l1 = fit_w(Text("trọng lực THẮNG", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        l2 = fit_w(Text("→ nguyên xô đổ thẳng vào mặt!", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY), CW).move_to([0, -0.3, 0])
        l3 = fit_w(Text("bí mật không phải phép màu — chỉ là đủ nhanh", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.5, 0])
        with self.voice("07_cham") as D:
            self._kara("07_cham", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.55); self.play(Write(l2), Indicate(l2, color=DEBT), run_time=0.8)
            self.cue(D * 0.82); self.play(FadeIn(l3), run_time=0.5)
            self._b = VGroup(t, l1, l2, l3)
        self._clear()

    # 8. ỨNG DỤNG -------------------------------------------------------
    def beat_ungdung(self):
        t = fit_w(Text("Cùng một nguyên lý", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.3, 0])
        items = ["tàu lượn lộn vòng", "máy giặt vắt khô", "khúc cua đua nghiêng"]
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
        l1 = fit_w(Text("Muốn không rơi…", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.8, 0])
        l2 = fit_w(Text("bí quyết là đi thật nhanh", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("chuyển động tròn · lực hướng tâm", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.3, 0])
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
