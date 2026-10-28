import hashlib
import json
import os

TARGET_FOLDER = "target_folder"
BASELINE_FILE = "baseline.json"

def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def create_baseline():
    baseline = {}
    for root, dirs, files in os.walk(TARGET_FOLDER):
        for filename in files:
            filepath = os.path.join(root, filename)
            baseline[filepath] = calculate_hash(filepath)

    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)

    print(f"Baseline created with {len(baseline)} files.")
    print(f"Saved to {BASELINE_FILE}")

if __name__ == "__main__":
    create_baseline()
