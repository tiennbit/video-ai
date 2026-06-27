"""
brand.py — BỘ NHẬN DIỆN THƯƠNG HIỆU dùng chung cho MỌI Short của kênh.

ĐỊNH DẠNG: DỌC 9:16 (1080×1920) — Reels / TikTok / YouTube Shorts.
Khung dọc: frame_height = 8, frame_width ≈ 4.5 → x ∈ [-2.25, 2.25], y ∈ [-4, 4].
=> Bố cục XẾP DỌC (không đặt cạnh nhau như bản ngang).

Mọi tập kế thừa `BrandScene`: cùng intro "con vẹt", khung template (chủ đề + tiến trình
+ watermark), phụ đề karaoke khớp giọng đọc, outro. Sửa thương hiệu ở hằng số bên dưới.
Render dọc:
    .venv/bin/manim -qh --resolution 1080,1920 --fps 60 scenes/<tap>.py <Scene>
Xem trước nhanh:
    .venv/bin/manim -ql --resolution 540,960 --fps 12 scenes/<tap>.py <Scene>
"""
import json
import os
import re
import wave
from contextlib import contextmanager

from manim import *

# ÉP KHUNG DỌC 9:16 — bắt buộc, nếu không Manim giữ khung ngang 14.2×8 mặc định
# rồi nhét nội dung vào DẢI GIỮA canvas dọc (trống lớn trên/dưới).
# 4.5×8 khớp tỉ lệ 0.5625 = 1080/1920 = 540/960 → lấp đầy chiều cao, không méo.
config.frame_width = 4.5
config.frame_height = 8.0

# ===================== THƯƠNG HIỆU (sửa ở đây) =====================
CHANNEL_NAME = "TOÁN LÝ ĐỜI THỰC"
TAGLINE = "Hiểu để dùng — đừng học vẹt"
SERIES_HOOK = "BẠN LÀ\nMỘT CON VẸT À?"      # 2 dòng cho khung dọc hẹp
FONT = "Arial"
KARAOKE_ON = False   # bỏ chữ chạy karaoke (đặt True để bật lại)

# ===================== BẢNG MÀU =====================
BG = "#0B1020"
BG_CARD = "#161C2E"
ACCENT = "#FFD93D"      # vàng
GROW = "#4ADE80"        # xanh lá — tăng trưởng / tiết kiệm
DEBT = "#FF6B6B"        # đỏ — nợ / "học vẹt"
PURPLE = "#A78BFA"
SPOKEN = "#FFFFFF"
UNSPOKEN = "#5A6472"
MUTED = "#9AA4B2"

# ===================== CỠ CHỮ CHUẨN (khung dọc) =====================
# Dùng chung cho mọi scene để nhất quán & gọn. Đã giảm ~2/3 so với bản đầu.
SZ_HERO = 0.78    # con số/kết quả "đinh" (vd 1/11 ≈ 9%)
SZ_TITLE = 0.5    # tiêu đề beat
SZ_BODY = 0.4     # câu/nhãn chính
SZ_LABEL = 0.34   # nhãn phụ
SZ_SMALL = 0.3    # ghi chú nhỏ
CW = 3.3          # bề ngang nội dung tối đa (chừa lề ~0.6 mỗi bên cho thoáng)


def fit_w(mob, w=CW):
    """Co chữ/nhóm cho vừa bề ngang khung dọc (không phóng to nếu đã nhỏ hơn)."""
    if mob.width > w:
        mob.set_width(w)
    return mob


# ===================== TIỆN ÍCH KARAOKE =====================
def wav_dur(path):
    with wave.open(path, "rb") as w:
        return w.getnframes() / float(w.getframerate())


def syl_w(word):
    return max(1, len(word.strip(".,?!:;…")))


def chunk_text(text, max_words=5):
    """Chia câu thành cụm NGẮN (≤ ~5 từ) — khung dọc hẹp."""
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
                if len(cur) >= max_words or (w.endswith(",") and len(cur) >= 3):
                    chunks.append(cur)
                    cur = []
            if cur:
                if len(cur) <= 2 and chunks:
                    chunks[-1].extend(cur)
                else:
                    chunks.append(cur)
    return chunks


