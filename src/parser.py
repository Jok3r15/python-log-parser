import os
import logging
import re

# Configuración de logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Patrones de seguridad (Regex)
# 1. Busca palabras como ERROR, CRITICAL o FAILED
# 2. Busca intentos fallidos de SSH (Failed password)
# 3. Busca códigos de estado HTTP de error (4xx, 5xx)
SECURITY_PATTERNS = {
    "auth_failure": re.compile(r"Failed password|Authentication failure|Invalid user"),
    "system_error": re.compile(r"ERROR|CRITICAL|FATAL"),
    "web_attack": re.compile(r" 404 | 403 | 500 ")
}

def load_log(file_path):
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def analyze_line(line):
    """
    Analiza una línea buscando patrones sospechosos.
    Retorna el tipo de anomalía si encuentra algo.
    """
    for alert_type, pattern in SECURITY_PATTERNS.items():
        if pattern.search(line):
            return alert_type
    return None

if __name__ == "__main__":
    sample_path = "data/sample.log"
    logging.info(f"Analyzing {sample_path} for security anomalies...")
    
    for log_line in load_log(sample_path):
        anomaly = analyze_line(log_line)
        if anomaly:
            logging.warning(f"ALERT [{anomaly.upper()}]: {log_line}")
        else:
            print(f"Normal: {log_line}")
