"""
Video parabol v2 — giọng CLONE của user + phụ đề KARAOKE + thiết kế đẹp hơn.

Bước 1 — sinh giọng clone (venv riêng):
    ~/voxcpm-venv/bin/python scenes/clone_narration.py
Bước 2 — render dọc:
    .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/parabol_video_v2.py ParabolVideoV2

Đồng bộ: mọi thứ (lấp thời lượng câu, thanh tiến trình, karaoke) chạy theo
self.renderer.time — thời gian render thực, khớp với audio add_sound().
"""
import os
import re
import wave
from contextlib import contextmanager

from manim import *

from narration_texts import SEGMENTS

# ---------- Bảng màu ----------
BG = "#0B1020"          # nền xanh đen
BG_CARD = "#161C2E"     # nền thẻ
ACCENT = "#FFD93D"      # vàng
WATER = "#4DD0E1"       # xanh nước
HILITE = "#FF6B6B"      # đỏ nhấn
PURPLE = "#A78BFA"      # tím phụ
SPOKEN = "#FFFFFF"      # chữ karaoke đã đọc
UNSPOKEN = "#5A6472"    # chữ karaoke chưa đọc
MUTED = "#9AA4B2"

FONT = "Arial"
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NARR = os.path.join(BASE, "output", "narration_cloned")

FW = config.frame_width    # ~4.5 (dọc)
LX, RX = -FW / 2 + 0.18, FW / 2 - 0.18


def wav_dur(path):
    with wave.open(path, "rb") as w:
        return w.getnframes() / float(w.getframerate())


def syl_w(word):
    return max(1, len(word.strip(".,?!:;…")))


def chunk_text(text, max_words=7):
    """Chia câu thành cụm ngắn (≤ ~7 từ) để phụ đề dễ đọc."""
    pieces = re.findall(r"[^.?!]+[.?!]?", text)
    chunks = []
    for s in pieces:
        s = s.strip()
        if not s:
            continue
        words = s.split()
        if len(words) <= max_words:
            chunks.append(words)
        else:
            cur = []
            for w in words:
                cur.append(w)
                if len(cur) >= max_words or (w.endswith(",") and len(cur) >= 4):
                    chunks.append(cur)
                    cur = []
            if cur:
                if len(cur) <= 2 and chunks:
                    chunks[-1].extend(cur)
                else:
                    chunks.append(cur)
    return chunks


