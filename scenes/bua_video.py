"""
"Cây búa giấu lực 8000 Newton" — định lý động năng: F·d = ½mv² ⇒ F = mv²/(2d).
Vật lý 10 (công - động năng) · SHORT DỌC 9:16 · ~1 phút 50 · KHÔNG intro.

Dùng bộ cỡ chữ chuẩn SZ_* (brand.py) + CANH NHỊP self.cue(): mỗi bước hiện hình được
rải trải đều theo lời đọc của cả đoạn (không dồn ở đầu beat).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_bua.py
Căn chỉnh:   .venv/bin/python scenes/align_narration.py output/narration_bua
Render HD:   .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/bua_video.py BuaVideo
"""
import os

from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_bua import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WOOD = "#8B5A2B"
WOOD_DK = "#5E3A18"
STEEL = "#C3CAD6"
STEEL_DK = "#8A93A3"
HANDLE = "#A8763E"


def nail(length=1.1, head_w=0.26):
    """Đinh thẳng đứng: thân mảnh + mũ tròn trên + mũi nhọn dưới."""
    body = Rectangle(width=0.09, height=length).set_fill(STEEL, 1).set_stroke(width=0)
    head = Rectangle(width=head_w, height=0.1).set_fill(STEEL, 1).set_stroke(STEEL_DK, 1)
    head.next_to(body, UP, buff=0)
    tip = Triangle().set_fill(STEEL_DK, 1).set_stroke(width=0)
    tip.set_width(0.09).set_height(0.16).rotate(PI)
    tip.next_to(body, DOWN, buff=0)
    return VGroup(tip, body, head)


def hammer(scale=1.0):
    """Búa đơn giản: đầu thép (chữ nhật) + cán gỗ chéo."""
    head = RoundedRectangle(corner_radius=0.06, width=0.7, height=0.34).set_fill(STEEL_DK, 1).set_stroke("#5A6473", 2)
    face = Rectangle(width=0.12, height=0.34).set_fill(STEEL, 1).set_stroke(width=0).align_to(head, RIGHT)
    handle = Rectangle(width=0.14, height=1.0).set_fill(HANDLE, 1).set_stroke(WOOD_DK, 2)
    handle.next_to(head, UP, buff=-0.05).shift(RIGHT * 0.22)
    g = VGroup(handle, head, face)
    return g.scale(scale)


class BuaVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_bua")
    SEGMENTS = SEGMENTS
    TOPIC = "VẬT LÝ 10"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_vande()
        self.beat_mohinh()
        self.beat_conso()
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

    # 1. HOOK -- búa + đinh cắm gỗ -> 8000 N -----------------------------
    def beat_hook(self):
        block = RoundedRectangle(corner_radius=0.12, width=2.4, height=1.0).set_fill(WOOD, 1).set_stroke(WOOD_DK, 3)
        block.move_to([0, -0.2, 0])
        grain = VGroup(*[Line([-1.0, y, 0], [1.0, y, 0]).set_stroke(WOOD_DK, 1.5, opacity=0.5) for y in (-0.45, 0.0, 0.45)])
        grain.move_to(block)
        nl = nail(0.95).move_to(block.get_top() + DOWN * 0.05 + UP * 0.4)
        ham = hammer(1.25).next_to(nl, UP, buff=0.05).shift(LEFT * 0.05)
        wood = VGroup(block, grain, nl)

        big = Text("8000 N", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO).move_to([0, 2.1, 0])
        sub = fit_w(Text("ép lên đầu đinh", font=FONT, color=MUTED).scale(SZ_LABEL), CW).next_to(big, DOWN, buff=0.18)
        car = fit_w(Text("≈ cả một ô tô con", font=FONT, weight=BOLD, color=DEBT).scale(SZ_BODY), CW).move_to([0, -1.75, 0])
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(FadeIn(wood, shift=UP * 0.2), run_time=0.7)
            self.cue(D * 0.22); self.play(FadeIn(ham, shift=DOWN * 0.3), run_time=0.6)
            self.cue(D * 0.42); self.play(ham.animate.shift(DOWN * 0.42), run_time=0.25, rate_func=rush_into)
            self.play(Flash(nl.get_top(), color=ACCENT, line_length=0.3, num_lines=14), run_time=0.3)
            self.cue(D * 0.6); self.play(Write(big), FadeIn(sub), run_time=0.8)
            self.cue(D * 0.82); self.play(FadeIn(car, shift=UP * 0.2), run_time=0.7)
            self._b = VGroup(wood, ham, big, sub, car)
        self._clear()

    # 2. VẤN ĐỀ -- khoảnh khắc va chạm: m, v, lún 2mm -------------------
    def beat_vande(self):
        title = fit_w(Text("Khoảnh khắc va chạm", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        ham = hammer(1.15).move_to([0, 1.45, 0])
        m_lbl = Text("m = 0,5 kg", font=FONT, weight=BOLD, color=STEEL).scale(SZ_LABEL).next_to(ham, LEFT, buff=0.3)
        varr = Arrow([0, 1.45, 0], [0, 0.75, 0], color=GROW, stroke_width=6, buff=0.12)
        v_lbl = Text("v = 8 m/s", font=FONT, weight=BOLD, color=GROW).scale(SZ_LABEL).next_to(varr, RIGHT, buff=0.22)

        block = RoundedRectangle(corner_radius=0.1, width=2.4, height=1.1).set_fill(WOOD, 1).set_stroke(WOOD_DK, 3).move_to([0, -0.4, 0])
        nl = nail(0.7).move_to(block.get_top() + DOWN * 0.32)
        # thước chỉ độ lún 2mm
        brace = Line([0.55, 0.18, 0], [0.55, -0.05, 0]).set_stroke(DEBT, 4)
        cap1 = Line([0.5, 0.18, 0], [0.6, 0.18, 0]).set_stroke(DEBT, 4)
        cap2 = Line([0.5, -0.05, 0], [0.6, -0.05, 0]).set_stroke(DEBT, 4)
        d_lbl = Text("d = 2 mm", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL).next_to(brace, RIGHT, buff=0.18)
        dgrp = VGroup(brace, cap1, cap2, d_lbl)
        q = fit_w(Text("đoạn bé xíu → lực khổng lồ?", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).move_to([0, -1.85, 0])
        with self.voice("02_vande") as D:
            self._kara("02_vande", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.18); self.play(FadeIn(ham, shift=DOWN * 0.2), FadeIn(m_lbl), run_time=0.7)
            self.cue(D * 0.38); self.play(GrowArrow(varr), FadeIn(v_lbl), run_time=0.7)
            self.cue(D * 0.56); self.play(FadeIn(block, shift=UP * 0.1), FadeIn(nl), run_time=0.7)
            self.cue(D * 0.72); self.play(Create(dgrp), run_time=0.7)
            self.cue(D * 0.86); self.play(FadeIn(q, shift=UP * 0.2), run_time=0.6)
            self._b = VGroup(title, ham, m_lbl, varr, v_lbl, block, nl, dgrp, q)
        self._clear()

    # 3. MÔ HÌNH -- định lý động năng: công lực cản = ½mv² -------------
    def beat_mohinh(self):
        title = fit_w(Text("Định lý động năng", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        ke_box = RoundedRectangle(corner_radius=0.14, width=2.7, height=1.0).set_fill(BG_CARD, 1).set_stroke(GROW, 2.5).move_to([0, 1.5, 0])
        ke = fit_w(Text("Động năng = ½ m v²", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), 2.4).move_to(ke_box)
        kegrp = VGroup(ke_box, ke)
        arr = Arrow([0, 0.95, 0], [0, 0.15, 0], color=MUTED, stroke_width=5, buff=0.1)
        note = fit_w(Text("bị gỗ 'tiêu' hết bởi lực cản", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -0.2, 0])
        eq_box = RoundedRectangle(corner_radius=0.14, width=3.0, height=1.05).set_fill(BG_CARD, 1).set_stroke(ACCENT, 3).move_to([0, -1.45, 0])
        eq = fit_w(Text("F · d  =  ½ m v²", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), 2.7).move_to(eq_box)
        eqgrp = VGroup(eq_box, eq)
        cap = Text("công lực cản = động năng", font=FONT, color=MUTED).scale(SZ_SMALL).next_to(eq_box, DOWN, buff=0.18)
        with self.voice("03_mohinh") as D:
            self._kara("03_mohinh", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.18); self.play(FadeIn(kegrp, shift=UP * 0.15), run_time=0.8)
            self.cue(D * 0.45); self.play(GrowArrow(arr), FadeIn(note), run_time=0.7)
            self.cue(D * 0.7); self.play(FadeIn(eqgrp, scale=0.85), FadeIn(cap), run_time=0.9)
            self.play(Flash(eq_box.get_center(), color=ACCENT, line_length=0.3, num_lines=14), run_time=0.4)
            self._b = VGroup(title, kegrp, arr, note, eqgrp, cap)
        self._clear()

    # 4. CON SỐ -- thay số: 16 J -> F = 8000 N ------------------------
    def beat_conso(self):
        title = fit_w(Text("Thay số vào", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 2.6, 0])
        l1 = fit_w(Text("½ · 0,5 · 8²", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.7, 0])
        ke = fit_w(Text("= 16 J", font=FONT, weight=BOLD, color=GROW).scale(SZ_TITLE), CW).next_to(l1, DOWN, buff=0.22)
        kegrp = VGroup(l1, ke)
        line = Line([-1.5, 0.3, 0], [1.5, 0.3, 0]).set_stroke(MUTED, 2)
        # F = KE / d  ->  16 / 0,002
        flbl = fit_w(Text("F = động năng / d", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, -0.1, 0])
        l2 = fit_w(Text("= 16 / 0,002", font=FONT, color=MUTED).scale(SZ_BODY), CW).next_to(flbl, DOWN, buff=0.2)
        res = Text("= 8000 N", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_HERO).move_to([0, -1.75, 0])
        with self.voice("04_conso") as D:
            self._kara("04_conso", D)
            self.cue(D * 0.0); self.play(Write(title), run_time=0.6)
            self.cue(D * 0.18); self.play(FadeIn(l1, shift=UP * 0.1), run_time=0.6)
            self.cue(D * 0.34); self.play(Write(ke), run_time=0.6)
            self.cue(D * 0.5); self.play(Create(line), FadeIn(flbl), run_time=0.6)
            self.cue(D * 0.66); self.play(FadeIn(l2), run_time=0.6)
            self.cue(D * 0.82); self.play(Write(res), Flash(res.get_center(), color=ACCENT, line_length=0.4, num_lines=18), run_time=1.0)
            self._b = VGroup(title, kegrp, line, flbl, l2, res)
        self._clear()

    # 5. Ý NGHĨA -- d nhỏ -> F lớn (so sánh hai thanh) ----------------
    def beat_ynghia(self):
        f = fit_w(Text("F = động năng / d", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        key = fit_w(Text("d càng NHỎ → F càng LỚN", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY), CW).move_to([0, 1.7, 0])
        # thanh d dài -> lực nhỏ
        long_d = Line([-1.3, 0.7, 0], [1.0, 0.7, 0]).set_stroke(GROW, 6)
        long_lbl = Text("d dài → F nhỏ", font=FONT, color=GROW).scale(SZ_SMALL).next_to(long_d, DOWN, buff=0.12)
        # thanh d ngắn -> lực to
        short_d = Line([-1.3, -0.3, 0], [-1.0, -0.3, 0]).set_stroke(DEBT, 7)
        short_lbl = Text("d = 2 mm → F = 8000 N", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(short_d, RIGHT, buff=0.2)
        shortgrp = VGroup(short_d, short_lbl)
        uses = VGroup(
            Text("→ vì sao mũi đinh phải NHỌN", font=FONT, color=WHITE).scale(SZ_LABEL),
            Text("→ va chạm vài cm trong tai nạn", font=FONT, color=WHITE).scale(SZ_LABEL),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT).move_to([0, -1.6, 0])
        for u in uses:
            fit_w(u, CW)
        with self.voice("05_ynghia") as D:
            self._kara("05_ynghia", D)
            self.cue(D * 0.0); self.play(Write(f), run_time=0.6)
            self.cue(D * 0.18); self.play(FadeIn(key, shift=UP * 0.15), run_time=0.6)
            self.cue(D * 0.34); self.play(Create(long_d), FadeIn(long_lbl), run_time=0.6)
            self.cue(D * 0.5); self.play(Create(short_d), FadeIn(short_lbl), run_time=0.6)
            self.cue(D * 0.66); self.play(FadeIn(uses[0], shift=RIGHT * 0.2), run_time=0.55)
            self.cue(D * 0.82); self.play(FadeIn(uses[1], shift=RIGHT * 0.2), run_time=0.55)
            self._b = VGroup(f, key, long_d, long_lbl, shortgrp, uses)
        self._clear()

    # 6. CTA ----------------------------------------------------------
    def beat_cta(self):
        l1 = fit_w(Text("Cùng năng lượng,", font=FONT, weight=BOLD, color=WHITE).scale(SZ_TITLE), CW).move_to([0, 1.9, 0])
        l2 = fit_w(Text("dừng càng gấp → lực càng lớn", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_BODY), CW).next_to(l1, DOWN, buff=0.25)
        sub_btn = RoundedRectangle(corner_radius=0.2, width=2.5, height=0.78).set_fill(DEBT, 1).set_stroke(width=0)
        sub_txt = Text("ĐĂNG KÝ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_BODY).move_to(sub_btn)
        sub = VGroup(sub_btn, sub_txt).move_to([0, -0.4, 0])
        with self.voice("06_cta", gap=0.4) as D:
            self._kara("06_cta", D)
            self.cue(D * 0.0); self.play(Write(l1), run_time=0.7)
            self.cue(D * 0.28); self.play(FadeIn(l2, shift=UP * 0.15), Indicate(l2, color=GROW, scale_factor=1.06), run_time=0.8)
            self.cue(D * 0.6); self.play(GrowFromCenter(sub), run_time=0.5)
            self.play(sub.animate.scale(1.08), rate_func=there_and_back, run_time=0.6)
            self._b = VGroup(l1, l2, sub)
        self._clear()
