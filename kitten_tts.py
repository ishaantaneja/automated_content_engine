import os
import soundfile as sf
from kittentts import KittenTTS

# Initialize the model (this will download required files)
tts = KittenTTS("KittenML/kitten-tts-nano-0.1")

input_dir = "generated"
output_dir = "audio"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(input_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read().strip()

        output_path = os.path.join(output_dir, filename.replace(".txt", ".wav"))
        print(f"[+] Generating: {output_path}")

        # Generate audio array using KittenTTS
        audio = tts.generate(text)

        # Save audio at 24 kHz sample rate
        sf.write(output_path, audio, 24000)
        print(f"[✔] Saved: {output_path}")
