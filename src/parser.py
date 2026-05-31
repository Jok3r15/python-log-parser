from collections import Counter

def parse_logs(file_path):
    ip_counts = Counter()
    try:
        with open(file_path, "r") as f:
            for line in f:
                ip = line.split(" ")[0]
                ip_counts[ip] += 1
        return ip_counts
    except FileNotFoundError:
        print("El archivo no existe.")
        return None

if __name__ == "__main__":
    results = parse_logs("data/access.log")
    if results:
        print("--- Análisis de Seguridad: Reporte de Tráfico ---")
        for ip, count in results.items():
            if count > 2:
                print(f"[!] ALERTA: Actividad sospechosa detectada: {ip} con {count} peticiones.")
            else:
                print(f"[*] IP: {ip} | Peticiones: {count} (Normal)")
