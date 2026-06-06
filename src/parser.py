import os
import json
import logging
import re
from datetime import datetime

# Configuración de carpetas
LOG_DIR = "data"
ALERTS_FILE = os.path.join(LOG_DIR, "alerts.json")
BLACKLIST_FILE = os.path.join(LOG_DIR, "blacklist.txt")

os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Patrones
SECURITY_PATTERNS = {
    "auth_failure": re.compile(r"Failed password|Authentication failure"),
    "system_error": re.compile(r"ERROR|CRITICAL"),
}

def load_log(file_path):
    """Generador que lee el archivo línea por línea."""
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()

def analyze_line(line):
    """Analiza una línea en busca de patrones."""
    for alert_type, pattern in SECURITY_PATTERNS.items():
        if pattern.search(line):
            return alert_type
    return None

def extract_ip(line):
    """Extrae una dirección IPv4 de una línea de log."""
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    match = re.search(ip_pattern, line)
    return match.group(0) if match else None

def save_alert_to_json(alert_type, line):
    """Persiste la alerta en JSON."""
    alert_data = {
        "timestamp": datetime.now().isoformat(),
        "type": alert_type,
        "message": line
    }
    with open(ALERTS_FILE, "a") as f:
        f.write(json.dumps(alert_data) + "\n")
    logging.info(f"Alert persisted to {ALERTS_FILE}")

def block_ip(ip):
    """Añade la IP a la lista de bloqueo si no existe."""
    if not ip:
        return
        
    # Verificar si ya está bloqueada
    if os.path.exists(BLACKLIST_FILE):
        with open(BLACKLIST_FILE, "r") as f:
            if ip in f.read():
                return
                
    with open(BLACKLIST_FILE, "a") as f:
        f.write(f"{ip}\n")
    logging.warning(f"IP {ip} añadida a la blacklist para mitigación.")