class ParabolVideoV2(Scene):
    # ---------- hạ tầng ----------
    def _dur(self, seg):
        return wav_dur(os.path.join(NARR, f"{seg}.wav"))

    @contextmanager
    def voice(self, seg, gap=0.3):
        d = self._dur(seg)
        self.beat_t0 = self.renderer.time
        self.add_sound(os.path.join(NARR, f"{seg}.wav"))
        yield d
        rem = d - (self.renderer.time - self.beat_t0)
        if rem > 1e-3:
            self.wait(rem)
        self.wait(gap)

    # ---------- karaoke ----------
    def make_karaoke(self, text, duration, t0):
        """Tạo phụ đề karaoke chia cụm; chữ sáng dần theo renderer.time."""
        chunks = chunk_text(text)
        weights = [sum(syl_w(w) for w in c) for c in chunks]
        total = sum(weights)
        lead, tail = 0.15, 0.35
        span = max(0.1, duration - lead - tail)

        groups = VGroup()
        acc = 0.0
        for c_words, wt in zip(chunks, weights):
            c_start = lead + span * (acc / total)
            c_end = lead + span * ((acc + wt) / total)
            acc += wt
            # thời điểm mỗi từ trong cụm
            ww = [syl_w(w) for w in c_words]
            tw = sum(ww)
            wstarts, a = [], 0.0
            cspan = max(0.05, c_end - c_start - 0.05)
            for x in ww:
                wstarts.append(c_start + cspan * (a / tw))
                a += x
            # dựng từ
            word_mobs = [Text(w, font=FONT, color=UNSPOKEN).scale(0.46) for w in c_words]
            block = self._wrap(word_mobs)
            block.move_to([0, -2.65, 0])
            card = RoundedRectangle(
                corner_radius=0.16, width=block.width + 0.5, height=block.height + 0.4,
            ).set_stroke(WATER, 1.5, opacity=0.5).set_fill(BG_CARD, opacity=0.92)
            card.move_to(block).set_z_index(-1)
            grp = VGroup(card, *word_mobs)

            # updater: hiện/ẩn theo cửa sổ cụm + tô sáng từng từ
            def make_upd(cs=c_start, ce=c_end, ws=list(wstarts), mobs=word_mobs, cd=card):
                def upd(_):
                    e = self.renderer.time - t0
                    vis = cs <= e < ce
                    cd.set_opacity(0.92 if vis else 0)
                    cd.set_stroke(opacity=0.5 if vis else 0)
                    for m, st in zip(mobs, ws):
                        if not vis:
                            m.set_opacity(0)
                        else:
                            m.set_opacity(1)
                            m.set_color(SPOKEN if e >= st else UNSPOKEN)
                return upd

            grp.add_updater(make_upd())
            grp.set_opacity(0)
            groups.add(grp)
        return groups

    def _wrap(self, mobs, max_w=3.9, wbuff=0.14, lbuff=0.16):
        lines, cur, cw = [], [], 0.0
        for m in mobs:
            add = m.width + wbuff
            if cur and cw + add > max_w:
                lines.append(cur); cur, cw = [], 0.0
            cur.append(m); cw += add
        if cur:
            lines.append(cur)
        line_g = [VGroup(*ln).arrange(RIGHT, buff=wbuff) for ln in lines]
        return VGroup(*line_g).arrange(DOWN, buff=lbuff, aligned_edge=LEFT)

    def end_karaoke(self, groups):
        for g in groups:
            g.clear_updaters()
        self.remove(groups)

    # ---------- nội dung ----------
    def construct(self):
        self.camera.background_color = BG

        # tổng thời lượng (cho thanh tiến trình)
        durs = {k: self._dur(k) for k in SEGMENTS}
        TOTAL = sum(durs.values()) + len(durs) * 0.9

        # nền trang trí: vầng sáng mờ phía trên
        glow = Ellipse(width=5.5, height=4.0, color=PURPLE).set_fill(PURPLE, 0.05).set_stroke(width=0)
        glow.move_to([0, 1.4, 0]).set_z_index(-5)
        self.add(glow)

        # thanh top: nhãn chủ đề + tiến trình
        topic = Text("TOÁN 10  ·  PARABOL", font=FONT, weight=BOLD, color=ACCENT).scale(0.4)
        topic.to_edge(UP, buff=0.42)
        dot = Dot(color=WATER, radius=0.05).next_to(topic, LEFT, buff=0.18)
        py = config.frame_height / 2 - 0.22
        pb_bg = Line([LX, py, 0], [RX, py, 0]).set_stroke("#2A3142", 3)
        pb_fg = Line([LX, py, 0], [LX + 0.001, py, 0]).set_stroke(ACCENT, 4)

        def pb_upd(m):
            frac = min(max(self.renderer.time / TOTAL, 0.0), 1.0)
            m.put_start_and_end_on([LX, py, 0], [LX + (RX - LX) * max(frac, 0.001), py, 0])
        pb_fg.add_updater(pb_upd)
        self.add(pb_bg, pb_fg, VGroup(dot, topic))

        # ===== BEAT 1 — HOOK =====
        title = Text("Vì sao tia nước cong\nthành hình này?", font=FONT, weight=BOLD,
                     color=ACCENT, line_spacing=1.15).scale(0.66).move_to([0, 0.9, 0])
        with self.voice("01_hook") as D:
            kar = self.make_karaoke(SEGMENTS["01_hook"], D, self.beat_t0)
            self.add(kar)
            self.play(Write(title), run_time=1.2)
            self.play(title.animate.set_color_by_gradient(ACCENT, WATER), run_time=0.8)
        self.end_karaoke(kar)
        self.play(FadeOut(title), run_time=0.4)

        # ===== Hệ trục dùng chung beat 2-4 (vùng trên) =====
        axes = Axes(
            x_range=[0, 6, 1], y_range=[0, 4, 1], x_length=3.4, y_length=2.8,
            axis_config={"color": "#3A4254", "include_tip": True, "stroke_width": 3},
        ).move_to([0, 0.45, 0])
        x_lbl = axes.get_x_axis_label(Text("khoảng cách", font=FONT, color=MUTED).scale(0.3))
        y_lbl = axes.get_y_axis_label(Text("độ cao", font=FONT, color=MUTED).scale(0.3))

        def f(x):
            return -0.5 * (x - 3) ** 2 + 3.5

        graph = axes.plot(f, x_range=[0.2, 5.8], stroke_width=7).set_color_by_gradient(WATER, "#80FFEA", WATER)
        drop = VGroup(
            Dot(color=WHITE, radius=0.13).set_opacity(0.25),
            Dot(color=WATER, radius=0.08),
        ).move_to(axes.c2p(0.2, f(0.2)))
        stage = VGroup(axes, x_lbl, y_lbl, graph, drop)

        # ===== BEAT 2 — VẼ PARABOL =====
        with self.voice("02_curve") as D:
            kar = self.make_karaoke(SEGMENTS["02_curve"], D, self.beat_t0)
            self.add(kar)
            self.play(Create(axes), FadeIn(x_lbl), FadeIn(y_lbl), run_time=1.1)
            self.play(Create(graph), MoveAlongPath(drop, graph), run_time=2.8)
        self.end_karaoke(kar)

        # ===== BEAT 3 — ĐỈNH =====
        vertex = Dot(axes.c2p(3, 3.5), color=HILITE, radius=0.1)
        vglow = Dot(axes.c2p(3, 3.5), color=HILITE, radius=0.2).set_opacity(0.25)
        vline = DashedLine(axes.c2p(3, 0), axes.c2p(3, 3.5), color=HILITE, stroke_width=2)
        vlabel = Text("ĐỈNH", font=FONT, weight=BOLD, color=HILITE).scale(0.42).next_to(vertex, UR, buff=0.06)
        stage.add(vertex, vglow, vline, vlabel)
        with self.voice("03_vertex") as D:
            kar = self.make_karaoke(SEGMENTS["03_vertex"], D, self.beat_t0)
            self.add(kar)
            self.play(FadeIn(vglow, scale=0.5), FadeIn(vertex, scale=0.4), Create(vline), run_time=1.0)
            self.play(Write(vlabel), Flash(vertex, color=HILITE, line_length=0.2), run_time=0.9)
        self.end_karaoke(kar)

        # ===== BEAT 4 — CÔNG THỨC =====
        formula = Text("y = a·x² + b·x + c", font=FONT, weight=BOLD, color=WHITE).scale(0.6)
        fcard = RoundedRectangle(corner_radius=0.14, width=formula.width + 0.5, height=formula.height + 0.4)
        fcard.set_stroke(ACCENT, 2).set_fill("#1E1A33", 0.9)
        fgroup = VGroup(fcard, formula).move_to([0, 2.78, 0])
        stage.add(fgroup)
        with self.voice("04_formula") as D:
            kar = self.make_karaoke(SEGMENTS["04_formula"], D, self.beat_t0)
            self.add(kar)
            self.play(FadeIn(fcard, shift=DOWN * 0.2), Write(formula), run_time=1.2)
            self.play(Indicate(formula, color=ACCENT, scale_factor=1.1), run_time=0.9)
        self.end_karaoke(kar)

        # ===== BEAT 5 — ỨNG DỤNG + CTA =====
        def mini(color, w=1.3, h=0.8):
            return FunctionGraph(lambda x: -h * x ** 2, x_range=[-1, 1, 0.04],
                                 color=color, stroke_width=5).stretch_to_fit_width(w)

        items = [("Bóng rổ", HILITE), ("Pháo hoa", ACCENT), ("Đài phun nước", WATER)]
        rows = VGroup()
        for name, col in items:
            chip = VGroup(mini(col), Text(name, font=FONT, color=WHITE).scale(0.46)).arrange(RIGHT, buff=0.35)
            rows.add(chip)
        rows.arrange(DOWN, buff=0.6, aligned_edge=LEFT).move_to([0, 0.9, 0])

        cta = Text("Toán học ở quanh ta!", font=FONT, weight=BOLD, color=ACCENT).scale(0.6).move_to([0, -0.9, 0])
        with self.voice("05_apply", gap=0.6) as D:
            kar = self.make_karaoke(SEGMENTS["05_apply"], D, self.beat_t0)
            self.add(kar)
            self.play(FadeOut(stage), run_time=0.5)
            for chip in rows:
                self.play(Create(chip[0]), Write(chip[1]), run_time=1.0)
            self.play(Write(cta), Indicate(cta, color=WATER, scale_factor=1.1), run_time=1.3)
        self.end_karaoke(kar)
        self.wait(0.3)
