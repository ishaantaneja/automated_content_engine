# kitten_tts.py
import os
from pathlib import Path
from kitten_tts import KittenTTS

# Directories
GENERATED_DIR = Path("generated")
AUDIO_DIR = Path("audio")
AUDIO_DIR.mkdir(exist_ok=True)

def text_to_speech(input_file: Path, output_file: Path):
    """Convert a text file into speech using KittenTTS."""
    tts = KittenTTS()
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        print(f"[!] Skipping empty file: {input_file}")
        return

    print(f"[+] Generating speech for {input_file.name}...")
    audio = tts.speak(text)

    # Save as WAV
    with open(output_file, "wb") as f_out:
        f_out.write(audio)

    print(f"[✓] Saved: {output_file}")

def main():
    txt_files = list(GENERATED_DIR.glob("*.txt"))
    if not txt_files:
        print("[!] No generated text files found in 'generated/' folder.")
        return

    for txt_file in txt_files:
        output_file = AUDIO_DIR / f"{txt_file.stem}.wav"
        text_to_speech(txt_file, output_file)

if __name__ == "__main__":
    main()
