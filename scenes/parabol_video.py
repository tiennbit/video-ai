"""
Video hoàn chỉnh — "Toán đời thực": Vì sao tia nước cong thành parabol? (Toán 10)
Có lời thoại tiếng Việt (edge-tts) tự đồng bộ với animation.

Bước 1 — sinh lời thoại:
    .venv/bin/python scenes/narration_parabol.py
Bước 2 — render dọc cho YouTube Shorts/Reels:
    .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/parabol_video.py ParabolVideo

Đồng bộ tiếng/hình: mỗi "beat" gọi self.add_sound() NGAY tại thời điểm hiện tại
(time_offset của manim tính tương đối so với thời gian render hiện tại, nên để mặc
định = 0), chạy animation, rồi tự chờ cho hết câu thoại -> hình và tiếng luôn khớp.
"""
import os
from contextlib import contextmanager

from manim import *
from mutagen.mp3 import MP3

# Bảng màu kênh
BG = "#0E1117"
ACCENT = "#FFD93D"   # vàng tiêu đề
WATER = "#4DD0E1"    # xanh nước
HILITE = "#FF6B6B"   # đỏ nhấn
MUTED = "#9AA4B2"    # xám phụ

FONT = "Arial"
NARR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "output", "narration"))


class ParabolVideo(Scene):
    # ---------- hạ tầng đồng bộ tiếng/hình ----------
    def _dur(self, seg):
        return MP3(os.path.join(NARR, f"{seg}.mp3")).info.length

    def _play(self, *anims, run_time=1.0, **kw):
        self.play(*anims, run_time=run_time, **kw)
        self.clock += run_time

    def _wait(self, t):
        if t and t > 1e-3:
            self.wait(t)
            self.clock += t

    @contextmanager
    def voice(self, seg, gap=0.3):
        """Phát câu thoại NGAY bây giờ; tự chờ cho hết câu khi thoát block."""
        d = self._dur(seg)
        start = self.clock
        self.add_sound(os.path.join(NARR, f"{seg}.mp3"))   # time_offset=0 -> phát ngay
        yield d
        self._wait(d - (self.clock - start))   # lấp cho đủ độ dài câu thoại
        self._wait(gap)                          # nghỉ nhẹ giữa các beat

    # ---------- nội dung ----------
    def construct(self):
        self.camera.background_color = BG
        self.clock = 0.0

        # ===== Beat 1 — HOOK =====
        title = Text("Vì sao tia nước cong\nthành hình này?", font=FONT,
                     weight=BOLD, color=ACCENT, line_spacing=1.15).scale(0.66)
        sub = Text("Toán 10  ·  Hàm số bậc hai", font=FONT, color=MUTED).scale(0.46)
        group1 = VGroup(title, sub).arrange(DOWN, buff=0.45).shift(UP * 0.2)
        with self.voice("01_hook"):
            self._play(Write(title), run_time=1.3)
            self._play(FadeIn(sub, shift=UP * 0.3), run_time=0.7)
        self._play(FadeOut(group1), run_time=0.5)

        # ===== Hệ trục dùng chung cho beat 2-4 =====
        axes = Axes(
            x_range=[0, 6, 1], y_range=[0, 4, 1],
            x_length=3.9, y_length=4.0,
            axis_config={"color": GREY_B, "include_tip": True, "stroke_width": 3},
        ).shift(UP * 0.2)
        x_lbl = axes.get_x_axis_label(Text("khoảng cách", font=FONT, color=MUTED).scale(0.34))
        y_lbl = axes.get_y_axis_label(Text("độ cao", font=FONT, color=MUTED).scale(0.34))

        def f(x):
            return -0.5 * (x - 3) ** 2 + 3.5     # đỉnh (3 ; 3.5)

        graph = axes.plot(f, x_range=[0.2, 5.8], color=WATER, stroke_width=7)
        dot = Dot(color=WATER, radius=0.1).move_to(axes.c2p(0.2, f(0.2)))
        stage = VGroup(axes, x_lbl, y_lbl, graph, dot)   # gom lại để fade out cuối

        def bottom_cap(text, color):
            return Text(text, font=FONT, color=color).scale(0.5).to_edge(DOWN, buff=0.85)

        # ===== Beat 2 — VẼ PARABOL =====
        cap2 = bottom_cap("Đường cong này gọi là PARABOL", WATER)
        with self.voice("02_curve"):
            self._play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=1.2)
            self._play(Create(graph), MoveAlongPath(dot, graph), run_time=3.2)
            self._play(Write(cap2), run_time=1.0)

        # ===== Beat 3 — ĐỈNH PARABOL =====
        vertex = Dot(axes.c2p(3, 3.5), color=HILITE, radius=0.11)
        vline = DashedLine(axes.c2p(3, 0), axes.c2p(3, 3.5), color=HILITE, stroke_width=2.5)
        vlabel = Text("ĐỈNH", font=FONT, weight=BOLD, color=HILITE).scale(0.5)
        vlabel.next_to(vertex, UR, buff=0.08)
        cap3 = bottom_cap("Đỉnh = điểm cao nhất", HILITE)
        stage.add(vertex, vline, vlabel)
        with self.voice("03_vertex"):
            self._play(FadeOut(cap2), FadeIn(vertex, scale=0.4), Create(vline), run_time=1.1)
            self._play(Write(vlabel), FadeIn(cap3, shift=UP * 0.2), run_time=0.9)
            self._play(Flash(vertex, color=HILITE, line_length=0.25), run_time=0.8)

        # ===== Beat 4 — CÔNG THỨC =====
        formula = Text("y = a·x² + b·x + c", font=FONT, color=WHITE).scale(0.74)
        formula.to_edge(UP, buff=0.85)
        box = SurroundingRectangle(formula, color=ACCENT, buff=0.22, corner_radius=0.12)
        note = bottom_cap("Vì a < 0  →  bề lõm quay xuống", ACCENT)
        stage.add(formula, box, note)
        with self.voice("04_formula"):
            self._play(FadeOut(cap3), Write(formula), run_time=1.3)
            self._play(Create(box), run_time=0.7)
            self._play(FadeIn(note, shift=UP * 0.25), run_time=0.9)
            self._play(Indicate(formula, color=ACCENT, scale_factor=1.12), run_time=1.0)

        # ===== Beat 5 — ỨNG DỤNG + CTA =====
        def mini_parab(color, w=1.7, h=1.0):
            p = FunctionGraph(lambda x: -h * (x ** 2), x_range=[-1, 1, 0.04],
                              color=color, stroke_width=6)
            return p.stretch_to_fit_width(w)

        items = [("Bóng rổ", HILITE), ("Pháo hoa", ACCENT), ("Đài phun nước", WATER)]
        rows = VGroup()
        for name, col in items:
            row = VGroup(mini_parab(col),
                         Text(name, font=FONT, color=WHITE).scale(0.52)).arrange(RIGHT, buff=0.4)
            rows.add(row)
        rows.arrange(DOWN, buff=0.85, aligned_edge=LEFT).shift(UP * 0.9)

        cta = Text("Toán học ở quanh ta!\nNhớ theo dõi kênh nhé!", font=FONT,
                   weight=BOLD, color=ACCENT, line_spacing=1.2).scale(0.58)
        cta.to_edge(DOWN, buff=1.1)

        with self.voice("05_apply", gap=0.6):
            self._play(FadeOut(stage), run_time=0.6)
            for row in rows:
                self._play(Create(row[0]), Write(row[1]), run_time=1.2)
            self._play(Write(cta), run_time=1.3)
            self._play(Indicate(cta, color=WATER, scale_factor=1.08), run_time=1.1)
