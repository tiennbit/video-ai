"""
Căn chỉnh karaoke — lấy thời điểm TỪNG TỪ từ giọng thật bằng faster-whisper,
NHƯNG hiển thị ĐÚNG CHỮ trong kịch bản (narration_texts_<slug>.py), chỉ mượn timing.
=> phụ đề luôn đúng chính tả/dấu (không bị Whisper nghe nhầm như "Bí"->"Bi").

Chạy:  .venv/bin/python scenes/align_narration.py output/narration_<slug>
Xuất:  output/narration_<slug>/<id>.words.json = [["từ", giây], ...]
Đổi model: WHISPER_MODEL=medium .venv/bin/python scenes/align_narration.py <dir>
"""
import difflib
import json
import os
import sys
import unicodedata

MODEL = os.environ.get("WHISPER_MODEL", "small")


def _norm(s):
    """Bỏ dấu + thường hoá để SO KHỚP (chỉ dùng khi khớp, không dùng để hiển thị)."""
    s = s.lower().strip(" .,?!:;…\"'()-—")
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def _map_times(our, wh_tokens, wh_times):
    """Gán cho mỗi từ trong KỊCH BẢN một mốc thời gian từ Whisper (khớp chuỗi)."""
    a = [_norm(x) for x in our]
    b = [_norm(x) for x in wh_tokens]
    times = [None] * len(our)
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                times[i1 + k] = wh_times[j1 + k]
        elif tag == "replace":
            n, m = i2 - i1, j2 - j1
            for k in range(n):
                if m > 0:
                    times[i1 + k] = wh_times[min(j1 + k * m // n, j2 - 1)]
        # delete (từ kịch bản thừa) -> để None, lấp sau; insert -> bỏ
    last = 0.0
    for k in range(len(times)):
        if times[k] is None:
            times[k] = last
        else:
            last = times[k]
    for k in range(1, len(times)):
        times[k] = max(times[k], times[k - 1])
    return times


def align_dir(d):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    slug = os.path.basename(d.rstrip("/")).replace("narration_", "")
    SEG = None
    try:
        SEG = __import__(f"narration_texts_{slug}").SEGMENTS
    except Exception as e:  # noqa: BLE001
        print(f"(!) Không import được narration_texts_{slug} ({e}) -> dùng nguyên văn Whisper", flush=True)

    from faster_whisper import WhisperModel
    print(f"Loading Whisper '{MODEL}' (CPU)...", flush=True)
    model = WhisperModel(MODEL, device="cpu", compute_type="int8")

    for f in sorted(x for x in os.listdir(d) if x.endswith(".wav")):
        seg_id = f[:-4]
        segs, _ = model.transcribe(os.path.join(d, f), language="vi", word_timestamps=True, vad_filter=False)
        wh = [(w.word.strip(), round(float(w.start), 3)) for s in segs for w in (s.words or []) if w.word.strip()]
        wh_tokens, wh_times = [x[0] for x in wh], [x[1] for x in wh]
        if SEG and seg_id in SEG and wh:
            our = SEG[seg_id].split()
            t = _map_times(our, wh_tokens, wh_times)
            words = [[our[k], t[k]] for k in range(len(our))]
            src = "kịch bản"
        else:
            words = [[w, ts] for w, ts in wh]
            src = "whisper"
        json.dump(words, open(os.path.join(d, seg_id + ".words.json"), "w", encoding="utf-8"), ensure_ascii=False)
        print(f"✓ {f}: {len(words)} từ ({src})", flush=True)
    print("ALIGN_DONE", flush=True)


if __name__ == "__main__":
    align_dir(os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "output/narration_xetnghiem"))
