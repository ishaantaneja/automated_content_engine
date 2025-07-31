import os
import json
import datetime
import subprocess

# Load prompts from prompts.json
with open("prompts.json", "r") as f:
    prompts = json.load(f)

# Create output folder if not exists
output_dir = "generated"
os.makedirs(output_dir, exist_ok=True)

# Today's date for file naming
today = datetime.date.today().isoformat()

# Loop through all niches
for topic, prompt in prompts.items():
    print(f"Generating script for: {topic}")

    # Run prompt through Ollama
    full_cmd = f'echo "{prompt}" | ollama run mistral'
    result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True, encoding='utf-8').stdout


    # Save to file
    filename = f"{today}_{topic}.txt"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Saved: {filepath}")
