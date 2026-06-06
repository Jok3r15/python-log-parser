# Python Log Parser

A lightweight, efficient log auditing tool designed for real-time monitoring and anomaly detection. This project is built for server-side log analysis, featuring automated infrastructure deployment and system orchestration.

## Features

* **Log Parsing:** Efficient, line-by-line processing of log files with low memory footprint.
* **Automation:** Fully automated infrastructure provisioning via **Terraform** (AWS).
* **Process Management:** Managed as a native Linux service via **systemd** for high availability.
* **CI/CD:** Automated testing and build pipeline via GitHub Actions.

## Repository Structure

```text
.
├── src/            # Core parsing logic
├── terraform/      # Infrastructure as Code (AWS configuration)
├── data/           # Sample log files for auditing
├── tests/          # Unit testing suite
├── Makefile        # Automation commands (Build, Test, Deploy)
└── main.py         # Main entry point for the auditing service

Infrastructure (AWS)
We use Terraform to provision the AWS environment, ensuring consistency across environments.

Instance: t3.micro (Ubuntu 22.04).

Networking: Secure VPC with Network Segmentation.

AMI: Automated dynamic selection of the latest Ubuntu AMI.

Deployment & Execution
1. Infrastructure
To provision the AWS environment:

Bash
cd terraform
terraform init
terraform apply
2. Service Management
The parser runs as a native Linux service. Manage it via systemd:

Bash
sudo systemctl start log-parser   # Start the service
sudo systemctl status log-parser  # Check status
sudo journalctl -u log-parser -f  # View logs in real-time
Getting Started
Clone the repo: git clone https://github.com/Jok3r15/python-log-parser.git

Setup Environment: python3 -m venv .venv && source .venv/bin/activate

Run: python3 main.py

License
Distributed under the MIT License. See LICENSE for more information.
