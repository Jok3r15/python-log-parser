# Python Log Parser

A lightweight, efficient log auditing tool designed to monitor server traffic and detect anomalies in real-time.

## Features
* **Log Generator:** Simulates real-world web traffic (IPs, HTTP methods, status codes).
* **Log Parser:** Efficiently processes log files line-by-line to ensure low memory footprint.
* **Anomaly Detection:** Identifies suspicious activity based on configurable traffic thresholds.

## Architecture
* **Language:** Python 3
* **Containerization:** Docker (with persistent volume mapping)
* **OS Compatibility:** Linux / WSL2 optimized
* **CI/CD:** Automated testing and build pipeline via GitHub Actions

## Getting Started
1. **Clone the repository:** `git clone https://github.com/Jok3r15/python-log-parser.git`
2. **Run the log generator:** `python3 src/generator.py`
3. **Run the parser:** `python3 src/parser.py`

## Project Status
* **Robust Sentinel:** Implemented real-time log monitoring with persistent state memory (Blacklist) optimized for WSL and Linux environments, fully containerized and integrated with a CI/CD pipeline.

## License
Distributed under the MIT License. See LICENSE for more information.
