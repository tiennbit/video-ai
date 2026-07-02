"""
"Tai nghe khử ồn: cộng âm ra im lặng" — giao thoa sóng, triệt tiêu ngược pha.
Lý 11 · SHORT DỌC 9:16 · ~2 phút (12 beat) · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_chongon.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/chongon_video.py ChongOnVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_chongon import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WAVE_W = 3.6  # bề ngang đồ thị sóng


def wave(y0, amp=0.45, phase=0.0, color=GROW, k=3.0, w=WAVE_W, stroke=3.5):
    """Sóng sin nằm ngang, tâm tại y0."""
    g = FunctionGraph(lambda x: amp * np.sin(k * x + phase), x_range=[-w / 2, w / 2], color=color)
    return g.set_stroke(color, stroke).move_to([0, y0, 0])


def earcup(center, color=PURPLE, scale=1.0):
    """Củ tai nghe tối giản: vòng ngoài + đệm."""
    c = np.array([center[0], center[1], 0.0])
    outer = RoundedRectangle(corner_radius=0.22, width=0.85 * scale, height=1.15 * scale)
    outer.set_fill(BG_CARD, 1).set_stroke(color, 3).move_to(c)
    pad = RoundedRectangle(corner_radius=0.16, width=0.5 * scale, height=0.85 * scale)
    pad.set_fill(color, 0.35).set_stroke(width=0).move_to(c)
    return VGroup(outer, pad)


class ChongOnVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_chongon")
    SEGMENTS = SEGMENTS
    TOPIC = "VẬT LÝ 11"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_song()
        self.beat_cong()
        self.beat_nguocpha()
        self.beat_dieukien()
        self.beat_mic()
        self.beat_chip()
        self.beat_tong()
        self.beat_gioihan()
        self.beat_vantoi()
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

    # 1. HOOK — bấm 1 nút, thế giới im bặt
    def beat_hook(self):
        t = fit_w(Text("Nút bấm IM LẶNG", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        plane = fit_w(Text("động cơ máy bay: ầm ầm ầm...", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, 1.4, 0])
        cup = earcup([0, 0.1, 0], PURPLE, 1.15)
        btn = Circle(radius=0.09).set_fill(ACCENT, 1).set_stroke(width=0).move_to([0.55, 0.35, 0])
        silent = fit_w(Text("...im bặt", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, -1.1, 0])
        tw = fit_w(Text("Nó KHÔNG chặn âm thanh\nnó tạo THÊM âm thanh?!", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -2.15, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(plane, shift=UP * 0.1), run_time=0.8)
            self.cue(D * 0.3); self.play(FadeIn(cup, scale=0.7), FadeIn(btn, scale=0.5),
                                         Flash(btn.get_center(), color=ACCENT, line_length=0.2, num_lines=10), run_time=0.8)
            self.cue(D * 0.5); self.play(FadeOut(plane), FadeIn(silent, shift=UP * 0.1), run_time=0.7)
            self.cue(D * 0.78); self.play(Write(tw), run_time=0.8)
            self._b = VGroup(t, cup, btn, silent, tw)
        self._clear()

    # 2. ÂM THANH LÀ SÓNG
    def beat_song(self):
        t = fit_w(Text("Âm thanh là SÓNG", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        w1 = wave(0.5, 0.5, 0.0, GROW)
        peak = Text("đỉnh", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL).move_to([-0.75, 1.35, 0])
        trough = Text("đáy", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL).move_to([0.3, -0.4, 0])
        note = fit_w(Text("lan trong không khí\nđỉnh và đáy nối nhau đều đặn", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -1.8, 0])
        with self.voice("02_song") as D:
            self._kara("02_song", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(Create(w1), run_time=1.2)
            self.cue(D * 0.6); self.play(FadeIn(peak, shift=DOWN * 0.1), FadeIn(trough, shift=UP * 0.1), run_time=0.6)
            self.cue(D * 0.82); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, w1, peak, trough, note)
        self._clear()

    # 3. CÙNG PHA — to gấp đôi
    def beat_cong(self):
        t = fit_w(Text("Hai sóng CỘNG vào nhau", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        w1 = wave(1.3, 0.32, 0.0, GROW)
        w2 = wave(0.35, 0.32, 0.0, PURPLE)
        plus = Text("+", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to([-2.0, 0.85, 0])
        line = DashedLine([-1.9, -0.35, 0], [1.9, -0.35, 0]).set_stroke(MUTED, 2)
        w3 = wave(-1.25, 0.62, 0.0, ACCENT)
        lbl = fit_w(Text("đỉnh gặp đỉnh → TO GẤP ĐÔI", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, -2.35, 0])
        with self.voice("03_cong") as D:
            self._kara("03_cong", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.28); self.play(Create(w1), run_time=0.7)
            self.cue(D * 0.45); self.play(Create(w2), FadeIn(plus), run_time=0.7)
            self.cue(D * 0.65); self.play(Create(line), Create(w3), run_time=0.9)
            self.cue(D * 0.85); self.play(Write(lbl), run_time=0.6)
            self._b = VGroup(t, w1, w2, plus, line, w3, lbl)
        self._clear()

    # 4. NGƯỢC PHA — tổng bằng 0
    def beat_nguocpha(self):
        t = fit_w(Text("Kịch bản kỳ diệu hơn", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        w1 = wave(1.3, 0.32, 0.0, GROW)
        w2 = wave(0.35, 0.32, PI, DEBT)
        plus = Text("+", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to([-2.0, 0.85, 0])
        flat = Line([-WAVE_W / 2, -1.25, 0], [WAVE_W / 2, -1.25, 0]).set_stroke(ACCENT, 4)
        zero = fit_w(Text("đỉnh gặp đáy → tổng = 0", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -2.35, 0])
        with self.voice("04_nguocpha") as D:
            self._kara("04_nguocpha", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.28); self.play(Create(w1), run_time=0.7)
            self.cue(D * 0.48); self.play(Create(w2), FadeIn(plus), run_time=0.7)
            self.cue(D * 0.7); self.play(Create(flat), run_time=0.8)
            self.cue(D * 0.87); self.play(Write(zero), run_time=0.6)
            self._b = VGroup(t, w1, w2, plus, flat, zero)
        self._clear()

    # 5. ĐIỀU KIỆN TRIỆT TIÊU
    def beat_dieukien(self):
        t = fit_w(Text("GIAO THOA TRIỆT TIÊU", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        card = RoundedRectangle(corner_radius=0.2, width=3.4, height=1.5).set_fill(BG_CARD, 1).set_stroke(GROW, 2.5).move_to([0, 0.9, 0])
        rule = fit_w(Text("lệch nhau NỬA BƯỚC SÓNG\n= ngược pha hoàn toàn", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.1).scale(SZ_BODY), 3.0).move_to(card)
        hero = fit_w(Text("ồn + ồn = IM LẶNG", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO * 0.8), CW).move_to([0, -1.2, 0])
        with self.voice("05_dieukien") as D:
            self._kara("05_dieukien", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.7)
            self.cue(D * 0.3); self.play(GrowFromCenter(card), Write(rule), run_time=1.0)
            self.cue(D * 0.7); self.play(Write(hero), Flash(hero.get_center(), color=GROW, line_length=0.4, num_lines=14), run_time=0.9)
            self._b = VGroup(t, card, rule, hero)
        self._clear()

    # 6. MICRO NGHE LÉN TIẾNG ỒN
    def beat_mic(self):
        t = fit_w(Text("Bước 1: NGHE LÉN", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        cup = earcup([0.4, 0.2, 0], PURPLE, 1.3)
        mics = VGroup(*[Dot([mx, my, 0], radius=0.07).set_fill(ACCENT, 1).set_stroke(width=0)
                        for mx, my in [(-0.2, 0.85), (-0.25, 0.2), (-0.2, -0.45)]])
        mlbl = Text("micro tí hon", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL).move_to([-1.3, 1.1, 0])
        noise = wave(0.2, 0.22, 0.0, DEBT, k=5.0, w=1.3).move_to([-1.55, 0.2, 0])
        nlbl = Text("tiếng ồn", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(noise, DOWN, buff=0.12)
        note = fit_w(Text("liên tục thu mọi tiếng ồn lao đến", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -2.0, 0])
        with self.voice("06_mic") as D:
            self._kara("06_mic", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(cup, scale=0.8), run_time=0.7)
            self.cue(D * 0.35); self.play(LaggedStartMap(FadeIn, mics, lag_ratio=0.2), FadeIn(mlbl), run_time=0.8)
            self.cue(D * 0.6); self.play(Create(noise), FadeIn(nlbl), run_time=0.8)
            self.cue(D * 0.85); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, cup, mics, mlbl, noise, nlbl, note)
        self._clear()

    # 7. CHIP ĐẢO SÓNG
    def beat_chip(self):
        t = fit_w(Text("Bước 2: LỘN NGƯỢC sóng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        chip = RoundedRectangle(corner_radius=0.12, width=1.1, height=1.1).set_fill(BG_CARD, 1).set_stroke(ACCENT, 3).move_to([0, 1.2, 0])
        clbl = Text("CHIP", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL).move_to(chip)
        w_in = wave(0.0, 0.28, 0.0, DEBT, k=4.0, w=2.6).move_to([0, -0.1, 0])
        w_out = wave(0.0, 0.28, PI, GROW, k=4.0, w=2.6).move_to([0, -1.1, 0])
        olbl = fit_w(Text("đỉnh thành đáy — trong chưa đến 1/1000 giây", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -2.0, 0])
        with self.voice("07_chip") as D:
            self._kara("07_chip", D)
            self.cue(D * 0.0); self.play(Write(t), GrowFromCenter(chip), FadeIn(clbl), run_time=0.8)
            self.cue(D * 0.3); self.play(Create(w_in), run_time=0.8)
            self.cue(D * 0.55); self.play(Create(w_out), run_time=0.8)
            self.cue(D * 0.82); self.play(FadeIn(olbl, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, chip, clbl, w_in, w_out, olbl)
        self._clear()

    # 8. TỔNG TẠI TAI = IM LẶNG
    def beat_tong(self):
        t = fit_w(Text("Bước 3: chạm mặt tại tai", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        w1 = wave(1.35, 0.3, 0.0, DEBT, k=4.0)
        l1 = Text("ồn thật", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).move_to([-1.55, 1.9, 0])
        w2 = wave(0.4, 0.3, PI, GROW, k=4.0)
        l2 = Text("bản sao lộn ngược", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL).move_to([-1.05, 0.95, 0])
        flat = Line([-WAVE_W / 2, -1.0, 0], [WAVE_W / 2, -1.0, 0]).set_stroke(ACCENT, 4)
        hero = fit_w(Text("TAN BIẾN thành im lặng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, -2.0, 0])
        with self.voice("08_tong") as D:
            self._kara("08_tong", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.25); self.play(Create(w1), FadeIn(l1), run_time=0.7)
            self.cue(D * 0.45); self.play(Create(w2), FadeIn(l2), run_time=0.7)
            self.cue(D * 0.7); self.play(Create(flat), run_time=0.8)
            self.cue(D * 0.87); self.play(Write(hero), run_time=0.6)
            self._b = VGroup(t, w1, l1, w2, l2, flat, hero)
        self._clear()

    # 9. GIỚI HẠN — vì sao giọng nói vẫn lọt
    def beat_gioihan(self):
        t = fit_w(Text("Vì sao giọng nói vẫn lọt?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        r1c = RoundedRectangle(corner_radius=0.16, width=3.3, height=1.05).set_fill(BG_CARD, 1).set_stroke(GROW, 2.5).move_to([0, 0.95, 0])
        r1 = fit_w(Text("tiếng ù ĐỀU ĐẶN\n→ đoán trước được → khử sạch", font=FONT, weight=BOLD, color=GROW, line_spacing=1.05).scale(SZ_SMALL), 3.0).move_to(r1c)
        r2c = RoundedRectangle(corner_radius=0.16, width=3.3, height=1.05).set_fill(BG_CARD, 1).set_stroke(DEBT, 2.5).move_to([0, -0.45, 0])
        r2 = fit_w(Text("giọng nói ĐỘT NGỘT\n→ đảo không kịp → chỉ khử một phần", font=FONT, weight=BOLD, color=DEBT, line_spacing=1.05).scale(SZ_SMALL), 3.0).move_to(r2c)
        note = fit_w(Text("nên ANC giỏi nhất với tiếng động cơ", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.75, 0])
        with self.voice("09_gioihan") as D:
            self._kara("09_gioihan", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.7)
            self.cue(D * 0.3); self.play(GrowFromCenter(VGroup(r1c, r1)), run_time=0.8)
            self.cue(D * 0.6); self.play(GrowFromCenter(VGroup(r2c, r2)), run_time=0.8)
            self.cue(D * 0.88); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, r1c, r1, r2c, r2, note)
        self._clear()

    # 10. VÂN LẶNG TRÊN MẶT NƯỚC
    def beat_vantoi(self):
        t = fit_w(Text("Trên mặt hồ cũng vậy", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        s1 = Dot([-0.9, 0.9, 0], radius=0.08).set_fill(GROW, 1).set_stroke(width=0)
        s2 = Dot([0.9, 0.9, 0], radius=0.08).set_fill(PURPLE, 1).set_stroke(width=0)
        rip1 = VGroup(*[Circle(radius=r).set_stroke(GROW, 2, opacity=o).move_to(s1.get_center())
                        for r, o in [(0.35, 0.8), (0.7, 0.5), (1.05, 0.3)]])
        rip2 = VGroup(*[Circle(radius=r).set_stroke(PURPLE, 2, opacity=o).move_to(s2.get_center())
                        for r, o in [(0.35, 0.8), (0.7, 0.5), (1.05, 0.3)]])
        calm = DashedLine([0, 0.15, 0], [0, -1.15, 0]).set_stroke(ACCENT, 3)
        clbl = fit_w(Text("vân LẶNG: nước đứng yên lạ thường", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL), CW).move_to([0, -1.6, 0])
        note = fit_w(Text("hai gợn ngược pha gặp nhau và tự xoá", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -2.3, 0])
        with self.voice("10_vantoi") as D:
            self._kara("10_vantoi", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(s1), FadeIn(s2), run_time=0.7)
            self.cue(D * 0.3); self.play(LaggedStartMap(Create, rip1, lag_ratio=0.2),
                                         LaggedStartMap(Create, rip2, lag_ratio=0.2), run_time=1.3)
            self.cue(D * 0.65); self.play(Create(calm), Write(clbl), run_time=0.8)
            self.cue(D * 0.88); self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
            self._b = VGroup(t, s1, s2, rip1, rip2, calm, clbl, note)
        self._clear()

    # 11. ỨNG DỤNG
    def beat_ung(self):
        t = fit_w(Text("Phép cộng ra SỐ KHÔNG", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        rows = [("cabin xe hơi tự khử ồn máy", GROW), ("ống xả chủ động dịu tiếng nổ", ACCENT), ("phòng thu lọc sạch tạp âm", PURPLE)]
        chips = VGroup()
        for txt, col in rows:
            card = RoundedRectangle(corner_radius=0.16, width=3.2, height=0.9).set_fill(BG_CARD, 1).set_stroke(col, 2.5)
            lab = fit_w(Text(txt, font=FONT, weight=BOLD, color=col).scale(SZ_LABEL), 2.9).move_to(card)
            chips.add(VGroup(card, lab))
        chips.arrange(DOWN, buff=0.35).move_to([0, -0.3, 0])
        with self.voice("11_ung") as D:
            self._kara("11_ung", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            for i, ch in enumerate(chips):
                self.cue(D * (0.28 + 0.22 * i)); self.play(GrowFromCenter(ch), run_time=0.55)
            self._b = VGroup(t, chips)
        self._clear()

    # 12. CTA
    def beat_cta(self):
        l1 = fit_w(Text("Nút im lặng không phải phép màu", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.9, 0])
        l2 = fit_w(Text("chỉ là SÓNG NGƯỢC PHA", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("giao thoa · triệt tiêu · nửa bước sóng", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.25, 0])
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
