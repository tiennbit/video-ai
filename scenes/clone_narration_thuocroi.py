"""
Sinh giọng clone cho video "Bắt cây thước rơi" (VoxCPM2, CPU).
Chạy:  ~/voxcpm-venv/bin/python scenes/clone_narration_thuocroi.py
Nguồn: narration_texts_thuocroi.py · Mẫu: output/narration/voice-yeu_ref16k.wav
Xuất: output/narration_thuocroi/<id>.wav (48kHz). Sau đó nhớ chạy align_narration.py.
"""
import os
import sys
import time

import soundfile as sf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from narration_texts_thuocroi import SEGMENTS

INFERENCE_TIMESTEPS = 16
CFG_VALUE = 2.0
LOAD_DENOISER = False

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REF = os.path.join(BASE, "output", "narration", "voice-yeu_ref16k.wav")
OUTDIR = os.path.join(BASE, "output", "narration_thuocroi")


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
        wav = model.generate(text=text, reference_wav_path=REF,
                             cfg_value=CFG_VALUE, inference_timesteps=INFERENCE_TIMESTEPS)
        path = os.path.join(OUTDIR, f"{name}.wav")
        sf.write(path, wav, model.tts_model.sample_rate)
        print(f"OK {name}: {time.time()-t:.0f}s render, {len(wav)/model.tts_model.sample_rate:.1f}s audio -> {path}", flush=True)
    print("ALL_CLONED_DONE", flush=True)


if __name__ == "__main__":
    main()
