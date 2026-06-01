import argparse
from logger_config import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Parser de Logs Profesional")
    parser.add_argument("--file", required=True, help="Ruta al archivo de log")
    parser.add_argument("--threshold", type=int, default=5, help="Umbral de alertas")
    
    args = parser.parse_args()
    
    logger.info(f"Iniciando análisis del archivo: {args.file} con umbral: {args.threshold}")
    # Aquí iría tu lógica que usa args.file y args.threshold
    print(f"Analizando {args.file}...")

if __name__ == "__main__":
    main()
