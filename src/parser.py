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
        print("El archivo no existe. ¡Ejecuta el generador primero!")

if __name__ == "__main__":
    results = parse_logs("data/access.log")
    print("Resumen de tráfico por IP:")
    for ip, count in results.items():
        print(f"IP: {ip} | Peticiones: {count}")
