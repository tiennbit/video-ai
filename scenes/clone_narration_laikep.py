"""
Sinh lời thoại TẬP 1 (lãi kép / cấp số nhân) bằng GIỌNG CLONE của user (VoxCPM2, CPU).

Chạy bằng venv riêng:
    ~/voxcpm-venv/bin/python scenes/clone_narration_laikep.py

Nguồn thoại: narration_texts_laikep.py (NGUỒN DUY NHẤT).
Mẫu tham chiếu (giọng bạn): output/narration/voice-yeu_ref16k.wav  (16kHz, ~20s)
Xuất: output/narration_laikep/<id>.wav  (48kHz) — scene Manim đọc trực tiếp.

--- TỐI ƯU GIỌNG (các núm chỉnh) ---
* INFERENCE_TIMESTEPS: 10 (nhanh) → 16–24 (nét hơn, mượt hơn). Trên CPU mỗi bước
  ~tỉ lệ thuận thời gian: 16 bước ≈ gấp 1.6× thời gian render so với 10. ~4.5 phút
  thoại ở 16 bước có thể mất ~45–60 phút trên máy này (RTF cao). Chạy qua đêm/nền.
* CFG_VALUE: 2.0 (cân bằng). Tăng 2.3–2.6 → bám timbre của bạn sát hơn nhưng dễ "cứng";
  giảm 1.4–1.7 → tự nhiên hơn nhưng bớt giống. Nên A/B 2.0 vs 2.4 trên 1 câu trước.
* LOAD_DENOISER: True → khử ồn nền của mẫu tham chiếu trước khi clone (sạch hơn,
  tốn thêm RAM/thời gian load). Bật nếu file voice-yeu hơi rè/ồn.
* Mẫu tham chiếu là YẾU TỐ QUYẾT ĐỊNH: dùng đoạn ~15–20s giọng bạn đọc RÕ, đúng tông
  "kể chuyện/bí mật" mà bạn muốn video có — VoxCPM sao chép cả ngữ điệu, không chỉ chất giọng.
"""
import os
import sys
import time

import soundfile as sf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from narration_texts_laikep import SEGMENTS

# ---------- Núm tối ưu ----------
INFERENCE_TIMESTEPS = 16     # 10 nhanh · 16–24 nét hơn
CFG_VALUE = 2.0              # 2.0 cân bằng · ↑ giống hơn/cứng · ↓ tự nhiên hơn/bớt giống
LOAD_DENOISER = False        # True nếu mẫu tham chiếu có tạp âm

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REF = os.path.join(BASE, "output", "narration", "voice-yeu_ref16k.wav")
OUTDIR = os.path.join(BASE, "output", "narration_laikep")


def main():
    if not os.path.exists(REF):
        sys.exit(f"Không thấy mẫu tham chiếu giọng bạn: {REF}")
    os.makedirs(OUTDIR, exist_ok=True)

    from voxcpm import VoxCPM
    print(f"Loading VoxCPM2 on CPU (denoiser={LOAD_DENOISER})...", flush=True)
    t0 = time.time()
    model = VoxCPM.from_pretrained(
        "openbmb/VoxCPM2", load_denoiser=LOAD_DENOISER, optimize=False, device="cpu"
    )
    print(f"Loaded in {time.time()-t0:.0f}s | cfg={CFG_VALUE} steps={INFERENCE_TIMESTEPS}", flush=True)

    for name, text in SEGMENTS.items():
        t = time.time()
        wav = model.generate(
            text=text,
            reference_wav_path=REF,
            cfg_value=CFG_VALUE,
            inference_timesteps=INFERENCE_TIMESTEPS,
        )
        path = os.path.join(OUTDIR, f"{name}.wav")
        sf.write(path, wav, model.tts_model.sample_rate)
        dur = len(wav) / model.tts_model.sample_rate
        print(f"OK {name}: {time.time()-t:.0f}s render, {dur:.1f}s audio -> {path}", flush=True)

    print("ALL_CLONED_DONE", flush=True)


if __name__ == "__main__":
    main()
