"""
"Vì sao lon nước ngọt có đúng hình dạng đó?" — tối ưu diện tích vỏ, đạo hàm, cực trị (h = 2r).
Toán 12 · SHORT DỌC 9:16 · ~2 phút (12 beat) · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_lonnuoc.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/lonnuoc_video.py LonNuocVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_lonnuoc import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ALU = "#C8CDD8"


def can(center, r, h, color=ALU):
    center = np.array(center, dtype=float)
    body = RoundedRectangle(corner_radius=0.12, width=2 * r, height=h).set_fill(color, 0.85).set_stroke(WHITE, 2).move_to(center)
    top = Ellipse(width=2 * r, height=r * 0.5).set_fill("#E8ECF2", 1).set_stroke(WHITE, 2).move_to(center + np.array([0, h / 2, 0]))
    return VGroup(body, top)


class LonNuocVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_lonnuoc")
    SEGMENTS = SEGMENTS
    TOPIC = "TOÁN 12"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_baitoan()
        self.beat_bien()
        self.beat_dientich()
        self.beat_the()
        self.beat_hamso()
        self.beat_daoham()
        self.beat_giai()
        self.beat_ketqua()
        self.beat_thucte()
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
        t = fit_w(Text("Hàng trăm tỉ lon mỗi năm", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.5, 0])
        c = can([0, 0.4, 0], 0.55, 1.7)
        q = fit_w(Text("Hình dạng này KHÔNG ngẫu nhiên", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.7, 0])
        sub = fit_w(Text("toán chọn để tốn ít nhôm nhất", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL), CW).move_to([0, -2.5, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(GrowFromEdge(c, DOWN), run_time=0.8)
            self.cue(D * 0.6); self.play(FadeIn(q, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.85); self.play(Write(sub), run_time=0.6)
            self._b = VGroup(t, c, q, sub)
        self._clear()

    # 2. BÀI TOÁN
    def beat_baitoan(self):
        t = fit_w(Text("Bài toán của hãng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        r1 = fit_w(Text("chứa cố định 330 ml", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.0, 0])
        r2 = fit_w(Text("vỏ nhôm CÀNG ÍT càng tốt", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, -0.3, 0])
        note = fit_w(Text("thể tích giữ nguyên, tiết kiệm vật liệu", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.6, 0])
        with self.voice("02_baitoan") as D:
            self._kara("02_baitoan", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.35); self.play(FadeIn(r1, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.65); self.play(FadeIn(r2, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.88); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, r1, r2, note)
        self._clear()

    # 3. BIẾN: r và h
    def beat_bien(self):
        t = fit_w(Text("Lon = hình TRỤ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        c = can([0, 0.3, 0], 0.6, 1.7)
        hbar = DoubleArrow([1.0, -0.55, 0], [1.0, 1.15, 0], color=ACCENT, buff=0, stroke_width=4)
        hlbl = Text("h", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY).next_to(hbar, RIGHT, buff=0.12)
        rbar = DoubleArrow([0, -0.55, 0], [0.6, -0.55, 0], color=GROW, buff=0, stroke_width=4)
        rlbl = Text("r", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY).next_to(rbar, DOWN, buff=0.1)
        note = fit_w(Text("V = π r² h  (giữ cố định)", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        with self.voice("03_bien") as D:
            self._kara("03_bien", D)
            self.cue(D * 0.0); self.play(Write(t), GrowFromEdge(c, DOWN), run_time=0.8)
            self.cue(D * 0.4); self.play(GrowArrow(hbar), FadeIn(hlbl), GrowArrow(rbar), FadeIn(rlbl), run_time=0.8)
            self.cue(D * 0.75); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, c, hbar, hlbl, rbar, rlbl, note)
        self._clear()

    # 4. DIỆN TÍCH VỎ
    def beat_dientich(self):
        t = fit_w(Text("Nhôm = diện tích vỏ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        caps = fit_w(Text("2 nắp tròn:  2 π r²", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, 1.1, 0])
        side = fit_w(Text("thân cuốn quanh:  2 π r h", font=FONT, weight=BOLD, color=PURPLE).scale(SZ_BODY), CW).move_to([0, -0.1, 0])
        s = fit_w(Text("S = 2 π r² + 2 π r h", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -1.4, 0])
        with self.voice("04_dientich") as D:
            self._kara("04_dientich", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(caps, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.55); self.play(FadeIn(side, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.82); self.play(Write(s), run_time=0.7)
            self._b = VGroup(t, caps, side, s)
        self._clear()

    # 5. THẾ h THEO r
    def beat_the(self):
        t = fit_w(Text("Đưa về 1 biến", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        r1 = fit_w(Text("từ V cố định →  h = V / (π r²)", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), CW).move_to([0, 1.0, 0])
        arr = Arrow([0, 0.5, 0], [0, -0.2, 0], color=ACCENT, buff=0, stroke_width=6)
        r2 = fit_w(Text("S(r) = 2 π r² + 2V / r", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -0.9, 0])
        note = fit_w(Text("diện tích chỉ còn phụ thuộc r", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.9, 0])
        with self.voice("05_the") as D:
            self._kara("05_the", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(r1, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.55); self.play(GrowArrow(arr), run_time=0.4)
            self.cue(D * 0.7); self.play(Write(r2), run_time=0.7)
            self.cue(D * 0.9); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, r1, arr, r2, note)
        self._clear()

    # 6. ĐỒ THỊ HÀM S(r) — điểm ngọt
    def beat_hamso(self):
        t = fit_w(Text("Có 1 điểm NGỌT", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        ax_x = Line([-1.7, -0.9, 0], [1.7, -0.9, 0]).set_stroke(MUTED, 2)
        ax_y = Line([-1.7, -0.9, 0], [-1.7, 1.5, 0]).set_stroke(MUTED, 2)
        xs = np.linspace(0.35, 1.55, 40)
        ys = 2.0 * xs ** 2 + 0.55 / xs   # hình chữ U
        pts = [np.array([-1.7 + (x - 0.35) / 1.2 * 3.2, -0.9 + (y - min(ys)) * 0.7, 0]) for x, y in zip(xs, ys)]
        curve = VMobject().set_points_smoothly(pts).set_stroke(GROW, 4)
        imin = int(np.argmin(ys))
        low = Dot(pts[imin], radius=0.09).set_fill(ACCENT, 1).set_stroke(width=0)
        l1 = fit_w(Text("r nhỏ → thân cao ngồng, tốn nhôm", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.6, 0])
        l2 = fit_w(Text("r to → nắp bè, tốn nhôm", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -2.3, 0])
        with self.voice("06_hamso") as D:
            self._kara("06_hamso", D)
            self.cue(D * 0.0); self.play(Write(t), Create(ax_x), Create(ax_y), run_time=0.8)
            self.cue(D * 0.35); self.play(Create(curve), run_time=1.0)
            self.cue(D * 0.6); self.play(FadeIn(l1), run_time=0.5)
            self.cue(D * 0.75); self.play(FadeIn(l2), run_time=0.5)
            self.cue(D * 0.9); self.play(FadeIn(low, scale=0.4), Flash(pts[imin], color=ACCENT, line_length=0.3, num_lines=12), run_time=0.6)
            self._b = VGroup(t, ax_x, ax_y, curve, low, l1, l2)
        self._clear()

    # 7. ĐẠO HÀM = 0
    def beat_daoham(self):
        t = fit_w(Text("Đạo hàm ra tay", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        hero = fit_w(Text("S nhỏ nhất khi  S '(r) = 0", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 0.7, 0])
        note = fit_w(Text("nơi đồ thị chạm đáy rồi đi lên", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -0.8, 0])
        with self.voice("07_daoham") as D:
            self._kara("07_daoham", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.35); self.play(Write(hero), Flash(hero.get_center(), color=ACCENT, line_length=0.4, num_lines=14), run_time=1.0)
            self.cue(D * 0.75); self.play(FadeIn(note), run_time=0.6)
            self._b = VGroup(t, hero, note)
        self._clear()

    # 8. GIẢI
    def beat_giai(self):
        t = fit_w(Text("Giải phương trình", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        s1 = fit_w(Text("S '(r) = 4 π r − 2V / r² = 0", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, 1.1, 0])
        arr = Arrow([0, 0.6, 0], [0, -0.1, 0], color=ACCENT, buff=0, stroke_width=6)
        s2 = fit_w(Text("→  V = 2 π r³", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, -0.8, 0])
        note = fit_w(Text("một điều kiện đẹp bất ngờ", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.8, 0])
        with self.voice("08_giai") as D:
            self._kara("08_giai", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(Write(s1), run_time=0.8)
            self.cue(D * 0.6); self.play(GrowArrow(arr), Write(s2), run_time=0.8)
            self.cue(D * 0.88); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, s1, arr, s2, note)
        self._clear()

    # 9. KẾT QUẢ h = 2r
    def beat_ketqua(self):
        hero = Text("h = 2r", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO * 1.1).move_to([0, 1.5, 0])
        note = fit_w(Text("chiều cao ĐÚNG BẰNG đường kính", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, 0.4, 0])
        c = can([0, -1.2, 0], 0.62, 1.24)
        sq = Square(side_length=1.24).set_stroke(ACCENT, 2.5).move_to([0, -1.2, 0])
        with self.voice("09_ketqua") as D:
            self._kara("09_ketqua", D)
            self.cue(D * 0.0); self.play(Write(hero), Flash(hero.get_center(), color=GROW, line_length=0.5, num_lines=18), run_time=1.0)
            self.cue(D * 0.4); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.65); self.play(GrowFromEdge(c, DOWN), run_time=0.6)
            self.cue(D * 0.85); self.play(Create(sq), run_time=0.6)
            self._b = VGroup(hero, note, c, sq)
        self._clear()

    # 10. THỰC TẾ LON HƠI CAO HƠN
    def beat_thucte(self):
        t = fit_w(Text("Lon thật hơi CAO hơn", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        r1 = fit_w(Text("nắp lon DÀY & cứng hơn thân", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, 1.0, 0])
        r2 = fit_w(Text("→ tối ưu đẩy lon cao lên\nđể bớt diện tích nắp đắt", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -0.5, 0])
        note = fit_w(Text("toán lý thuyết vs chi phí thật", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.9, 0])
        with self.voice("10_thucte") as D:
            self._kara("10_thucte", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(r1, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.6); self.play(FadeIn(r2, shift=UP * 0.12), run_time=0.8)
            self.cue(D * 0.88); self.play(FadeIn(note), run_time=0.5)
            self._b = VGroup(t, r1, r2, note)
        self._clear()

    # 11. ỨNG DỤNG
    def beat_ungdung(self):
        t = fit_w(Text("Cùng bài toán ở khắp nơi", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        rows = [("thùng phuy, bể chứa", GROW), ("hộp sữa, bao bì", PURPLE), ("logistics, đóng gói", ACCENT)]
        chips = VGroup()
        for txt, col in rows:
            card = RoundedRectangle(corner_radius=0.16, width=3.2, height=0.85).set_fill(BG_CARD, 1).set_stroke(col, 2.5)
            lab = fit_w(Text(txt, font=FONT, weight=BOLD, color=col).scale(SZ_LABEL), 2.9).move_to(card)
            chips.add(VGroup(card, lab))
        chips.arrange(DOWN, buff=0.3).move_to([0, -0.1, 0])
        note = fit_w(Text("tiết kiệm hàng triệu đô vật liệu / năm", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -2.3, 0])
        with self.voice("11_ungdung") as D:
            self._kara("11_ungdung", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            for i, c in enumerate(chips):
                self.cue(D * (0.25 + 0.18 * i)); self.play(GrowFromCenter(c), run_time=0.5)
            self.cue(D * 0.85); self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
            self._b = VGroup(t, chips, note)
        self._clear()

    # 12. CTA
    def beat_cta(self):
        l1 = fit_w(Text("1 chiếc lon = 1 bài cực trị", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.9, 0])
        l2 = fit_w(Text("Đạo hàm thiết kế mọi thứ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("cực trị · tối ưu · đạo hàm lớp 12", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, 0.25, 0])
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
