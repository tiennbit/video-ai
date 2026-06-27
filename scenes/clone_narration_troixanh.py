"""Sinh giọng clone — "Vì sao trời xanh, hoàng hôn đỏ?" (VoxCPM2, CPU).
Chạy:  ~/voxcpm-venv/bin/python scenes/clone_narration_troixanh.py
Nguồn: narration_texts_troixanh.py · Mẫu: output/narration/voice-yeu_ref16k.wav
Xuất:  output/narration_troixanh/<id>.wav
"""
import os
import sys
import time

import soundfile as sf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from narration_texts_troixanh import SEGMENTS

INFERENCE_TIMESTEPS = 16
CFG_VALUE = 2.0
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REF = os.path.join(BASE, "output", "narration", "voice-yeu_ref16k.wav")
OUTDIR = os.path.join(BASE, "output", "narration_troixanh")


def main():
    if not os.path.exists(REF):
        sys.exit(f"Không thấy mẫu giọng: {REF}")
    os.makedirs(OUTDIR, exist_ok=True)
    from voxcpm import VoxCPM
    print("Loading VoxCPM2 on CPU...", flush=True)
    t0 = time.time()
    model = VoxCPM.from_pretrained("openbmb/VoxCPM2", load_denoiser=False, optimize=False, device="cpu")
    print(f"Loaded in {time.time()-t0:.0f}s | cfg={CFG_VALUE} steps={INFERENCE_TIMESTEPS}", flush=True)
    for name, text in SEGMENTS.items():
        t = time.time()
        wav = model.generate(text=text, reference_wav_path=REF, cfg_value=CFG_VALUE, inference_timesteps=INFERENCE_TIMESTEPS)
        path = os.path.join(OUTDIR, f"{name}.wav")
        sf.write(path, wav, model.tts_model.sample_rate)
        print(f"OK {name}: {time.time()-t:.0f}s render, {len(wav)/model.tts_model.sample_rate:.1f}s audio -> {path}", flush=True)
    print("ALL_CLONED_DONE", flush=True)


if __name__ == "__main__":
    main()