# ===================== MASCOT: VẸT "VẸC-TƠ" =====================
def mascot_parrot(scale=1.0, smart=False):
    P_BODY, P_WING, P_BELLY = "#34D399", "#10B981", "#A7F3D0"
    P_BEAK, P_BEAK2 = "#FB923C", "#EA8C2B"

    tail = Polygon([-0.35, -0.7, 0], [-1.0, -1.4, 0], [-0.18, -1.0, 0]).set_fill(P_WING, 1).set_stroke(width=0)
    body = Ellipse(width=1.15, height=1.6).set_fill(P_BODY, 1).set_stroke(width=0).rotate(-0.18).move_to([0.05, -0.15, 0])
    belly = Ellipse(width=0.66, height=1.02).set_fill(P_BELLY, 1).set_stroke(width=0).move_to([0.2, -0.28, 0])
    wing = Ellipse(width=0.55, height=1.0).set_fill(P_WING, 1).set_stroke(width=0).rotate(-0.25).move_to([-0.12, -0.12, 0])
    head = Circle(radius=0.56).set_fill(P_BODY, 1).set_stroke(width=0).move_to([0.05, 0.78, 0])
    crest = VGroup(
        Polygon([0.0, 1.28, 0], [-0.14, 1.6, 0], [0.13, 1.42, 0]).set_fill(DEBT, 1).set_stroke(width=0),
        Polygon([0.16, 1.26, 0], [0.12, 1.64, 0], [0.32, 1.42, 0]).set_fill(ACCENT, 1).set_stroke(width=0),
    )
    beak_up = Polygon([0.5, 0.92, 0], [0.98, 0.74, 0], [0.5, 0.58, 0]).set_fill(P_BEAK, 1).set_stroke(width=0)
    beak_lo = Polygon([0.5, 0.74, 0], [0.82, 0.64, 0], [0.5, 0.52, 0]).set_fill(P_BEAK2, 1).set_stroke(width=0)
    eye_w = Dot([0.3, 0.98, 0], radius=0.14).set_fill(WHITE, 1).set_stroke(width=0)
    eye_b = Dot([0.34, 0.96, 0], radius=0.06).set_fill(BG, 1).set_stroke(width=0)

    g = VGroup(tail, body, wing, belly, head, crest, beak_up, beak_lo, eye_w, eye_b)
    if smart:
        glasses = VGroup(
            Circle(radius=0.2).set_stroke(ACCENT, 5).move_to([0.32, 0.98, 0]),
            Circle(radius=0.14).set_stroke(ACCENT, 5).move_to([0.66, 0.92, 0]),
            Line([0.5, 1.0, 0], [0.54, 0.97, 0]).set_stroke(ACCENT, 5),
        )
        g.add(glasses)
    return g.scale(scale)


