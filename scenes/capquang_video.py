"""
"Ống hút gãy & sợi cáp chở cả Internet" — khúc xạ, phản xạ toàn phần, cáp quang.
Lý 11 · SHORT DỌC 9:16 · ~2 phút (12 beat) · KHÔNG intro. Dùng Text (không MathTex).
Sinh giọng:  ~/voxcpm-venv/bin/python scenes/clone_narration_capquang.py
Render HD:   /app/.venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/capquang_video.py CapQuangVideo
"""
import os

import numpy as np
from manim import *

from brand import (BrandScene, fit_w, FONT, BG, BG_CARD, ACCENT, GROW, DEBT, PURPLE, MUTED,
                   SZ_HERO, SZ_TITLE, SZ_BODY, SZ_LABEL, SZ_SMALL, CW)
from narration_texts_capquang import SEGMENTS

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WATER = "#3B82C4"
GLASS = "#5EC8F2"


def ray(a, b, color=ACCENT, w=4):
    return Line(np.array(a, dtype=float), np.array(b, dtype=float)).set_stroke(color, w)


class CapQuangVideo(BrandScene):
    NARR = os.path.join(BASE, "output", "narration_capquang")
    SEGMENTS = SEGMENTS
    TOPIC = "LÝ 11"

    def construct(self):
        self.camera.background_color = BG
        total = sum(self._dur(k) for k in SEGMENTS) + len(SEGMENTS) * 0.9
        self.start_template(total)
        self.beat_hook()
        self.beat_khucxa()
        self.beat_vitoc()
        self.beat_onghut()
        self.beat_nguoclai()
        self.beat_gioihan()
        self.beat_toanphan()
        self.beat_guong()
        self.beat_capquang()
        self.beat_ziczac()
        self.beat_internet()
        self.beat_cta()
        self.brand_stinger()
        self.wait(0.3)

    def _kara(self, seg, D):
        self._kar = self.make_karaoke(SEGMENTS[seg], D, self.beat_t0)
        self.add(self._kar)

    def _clear(self):
        self.end_karaoke(self._kar)
        self.play(FadeOut(self._b), run_time=0.35)

    # 1. HOOK — ống hút gãy + sợi cáp
    def beat_hook(self):
        t = fit_w(Text("Ống hút gãy trong ly nước", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.5, 0])
        glass = VGroup(
            Line([-0.7, 1.4, 0], [-0.7, -0.4, 0]).set_stroke(MUTED, 3),
            Line([0.7, 1.4, 0], [0.7, -0.4, 0]).set_stroke(MUTED, 3),
            Line([-0.7, -0.4, 0], [0.7, -0.4, 0]).set_stroke(MUTED, 3),
        )
        water = Rectangle(width=1.4, height=1.1).set_fill(WATER, 0.35).set_stroke(width=0).move_to([0, 0.15, 0])
        surf = Line([-0.7, 0.7, 0], [0.7, 0.7, 0]).set_stroke(GLASS, 3)
        straw_top = Line([0.1, 1.3, 0], [-0.05, 0.7, 0]).set_stroke(ACCENT, 6)
        straw_bot = Line([-0.05, 0.7, 0], [-0.45, -0.25, 0]).set_stroke(ACCENT, 6)
        fiber = VGroup(
            Line([-1.6, -1.6, 0], [1.6, -1.6, 0]).set_stroke(GLASS, 6),
            Text("cáp quang chở cả Internet", font=FONT, weight=BOLD, color=GLASS).scale(SZ_SMALL).move_to([0, -2.15, 0]),
        )
        with self.voice("01_hook") as D:
            self._kara("01_hook", D)
            self.cue(D * 0.0); self.play(Create(glass), FadeIn(water), Create(surf), run_time=0.9)
            self.cue(D * 0.3); self.play(Create(straw_top), Create(straw_bot), run_time=0.7)
            self.cue(D * 0.6); self.play(Create(fiber[0]), FadeIn(fiber[1]), run_time=0.9)
            self._b = VGroup(t, glass, water, surf, straw_top, straw_bot, fiber)
        self._clear()

    # 2. KHÚC XẠ
    def beat_khucxa(self):
        t = fit_w(Text("Ánh sáng bị BẺ HƯỚNG", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        bnd = Line([-2.0, 0.4, 0], [2.0, 0.4, 0]).set_stroke(GLASS, 3)
        water = Rectangle(width=4.0, height=2.0).set_fill(WATER, 0.22).set_stroke(width=0).move_to([0, -0.6, 0])
        nrm = DashedLine([0, 1.7, 0], [0, -1.1, 0]).set_stroke(MUTED, 2)
        inc = ray([-1.5, 1.6, 0], [0, 0.4, 0], ACCENT)
        ref = ray([0, 0.4, 0], [0.75, -1.1, 0], ACCENT)
        la = Text("không khí", font=FONT, color=MUTED).scale(SZ_SMALL).move_to([-1.3, 1.05, 0])
        lw = Text("nước", font=FONT, color=GLASS).scale(SZ_SMALL).move_to([-1.5, -0.3, 0])
        with self.voice("02_khucxa") as D:
            self._kara("02_khucxa", D)
            self.cue(D * 0.0); self.play(Write(t), Create(bnd), FadeIn(water), FadeIn(la), FadeIn(lw), run_time=0.9)
            self.cue(D * 0.4); self.play(Create(nrm), Create(inc), run_time=0.8)
            self.cue(D * 0.72); self.play(Create(ref), Flash([0, 0.4, 0], color=ACCENT, line_length=0.3, num_lines=12), run_time=0.8)
            self._b = VGroup(t, bnd, water, nrm, inc, ref, la, lw)
        self._clear()

    # 3. VÌ ÁNH SÁNG ĐỔI TỐC ĐỘ
    def beat_vitoc(self):
        t = fit_w(Text("Vì ánh sáng ĐỔI TỐC ĐỘ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        r1 = fit_w(Text("trong nước / thuỷ tinh: chạy CHẬM hơn", font=FONT, weight=BOLD, color=GLASS).scale(SZ_LABEL), CW).move_to([0, 1.2, 0])
        cart = RoundedRectangle(corner_radius=0.1, width=0.9, height=0.4).set_fill(ACCENT, 1).set_stroke(width=0).move_to([-1.0, -0.2, 0])
        road = Line([-2.0, -0.5, 0], [0, -0.5, 0]).set_stroke(MUTED, 4)
        sand = Line([0, -0.5, 0], [2.0, -0.5, 0]).set_stroke(DEBT, 6)
        note = fit_w(Text("đổi tốc độ → đổi hướng\nnhư xe lao từ nhựa xuống cát", font=FONT, weight=BOLD, color=WHITE, line_spacing=1.05).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        with self.voice("03_vitoc") as D:
            self._kara("03_vitoc", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.3); self.play(FadeIn(r1, shift=UP * 0.12), run_time=0.7)
            self.cue(D * 0.5); self.play(Create(road), Create(sand), FadeIn(cart), run_time=0.7)
            self.cue(D * 0.62); self.play(cart.animate.move_to([1.0, -0.2, 0]), run_time=min(D * 0.25, 1.3), rate_func=rush_from)
            self.cue(D * 0.85); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, r1, cart, road, sand, note)
        self._clear()

    # 4. ỐNG HÚT NHƯ GÃY
    def beat_onghut(self):
        t = fit_w(Text("Nên mắt thấy ống GÃY", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        surf = Line([-1.7, 0.4, 0], [1.7, 0.4, 0]).set_stroke(GLASS, 3)
        water = Rectangle(width=3.4, height=1.9).set_fill(WATER, 0.22).set_stroke(width=0).move_to([0, -0.55, 0])
        straw_r = Line([0.35, 1.5, 0], [0.1, 0.4, 0]).set_stroke(ACCENT, 6)
        straw_w = Line([0.1, 0.4, 0], [-0.4, -1.0, 0]).set_stroke(ACCENT, 6)
        ghost = DashedLine([0.1, 0.4, 0], [-0.1, -1.0, 0]).set_stroke(MUTED, 3)
        eye = VGroup(Ellipse(width=0.5, height=0.3).set_stroke(WHITE, 2), Dot(radius=0.07).set_fill(WHITE, 1)).move_to([-1.35, 0.9, 0])
        note = fit_w(Text("não tưởng tia đi thẳng → dựng sai chỗ", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -1.9, 0])
        with self.voice("04_onghut") as D:
            self._kara("04_onghut", D)
            self.cue(D * 0.0); self.play(Write(t), Create(surf), FadeIn(water), run_time=0.7)
            self.cue(D * 0.3); self.play(Create(straw_r), Create(straw_w), run_time=0.7)
            self.cue(D * 0.55); self.play(FadeIn(eye), Create(ghost), run_time=0.7)
            self.cue(D * 0.82); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, surf, water, straw_r, straw_w, ghost, eye, note)
        self._clear()

    # 5. NGƯỢC LẠI: NƯỚC -> KHÔNG KHÍ, BẺ RA XA
    def beat_nguoclai(self):
        t = fit_w(Text("Từ nước ra không khí", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        bnd = Line([-2.0, 0.5, 0], [2.0, 0.5, 0]).set_stroke(GLASS, 3)
        water = Rectangle(width=4.0, height=2.2).set_fill(WATER, 0.22).set_stroke(width=0).move_to([0, -0.6, 0])
        nrm = DashedLine([0, 1.7, 0], [0, -1.3, 0]).set_stroke(MUTED, 2)
        inc = ray([-0.7, -1.2, 0], [0, 0.5, 0], ACCENT)
        out = ray([0, 0.5, 0], [1.4, 1.5, 0], ACCENT)
        note = fit_w(Text("chậm → nhanh: bẻ RA XA pháp tuyến", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        with self.voice("05_nguoclai") as D:
            self._kara("05_nguoclai", D)
            self.cue(D * 0.0); self.play(Write(t), Create(bnd), FadeIn(water), Create(nrm), run_time=0.8)
            self.cue(D * 0.4); self.play(Create(inc), run_time=0.6)
            self.cue(D * 0.6); self.play(Create(out), run_time=0.7)
            self.cue(D * 0.82); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, bnd, water, nrm, inc, out, note)
        self._clear()

    # 6. GÓC TỚI HẠN
    def beat_gioihan(self):
        t = fit_w(Text("Góc TỚI HẠN", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        bnd = Line([-2.0, 0.5, 0], [2.0, 0.5, 0]).set_stroke(GLASS, 3)
        water = Rectangle(width=4.0, height=2.2).set_fill(WATER, 0.22).set_stroke(width=0).move_to([0, -0.6, 0])
        nrm = DashedLine([0, 1.6, 0], [0, -1.3, 0]).set_stroke(MUTED, 2)
        rays = VGroup(*[ray([-0.9 + 0.0, -1.1, 0], [0, 0.5, 0], MUTED, 3) for _ in range(1)])
        inc = ray([-1.0, -1.0, 0], [0, 0.5, 0], ACCENT)
        graze = ray([0, 0.5, 0], [1.9, 0.62, 0], DEBT)
        note = fit_w(Text("tia ló nằm SÁT RẠT mặt nước", font=FONT, weight=BOLD, color=DEBT).scale(SZ_LABEL), CW).move_to([0, -1.9, 0])
        with self.voice("06_gioihan") as D:
            self._kara("06_gioihan", D)
            self.cue(D * 0.0); self.play(Write(t), Create(bnd), FadeIn(water), Create(nrm), run_time=0.8)
            self.cue(D * 0.4); self.play(Create(inc), run_time=0.6)
            self.cue(D * 0.62); self.play(Create(graze), Flash([0, 0.5, 0], color=DEBT, line_length=0.3, num_lines=12), run_time=0.8)
            self.cue(D * 0.85); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, bnd, water, nrm, inc, graze, note)
        self._clear()

    # 7. PHẢN XẠ TOÀN PHẦN
    def beat_toanphan(self):
        t = fit_w(Text("PHẢN XẠ TOÀN PHẦN", font=FONT, weight=BOLD, color=GROW).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        bnd = Line([-2.0, 0.5, 0], [2.0, 0.5, 0]).set_stroke(GLASS, 3)
        water = Rectangle(width=4.0, height=2.2).set_fill(WATER, 0.22).set_stroke(width=0).move_to([0, -0.6, 0])
        nrm = DashedLine([0, 1.6, 0], [0, -1.3, 0]).set_stroke(MUTED, 2)
        inc = ray([-1.4, -0.9, 0], [0, 0.5, 0], ACCENT)
        refl = ray([0, 0.5, 0], [1.4, -0.9, 0], GROW)
        note = fit_w(Text("vượt góc tới hạn → dội NGƯỢC hoàn toàn", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -1.9, 0])
        with self.voice("07_toanphan") as D:
            self._kara("07_toanphan", D)
            self.cue(D * 0.0); self.play(Write(t), Create(bnd), FadeIn(water), Create(nrm), run_time=0.8)
            self.cue(D * 0.35); self.play(Create(inc), run_time=0.6)
            self.cue(D * 0.6); self.play(Create(refl), Flash([0, 0.5, 0], color=GROW, line_length=0.4, num_lines=14), run_time=0.9)
            self.cue(D * 0.85); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, bnd, water, nrm, inc, refl, note)
        self._clear()

    # 8. GƯƠNG HOÀN HẢO
    def beat_guong(self):
        t = fit_w(Text("Mặt nước = GƯƠNG hoàn hảo", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, 2.4, 0])
        hero = fit_w(Text("phản chiếu ~100% ánh sáng", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY), CW).move_to([0, 0.6, 0])
        note = fit_w(Text("gần như không rò rỉ, không mất mát", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -0.9, 0])
        with self.voice("08_guong") as D:
            self._kara("08_guong", D)
            self.cue(D * 0.0); self.play(Write(t), run_time=0.6)
            self.cue(D * 0.35); self.play(Write(hero), Flash(hero.get_center(), color=GROW, line_length=0.5, num_lines=16), run_time=1.0)
            self.cue(D * 0.75); self.play(FadeIn(note), run_time=0.6)
            self._b = VGroup(t, hero, note)
        self._clear()

    # 9. TRÁI TIM CÁP QUANG
    def beat_capquang(self):
        t = fit_w(Text("Trái tim của CÁP QUANG", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        top = Line([-2.0, 0.7, 0], [2.0, 0.7, 0]).set_stroke(GLASS, 4)
        bot = Line([-2.0, -0.7, 0], [2.0, -0.7, 0]).set_stroke(GLASS, 4)
        core = Rectangle(width=4.0, height=1.4).set_fill(GLASS, 0.12).set_stroke(width=0).move_to([0, 0, 0])
        laser = Dot([-1.9, 0, 0], radius=0.12).set_fill(DEBT, 1).set_stroke(width=0)
        llbl = Text("tia laze", font=FONT, weight=BOLD, color=DEBT).scale(SZ_SMALL).next_to(laser, DOWN, buff=0.15)
        note = fit_w(Text("sợi thuỷ tinh mảnh hơn sợi tóc", font=FONT, color=MUTED).scale(SZ_LABEL), CW).move_to([0, -1.7, 0])
        with self.voice("09_capquang") as D:
            self._kara("09_capquang", D)
            self.cue(D * 0.0); self.play(Write(t), Create(top), Create(bot), FadeIn(core), run_time=0.9)
            self.cue(D * 0.45); self.play(FadeIn(laser, scale=0.5), FadeIn(llbl), run_time=0.6)
            self.cue(D * 0.75); self.play(FadeIn(note), run_time=0.6)
            self._b = VGroup(t, top, bot, core, laser, llbl, note)
        self._clear()

    # 10. NẢY ZÍC ZẮC
    def beat_ziczac(self):
        t = fit_w(Text("Nảy zíc zắc dọc sợi", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        top = Line([-2.0, 0.7, 0], [2.0, 0.7, 0]).set_stroke(GLASS, 4)
        bot = Line([-2.0, -0.7, 0], [2.0, -0.7, 0]).set_stroke(GLASS, 4)
        xs = np.linspace(-2.0, 2.0, 7)
        pts = [[x, 0.7 if i % 2 == 0 else -0.7, 0] for i, x in enumerate(xs)]
        zig = VMobject().set_points_as_corners([np.array(p, dtype=float) for p in pts]).set_stroke(DEBT, 4)
        note = fit_w(Text("chạy hàng nghìn km, gần như không thoát ra", font=FONT, weight=BOLD, color=WHITE).scale(SZ_SMALL), CW).move_to([0, -1.8, 0])
        with self.voice("10_ziczac") as D:
            self._kara("10_ziczac", D)
            self.cue(D * 0.0); self.play(Write(t), Create(top), Create(bot), run_time=0.7)
            self.cue(D * 0.35); self.play(Create(zig), run_time=min(D * 0.45, 1.8))
            self.cue(D * 0.85); self.play(FadeIn(note, shift=UP * 0.12), run_time=0.6)
            self._b = VGroup(t, top, bot, zig, note)
        self._clear()

    # 11. CẢ INTERNET
    def beat_internet(self):
        t = fit_w(Text("Mỗi chớp tắt = 1 bit", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 2.5, 0])
        bits = Text("1 0 1 1 0 0 1 0", font=FONT, weight=BOLD, color=GROW).scale(SZ_BODY).move_to([0, 1.3, 0])
        r1 = fit_w(Text("chớp hàng tỉ lần / giây", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, 0.2, 0])
        r2 = fit_w(Text("1 sợi = hàng triệu cuộc gọi cùng lúc", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_LABEL), CW).move_to([0, -0.9, 0])
        r3 = fit_w(Text("bó cáp dưới đáy đại dương nối cả hành tinh", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, -1.9, 0])
        with self.voice("11_internet") as D:
            self._kara("11_internet", D)
            self.cue(D * 0.0); self.play(Write(t), FadeIn(bits), run_time=0.7)
            self.cue(D * 0.35); self.play(FadeIn(r1, shift=UP * 0.12), run_time=0.6)
            self.cue(D * 0.6); self.play(FadeIn(r2, shift=UP * 0.12), Indicate(r2, color=GROW), run_time=0.7)
            self.cue(D * 0.85); self.play(FadeIn(r3), run_time=0.5)
            self._b = VGroup(t, bits, r1, r2, r3)
        self._clear()

    # 12. CTA
    def beat_cta(self):
        l1 = fit_w(Text("Ống hút gãy & Internet toàn cầu", font=FONT, weight=BOLD, color=WHITE).scale(SZ_LABEL), CW).move_to([0, 1.9, 0])
        l2 = fit_w(Text("cùng 1 định luật khúc xạ", font=FONT, weight=BOLD, color=ACCENT).scale(SZ_TITLE), CW).move_to([0, 1.0, 0])
        tags = fit_w(Text("khúc xạ · góc tới hạn · phản xạ toàn phần", font=FONT, color=MUTED).scale(SZ_SMALL), CW).move_to([0, 0.25, 0])
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
