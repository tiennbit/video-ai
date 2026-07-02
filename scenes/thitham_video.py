"""
"Bí mật phòng thì thầm" — elip, hai tiêu điểm và tính chất phản xạ hội tụ.
Toán 10 · SHORT DỌC 9:16 · ~2 phút (12 beat) · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_thitham.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/thitham_video.py ThiThamVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_thitham import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Hình học elip dùng chung: a=1.9, b=1.25 -> c = sqrt(a^2-b^2) ~ 1.43
ELL_A, ELL_B = 1.9, 1.25
ELL_C = float(np.sqrt(ELL_A ** 2 - ELL_B ** 2))


def room(center=(0.0, 0.4), color=PURPLE):
    """Elip 'căn phòng' + 2 tiêu điểm. Trả về (ellipse, F1 dot, F2 dot, np center)."""
    c = np.array([center[0], center[1], 0.0])
    e = Ellipse(width=2 * ELL_A, height=2 * ELL_B).set_stroke(color, 3.5).move_to(c)
    f1 = Dot(c + np.array([-ELL_C, 0, 0]), radius=0.07).set_fill(GROW, 1).set_stroke(width=0)
    f2 = Dot(c + np.array([ELL_C, 0, 0]), radius=0.07).set_fill(DEBT, 1).set_stroke(width=0)
    return e, f1, f2, c


def ell_pt(c, theta):
    """Điểm trên elip tâm c theo góc tham số theta."""
    return c + np.array([ELL_A * np.cos(theta), ELL_B * np.sin(theta), 0.0])


def ray_pair(c, theta, col=ACCENT, w=3):
    """Cặp đoạn F1 -> P(theta) -> F2."""
    p = ell_pt(c, theta)
    f1 = c + np.array([-ELL_C, 0, 0])
    f2 = c + np.array([ELL_C, 0, 0])
    return VGroup(Line(f1, p).set_stroke(col, w), Line(p, f2).set_stroke(col, w))


def person(center, col=MUTED, scale=1.0):
    """Người tối giản: đầu + thân."""
    c = np.array([center[0], center[1], 0.0])
    head = Circle(radius=0.12 * scale).set_fill(col, 1).set_stroke(width=0).move_to(c + np.array([0, 0.3 * scale, 0]))
    body = RoundedRectangle(corner_radius=0.08 * scale, width=0.3 * scale, height=0.42 * scale)
    body.set_fill(col, 1).set_stroke(width=0).move_to(c)
    return VGroup(head, body)


class ThiThamVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_thitham")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 10"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_binhthuong()
        self.beat_elip()
        self.beat_tieudiem()
        self.beat_phanxa()
        self.beat_moitia()
        self.beat_cungpha()
        self.beat_thinghiem()
        self.beat_parabol()
        self.beat_soithan()
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

    # 1. HOOK — thì thầm xuyên 30 mét
    def beat_hook(self):
        t = fit_w(Text("Căn phòng thì thầm", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        dome = Arc(radius=1.9, start_angle=0, angle=PI).set_stroke(PURPLE, 4).move_to([0, 0.7, 0])
        p1 = person([-1.65, -0.55, 0], GROW)
        p2 = person([1.65, -0.55, 0], DEBT)
        whis = Text("thì thầm...", font=FONT, color=GROW).scale(SZ_SMALL).next_to(p1, UP, buff=0.15)
        dist = DoubleArrow([-1.55, -1.25, 0], [1.55, -1.25, 0], color=MUTED, buff=0, stroke_width=4)
        dlbl = Text("hơn 30 mét", font=FONT, weight=BOLD, color=MUTED).scale(SZ_SMALL).next_to(dist, DOWN, buff=0.1)
        q = fit_w(Text("Sao vẫn nghe RÕ TỪNG CHỮ?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -2.3, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Write(t), Create(dome), run_time=0.9)
            self.cue(D * 0.3); self.play(FadeIn(p1, scale=0.7), FadeIn(whis), run_time=0.6)
            self.cue(D * 0.5); self.play(FadeIn(p2, scale=0.7), GrowFromCenter(dist), FadeIn(dlbl), run_time=0.7)
            self.cue(D * 0.82); self.play(Write(q), run_time=0.7)
            self._b = VGroup(t, dome, p1, p2, whis, dist, dlbl, q)
        self._clear()

    # 2. BÌNH THƯỜNG — âm loang ra, yếu dần
    def beat_binhthuong(self):
        t = fit_w(Text("Âm thanh bình thường", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        src = Dot([0, 0.7, 0], radius=0.09).set_fill(GROW, 1).set_stroke(width=0)
        waves = VGroup(*[Circle(radius=r).set_stroke(GROW, 3, opacity=o).move_to([0, 0.7, 0])
                         for r, o in [(0.45, 0.9), (0.9, 0.55), (1.35, 0.3), (1.8, 0.15)]])
        note = fit_w(Text("loang ra mọi hướng\ncàng xa càng LOÃNG, càng YẾU", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -1.5, 0])
        sub = fit_w(Text("thì thầm vài mét đã khó nghe", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -2.35, 0])
        with self.voice("02_binhthuong") as D:
            self._kara("02_binhthuong", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(src, scale=0.5), run_time=0.6)
            self.cue(D * 0.25); self.play(LaggedStartMap(Create, waves, lag_ratio=0.25), run_time=1.4)
            self.cue(D * 0.55); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.85); self.play(FadeIn(sub), run_time=0.5)
            self._b = VGroup(t, src, waves, note, sub)
        self._clear()

    # 3. BÍ MẬT — hình dáng phòng là ELIP
    def beat_elip(self):
        t = fit_w(Text("Bí mật: hình dáng phòng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        e, _f1, _f2, c = room()
        hero = fit_w(Text("ELIP", font=FONT, weight=BOLD, color=PURPLE).scale(SZ_HERO), CW).move_to([0, -1.5, 0])
        note = fit_w(Text("mặt cắt vòm trần là một elip", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -2.4, 0])
        with self.voice("03_elip") as D:
            self._kara("03_elip", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.35); self.play(Create(e), run_time=1.3)
            self.cue(D * 0.7); self.play(Write(hero), FadeIn(note, shift=UP * 0.12), run_time=0.9)
            self._b = VGroup(t, e, hero, note)
        self._clear()

    # 4. HAI TIÊU ĐIỂM — tổng khoảng cách không đổi
    def beat_tieudiem(self):
        t = fit_w(Text("Hai TIÊU ĐIỂM giấu bên trong", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        e, f1, f2, c = room()
        l1 = Text("F1", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL).next_to(f1, DOWN, buff=0.1)
        l2 = Text("F2", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(f2, DOWN, buff=0.1)
        p = ell_pt(c, 1.15)
        m = Dot(p, radius=0.06).set_fill(ACCENT, 1).set_stroke(width=0)
        s1 = Line(f1.get_center(), p).set_stroke(GROW, 3)
        s2 = Line(p, f2.get_center()).set_stroke(DEBT, 3)
        rule = fit_w(Text("MF1 + MF2 = luôn KHÔNG ĐỔI", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -1.6, 0])
        with self.voice("04_tieudiem") as D:
            self._kara("04_tieudiem", D)
            self.cue(D * 0.0); self.play(Write(t), Create(e), run_time=0.8)
            self.cue(D * 0.25); self.play(FadeIn(f1, scale=0.5), FadeIn(f2, scale=0.5), FadeIn(l1), FadeIn(l2), run_time=0.7)
            self.cue(D * 0.5); self.play(FadeIn(m, scale=0.5), Create(s1), Create(s2), run_time=0.9)
            self.cue(D * 0.78); self.play(Write(rule), run_time=0.8)
            self._b = VGroup(t, e, f1, f2, l1, l2, m, s1, s2, rule)
        self._clear()

    # 5. PHẢN XẠ — tia từ F1 dội thành về F2
    def beat_phanxa(self):
        t = fit_w(Text("Tính chất phản xạ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        e, f1, f2, c = room()
        r = ray_pair(c, 1.35, ACCENT, 4)
        note = fit_w(Text("tia từ F1 đập vào thành\n→ bật ra bay thẳng về F2", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -1.7, 0])
        with self.voice("05_phanxa") as D:
            self._kara("05_phanxa", D)
            self.cue(D * 0.0); self.play(Write(t), Create(e), FadeIn(f1), FadeIn(f2), run_time=0.8)
            self.cue(D * 0.4); self.play(Create(r[0]), run_time=0.7)
            self.cue(D * 0.6); self.play(Create(r[1]), Flash(f2.get_center(), color=DEBT, line_length=0.3, num_lines=12), run_time=0.8)
            self.cue(D * 0.82); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, e, f1, f2, r, note)
        self._clear()

    # 6. MỌI TIA — 100% hội tụ về một điểm
    def beat_moitia(self):
        t = fit_w(Text("MỌI tia đều như vậy", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        e, f1, f2, c = room()
        thetas = [0.6, 1.1, 1.6, 2.1, 2.6, -1.1, -1.9, -2.5]
        rays = VGroup(*[ray_pair(c, th, ACCENT, 2.5) for th in thetas])
        hero = fit_w(Text("100% dội về ĐÚNG 1 ĐIỂM", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, -1.7, 0])
        with self.voice("06_moitia") as D:
            self._kara("06_moitia", D)
            self.cue(D * 0.0); self.play(Write(t), Create(e), FadeIn(f1), FadeIn(f2), run_time=0.8)
            self.cue(D * 0.3); self.play(LaggedStartMap(Create, rays, lag_ratio=0.1), run_time=2.0)
            self.cue(D * 0.75); self.play(Write(hero), Flash(f2.get_center(), color=DEBT, line_length=0.4, num_lines=14), run_time=0.9)
            self._b = VGroup(t, e, f1, f2, rays, hero)
        self._clear()

    # 7. CÙNG PHA — quãng đường bằng nhau, đến cùng lúc
    def beat_cungpha(self):
        t = fit_w(Text("Đến nơi CÙNG MỘT LÚC", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        e, f1, f2, c = room()
        r1 = ray_pair(c, 1.5, GROW, 3.5)
        r2 = ray_pair(c, -0.9, ACCENT, 3.5)
        eq = fit_w(Text("đường ngắn + đường dài\n= tổng LUÔN BẰNG NHAU", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -1.6, 0])
        sub = fit_w(Text("→ âm chồng lên nhau, không lệch nhịp", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL), CW).move_to([0, -2.45, 0])
        with self.voice("07_cungpha") as D:
            self._kara("07_cungpha", D)
            self.cue(D * 0.0); self.play(Write(t), Create(e), FadeIn(f1), FadeIn(f2), run_time=0.8)
            self.cue(D * 0.3); self.play(Create(r1[0]), Create(r1[1]), run_time=0.8)
            self.cue(D * 0.5); self.play(Create(r2[0]), Create(r2[1]), run_time=0.8)
            self.cue(D * 0.7); self.play(FadeIn(eq, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.9); self.play(FadeIn(sub), run_time=0.5)
            self._b = VGroup(t, e, f1, f2, r1, r2, eq, sub)
        self._clear()

    # 8. GIẢI THÍCH TRÒ ẢO THUẬT — người ở đúng 2 tiêu điểm
    def beat_thinghiem(self):
        t = fit_w(Text("Trò ảo thuật lộ bài", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        e, f1, f2, c = room()
        pa = person([c[0] - ELL_C, c[1] - 0.05, 0], GROW, 0.85)
        pb = person([c[0] + ELL_C, c[1] - 0.05, 0], DEBT, 0.85)
        la = Text("người nói ở F1", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL).move_to([-1.05, -1.35, 0])
        lb = Text("người nghe ở F2", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).move_to([1.05, -1.35, 0])
        note = fit_w(Text("cả căn phòng thành CHIẾC LOA\ngom âm về một chỗ", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -2.25, 0])
        rays = VGroup(*[ray_pair(c, th, ACCENT, 2) for th in [0.9, 1.7, 2.4]])
        with self.voice("08_thinghiem") as D:
            self._kara("08_thinghiem", D)
            self.cue(D * 0.0); self.play(Write(t), Create(e), run_time=0.8)
            self.cue(D * 0.3); self.play(FadeIn(pa, scale=0.7), FadeIn(la), run_time=0.6)
            self.cue(D * 0.48); self.play(FadeIn(pb, scale=0.7), FadeIn(lb), run_time=0.6)
            self.cue(D * 0.65); self.play(LaggedStartMap(Create, rays, lag_ratio=0.15), run_time=1.0)
            self.cue(D * 0.85); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, e, pa, pb, la, lb, rays, note)
        self._clear()

    # 9. HỌ HÀNG PARABOL — đèn pha, chảo vệ tinh
    def beat_parabol(self):
        t = fit_w(Text("Họ hàng của elip", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        # parabol mở sang phải: x = y^2 - 1
        par = FunctionGraph(lambda y: y * y - 1.0, x_range=[-1.35, 1.35], color=PURPLE).rotate(-PI / 2)
        par.set_stroke(PURPLE, 3.5).move_to([-0.9, 0.55, 0])
        bulb = Dot([-0.55, 0.55, 0], radius=0.08).set_fill(ACCENT, 1).set_stroke(width=0)
        beams = VGroup(*[Arrow([-0.35, y, 0], [1.75, y, 0], color=ACCENT, buff=0, stroke_width=3.5,
                               max_tip_length_to_length_ratio=0.06)
                         for y in [1.25, 0.9, 0.55, 0.2, -0.15]])
        note = fit_w(Text("đèn pha: đèn ở tiêu điểm → chùm thẳng\nchảo vệ tinh: sóng trời → dồn đầu thu", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_SMALL), CW).move_to([0, -1.8, 0])
        with self.voice("09_parabol") as D:
            self._kara("09_parabol", D)
            self.cue(D * 0.0); self.play(Write(t), Create(par), run_time=0.9)
            self.cue(D * 0.3); self.play(FadeIn(bulb, scale=0.5), Flash(bulb.get_center(), color=ACCENT, line_length=0.25, num_lines=10), run_time=0.6)
            self.cue(D * 0.5); self.play(LaggedStartMap(GrowArrow, beams, lag_ratio=0.12), run_time=1.1)
            self.cue(D * 0.8); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.7)
            self._b = VGroup(t, par, bulb, beams, note)
        self._clear()

    # 10. TÁN SỎI THẬN — chữa bệnh không cần mổ
    def beat_soithan(self):
        t = fit_w(Text("Elip chữa bệnh không cần mổ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.5, 0])
        e, f1, f2, c = room()
        src = Dot(f1.get_center(), radius=0.09).set_fill(ACCENT, 1).set_stroke(width=0)
        slbl = Text("nguồn sóng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_SMALL).next_to(src, DOWN, buff=0.12)
        stone = RegularPolygon(6, radius=0.14).set_fill(DEBT, 1).set_stroke(width=0).move_to(f2.get_center())
        klbl = Text("viên sỏi", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(stone, DOWN, buff=0.12)
        rays = VGroup(*[ray_pair(c, th, PURPLE, 2) for th in [0.7, 1.4, 2.1, -1.4]])
        note = fit_w(Text("sóng xung kích hội tụ đúng viên sỏi\n→ nghiền nát từ bên ngoài cơ thể", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_SMALL), CW).move_to([0, -1.85, 0])
        with self.voice("10_soithan") as D:
            self._kara("10_soithan", D)
            self.cue(D * 0.0); self.play(Write(t), Create(e), run_time=0.8)
            self.cue(D * 0.3); self.play(FadeIn(src, scale=0.5), FadeIn(slbl), FadeIn(stone, scale=0.5), FadeIn(klbl), run_time=0.7)
            self.cue(D * 0.55); self.play(LaggedStartMap(Create, rays, lag_ratio=0.12), run_time=1.2)
            self.cue(D * 0.75); self.play(Flash(stone.get_center(), color=DEBT, line_length=0.4, num_lines=14),
                                          FadeIn(note, shift=UP * 0.12), run_time=0.9)
            self._b = VGroup(t, e, src, slbl, stone, klbl, rays, note)
        self._clear()

    # 11. ỨNG DỤNG KHẮP NƠI
    def beat_ung(self):
        t = fit_w(Text("Cùng ý tưởng HỘI TỤ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        rows = [("kính thiên văn gom ánh sao mờ", GROW), ("micro gián điệp gom tiếng xa", ACCENT), ("lò mặt trời gom nắng nấu ăn", PURPLE)]
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
        l1 = fit_w(Text("Phòng thì thầm không có ma thuật", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.9, 0])
        l2 = fit_w(Text("chỉ là MỘT ĐƯỜNG ELIP", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("elip · tiêu điểm · phản xạ hội tụ", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.25, 0])
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
