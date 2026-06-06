import time
import os
import sys
from collections import defaultdict

def main():
    log_file = "access.log"
    threshold = 3
    blacklist_file = "blacklist.txt"
    
    # 1. Cargamos persistencia UNA VEZ al inicio
    def load_blacklist():
        if os.path.exists(blacklist_file):
            with open(blacklist_file, "r") as f:
                return set(line.strip() for line in f)
        return set()

    blacklist = load_blacklist()
    # 2. IP_COUNTS VIVE FUERA DEL BUCLE
    ip_counts = defaultdict(int)
    
    print(f"--- Centinela Modo WSL Robusto | Blacklist: {len(blacklist)} IPs ---")
    
    # Aseguramos existencia del archivo
    if not os.path.exists(log_file):
        open(log_file, 'a').close()
        
    last_size = os.path.getsize(log_file)
    
    try:
        while True:
            current_size = os.path.getsize(log_file)
            
            # Si el archivo fue borrado o rotado, reiniciamos el tamaño
            if current_size < last_size:
                last_size = 0
            
            if current_size > last_size:
                with open(log_file, "r") as f:
                    f.seek(last_size)
                    new_lines = f.readlines()
                    
                    for line in new_lines:
                        line = line.strip()
                        if line:
                            ip = line.split()[0]
                            # Solo contamos si no está bloqueada
                            if ip not in blacklist:
                                ip_counts[ip] += 1
                                print(f"[EVENTO] {ip} | Intentos acumulados: {ip_counts[ip]}")
                                
                                if ip_counts[ip] > threshold:
                                    print(f"[!!!] BLOQUEANDO: {ip}")
                                    with open(blacklist_file, "a") as b:
                                        b.write(f"{ip}\n")
                                    blacklist.add(ip)
                
                last_size = current_size
            
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nCentinela detenido.")

if __name__ == "__main__":
    main()
