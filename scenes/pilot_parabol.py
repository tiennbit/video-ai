"""
Video pilot — "Toán đời thực": Quỹ đạo parabol của vòi phun nước (Toán 10).
Render dọc cho YouTube Shorts/Reels:
    manim -pqh --resolution 1080,1920 --fps 60 scenes/pilot_parabol.py PilotParabol
"""
from manim import *

# Bảng màu kênh (nền xanh đen giống video tham khảo)
BG = "#0E1117"
ACCENT = "#FFD93D"   # vàng tiêu đề
WATER = "#4DD0E1"    # xanh nước
HILITE = "#FF6B6B"   # đỏ nhấn


class PilotParabol(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ---------- 1. HOOK: tiêu đề ----------
        title = Text("Vì sao tia nước cong\nthành hình này?",
                     font="Arial", weight=BOLD, color=ACCENT,
                     line_spacing=1.1).scale(0.9)
        sub = Text("Toán 10 — Hàm số bậc hai", font="Arial",
                   color=WHITE).scale(0.5).next_to(title, DOWN, buff=0.5)
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(sub, shift=UP * 0.3))
        self.wait(0.8)
        self.play(FadeOut(title), FadeOut(sub))

        # ---------- 2. Hệ trục + vòi nước ----------
        axes = Axes(
            x_range=[0, 6, 1], y_range=[0, 4, 1],
            x_length=6, y_length=4,
            axis_config={"color": GREY_B, "include_tip": True},
        ).to_edge(DOWN, buff=1.5)
        x_lbl = axes.get_x_axis_label(Text("khoảng cách", font="Arial").scale(0.4))
        y_lbl = axes.get_y_axis_label(Text("độ cao", font="Arial").scale(0.4))
        self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl))

        # ---------- 3. Vẽ tia nước parabol ----------
        def f(x):
            return -0.5 * (x - 3) ** 2 + 3.5   # đỉnh (3 ; 3.5)

        graph = axes.plot(f, x_range=[0.2, 5.8], color=WATER, stroke_width=6)
        dot = Dot(color=WATER).move_to(axes.c2p(0.2, f(0.2)))
        self.play(Create(graph, run_time=2), MoveAlongPath(dot, graph, run_time=2))
        self.wait(0.3)

        # ---------- 4. Đỉnh parabol ----------
        vertex = Dot(axes.c2p(3, 3.5), color=HILITE, radius=0.09)
        v_lbl = Text("đỉnh cao nhất", font="Arial", color=HILITE).scale(0.45)
        v_lbl.next_to(vertex, UP)
        self.play(FadeIn(vertex, scale=0.5), Write(v_lbl))
        self.wait(0.5)

        # ---------- 5. Công thức ----------
        # Dùng Text (Pango) để không cần LaTeX. Khi đã cài gói 'standalone'
        # có thể đổi thành: formula = MathTex("y = ax^2 + bx + c")
        formula = Text("y = ax² + bx + c", font="Arial", color=WHITE).scale(0.9)
        formula.to_edge(UP, buff=1.2)
        box = SurroundingRectangle(formula, color=ACCENT, buff=0.25, corner_radius=0.1)
        self.play(Write(formula))
        self.play(Create(box))
        self.wait(0.5)

        note = Text("Mọi tia nước, quả bóng, pháo hoa…\nđều đi theo parabol!",
                    font="Arial", color=ACCENT, line_spacing=1.1).scale(0.5)
        note.next_to(axes, DOWN, buff=0.4)
        self.play(FadeIn(note, shift=UP * 0.3))
        self.wait(1.2)
