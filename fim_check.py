import hashlib
import json
import os
from datetime import datetime

TARGET_FOLDER = "target_folder"
BASELINE_FILE = "baseline.json"
LOG_FILE = "fim_log.txt"

def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")

def check_integrity():
    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    current_files = {}
    for root, dirs, files in os.walk(TARGET_FOLDER):
        for filename in files:
            filepath = os.path.join(root, filename)
            current_files[filepath] = calculate_hash(filepath)

    changes_found = False

    for filepath, old_hash in baseline.items():
        if filepath not in current_files:
            log_alert(f"DELETED: {filepath}")
            changes_found = True
        elif current_files[filepath] != old_hash:
            log_alert(f"MODIFIED: {filepath}")
            changes_found = True

    for filepath in current_files:
        if filepath not in baseline:
            log_alert(f"NEW FILE: {filepath}")
            changes_found = True

    if not changes_found:
        print("No changes detected. All files match baseline.")

if __name__ == "__main__":
    check_integrity()
