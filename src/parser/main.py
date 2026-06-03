import argparse
from datetime import datetime
from collections import defaultdict

def main():
    # 1. Definición estricta de argumentos
    parser = argparse.ArgumentParser(description="Log Parser Profesional")
    parser.add_argument("--file", required=True, help="Archivo de logs a analizar")
    parser.add_argument("--threshold", type=int, default=3, help="Umbral de alertas")
    args = parser.parse_args()

    # 2. Inicialización de estructuras de datos
    ip_counts = defaultdict(int)
    report_file_name = "reporte_seguridad.txt"
    found_suspicious = False
# Genera un nombre como: reporte_2026-06-02_20-15.txt
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    report_file_name = f"reporte_{timestamp}.txt"

    # 3. Lógica de procesamiento segura
    try:
        with open(args.file, 'r') as f:
            for line in f:
                if line.strip(): # Evita errores con líneas vacías
                    ip = line.split()[0]
                    ip_counts[ip] += 1
        
        # 4. Generación de reporte
        with open(report_file_name, 'w') as report_file:
            for ip, count in ip_counts.items():
                if count > args.threshold:
                    msg = f"ALERTA: IP {ip} superó el umbral con {count} peticiones.\n"
                    print(msg.strip())
                    report_file.write(msg)
                    found_suspicious = True
        
        if not found_suspicious:
            print("No se encontraron IPs sospechosas.")
        else:
            print(f"Reporte generado en: {report_file_name}")

    except FileNotFoundError:
        print(f"Error: El archivo '{args.file}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
