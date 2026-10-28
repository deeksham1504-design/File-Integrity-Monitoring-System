# File Integrity Monitoring System

A Python tool that detects modified, deleted, and new files in a
monitored folder using SHA-256 hashing and real-time monitoring on Linux.

## Features
- Baseline creation using SHA-256 hashes (fim_baseline.py)
- On-demand integrity check (fim_check.py)
- Real-time monitoring using watchdog / inotify (fim_watch.py)
- Colored terminal alerts
- Timestamped logging

## Tech Stack
Python 3, hashlib, watchdog, Ubuntu (WSL)

## How to Run
git clone https://github.com/deeksham1504-design/File-Integrity-Monitoring-System.git
cd File-Integrity-Monitoring-System
python3 -m venv venv
source venv/bin/activate
pip install watchdog
python3 fim_baseline.py
python3 fim_check.py
python3 fim_watch.py

## Future Scope
Email alerts, web dashboard, running as a background service
