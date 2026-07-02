"""
"Vì sao chim đậu dây điện không bị giật?" — hiệu điện thế, dòng điện, đường dẫn.
Lý 11 · SHORT DỌC 9:16 · ~2 phút (12 beat) · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_chimday.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/chimday_video.py ChimDayVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_chimday import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WIRE = "#9AA4B2"
COPPER = "#E0964E"


def bird(center, s=1.0, color=GROW):
    center = np.array(center, dtype=float)
    body = Ellipse(width=0.7 * s, height=0.42 * s).set_fill(color, 1).set_stroke(width=0).move_to(center + np.array([0, 0.12 * s, 0]))
    head = Circle(radius=0.16 * s).set_fill(color, 1).set_stroke(width=0).move_to(center + np.array([0.28 * s, 0.3 * s, 0]))
    beak = Polygon(center + np.array([0.4 * s, 0.32 * s, 0]), center + np.array([0.56 * s, 0.28 * s, 0]),
                   center + np.array([0.4 * s, 0.24 * s, 0])).set_fill(ACCENT, 1).set_stroke(width=0)
    tail = Polygon(center + np.array([-0.32 * s, 0.16 * s, 0]), center + np.array([-0.6 * s, 0.24 * s, 0]),
                   center + np.array([-0.32 * s, 0.06 * s, 0])).set_fill(color, 1).set_stroke(width=0)
    eye = Dot(center + np.array([0.33 * s, 0.33 * s, 0]), radius=0.03 * s).set_fill(BG, 1).set_stroke(width=0)
    leg1 = Line(center + np.array([0.1 * s, -0.08 * s, 0]), center + np.array([0.1 * s, -0.32 * s, 0])).set_stroke(ACCENT, 2)
    leg2 = Line(center + np.array([-0.05 * s, -0.08 * s, 0]), center + np.array([-0.05 * s, -0.32 * s, 0])).set_stroke(ACCENT, 2)
    return VGroup(tail, body, head, beak, eye, leg1, leg2)


class ChimDayVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_chimday")
    SEGMENTS = SEGMENTS
    TOPIC = "LÝ 11"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_dongdien()
        self.beat_nuoc()
        self.beat_haichan()
        self.beat_cungthe()
        self.beat_khongdong()
        self.beat_duongtat()
        self.beat_nguoi()
        self.beat_mach()
        self.beat_chet()
        self.beat_haiday()
        self.beat_cta()
        self.brand_stinger()
        self.wait(0.3)

    def _kara(self, seg, D):
        self._kar = self.make_karaoke(SEGMENTS[seg], D, self.beat_t0)
        self.add(self._kar)

    def _clear(self):
        self.end_karaoke(self._kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 1. HOOK — chim trên dây cao thế
    def beat_hook(self):
        t = fit_w(Text("Chim đậu dây cao thế", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        wire = Line([-2.1, 0.4, 0], [2.1, 0.4, 0]).set_stroke(WIRE, 5)
        b = bird([0, 0.55, 0], 1.2, GROW)
        volt = fit_w(Text("dòng điện chết người ngay dưới chân", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL), CW).move_to([0, -0.6, 0])
        q = fit_w(Text("Sao nó không bị giật?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -2.4, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Write(t), Create(wire), run_time=0.8)
            self.cue(D * 0.3); self.play(FadeIn(b, scale=0.7), run_time=0.6)
            self.cue(D * 0.55); self.play(FadeIn(volt, shift=UP * 0.1), run_time=0.7)
            self.cue(D * 0.85); self.play(Write(q), run_time=0.7)
            self._b = VGroup(t, wire, b, volt, q)
        self._clear()

    # 2. CẦN CHÊNH LỆCH ĐIỆN THẾ
    def beat_dongdien(self):
        t = fit_w(Text("Bị giật cần điều gì?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        r1 = fit_w(Text("KHÔNG phải vì chạm vào điện", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, 1.1, 0])
        r2 = fit_w(Text("mà vì CHÊNH LỆCH điện thế\ngiữa 2 điểm cơ thể chạm", font=FONT, weight=BOLD, color=GROW, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -0.4, 0])
        note = fit_w(Text("không chênh lệch → không dòng qua bạn", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.9, 0])
        with self.voice("02_dongdien") as D:
            self._kara("02_dongdien", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(r1, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.55); self.play(FadeIn(r2, shift=UP * 0.12), run_time=0.8)
            self.cue(D * 0.85); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, r1, r2, note)
        self._clear()

    # 3. VÍ DỤ NƯỚC
    def beat_nuoc(self):
        t = fit_w(Text("Giống như dòng nước", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        tankL = Rectangle(width=0.9, height=1.1).set_fill(PURPLE, 0.4).set_stroke(WIRE, 2).move_to([-1.1, 0.3, 0])
        tankR = Rectangle(width=0.9, height=1.1).set_fill(PURPLE, 0.4).set_stroke(WIRE, 2).move_to([1.1, 0.3, 0])
        pipe = Line([-0.65, -0.1, 0], [0.65, -0.1, 0]).set_stroke(WIRE, 4)
        note = fit_w(Text("hai bên NGANG BẰNG → nước đứng yên", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -1.7, 0])
        eq = fit_w(Text("chênh cao = 0 → không chảy", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), CW).move_to([0, 1.5, 0])
        with self.voice("03_nuoc") as D:
            self._kara("03_nuoc", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(tankL), FadeIn(tankR), Create(pipe), run_time=0.8)
            self.cue(D * 0.6); self.play(Write(eq), run_time=0.6)
            self.cue(D * 0.82); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, tankL, tankR, pipe, eq, note)
        self._clear()

    # 4. HAI CHÂN CÙNG 1 DÂY
    def beat_haichan(self):
        t = fit_w(Text("Hai chân, CÙNG 1 dây", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        wire = Line([-2.1, 0.2, 0], [2.1, 0.2, 0]).set_stroke(WIRE, 6)
        b = bird([0, 0.35, 0], 1.8, GROW)
        f1 = Dot([0.18, 0.06, 0], radius=0.06).set_fill(DEBT, 1).set_stroke(width=0)
        f2 = Dot([-0.09, 0.06, 0], radius=0.06).set_fill(DEBT, 1).set_stroke(width=0)
        note = fit_w(Text("2 chân cách nhau vài cm trên đúng 1 dây", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -1.8, 0])
        with self.voice("04_haichan") as D:
            self._kara("04_haichan", D)
            self.cue(D * 0.0); self.play(Write(t), Create(wire), run_time=0.7)
            self.cue(D * 0.35); self.play(FadeIn(b, scale=0.8), run_time=0.6)
            self.cue(D * 0.6); self.play(FadeIn(f1, scale=0.4), FadeIn(f2, scale=0.4), run_time=0.5)
            self.cue(D * 0.82); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, wire, b, f1, f2, note)
        self._clear()

    # 5. CÙNG ĐIỆN THẾ
    def beat_cungthe(self):
        t = fit_w(Text("2 chân ~ CÙNG điện thế", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        wire = Line([-2.1, 0.7, 0], [2.1, 0.7, 0]).set_stroke(WIRE, 6)
        vL = Text("V", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY).move_to([-0.5, 1.3, 0])
        vR = Text("V", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY).move_to([0.5, 1.3, 0])
        hero = fit_w(Text("ΔV giữa 2 chân ≈ 0", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO * 0.7), CW).move_to([0, -0.4, 0])
        note = fit_w(Text("hai điểm sát nhau trên dây tốt = cùng mức điện", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.8, 0])
        with self.voice("05_cungthe") as D:
            self._kara("05_cungthe", D)
            self.cue(D * 0.0); self.play(Write(t), Create(wire), run_time=0.7)
            self.cue(D * 0.35); self.play(FadeIn(vL), FadeIn(vR), run_time=0.6)
            self.cue(D * 0.6); self.play(Write(hero), Flash(hero.get_center(), color=GROW, line_length=0.4, num_lines=14), run_time=0.9)
            self.cue(D * 0.85); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, wire, vL, vR, hero, note)
        self._clear()

    # 6. KHÔNG DÒNG QUA CHIM
    def beat_khongdong(self):
        t = fit_w(Text("→ KHÔNG dòng qua chim", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        wire = Line([-2.1, 0.3, 0], [2.1, 0.3, 0]).set_stroke(WIRE, 6)
        b = bird([0, 0.45, 0], 1.5, GROW)
        flow = Arrow([-1.8, 0.3, 0], [1.8, 0.3, 0], color=ACCENT, buff=0, stroke_width=6)
        cross = VGroup(
            Line([-0.22, 0.9, 0], [0.22, 1.24, 0]).set_stroke(DEBT, 5),
            Line([-0.22, 1.24, 0], [0.22, 0.9, 0]).set_stroke(DEBT, 5),
        )
        note = fit_w(Text("thân chim không nằm trên đường đi của dòng", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -1.8, 0])
        with self.voice("06_khongdong") as D:
            self._kara("06_khongdong", D)
            self.cue(D * 0.0); self.play(Write(t), Create(wire), FadeIn(b), run_time=0.8)
            self.cue(D * 0.4); self.play(GrowArrow(flow), run_time=0.7)
            self.cue(D * 0.62); self.play(Create(cross), run_time=0.5)
            self.cue(D * 0.82); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, wire, b, flow, cross, note)
        self._clear()

    # 7. DÒNG CHỌN ĐƯỜNG DỄ
    def beat_duongtat(self):
        t = fit_w(Text("Dòng chọn đường DỄ nhất", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        r1 = fit_w(Text("dây đồng: điện trở CỰC NHỎ", font=FONT, weight=BOLD, color=COPPER).scale(SZ_LABEL), CW).move_to([0, 1.1, 0])
        r2 = fit_w(Text("thân chim: điện trở LỚN hơn nhiều", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), CW).move_to([0, -0.1, 0])
        big = fit_w(Text("→ dòng bỏ qua chim, chạy trong dây", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.4, 0])
        with self.voice("07_duongtat") as D:
            self._kara("07_duongtat", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(r1, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.55); self.play(FadeIn(r2, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.8); self.play(FadeIn(big, shift=UP * 0.12), Indicate(big, color=ACCENT), run_time=0.7)
            self._b = VGroup(t, r1, r2, big)
        self._clear()

    # 8. CON NGƯỜI THÌ KHÁC
    def beat_nguoi(self):
        t = fit_w(Text("Con người thì NGƯỢC LẠI", font=FONT, weight=BOLD, color=DEBT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        wire = Line([-2.1, 1.5, 0], [2.1, 1.5, 0]).set_stroke(WIRE, 5)
        ground = Line([-2.1, -2.1, 0], [2.1, -2.1, 0]).set_stroke(COPPER, 5)
        person = VGroup(
            Circle(radius=0.18).set_fill(MUTED, 1).set_stroke(width=0).move_to([0, 0.9, 0]),
            Line([0, 0.72, 0], [0, -0.2, 0]).set_stroke(MUTED, 5),
            Line([0, 0.5, 0], [0.35, 1.35, 0]).set_stroke(MUTED, 5),
            Line([0, -0.2, 0], [-0.3, -2.0, 0]).set_stroke(MUTED, 5),
            Line([0, -0.2, 0], [0.3, -2.0, 0]).set_stroke(MUTED, 5),
        )
        note = fit_w(Text("đứng trên đất mà chạm vào dây", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -2.5, 0])
        with self.voice("08_nguoi") as D:
            self._kara("08_nguoi", D)
            self.cue(D * 0.0); self.play(Write(t), Create(wire), Create(ground), run_time=0.8)
            self.cue(D * 0.4); self.play(Create(person), run_time=0.9)
            self.cue(D * 0.8); self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
            self._b = VGroup(t, wire, ground, person, note)
        self._clear()

    # 9. BẮC CẦU HAI MỨC ĐIỆN
    def beat_mach(self):
        t = fit_w(Text("Bắc cầu 2 mức điện", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        hi = fit_w(Text("dây: điện thế RẤT CAO", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, 1.5, 0])
        body = Arrow([0, 1.1, 0], [0, -1.1, 0], color=ACCENT, buff=0, stroke_width=9)
        blbl = Text("cơ thể bạn", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL).next_to(body, RIGHT, buff=0.2)
        lo = fit_w(Text("đất: điện thế = 0", font=FONT, weight=BOLD, color=COPPER).scale(SZ_LABEL), CW).move_to([0, -1.5, 0])
        hero = fit_w(Text("ΔV LỚN xuất hiện trên người", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, -2.4, 0])
        with self.voice("09_mach") as D:
            self._kara("09_mach", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(hi, shift=DOWN * 0.1), run_time=0.7)
            self.cue(D * 0.35); self.play(GrowArrow(body), FadeIn(blbl), run_time=0.7)
            self.cue(D * 0.6); self.play(FadeIn(lo, shift=UP * 0.1), run_time=0.6)
            self.cue(D * 0.82); self.play(Write(hero), Indicate(hero, color=DEBT), run_time=0.7)
            self._b = VGroup(t, hi, body, blbl, lo, hero)
        self._clear()

    # 10. DÒNG QUA TIM -> NGUY HIỂM
    def beat_chet(self):
        t = fit_w(Text("Dòng tràn qua TIM", font=FONT, weight=BOLD, color=DEBT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        heart = VGroup(
            Circle(radius=0.22).set_fill(DEBT, 1).set_stroke(width=0).move_to([-0.16, 0.7, 0]),
            Circle(radius=0.22).set_fill(DEBT, 1).set_stroke(width=0).move_to([0.16, 0.7, 0]),
            Triangle().set_fill(DEBT, 1).set_stroke(width=0).scale(0.42).rotate(PI).move_to([0, 0.42, 0]),
        )
        hero = fit_w(Text("vài chục mA qua tim = nguy hiểm", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -0.7, 0])
        note = fit_w(Text("đủ gây tử vong", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY), CW).move_to([0, -1.9, 0])
        with self.voice("10_chet") as D:
            self._kara("10_chet", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(GrowFromCenter(heart), run_time=0.6)
            self.cue(D * 0.45); self.play(heart.animate.scale(1.12), rate_func=there_and_back, run_time=0.6)
            self.cue(D * 0.6); self.play(FadeIn(hero, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.85); self.play(Write(note), run_time=0.6)
            self._b = VGroup(t, heart, hero, note)
        self._clear()

    # 11. CHIM CHẠM 2 DÂY CŨNG CHẾT
    def beat_haiday(self):
        t = fit_w(Text("Chim cũng không bất tử", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        w1 = Line([-2.1, 0.9, 0], [2.1, 0.9, 0]).set_stroke(WIRE, 5)
        w2 = Line([-2.1, -0.5, 0], [2.1, -0.5, 0]).set_stroke(WIRE, 5)
        b = bird([0, 0.4, 0], 1.4, GROW)
        spark = Flash([0, 0.2, 0], color=DEBT, line_length=0.5, num_lines=18)
        note = fit_w(Text("chạm 2 dây khác nhau, hoặc dây + cột đất\n→ cũng bị giật chết", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_SMALL), CW).move_to([0, -1.9, 0])
        with self.voice("11_haiday") as D:
            self._kara("11_haiday", D)
            self.cue(D * 0.0); self.play(Write(t), Create(w1), Create(w2), run_time=0.8)
            self.cue(D * 0.4); self.play(FadeIn(b, scale=0.8), run_time=0.6)
            self.cue(D * 0.62); self.play(spark, run_time=0.7)
            self.cue(D * 0.82); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, w1, w2, b, note)
        self._clear()

    # 12. CTA
    def beat_cta(self):
        l1 = fit_w(Text("Chạm 1 điểm: an toàn", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, 1.9, 0])
        l2 = fit_w(Text("Bắc cầu 2 mức điện: chết người", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("hiệu điện thế · dòng điện · điện trở", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, 0.25, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.7, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("THEO DÕI", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.75, 0])
        with self.voice("12_cta", gap=0.4) as D:
            self._kara("12_cta", D)
            self.cue(D * 0.0); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(l2, shift=UP * 0.12), Indicate(l2, color=GROW, scale_factor=1.06), run_time=0.8)
            self.cue(D * 0.55); self.play(FadeIn(tags, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.75); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, tags, sub)
        self._clear()
