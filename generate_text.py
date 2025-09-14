import subprocess
import json
from pathlib import Path
//set comment

GENERATED_DIR = Path("generated")
GENERATED_DIR.mkdir(exist_ok=True)

with open("prompts.json", "r", encoding="utf-8") as f:
    prompts = json.load(f)

for topic, prompt in prompts.items():
    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True,
        text=True
    )
    output = result.stdout.strip()

    # save to file
    with open(GENERATED_DIR / f"{topic}.txt", "w", encoding="utf-8") as f_out:
        f_out.write(output)

    print(f"[+] Generated script for {topic}")
