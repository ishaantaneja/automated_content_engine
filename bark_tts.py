import os
from bark import generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

# Load Bark models (first time = downloads weights)
preload_models()

# Input/output directories
input_dir = "generated"
output_dir = "audio"
os.makedirs(output_dir, exist_ok=True)

# Loop through all .txt scripts
for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(input_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            script = f.read()

        try:
            print(f"Generating voice for {filename}...")

            # Generate voice
            audio_array = generate_audio(script)

            # Save to .wav file (24kHz required by Bark)
            output_name = filename.replace(".txt", ".wav")
            output_path = os.path.join(output_dir, output_name)
            write_wav(output_path, rate=24000, data=audio_array)

            print(f"Saved: {output_path}")
        except Exception as e:
            print(f"Error with {filename}: {e}")
