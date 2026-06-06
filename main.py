import argparse
import logging
from src.parser import load_log, analyze_line, save_alert_to_json, extract_ip, block_ip

def main():
    parser = argparse.ArgumentParser(description="SecOps Log Parser - Tool for security auditing")
    parser.add_argument("-f", "--file", required=True, help="Path to the log file to analyze")
    args = parser.parse_args()

    logging.info(f"Starting analysis on: {args.file}")
    
    for log_line in load_log(args.file):
        anomaly = analyze_line(log_line)
        
        if anomaly:
            logging.warning(f"ALERT [{anomaly.upper()}]: {log_line}")
            
            # 1. Guardar evidencia en JSON
            save_alert_to_json(anomaly, log_line)
            
            # 2. Extraer IP y Bloquear (Mitigación)
            ip = extract_ip(log_line)
            if ip:
                block_ip(ip)
        else:
            print(f"Normal: {log_line}")

if __name__ == "__main__":
    main()
