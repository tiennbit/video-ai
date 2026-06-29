"""
"Còi xe đổi tiếng khi vụt qua" — hiệu ứng Doppler.
Lý 12 · SHORT DỌC 9:16 · ~2 phút (12 beat) · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_coixe.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/coixe_video.py CoiXeVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_coixe import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WATER = "#5EC8F2"


def car(center, color=DEBT):
    body = RoundedRectangle(corner_radius=0.1, width=0.72, height=0.3).set_fill(color, 1).set_stroke(WHITE, 1.5)
    top = RoundedRectangle(corner_radius=0.08, width=0.4, height=0.22).set_fill(color, 1).set_stroke(WHITE, 1.5).next_to(body, UP, buff=-0.04)
    w1 = Dot(radius=0.08).set_fill("#1A1A1A", 1).set_stroke(width=0).move_to(body.get_bottom() + LEFT * 0.2)
    w2 = Dot(radius=0.08).set_fill("#1A1A1A", 1).set_stroke(width=0).move_to(body.get_bottom() + RIGHT * 0.2)
    return VGroup(body, top, w1, w2).move_to(center)


def vlines(x0, n, dx, color, y=0.55, h=0.85):
    return VGroup(*[Line([x0 + i * dx, y - h / 2, 0], [x0 + i * dx, y + h / 2, 0]).set_stroke(color, 3.5) for i in range(n)])


def rings(center, color=ACCENT, n=3, step=0.36):
    return VGroup(*[Circle(radius=step * k).set_stroke(color, 3, opacity=1 - 0.16 * k) for k in range(1, n + 1)]).move_to(center)


class CoiXeVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_coixe")
    SEGMENTS = SEGMENTS
    TOPIC = "LÝ 12"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_vande()
        self.beat_song()
        self.beat_dungyen()
        self.beat_laitoi()
        self.beat_caohon()
        self.beat_vuotqua()
        self.beat_doppler()
        self.beat_nhanh()
        self.beat_anhsang()
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
        amb = car([0, 0.9, 0], DEBT)
        rr = rings([0, 0.9, 0], ACCENT, 3, 0.4)
        q = fit_w(Text("Vụt qua → tiếng còi đổi ?!", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, -1.2, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(amb, shift=RIGHT * 0.2), run_time=0.6)
            self.cue(D * 0.3); self.play(LaggedStartMap(GrowFromCenter, rr, lag_ratio=0.2), run_time=0.9)
            self.cue(D * 0.7); self.play(Write(q), run_time=0.8)
            self._b = VGroup(amb, rr, q)
        self._clear()

    # 2. VẤN ĐỀ
    def beat_vande(self):
        l1 = fit_w(Text("Tài xế nghe còi Y HỆT", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.3, 0])
        l2 = fit_w(Text("thứ thay đổi nằm ở", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.2, 0])
        l3 = fit_w(Text("TAI người bên đường", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, -0.8, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.1); self.play(Write(l1), run_time=0.8)
            self.cue(D * 0.5); self.play(FadeIn(l2), run_time=0.5)
            self.cue(D * 0.7); self.play(Write(l3), run_time=0.8)
            self._b = VGroup(l1, l2, l3)
        self._clear()

    # 3. SÓNG
    def beat_song(self):
        t = fit_w(Text("Âm thanh = các vòng sóng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        rr = rings([0, 0.7, 0], ACCENT, 4, 0.42)
        src = Dot([0, 0.7, 0], radius=0.09).set_fill(WHITE, 1).set_stroke(width=0)
        note = fit_w(Text("sóng DÀY → cao   ·   sóng THƯA → trầm", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -1.9, 0])
        with self.voice("03_song") as D:
            self._kara("03_song", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(src), run_time=0.7)
            self.cue(D * 0.3); self.play(LaggedStartMap(GrowFromCenter, rr, lag_ratio=0.18), run_time=1.2)
            self.cue(D * 0.8); self.play(FadeIn(note), run_time=0.6)
            self._b = VGroup(t, rr, src, note)
        self._clear()

    # 4. ĐỨNG YÊN
    def beat_dungyen(self):
        t = fit_w(Text("Nguồn đứng yên", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        rr = rings([0, 0.5, 0], GROW, 4, 0.46)
        src = Dot([0, 0.5, 0], radius=0.1).set_fill(WHITE, 1).set_stroke(width=0)
        note = fit_w(Text("sóng đều mọi phía → 2 bên nghe như nhau", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -2.2, 0])
        with self.voice("04_dungyen") as D:
            self._kara("04_dungyen", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(src), run_time=0.6)
            self.cue(D * 0.3); self.play(LaggedStartMap(GrowFromCenter, rr, lag_ratio=0.15), run_time=1.0)
            self.cue(D * 0.8); self.play(FadeIn(note), run_time=0.6)
            self._b = VGroup(t, rr, src, note)
        self._clear()

    # 5. LAO TỚI — Doppler diagram (điểm nhấn)
    def beat_laitoi(self):
        t = fit_w(Text("Xe lao về phía bạn →", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        c = car([0, 0.6, 0], DEBT)
        arrow = Arrow([0.45, 0.6, 0], [1.15, 0.6, 0], color=WHITE, buff=0, stroke_width=4)
        front = vlines(0.55, 4, 0.2, DEBT, y=0.6, h=0.95)        # dồn (phải, trước)
        back = vlines(-0.55, 3, -0.5, WATER, y=0.6, h=0.95)      # giãn (trái, sau)
        fl = Text("DỒN", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).move_to([1.3, -0.25, 0])
        bl = Text("giãn", font=FONT, weight=BOLD, color=WATER).scale(SZ_SMALL).move_to([-1.5, -0.25, 0])
        note = fit_w(Text("sóng phía trước bị ÉP SÁT vào nhau", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        with self.voice("05_laitoi") as D:
            self._kara("05_laitoi", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(c), GrowArrow(arrow), run_time=0.8)
            self.cue(D * 0.4); self.play(Create(back), FadeIn(bl), run_time=0.6)
            self.cue(D * 0.6); self.play(Create(front), FadeIn(fl), run_time=0.7)
            self.cue(D * 0.85); self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
            self._b = VGroup(t, c, arrow, front, back, fl, bl, note)
        self._clear()

    # 6. CAO HƠN
    def beat_caohon(self):
        t = fit_w(Text("Phía trước: sóng DỒN", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.0, 0])
        dense = vlines(-0.7, 7, 0.22, DEBT, y=0.5, h=0.9)
        hero = fit_w(Text("→ TẦN SỐ CAO → nghe gắt", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY), CW).move_to([0, -1.0, 0])
        with self.voice("06_caohon") as D:
            self._kara("06_caohon", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.35); self.play(Create(dense), run_time=0.8)
            self.cue(D * 0.72); self.play(Write(hero), run_time=0.8)
            self._b = VGroup(t, dense, hero)
        self._clear()

    # 7. VƯỢT QUA
    def beat_vuotqua(self):
        t = fit_w(Text("Xe vượt qua, chạy ra xa", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.0, 0])
        sparse = vlines(-1.3, 5, 0.62, WATER, y=0.5, h=0.9)
        note = fit_w(Text("sóng phía sau bị KÉO GIÃN ra", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -1.0, 0])
        with self.voice("07_vuotqua") as D:
            self._kara("07_vuotqua", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.35); self.play(Create(sparse), run_time=0.8)
            self.cue(D * 0.72); self.play(FadeIn(note, shift=UP * 0.1), run_time=0.7)
            self._b = VGroup(t, sparse, note)
        self._clear()

    # 8. DOPPLER
    def beat_doppler(self):
        hero = fit_w(Text("sóng thưa → TẦN SỐ THẤP", font=FONT, weight=BOLD, color=WATER).scale(SZ_BODY), CW).move_to([0, 1.4, 0])
        sub = fit_w(Text("→ tiếng còi tụt TRẦM ngay", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 0.2, 0])
        name = fit_w(Text("= hiệu ứng DOPPLER", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, -1.2, 0])
        with self.voice("08_doppler") as D:
            self._kara("08_doppler", D)
            self.cue(D * 0.0); self.play(FadeIn(hero, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.35); self.play(FadeIn(sub, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.7); self.play(Write(name), Flash(name.get_center(), color=ACCENT, line_length=0.4, num_lines=14), run_time=0.9)
            self._b = VGroup(hero, sub, name)
        self._clear()

    # 9. CÀNG NHANH
    def beat_nhanh(self):
        t = fit_w(Text("Xe càng nhanh → càng rõ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.6, 0])
        hero = Text("60 km/h", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO).move_to([0, 0.1, 0])
        note = fit_w(Text("đủ làm độ cao tiếng còi nhảy 1 bậc rõ rệt", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.3, 0])
        with self.voice("09_nhanh") as D:
            self._kara("09_nhanh", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.4); self.play(Write(hero), run_time=0.8)
            self.cue(D * 0.78); self.play(FadeIn(note), run_time=0.6)
            self._b = VGroup(t, hero, note)
        self._clear()

    # 10. ÁNH SÁNG
    def beat_anhsang(self):
        t = fit_w(Text("Ánh sáng cũng có Doppler", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.3, 0])
        star = Star(n=5, outer_radius=0.3, inner_radius=0.13).set_fill(WHITE, 1).set_stroke(width=0).move_to([-1.0, 0.7, 0])
        arrow = Arrow([-0.6, 0.7, 0], [0.3, 0.7, 0], color=MUTED, buff=0, stroke_width=4)
        red = Dot([1.0, 0.7, 0], radius=0.26).set_fill(DEBT, 1).set_stroke(width=0)
        l = fit_w(Text("sao chạy ra xa → ngả ĐỎ", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY), CW).move_to([0, -0.7, 0])
        l2 = fit_w(Text("= dịch chuyển đỏ (redshift)", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.6, 0])
        with self.voice("10_anhsang") as D:
            self._kara("10_anhsang", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(star), run_time=0.7)
            self.cue(D * 0.4); self.play(GrowArrow(arrow), FadeIn(red, shift=RIGHT * 0.1), run_time=0.7)
            self.cue(D * 0.65); self.play(Write(l), run_time=0.6)
            self.cue(D * 0.85); self.play(FadeIn(l2), run_time=0.5)
            self._b = VGroup(t, star, arrow, red, l, l2)
        self._clear()

    # 11. ỨNG DỤNG
    def beat_ungdung(self):
        t = fit_w(Text("Doppler ở khắp nơi", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.3, 0])
        items = ["vũ trụ đang giãn nở", "súng bắn tốc độ", "siêu âm dòng máu tim"]
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
        l1 = fit_w(Text("Đứng yên hay chuyển động", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.8, 0])
        l2 = fit_w(Text("nghe khác hẳn", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("sóng âm · tần số · Doppler", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.3, 0])
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
