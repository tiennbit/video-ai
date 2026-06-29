"""
Hàm sinh giọng clone DÙNG CHUNG cho mọi tập (VoxCPM2, CPU).
Mỗi clone_narration_<slug>.py chỉ cần:  run("<slug>", SEGMENTS)
Mẫu giọng: output/narration/voice-yeu_ref16k.wav · Xuất: output/narration_<slug>/<id>.wav (48kHz).
"""
import os
import sys
import time

import soundfile as sf

INFERENCE_TIMESTEPS = 16
CFG_VALUE = 2.0
LOAD_DENOISER = False


def run(slug, segments, spoken=None):
    """slug: tên tập; segments: dict {id: text}; spoken: hàm id->text đọc (tuỳ chọn)."""
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ref = os.path.join(base, "output", "narration", "voice-yeu_ref16k.wav")
    outdir = os.path.join(base, "output", f"narration_{slug}")
    if not os.path.exists(ref):
        sys.exit(f"Không thấy mẫu tham chiếu giọng bạn: {ref}")
    os.makedirs(outdir, exist_ok=True)
    from voxcpm import VoxCPM
    print(f"Loading VoxCPM2 on CPU (denoiser={LOAD_DENOISER})...", flush=True)
    t0 = time.time()
    model = VoxCPM.from_pretrained(
        "openbmb/VoxCPM2", load_denoiser=LOAD_DENOISER, optimize=False, device="cpu"
    )
    print(f"Loaded in {time.time()-t0:.0f}s | cfg={CFG_VALUE} steps={INFERENCE_TIMESTEPS}", flush=True)
    for name in segments:
        text = spoken(name) if spoken else segments[name]
        t = time.time()
        wav = model.generate(text=text, reference_wav_path=ref,
                             cfg_value=CFG_VALUE, inference_timesteps=INFERENCE_TIMESTEPS)
        path = os.path.join(outdir, f"{name}.wav")
        sf.write(path, wav, model.tts_model.sample_rate)
        print(f"OK {name}: {time.time()-t:.0f}s render, {len(wav)/model.tts_model.sample_rate:.1f}s audio -> {path}", flush=True)
    print("ALL_CLONED_DONE", flush=True)
