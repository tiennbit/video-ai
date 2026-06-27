"""
Sinh 5 đoạn lời thoại bằng GIỌNG CLONE của user (VoxCPM2, chạy CPU).
Chạy bằng venv riêng:
    ~/voxcpm-venv/bin/python scenes/clone_narration.py

Yêu cầu: file tham chiếu 16kHz tại output/narration/voice-yeu_ref16k.wav
Xuất: output/narration_cloned/<id>.wav  (48kHz)
"""
import os
import sys
import time

import soundfile as sf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from narration_texts import SEGMENTS, tts_text

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REF = os.path.join(BASE, "output", "narration", "voice-yeu_ref16k.wav")
OUTDIR = os.path.join(BASE, "output", "narration_cloned")


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    from voxcpm import VoxCPM
    print("Loading VoxCPM2 on CPU...", flush=True)
    t0 = time.time()
    model = VoxCPM.from_pretrained(
        "openbmb/VoxCPM2", load_denoiser=False, optimize=False, device="cpu"
    )
    print(f"Loaded in {time.time()-t0:.0f}s", flush=True)

    # Cho phép truyền id đoạn cần sinh lại: python clone_narration.py 04_formula
    ids = [a for a in sys.argv[1:] if a in SEGMENTS] or list(SEGMENTS.keys())
    for name in ids:
        text = tts_text(name)
        t = time.time()
        wav = model.generate(
            text=text,
            reference_wav_path=REF,
            cfg_value=2.0,
            inference_timesteps=10,
        )
        path = os.path.join(OUTDIR, f"{name}.wav")
        sf.write(path, wav, model.tts_model.sample_rate)
        dur = len(wav) / model.tts_model.sample_rate
        print(f"OK {name}: {time.time()-t:.0f}s render, {dur:.1f}s audio -> {path}", flush=True)

    print("ALL_CLONED_DONE", flush=True)


if __name__ == "__main__":
    main()
