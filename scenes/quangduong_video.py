"""
"Điện thoại biết bạn đi bao xa mà không cần GPS?" — quãng đường = diện tích dưới đồ thị
vận tốc = tích phân của v(t). Toán 12 (tích phân). SHORT DỌC 9:16 · ~1 phút 50 · KHÔNG intro.

Dùng bộ cỡ chữ chuẩn SZ_* (brand.py) + CANH NHỊP self.cue(): mỗi bước hiện hình được
rải trải đều theo lời đọc của cả đoạn (không dồn ở đầu beat).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_quangduong.py
Căn chỉnh:   .venv/bin/python scenes/align_narration.py output/narration_quangduong
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/quangduong_video.py QuangDuongVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_quangduong import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BLUE_V = "#60A5FA"   # đường vận tốc


def vt(t):
    """Vận tốc minh hoạ (km/h) theo thời gian t (phút): tăng tốc - chạy đều - giảm tốc."""
    if t < 3:
        return 12.0 * t / 3.0
    if t < 9:
        return 12.0
    return 12.0 * (12.0 - t) / 3.0


def velocity_axes():
    ax = Axes(
        x_range=[0, 12, 3], y_range=[0, 14, 7],
        x_length=2.9, y_length=2.4,
        axis_config={"include_tip": True, "tip_width": 0.16, "tip_height": 0.16,
                     "stroke_width": 3, "color": MUTED, "include_ticks": False},
    )
    return ax


class QuangDuongVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_quangduong")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 12"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_vande()
        self.beat_dothi()
        self.beat_dientich()
        self.beat_conso()
        self.beat_cta()
        self.brand_stinger()
        self.wait(0.3)

    def _kara(self, seg, D):
        self._kar = self.make_karaoke(SEGMENTS[seg], D, self.beat_t0)
        self.add(self._kar)

    def _clear(self):
        self.end_karaoke(self._kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 1. HOOK — điện thoại trong túi báo 2,4 km, không GPS ----------------
    def beat_hook(self):
        phone = RoundedRectangle(corner_radius=0.16, width=1.25, height=2.2).set_fill(BG_CARD, 1).set_stroke(BLUE_V, 3).move_to([0, 1.5, 0])
        screen = RoundedRectangle(corner_radius=0.1, width=1.0, height=1.7).set_fill("#0E1424", 1).set_stroke(width=0).move_to(phone)
        run = Text("CHẠY BỘ", font=FONT, weight=BOLD, color=MUTED).scale(SZ_SMALL).move_to(screen.get_top() + DOWN * 0.32)
        dist = Text("2,4 km", font=FONT, weight=BOLD, color=GROW).scale(SZ_TITLE).move_to(screen.get_center() + UP * 0.15)
        nogps = Text("GPS: TẮT", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).move_to(screen.get_center() + DOWN * 0.55)
        q = fit_w(Text("Sao biết đi bao xa?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO), CW).move_to([0, -1.5, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(phone, shift=DOWN * 0.2), FadeIn(screen), run_time=0.7)
            self.cue(D * 0.28); self.play(Write(run), Write(dist), run_time=0.8)
            self.cue(D * 0.55); self.play(FadeIn(nogps, scale=0.6), Indicate(nogps, color=DEBT, scale_factor=1.1), run_time=0.7)
            self.cue(D * 0.74); self.play(Write(q), run_time=0.9)
            self._b = VGroup(phone, screen, run, dist, nogps, q)
        self._clear()

    # 2. VẤN ĐỀ — cảm biến chỉ đo vận tốc, mà vận tốc thay đổi -----------
    def beat_vande(self):
        title = fit_w(Text("Cảm biến chỉ đo VẬN TỐC", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.4, 0])
        phases = VGroup(
            VGroup(Arrow([-0.35, 0, 0], [0.35, 0.35, 0], color=GROW, stroke_width=5, buff=0),
                   Text("tăng tốc", font=FONT, color=GROW).scale(SZ_LABEL)).arrange(DOWN, buff=0.18),
            VGroup(Arrow([-0.35, 0, 0], [0.35, 0, 0], color=ACCENT, stroke_width=5, buff=0),
                   Text("chạy đều", font=FONT, color=ACCENT).scale(SZ_LABEL)).arrange(DOWN, buff=0.18),
            VGroup(Arrow([-0.35, 0.35, 0], [0.35, 0, 0], color=DEBT, stroke_width=5, buff=0),
                   Text("chậm lại", font=FONT, color=DEBT).scale(SZ_LABEL)).arrange(DOWN, buff=0.18),
        ).arrange(RIGHT, buff=0.45).move_to([0, 0.9, 0])
        ask = fit_w(Text("Gộp lại thành QUÃNG ĐƯỜNG?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, -1.0, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.7)
            self.cue(D * 0.28); self.play(LaggedStart(*[FadeIn(p, shift=UP * 0.15) for p in phases], lag_ratio=0.3), run_time=1.2)
            self.cue(D * 0.7); self.play(Write(ask), run_time=0.8)
            self._b = VGroup(title, phases, ask)
        self._clear()

    # 3. ĐỒ THỊ — vẽ v(t): lên - ngang - xuống ---------------------------
    def beat_dothi(self):
        title = fit_w(Text("Vẽ vận tốc theo thời gian", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        ax = velocity_axes().move_to([0, 0.3, 0])
        xlab = Text("thời gian", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(ax, DOWN, buff=0.12)
        ylab = Text("vận tốc", font=FONT, color=MUTED).scale(SZ_SMALL).rotate(PI / 2).next_to(ax, LEFT, buff=0.1)
        curve = ax.plot(vt, x_range=[0, 12], color=BLUE_V, stroke_width=6)
        c_up = ax.plot(vt, x_range=[0, 3], color=GROW, stroke_width=6)
        c_flat = ax.plot(vt, x_range=[3, 9], color=ACCENT, stroke_width=6)
        c_dn = ax.plot(vt, x_range=[9, 12], color=DEBT, stroke_width=6)
        note = fit_w(Text("lên · ngang · xuống", font=FONT, weight=BOLD, color=MUTED).scale(SZ_BODY), CW).move_to([0, -1.7, 0])
        with self.voice("03_dothi") as D:
            self._kara("03_dothi", D)
            self.cue(D * 0.0); self.play(Create(ax), FadeIn(xlab), FadeIn(ylab), run_time=0.9)
            self.cue(D * 0.35); self.play(Create(c_up), run_time=0.6)
            self.cue(D * 0.5); self.play(Create(c_flat), run_time=0.6)
            self.cue(D * 0.62); self.play(Create(c_dn), run_time=0.6)
            self.add(curve); self.remove(c_up, c_flat, c_dn)
            self.cue(D * 0.8); self.play(FadeIn(note, shift=UP * 0.15), run_time=0.6)
            self._b = VGroup(title, ax, xlab, ylab, curve, note)
        self._clear()

    # 4. DIỆN TÍCH — quãng đường = diện tích dưới đường cong = tích phân --
    def beat_dientich(self):
        title = fit_w(Text("Quãng đường = DIỆN TÍCH", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        ax = velocity_axes().move_to([0, 0.5, 0])
        curve = ax.plot(vt, x_range=[0, 12], color=BLUE_V, stroke_width=6)
        area = ax.get_area(curve, x_range=[0, 12], color=ACCENT, opacity=0.35)
        sub = fit_w(Text("dưới đường cong vận tốc", font=FONT, color=MUTED).scale(SZ_LABEL), CW).next_to(ax, DOWN, buff=0.2)
        why = fit_w(Text("vận tốc × thời gian = quãng đường", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -1.4, 0])
        integ = fit_w(Text("s = tích phân v(t) dt", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, -2.2, 0])
        with self.voice("04_dientich") as D:
            self._kara("04_dientich", D)
            self.cue(D * 0.0); self.play(Create(ax), Create(curve), run_time=0.9)
            self.cue(D * 0.3); self.play(Write(title), run_time=0.7)
            self.cue(D * 0.45); self.play(FadeIn(area), FadeIn(sub), run_time=0.9)
            self.cue(D * 0.65); self.play(Write(why), run_time=0.8)
            self.cue(D * 0.82); self.play(Write(integ), run_time=0.9)
            self._b = VGroup(title, ax, curve, area, sub, why, integ)
        self._clear()

    # 5. CON SỐ — tam giác + chữ nhật + tam giác = 2,4 km ----------------
    def beat_conso(self):
        title = fit_w(Text("Chia thành 3 mảnh", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        ax = velocity_axes().move_to([0, 0.6, 0])
        curve = ax.plot(vt, x_range=[0, 12], color=BLUE_V, stroke_width=5)
        p0, p3, p9, p12 = ax.c2p(0, 0), ax.c2p(3, 12), ax.c2p(9, 12), ax.c2p(12, 0)
        b3, b9 = ax.c2p(3, 0), ax.c2p(9, 0)
        tri1 = Polygon(p0, p3, b3).set_fill(GROW, 0.5).set_stroke(GROW, 3)
        rect = Polygon(b3, p3, p9, b9).set_fill(ACCENT, 0.45).set_stroke(ACCENT, 3)
        tri2 = Polygon(b9, p9, p12).set_fill(DEBT, 0.5).set_stroke(DEBT, 3)
        labels = VGroup(
            Text("tam giác", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL),
            Text("+  chữ nhật", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL),
            Text("+  tam giác", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL),
        ).arrange(RIGHT, buff=0.2).move_to([0, -1.2, 0])
        fit_w(labels, CW)
        res = Text("= 2,4 km", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO).move_to([0, -2.1, 0])
        with self.voice("05_conso") as D:
            self._kara("05_conso", D)
            self.cue(D * 0.0); self.play(Write(title), Create(ax), Create(curve), run_time=0.9)
            self.cue(D * 0.28); self.play(FadeIn(tri1), FadeIn(labels[0]), run_time=0.6)
            self.cue(D * 0.42); self.play(FadeIn(rect), FadeIn(labels[1]), run_time=0.6)
            self.cue(D * 0.56); self.play(FadeIn(tri2), FadeIn(labels[2]), run_time=0.6)
            self.cue(D * 0.74); self.play(Write(res), Flash(res.get_center(), color=ACCENT, line_length=0.4, num_lines=18), run_time=1.0)
            self._b = VGroup(title, ax, curve, tri1, rect, tri2, labels, res)
        self._clear()

    # 6. CTA — tên lửa, máy bay, xe tự lái + đăng ký --------------------
    def beat_cta(self):
        idea = fit_w(Text("Diện tích dưới đồ thị vận tốc", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, 2.3, 0])
        icons = VGroup(
            VGroup(Triangle().set_fill(BLUE_V, 1).set_stroke(width=0).scale(0.28).rotate(-PI / 2),
                   Text("tên lửa", font=FONT, color=WHITE).scale(SZ_SMALL)).arrange(DOWN, buff=0.18),
            VGroup(Polygon([-0.3, -0.12, 0], [0.3, 0, 0], [-0.3, 0.12, 0]).set_fill(GROW, 1).set_stroke(width=0),
                   Text("máy bay", font=FONT, color=WHITE).scale(SZ_SMALL)).arrange(DOWN, buff=0.18),
            VGroup(RoundedRectangle(corner_radius=0.08, width=0.6, height=0.32).set_fill(DEBT, 1).set_stroke(width=0),
                   Text("xe tự lái", font=FONT, color=WHITE).scale(SZ_SMALL)).arrange(DOWN, buff=0.18),
        ).arrange(RIGHT, buff=0.4).move_to([0, 1.2, 0])
        l1 = fit_w(Text("Đều biết mình ở đâu nhờ tích phân", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, 0.1, 0])
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.5, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("ĐĂNG KÝ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -1.0, 0])
        with self.voice("06_cta", gap=0.4) as D:
            self._kara("06_cta", D)
            self.cue(D * 0.0); self.play(FadeIn(idea, shift=DOWN * 0.15), run_time=0.7)
            self.cue(D * 0.22); self.play(LaggedStart(*[FadeIn(ic, scale=0.6) for ic in icons], lag_ratio=0.25), run_time=1.0)
            self.cue(D * 0.5); self.play(Write(l1), run_time=0.8)
            self.cue(D * 0.72); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(idea, icons, l1, sub)
        self._clear()
