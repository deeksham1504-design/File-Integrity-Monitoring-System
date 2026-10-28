import time
import subprocess
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

TARGET_FOLDER = "target_folder"
LOG_FILE = "fim_log.txt"

# ANSI color codes
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_banner(message, color):
    line = "=" * 60
    print(f"\n{color}{BOLD}{line}")
    print(f" ALERT: {message}")
    print(f"{line}{RESET}\n")

def log_alert(message, color=RED):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")
    print_banner(entry, color)

class FIMHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            log_alert(f"FILE MODIFIED: {event.src_path}", YELLOW)

    def on_created(self, event):
        if not event.is_directory:
            log_alert(f"NEW FILE DETECTED: {event.src_path}", CYAN)

    def on_deleted(self, event):
        if not event.is_directory:
            log_alert(f"FILE DELETED: {event.src_path}", RED)

if __name__ == "__main__":
    print(f"{GREEN}{BOLD}Watching '{TARGET_FOLDER}' in real time... Press Ctrl+C to stop.{RESET}")
    observer = Observer()
    observer.schedule(FIMHandler(), path=TARGET_FOLDER, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
