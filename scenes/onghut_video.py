"""
"Ống hút cao tối đa 10 mét" — áp suất khí quyển đẩy cột chất lỏng, h = p/(rho.g).
Lý 10 · SHORT DỌC 9:16 · ~2 phút (12 beat) · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_onghut.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/onghut_video.py OngHutVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_onghut import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WATER = "#38BDF8"


def glass(center, w=1.2, h=0.9, fill=0.7):
    """Ly nước: khung chữ U + khối nước."""
    c = np.array([center[0], center[1], 0.0])
    left = Line(c + np.array([-w / 2, h / 2, 0]), c + np.array([-w / 2, -h / 2, 0]))
    bot = Line(c + np.array([-w / 2, -h / 2, 0]), c + np.array([w / 2, -h / 2, 0]))
    right = Line(c + np.array([w / 2, -h / 2, 0]), c + np.array([w / 2, h / 2, 0]))
    frame = VGroup(left, bot, right).set_stroke(MUTED, 3.5)
    wtr = Rectangle(width=w - 0.08, height=h * fill).set_fill(WATER, 0.55).set_stroke(width=0)
    wtr.move_to(c + np.array([0, -h / 2 + h * fill / 2 + 0.04, 0]))
    return VGroup(frame, wtr)


def straw(bottom, top, w=0.22, color=ACCENT):
    """Ống hút thẳng đứng (2 vạch song song)."""
    b, t = np.array([bottom[0], bottom[1], 0.0]), np.array([top[0], top[1], 0.0])
    l1 = Line(b + np.array([-w / 2, 0, 0]), t + np.array([-w / 2, 0, 0]))
    l2 = Line(b + np.array([w / 2, 0, 0]), t + np.array([w / 2, 0, 0]))
    return VGroup(l1, l2).set_stroke(color, 3.5)


def water_col(bottom, h, w=0.16):
    """Cột nước trong ống, tính từ đáy bottom cao h."""
    b = np.array([bottom[0], bottom[1], 0.0])
    r = Rectangle(width=w, height=max(h, 0.01)).set_fill(WATER, 0.8).set_stroke(width=0)
    r.move_to(b + np.array([0, h / 2, 0]))
    return r


class OngHutVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_onghut")
    SEGMENTS = SEGMENTS
    TOPIC = "VẬT LÝ 10"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_hut()
        self.beat_giamap()
        self.beat_khiquyen()
        self.beat_canbang()
        self.beat_congthuc()
        self.beat_tinh()
        self.beat_chankhong()
        self.beat_gieng()
        self.beat_thuyngan()
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

    # 1. HOOK — ống hút từ ban công tầng 4
    def beat_hook(self):
        t = fit_w(Text("Thử thách ống hút tầng 4", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        floors = VGroup(*[RoundedRectangle(corner_radius=0.05, width=1.5, height=0.62).set_fill(BG_CARD, 1).set_stroke(MUTED, 2)
                          for _ in range(4)]).arrange(UP, buff=0.06).move_to([-1.05, 0.35, 0])
        head = Circle(radius=0.13).set_fill(GROW, 1).set_stroke(width=0).move_to([-0.2, 1.7, 0])
        g = glass([0.45, -1.1, 0])
        st = straw([0.45, -1.05, 0], [-0.1, 1.55, 0])
        q = fit_w(Text("Phổi khoẻ mấy cũng KHÔNG hút nổi?", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -2.35, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Write(t), LaggedStartMap(FadeIn, floors, lag_ratio=0.1), run_time=0.9)
            self.cue(D * 0.3); self.play(FadeIn(head, scale=0.6), FadeIn(g), run_time=0.6)
            self.cue(D * 0.5); self.play(Create(st), run_time=0.9)
            self.cue(D * 0.82); self.play(Write(q), run_time=0.7)
            self._b = VGroup(t, floors, head, g, st, q)
        self._clear()

    # 2. HÚT LÀ GÌ — bạn tưởng là "kéo"
    def beat_hut(self):
        t = fit_w(Text("HÚT thật ra là gì?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        wrong = fit_w(Text("bạn tưởng: miệng KÉO nước lên\nnhư kéo một sợi dây", font=FONT, weight=BOLD, color=DEBT, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, 0.9, 0])
        x1 = Line([-0.45, -0.25, 0], [0.45, -1.15, 0]).set_stroke(DEBT, 8)
        x2 = Line([0.45, -0.25, 0], [-0.45, -1.15, 0]).set_stroke(DEBT, 8)
        truth = fit_w(Text("miệng chẳng hề CHẠM vào nước", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -2.1, 0])
        with self.voice("02_hut") as D:
            self._kara("02_hut", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(wrong, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.6); self.play(Create(x1), Create(x2), run_time=0.6)
            self.cue(D * 0.82); self.play(Write(truth), run_time=0.7)
            self._b = VGroup(t, wrong, x1, x2, truth)
        self._clear()

    # 3. HÚT = GIẢM ÁP TRONG ỐNG
    def beat_giamap(self):
        t = fit_w(Text("Hút = RÚT BỚT không khí", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        st = straw([0, -1.6, 0], [0, 1.4, 0], w=0.5)
        dots = VGroup(*[Dot([dx, dy, 0], radius=0.045).set_fill(MUTED, 1).set_stroke(width=0)
                        for dx, dy in [(-0.1, 0.9), (0.12, 0.5), (-0.08, 0.1), (0.1, -0.4), (-0.11, -0.9)]])
        up = Arrow([0.65, 0.2, 0], [0.65, 1.3, 0], color=DEBT, buff=0, stroke_width=6)
        ulbl = Text("khí bị rút ra", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(up, RIGHT, buff=0.1).shift(LEFT * 0.05)
        note = fit_w(Text("áp suất TRONG ỐNG giảm xuống", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), CW).move_to([0, -2.25, 0])
        with self.voice("03_giamap") as D:
            self._kara("03_giamap", D)
            self.cue(D * 0.0); self.play(Write(t), Create(st), run_time=0.7)
            self.cue(D * 0.3); self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.1), run_time=0.7)
            self.cue(D * 0.5); self.play(GrowArrow(up), FadeIn(ulbl),
                                         LaggedStart(*[d.animate.shift(UP * 1.6).set_opacity(0) for d in dots], lag_ratio=0.1),
                                         run_time=1.1)
            self.cue(D * 0.8); self.play(Write(note), run_time=0.7)
            self._b = VGroup(t, st, dots, up, ulbl, note)
        self._clear()

    # 4. KHÍ QUYỂN ĐÈ — 10 tấn mỗi mét vuông
    def beat_khiquyen(self):
        t = fit_w(Text("Ai ĐẨY nước lên?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        sky = Rectangle(width=3.9, height=1.15).set_fill(PURPLE, 0.22).set_stroke(width=0).move_to([0, 1.35, 0])
        slbl = Text("khí quyển dày hàng chục km", font=FONT, color=PURPLE).scale(SZ_SMALL).move_to(sky)
        g = glass([0, -1.35, 0], w=1.6, h=1.0)
        downs = VGroup(*[Arrow([x, 0.6, 0], [x, -0.5, 0], color=DEBT, buff=0, stroke_width=5) for x in [-1.1, -0.37, 0.37, 1.1]])
        hero = fit_w(Text("~10 TẤN đè mỗi mét vuông", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -2.35, 0])
        with self.voice("04_khiquyen") as D:
            self._kara("04_khiquyen", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(sky), FadeIn(slbl), run_time=0.8)
            self.cue(D * 0.3); self.play(FadeIn(g), run_time=0.5)
            self.cue(D * 0.45); self.play(LaggedStartMap(GrowArrow, downs, lag_ratio=0.12), run_time=0.9)
            self.cue(D * 0.72); self.play(Write(hero), run_time=0.8)
            self._b = VGroup(t, sky, slbl, g, downs, hero)
        self._clear()

    # 5. CÂN BẰNG — cột nước nặng ghì lại
    def beat_canbang(self):
        t = fit_w(Text("Nước dừng ở đâu?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        g = glass([0, -1.5, 0], w=1.6, h=0.9)
        st = straw([0, -1.45, 0], [0, 1.7, 0], w=0.3)
        col = water_col([0, -1.45, 0], 2.1, w=0.22)
        up = Arrow([-0.85, -1.3, 0], [-0.85, -0.1, 0], color=GROW, buff=0, stroke_width=6)
        ulbl = Text("khí quyển\nđẩy lên", font=FONT, weight=BOLD, color=GROW, line_spacing=0.95).scale(SZ_SMALL).next_to(up, LEFT, buff=0.1)
        dn = Arrow([0.85, 0.6, 0], [0.85, -0.6, 0], color=DEBT, buff=0, stroke_width=6)
        dlbl = Text("cột nước\nghì xuống", font=FONT, weight=BOLD, color=DEBT, line_spacing=0.95).scale(SZ_SMALL).next_to(dn, RIGHT, buff=0.1)
        note = fit_w(Text("dừng đúng lúc HAI BÊN CÂN BẰNG", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -2.6, 0])
        with self.voice("05_canbang") as D:
            self._kara("05_canbang", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(g), Create(st), run_time=0.8)
            self.cue(D * 0.28); self.play(GrowFromEdge(col, DOWN), run_time=1.0)
            self.cue(D * 0.5); self.play(GrowArrow(up), FadeIn(ulbl), run_time=0.6)
            self.cue(D * 0.66); self.play(GrowArrow(dn), FadeIn(dlbl), run_time=0.6)
            self.cue(D * 0.85); self.play(Write(note), run_time=0.6)
            self._b = VGroup(t, g, st, col, up, ulbl, dn, dlbl, note)
        self._clear()

    # 6. CÔNG THỨC h = p/(ρg)
    def beat_congthuc(self):
        t = fit_w(Text("Công thức gọn gàng", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        card = RoundedRectangle(corner_radius=0.2, width=3.4, height=1.15).set_fill(BG_CARD, 1).set_stroke(ACCENT, 2.5).move_to([0, 0.8, 0])
        eq = fit_w(Text("h = p / (ρ · g)", font=FONT, weight=BOLD, color=WHITE).scale(SZ_HERO * 0.85), 3.0).move_to(card)
        r1 = fit_w(Text("p: áp suất khí quyển", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL), CW).move_to([0, -0.55, 0])
        r2 = fit_w(Text("ρ: khối lượng riêng chất lỏng", font=FONT, weight=BOLD, color=PURPLE).scale(SZ_LABEL), CW).move_to([0, -1.25, 0])
        r3 = fit_w(Text("g: gia tốc trọng trường", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, -1.95, 0])
        with self.voice("06_congthuc") as D:
            self._kara("06_congthuc", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(GrowFromCenter(card), Write(eq), run_time=0.9)
            self.cue(D * 0.58); self.play(FadeIn(r1, shift=UP * 0.1), run_time=0.5)
            self.cue(D * 0.72); self.play(FadeIn(r2, shift=UP * 0.1), run_time=0.5)
            self.cue(D * 0.86); self.play(FadeIn(r3, shift=UP * 0.1), run_time=0.5)
            self._b = VGroup(t, card, eq, r1, r2, r3)
        self._clear()

    # 7. THAY SỐ — 10,3 m
    def beat_tinh(self):
        t = fit_w(Text("Thay số vào", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        l1 = fit_w(Text("h = 101 325 / (1000 × 9,8)", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.2, 0])
        card = RoundedRectangle(corner_radius=0.2, width=3.2, height=1.2).set_fill(BG_CARD, 1).set_stroke(GROW, 3).move_to([0, -0.35, 0])
        hero = fit_w(Text("≈ 10,3 mét", font=FONT, weight=BOLD, color=GROW).scale(SZ_HERO), 2.8).move_to(card)
        note = fit_w(Text("giới hạn cho MỌI ống hút nước", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.85, 0])
        with self.voice("07_tinh") as D:
            self._kara("07_tinh", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(Write(l1), run_time=0.9)
            self.cue(D * 0.62); self.play(GrowFromCenter(card), Write(hero), Flash(card.get_center(), color=GROW, line_length=0.4, num_lines=14), run_time=1.0)
            self.cue(D * 0.88); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.5)
            self._b = VGroup(t, l1, card, hero, note)
        self._clear()

    # 8. CHÂN KHÔNG TUYỆT ĐỐI cũng chịu
    def beat_chankhong(self):
        t = fit_w(Text("Trần TUYỆT ĐỐI", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        st = straw([0, -2.0, 0], [0, 1.6, 0], w=0.3)
        col = water_col([0, -2.0, 0], 2.6, w=0.22)
        vac = fit_w(Text("chân không 100%", font=FONT, weight=BOLD, color=PURPLE).scale(SZ_SMALL), 1.6).move_to([1.25, 1.35, 0])
        lim = DashedLine([-1.5, 0.6, 0], [1.5, 0.6, 0]).set_stroke(DEBT, 3)
        llbl = Text("10,3 m — hết cỡ", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(lim, UP, buff=0.08).shift(LEFT * 0.7)
        note = fit_w(Text("khí quyển chỉ đẩy nổi ĐẾN THẾ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -2.6, 0])
        with self.voice("08_chankhong") as D:
            self._kara("08_chankhong", D)
            self.cue(D * 0.0); self.play(Write(t), Create(st), run_time=0.7)
            self.cue(D * 0.3); self.play(GrowFromEdge(col, DOWN), FadeIn(vac), run_time=1.0)
            self.cue(D * 0.6); self.play(Create(lim), FadeIn(llbl), run_time=0.7)
            self.cue(D * 0.85); self.play(Write(note), run_time=0.6)
            self._b = VGroup(t, st, col, vac, lim, llbl, note)
        self._clear()

    # 9. GIẾNG SÂU — bơm hút chịu thua
    def beat_gieng(self):
        t = fit_w(Text("Vì sao giếng sâu phải bơm ĐẨY", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.5, 0])
        ground = Line([-2.0, 1.3, 0], [2.0, 1.3, 0]).set_stroke(MUTED, 4)
        wall1 = Line([-0.55, 1.3, 0], [-0.55, -1.9, 0]).set_stroke(MUTED, 3)
        wall2 = Line([0.55, 1.3, 0], [0.55, -1.9, 0]).set_stroke(MUTED, 3)
        wtr = Rectangle(width=1.02, height=0.65).set_fill(WATER, 0.55).set_stroke(width=0).move_to([0, -1.55, 0])
        pump_up = RoundedRectangle(corner_radius=0.08, width=0.7, height=0.45).set_fill(DEBT, 1).set_stroke(width=0).move_to([0, 1.6, 0])
        pl = Text("bơm hút: thua nếu sâu hơn 10 m", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).move_to([0, 0.75, 0])
        pump_dn = RoundedRectangle(corner_radius=0.08, width=0.7, height=0.45).set_fill(GROW, 1).set_stroke(width=0).move_to([0, -1.5, 0])
        pl2 = fit_w(Text("bơm đẩy thả xuống đáy: đẩy cao bao nhiêu cũng được", font=FONT, weight=BOLD, color=GROW).scale(SZ_SMALL), CW).move_to([0, -2.5, 0])
        with self.voice("09_gieng") as D:
            self._kara("09_gieng", D)
            self.cue(D * 0.0); self.play(Write(t), Create(ground), Create(wall1), Create(wall2), FadeIn(wtr), run_time=0.9)
            self.cue(D * 0.3); self.play(GrowFromCenter(pump_up), FadeIn(pl), run_time=0.7)
            self.cue(D * 0.62); self.play(GrowFromCenter(pump_dn), run_time=0.6)
            self.cue(D * 0.78); self.play(FadeIn(pl2, shift=UP * 0.12), run_time=0.7)
            self._b = VGroup(t, ground, wall1, wall2, wtr, pump_up, pl, pump_dn, pl2)
        self._clear()

    # 10. THUỶ NGÂN 76 cm — barometer
    def beat_thuyngan(self):
        t = fit_w(Text("Đổi nước → THUỶ NGÂN", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        s1 = straw([-0.9, -1.7, 0], [-0.9, 1.5, 0], w=0.26)
        c1 = water_col([-0.9, -1.7, 0], 2.9, w=0.18)
        l1 = Text("nước\n10,3 m", font=FONT, weight=BOLD, color=WATER, line_spacing=0.95).scale(SZ_SMALL).next_to(s1, DOWN, buff=0.12)
        s2 = straw([0.9, -1.7, 0], [0.9, 1.5, 0], w=0.26)
        c2 = Rectangle(width=0.18, height=0.55).set_fill("#C0C7D1", 1).set_stroke(width=0).move_to([0.9, -1.42, 0])
        l2 = Text("thuỷ ngân\n76 cm", font=FONT, weight=BOLD, color=WHITE, line_spacing=0.95).scale(SZ_SMALL).next_to(s2, DOWN, buff=0.12)
        note = fit_w(Text("nặng gấp 13,6 lần → thấp hơn 13,6 lần\n= máy đo áp suất đầu tiên", font=FONT, weight=BOLD, color=GROW, line_spacing=1.05).scale(SZ_SMALL), CW).move_to([0, 1.95, 0])
        with self.voice("10_thuyngan") as D:
            self._kara("10_thuyngan", D)
            self.cue(D * 0.0); self.play(Write(t), Create(s1), Create(s2), run_time=0.8)
            self.cue(D * 0.3); self.play(GrowFromEdge(c1, DOWN), FadeIn(l1), run_time=0.9)
            self.cue(D * 0.55); self.play(GrowFromEdge(c2, DOWN), FadeIn(l2), run_time=0.7)
            self.cue(D * 0.8); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.7)
            self._b = VGroup(t, s1, c1, l1, s2, c2, l2, note)
        self._clear()

    # 11. ỨNG DỤNG — đẩy thay vì kéo
    def beat_ung(self):
        t = fit_w(Text("ĐẨY chứ không KÉO — khắp nơi", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        rows = [("xi phông chuyển nước qua thành bể", GROW), ("máy hút bụi gom rác vào trong", ACCENT), ("giác hút treo chục ký lên kính", PURPLE)]
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
        l1 = fit_w(Text("Thứ nâng ly trà sữa lên miệng bạn", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.9, 0])
        l2 = fit_w(Text("là CẢ BẦU KHÍ QUYỂN", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("áp suất khí quyển · h = p/(ρg) · 10,3 m", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, 0.25, 0])
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