# ===================== LỚP CƠ SỞ (DỌC) =====================
class BrandScene(Scene):
    NARR = ""
    SEGMENTS = {}
    TOPIC = ""

    # ---------- thời lượng + giọng ----------
    def _dur(self, seg):
        p = os.path.join(self.NARR, f"{seg}.wav")
        if os.path.exists(p):
            return wav_dur(p)
        n_syl = len(self.SEGMENTS.get(seg, "").split())
        return max(1.8, n_syl / 2.4 + 0.4)

    @contextmanager
    def voice(self, seg, gap=0.25):
        d = self._dur(seg)
        self.beat_t0 = self.renderer.time
        self.beat_seg = seg
        p = os.path.join(self.NARR, f"{seg}.wav")
        if os.path.exists(p):
            self.add_sound(p)        # time_offset mặc định = 0 (RELATIVE)
        yield d
        rem = d - (self.renderer.time - self.beat_t0)
        if rem > 1e-3:
            self.wait(rem)
        self.wait(gap)

    def cue(self, t_rel):
        """Canh nhịp: chờ tới mốc t_rel giây (tính từ đầu beat) rồi mới diễn bước tiếp.
        Dùng để rải các bước hiện hình trải đều theo lời đọc của cả đoạn.
        Nếu đã quá mốc thì không chờ (không lùi)."""
        dt = (self.beat_t0 + t_rel) - self.renderer.time
        if dt > 1e-3:
            self.wait(dt)

    # ---------- karaoke (băng dưới, khung DỌC hẹp) ----------
    def _wrap(self, mobs, max_w=3.3, wbuff=0.13, lbuff=0.15):
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

    # ---------- karaoke CĂN CHỈNH (đọc timestamp thật từ <seg>.words.json) ----------
    def _load_words(self, seg):
        if not seg or not self.NARR:
            return None
        p = os.path.join(self.NARR, f"{seg}.words.json")
        if not os.path.exists(p):
            return None
        try:
            data = json.load(open(p, encoding="utf-8"))
            return [(d[0], float(d[1])) for d in data] or None
        except Exception:  # noqa: BLE001
            return None

    def _karaoke_aligned(self, words, t0, y, wscale):
        """Chia cụm theo khoảng nghỉ thật của giọng; chữ sáng đúng lúc từ được đọc."""
        chunks, cur = [], []
        for i, (w, t) in enumerate(words):
            cur.append((w, t))
            nxt = words[i + 1][1] if i + 1 < len(words) else None
            gap = (nxt - t) if nxt is not None else 99
            if len(cur) >= 6 or gap > 0.45:
                chunks.append(cur); cur = []
        if cur:
            chunks.append(cur)

        groups = VGroup()
        for ci, chunk in enumerate(chunks):
            cs = chunk[0][1]
            ce = chunks[ci + 1][0][1] if ci + 1 < len(chunks) else chunk[-1][1] + 0.9
            word_mobs = [Text(w, font=FONT, weight=BOLD, color=UNSPOKEN).scale(wscale) for (w, _t) in chunk]
            block = self._wrap(word_mobs).move_to([0, y, 0])
            card = RoundedRectangle(
                corner_radius=0.16, width=block.width + 0.5, height=block.height + 0.4,
            ).set_stroke(GROW, 1.5, opacity=0.45).set_fill(BG_CARD, opacity=0.92)
            card.move_to(block).set_z_index(-1)
            grp = VGroup(card, *word_mobs)
            wt = [t for (_w, t) in chunk]

            def make_upd(cs=cs, ce=ce, ws=wt, mobs=word_mobs, cd=card):
                def upd(_):
                    e = self.renderer.time - t0
                    vis = (cs - 0.12) <= e < ce
                    cd.set_opacity(0.92 if vis else 0)
                    cd.set_stroke(opacity=0.45 if vis else 0)
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

    def make_karaoke(self, text, duration, t0, y=-2.95, wscale=0.32):
        if not KARAOKE_ON:
            return VGroup()   # đã tắt karaoke — không hiện chữ chạy
        # Nếu có file căn chỉnh -> dùng timestamp thật (khớp 100%); nếu không -> ước lượng.
        words = self._load_words(getattr(self, "beat_seg", None))
        if words:
            return self._karaoke_aligned(words, t0, y, wscale)
        chunks = chunk_text(text)
        weights = [sum(syl_w(w) for w in c) for c in chunks]
        total = sum(weights)
        lead, tail = 0.15, 0.3
        span = max(0.1, duration - lead - tail)

        groups = VGroup()
        acc = 0.0
        for c_words, wt in zip(chunks, weights):
            c_start = lead + span * (acc / total)
            c_end = lead + span * ((acc + wt) / total)
            acc += wt
            ww = [syl_w(w) for w in c_words]
            tw = sum(ww)
            wstarts, a = [], 0.0
            cspan = max(0.05, c_end - c_start - 0.05)
            for x in ww:
                wstarts.append(c_start + cspan * (a / tw))
                a += x
            word_mobs = [Text(w, font=FONT, weight=BOLD, color=UNSPOKEN).scale(wscale) for w in c_words]
            block = self._wrap(word_mobs).move_to([0, y, 0])
            card = RoundedRectangle(
                corner_radius=0.16, width=block.width + 0.5, height=block.height + 0.4,
            ).set_stroke(GROW, 1.5, opacity=0.45).set_fill(BG_CARD, opacity=0.92)
            card.move_to(block).set_z_index(-1)
            grp = VGroup(card, *word_mobs)

            def make_upd(cs=c_start, ce=c_end, ws=list(wstarts), mobs=word_mobs, cd=card):
                def upd(_):
                    e = self.renderer.time - t0
                    vis = cs <= e < ce
                    cd.set_opacity(0.92 if vis else 0)
                    cd.set_stroke(opacity=0.45 if vis else 0)
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

    def end_karaoke(self, groups):
        for g in groups:
            g.clear_updaters()
        self.remove(groups)

    # ---------- INTRO (dọc, ~3.5s) ----------
    def play_intro(self):
        self.camera.background_color = BG
        glow = Ellipse(width=5, height=7, color=PURPLE).set_fill(PURPLE, 0.06).set_stroke(width=0).set_z_index(-5)
        self.add(glow)

        parrot = mascot_parrot(1.5).move_to([0, 1.6, 0])
        hook = fit_w(Text(SERIES_HOOK, font=FONT, weight=BOLD, color=DEBT, line_spacing=1.1).scale(0.95), 4.1)
        hook.move_to([0, -1.1, 0])
        self.play(FadeIn(parrot, scale=0.85), run_time=0.45)
        self.play(Write(hook), run_time=0.7)
        self.play(Transform(parrot, mascot_parrot(1.5, smart=True).move_to(parrot)),
                  Flash(parrot.get_center() + UP * 0.7, color=ACCENT, line_length=0.5, num_lines=14), run_time=0.45)
        self.wait(0.15)

        name = fit_w(Text(CHANNEL_NAME, font=FONT, weight=BOLD, color=WHITE).scale(1.0), 4.0)
        tag = fit_w(Text(TAGLINE, font=FONT, color=ACCENT).scale(0.6), 4.0)
        brand = VGroup(name, tag).arrange(DOWN, buff=0.22).move_to([0, -0.8, 0])
        ul = Line(name.get_left(), name.get_right()).set_stroke(ACCENT, 4).next_to(name, DOWN, buff=0.1)
        self.play(FadeOut(hook), parrot.animate.scale(0.72).move_to([0, 1.7, 0]), run_time=0.4)
        self.play(Write(name), run_time=0.6)
        self.play(FadeIn(tag, shift=UP * 0.15), Create(ul), run_time=0.45)
        self.wait(0.45)
        self.play(FadeOut(VGroup(parrot, brand, ul, glow)), run_time=0.4)

    # ---------- KHUNG TEMPLATE (dọc) ----------
    def start_template(self, total):
        self._total = max(0.1, total)
        self._content_t0 = self.renderer.time
        fw, fh = config.frame_width, config.frame_height
        LX, RX = -fw / 2 + 0.25, fw / 2 - 0.25
        py = fh / 2 - 0.22

        pb_bg = Line([LX, py, 0], [RX, py, 0]).set_stroke("#2A3142", 5)
        pb_fg = Line([LX, py, 0], [LX + 0.001, py, 0]).set_stroke(ACCENT, 7)

        def pb_upd(m):
            frac = min(max((self.renderer.time - self._content_t0) / self._total, 0.0), 1.0)
            m.put_start_and_end_on([LX, py, 0], [LX + (RX - LX) * max(frac, 0.001), py, 0])
        pb_fg.add_updater(pb_upd)

        dot = Dot(color=ACCENT, radius=0.06)
        tp = Text(self.TOPIC, font=FONT, weight=BOLD, color=ACCENT).scale(0.38)
        chip = VGroup(dot, tp).arrange(RIGHT, buff=0.14)
        chip.next_to([LX, py, 0], DOWN, buff=0.18).align_to([LX, 0, 0], LEFT)

        # watermark: vẹt nhỏ ở góc TRÊN-PHẢI (tránh đè băng karaoke ở đáy)
        wm = mascot_parrot(0.3, smart=True).set_opacity(0.55)
        wm.next_to([RX, py, 0], DOWN, buff=0.12).align_to([RX, 0, 0], RIGHT)

        self.add(pb_bg, pb_fg, chip, wm)
        self._template = VGroup(pb_bg, pb_fg, chip, wm)

    # ---------- OUTRO ngắn (dọc) ----------
    def brand_stinger(self):
        parrot = mascot_parrot(1.0, smart=True).move_to([0, 1.0, 0])
        name = fit_w(Text(CHANNEL_NAME, font=FONT, weight=BOLD, color=WHITE).scale(0.95), 4.0)
        tag = fit_w(Text(TAGLINE, font=FONT, color=ACCENT).scale(0.55), 4.0)
        brand = VGroup(name, tag).arrange(DOWN, buff=0.2).next_to(parrot, DOWN, buff=0.5)
        self.play(FadeIn(parrot, shift=UP * 0.3), Write(name), run_time=0.6)
        self.play(FadeIn(tag, shift=UP * 0.15), Wiggle(parrot), run_time=0.6)
        self.wait(0.4)
