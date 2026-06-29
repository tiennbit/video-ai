"""
"GPS định vị bạn đến từng mét bằng cách nào?" — toạ độ, mặt cầu, giao điểm + thuyết tương đối.
Toán 12 · SHORT DỌC 9:16 · ~2 phút (12 beat) · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_gps.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/gps_video.py GpsVideo
"""
import math
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_gps import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

YOU = np.array([0.0, 0.25, 0.0])
RAD = 1.12
SATS = [YOU + RAD * np.array([math.cos(math.radians(a)), math.sin(math.radians(a)), 0]) for a in (90, 210, 330)]


def sat_icon(p, color=ACCENT):
    body = Dot(p, radius=0.12).set_fill(MUTED, 1).set_stroke(WHITE, 1.5)
    pL = Rectangle(width=0.16, height=0.07).set_fill(color, 1).set_stroke(width=0).next_to(p, LEFT, buff=0.03)
    pR = Rectangle(width=0.16, height=0.07).set_fill(color, 1).set_stroke(width=0).next_to(p, RIGHT, buff=0.03)
    return VGroup(pL, body, pR)


def circ(i, color=ACCENT):
    return Circle(radius=RAD).set_stroke(color, 2.5).move_to(SATS[i])


def you_dot(dim=False):
    d = Dot(YOU, radius=0.14).set_fill(GROW if not dim else MUTED, 1).set_stroke(WHITE, 1.5)
    return d


class GpsVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_gps")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 12"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_vande()
        self.beat_thoigian()
        self.beat_tocdo()
        self.beat_motcau()
        self.beat_haicau()
        self.beat_bacau()
        self.beat_bonve()
        self.beat_chinhxac()
        self.beat_tuongdoi()
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

    # 1. HOOK
    def beat_hook(self):
        phone = RoundedRectangle(corner_radius=0.12, width=0.8, height=1.5).set_fill(BG_CARD, 1).set_stroke(MUTED, 2).move_to([0, -1.0, 0])
        pin = Dot(radius=0.1).set_fill(GROW, 1).set_stroke(WHITE, 1.5).move_to(phone.get_center() + UP * 0.1)
        sat = sat_icon([0, 2.2, 0])
        beam = DashedLine(sat[1].get_center(), pin.get_center()).set_stroke(ACCENT, 2, opacity=0.6)
        q = fit_w(Text("sai số chỉ vài mét ?!", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 0.6, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(sat, shift=DOWN * 0.2), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(phone), FadeIn(pin), Create(beam), run_time=0.7)
            self.cue(D * 0.7); self.play(Write(q), run_time=0.8)
            self._b = VGroup(phone, pin, sat, beam, q)
        self._clear()

    # 2. VẤN ĐỀ
    def beat_vande(self):
        l1 = fit_w(Text("Vệ tinh KHÔNG biết bạn ở đâu", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.2, 0])
        l2 = fit_w(Text("tất cả chỉ là", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.1, 0])
        l3 = fit_w(Text("BÀI TOÁN KHOẢNG CÁCH", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, -0.9, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.1); self.play(Write(l1), run_time=0.8)
            self.cue(D * 0.55); self.play(FadeIn(l2), run_time=0.5)
            self.cue(D * 0.72); self.play(Write(l3), run_time=0.8)
            self._b = VGroup(l1, l2, l3)
        self._clear()

    # 3. THỜI GIAN
    def beat_thoigian(self):
        t = fit_w(Text("Tín hiệu kèm thời điểm gửi", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        sat = sat_icon([0, 1.4, 0])
        waves = VGroup(*[Arc(radius=0.3 + k * 0.22, start_angle=-PI * 0.75, angle=PI * 0.5).set_stroke(ACCENT, 3, opacity=0.8 - k * 0.2).move_to([0, 1.0 - k * 0.1, 0]) for k in range(3)])
        phone = RoundedRectangle(corner_radius=0.1, width=0.7, height=1.3).set_fill(BG_CARD, 1).set_stroke(MUTED, 2).move_to([0, -1.2, 0])
        dt = fit_w(Text("→ đo Δt tín hiệu đã đi", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -2.3, 0])
        with self.voice("03_thoigian") as D:
            self._kara("03_thoigian", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(sat), run_time=0.7)
            self.cue(D * 0.35); self.play(LaggedStartMap(FadeIn, waves, lag_ratio=0.3), FadeIn(phone), run_time=1.0)
            self.cue(D * 0.78); self.play(Write(dt), run_time=0.6)
            self._b = VGroup(t, sat, waves, phone, dt)
        self._clear()

    # 4. TỐC ĐỘ
    def beat_tocdo(self):
        hero = Text("d = c × t", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO).move_to([0, 1.0, 0])
        c = fit_w(Text("c ≈ 300.000 km/s (tốc độ ánh sáng)", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -0.3, 0])
        note = fit_w(Text("→ ra khoảng cách tới vệ tinh", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -1.4, 0])
        with self.voice("04_tocdo") as D:
            self._kara("04_tocdo", D)
            self.cue(D * 0.0); self.play(Write(hero), run_time=0.9)
            self.cue(D * 0.45); self.play(FadeIn(c, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.75); self.play(FadeIn(note), run_time=0.6)
            self._b = VGroup(hero, c, note)
        self._clear()

    # 5. MỘT MẶT CẦU
    def beat_motcau(self):
        t = fit_w(Text("1 vệ tinh → 1 mặt cầu", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        s1, c1, you = sat_icon(SATS[0]), circ(0, ACCENT), you_dot(dim=True)
        note = fit_w(Text("bạn ở đâu đó trên mặt cầu này", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -2.2, 0])
        with self.voice("05_motcau") as D:
            self._kara("05_motcau", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(s1), run_time=0.7)
            self.cue(D * 0.4); self.play(Create(c1), FadeIn(you), run_time=0.9)
            self.cue(D * 0.8); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, s1, c1, you, note)
        self._clear()

    # 6. HAI MẶT CẦU
    def beat_haicau(self):
        t = fit_w(Text("2 vệ tinh → 1 đường tròn", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        s1, c1 = sat_icon(SATS[0]), circ(0, ACCENT)
        s2, c2, you = sat_icon(SATS[1]), circ(1, PURPLE), you_dot(dim=True)
        note = fit_w(Text("giao 2 mặt cầu → thu hẹp còn 1 vòng", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -2.2, 0])
        with self.voice("06_haicau") as D:
            self._kara("06_haicau", D)
            self.add(s1, c1, you)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(s2), run_time=0.7)
            self.cue(D * 0.4); self.play(Create(c2), run_time=0.9)
            self.cue(D * 0.8); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, s1, c1, s2, c2, you, note)
        self._clear()

    # 7. BA MẶT CẦU = BẠN
    def beat_bacau(self):
        t = fit_w(Text("3 vệ tinh → 1 ĐIỂM", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        s1, c1 = sat_icon(SATS[0]), circ(0, ACCENT)
        s2, c2 = sat_icon(SATS[1]), circ(1, PURPLE)
        s3, c3 = sat_icon(SATS[2]), circ(2, GROW)
        you = you_dot()
        lbl = Text("BẠN", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL).next_to(you, RIGHT, buff=0.12)
        with self.voice("07_bacau") as D:
            self._kara("07_bacau", D)
            self.add(s1, c1, s2, c2)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(s3), run_time=0.7)
            self.cue(D * 0.4); self.play(Create(c3), run_time=0.9)
            self.cue(D * 0.78); self.play(FadeIn(you, scale=0.5), Write(lbl), Flash(YOU, color=GROW, line_length=0.4, num_lines=14), run_time=0.9)
            self._b = VGroup(t, s1, c1, s2, c2, s3, c3, you, lbl)
        self._clear()

    # 8. VỆ TINH THỨ 4
    def beat_bonve(self):
        t = fit_w(Text("Vệ tinh thứ 4?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.0, 0])
        l1 = fit_w(Text("đồng hồ điện thoại không đủ chính xác", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, 0.6, 0])
        l2 = fit_w(Text("→ vệ tinh thứ 4 sửa lại sai lệch đồng hồ", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), CW).move_to([0, -0.6, 0])
        with self.voice("08_bonve") as D:
            self._kara("08_bonve", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.35); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.72); self.play(FadeIn(l2, shift=UP * 0.12), run_time=0.7)
            self._b = VGroup(t, l1, l2)
        self._clear()

    # 9. ĐỘ CHÍNH XÁC
    def beat_chinhxac(self):
        t = fit_w(Text("Vì nhân tốc độ ánh sáng…", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.2, 0])
        hero = fit_w(Text("sai 1 phần triệu giây", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 0.7, 0])
        big = Text("→ lệch 300 m", font=FONT, weight=BOLD, color=DEBT).scale(SZ_HERO * 0.95).move_to([0, -0.8, 0])
        with self.voice("09_chinhxac") as D:
            self._kara("09_chinhxac", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.35); self.play(FadeIn(hero, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.65); self.play(Write(big), Flash(big.get_center(), color=DEBT, line_length=0.5, num_lines=16), run_time=1.0)
            self._b = VGroup(t, hero, big)
        self._clear()

    # 10. THUYẾT TƯƠNG ĐỐI
    def beat_tuongdoi(self):
        t = fit_w(Text("Và thuyết tương đối", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.2, 0])
        l1 = fit_w(Text("đồng hồ vệ tinh chạy NHANH hơn dưới đất", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, 0.7, 0])
        l2 = fit_w(Text("không hiệu chỉnh →", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -0.5, 0])
        l3 = fit_w(Text("lệch hàng km MỖI NGÀY", font=FONT, weight=BOLD, color=DEBT).scale(SZ_TITLE), CW).move_to([0, -1.5, 0])
        with self.voice("10_tuongdoi") as D:
            self._kara("10_tuongdoi", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(l1, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.62); self.play(FadeIn(l2), run_time=0.4)
            self.cue(D * 0.78); self.play(Write(l3), Indicate(l3, color=DEBT), run_time=0.8)
            self._b = VGroup(t, l1, l2, l3)
        self._clear()

    # 11. ỨNG DỤNG
    def beat_ungdung(self):
        t = fit_w(Text("Cùng nguyên lý giao mặt cầu", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.3, 0])
        items = ["máy bay · tàu biển", "drone · xe tự lái", "bản đồ trong điện thoại"]
        rows = VGroup()
        for s in items:
            dot = Dot(radius=0.07).set_fill(ACCENT, 1).set_stroke(width=0)
            txt = Text(s, font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY)
            rows.add(VGroup(dot, txt).arrange(RIGHT, buff=0.2))
        rows.arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        fit_w(rows, CW).move_to([0, -0.3, 0])
        with self.voice("11_ungdung") as D:
            self._kara("11_ungdung", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            for i, r in enumerate(rows):
                self.cue(D * (0.25 + i * 0.2)); self.play(FadeIn(r, shift=RIGHT * 0.2), run_time=0.5)
            self._b = VGroup(t, rows)
        self._clear()

    # 12. CTA
    def beat_cta(self):
        l1 = fit_w(Text("Định vị = hình học toạ độ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.8, 0])
        l2 = fit_w(Text("+ chút thuyết tương đối", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("toạ độ · mặt cầu · giao điểm", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.3, 0])
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
