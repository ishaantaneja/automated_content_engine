import os
import torch
import numpy as np
import textwrap
from bark import generate_audio, preload_models
from scipy.io.wavfile import write as write_wav, read as read_wav

# ────────────────────────────────────────────────────────────────────────────────
# ✅ ENV SETUP FOR LOW VRAM GPUs
os.environ["SUNO_USE_SMALL_MODELS"] = "True"   # Low VRAM support
os.environ["SUNO_OFFLOAD_CPU"] = "True"        # Offload heavy ops to CPU
# ────────────────────────────────────────────────────────────────────────────────

# ✅ CHECK CUDA STATUS
print("🧠 torch.cuda.is_available():", torch.cuda.is_available())
print("🚀 GPU:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "N/A")

# ────────────────────────────────────────────────────────────────────────────────
# 📂 DIRS
INPUT_DIR = "generated"
OUTPUT_DIR = "audio"
MAX_CHARS = 400  # ~13s per chunk
SAMPLE_RATE = 24000

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ✅ LOAD MODELS
preload_models()

# ────────────────────────────────────────────────────────────────────────────────
# 🔁 WAV MERGING FIX (handles float32 format)
def merge_wavs(paths, output_path):
    merged = []
    for path in paths:
        _, audio = read_wav(path)
        merged.append(audio)

    final_audio = np.concatenate(merged)
    write_wav(output_path, rate=SAMPLE_RATE, data=final_audio)

# ────────────────────────────────────────────────────────────────────────────────
# 🎯 MAIN LOOP
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".txt"):
        base = filename.replace(".txt", "")
        txt_path = os.path.join(INPUT_DIR, filename)

        with open(txt_path, "r", encoding="utf-8") as f:
            script = f.read()

        chunks = textwrap.wrap(script, width=MAX_CHARS)
        chunk_paths = []

        for i, chunk in enumerate(chunks):
            print(f"🎙️ Generating chunk {i+1}/{len(chunks)}: {base}")
            audio = generate_audio(chunk)

            chunk_path = os.path.join(OUTPUT_DIR, f"{base}_part{i}.wav")
            write_wav(chunk_path, SAMPLE_RATE, audio)
            chunk_paths.append(chunk_path)

        final_path = os.path.join(OUTPUT_DIR, f"{base}.wav")
        merge_wavs(chunk_paths, final_path)
        print(f"✅ Final merged voiceover saved to: {final_path}")
