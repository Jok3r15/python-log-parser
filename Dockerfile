# 1. Usar una imagen oficial de Python ligera como base
FROM python:3.10-slim

# 2. Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Variable de entorno crucial para DevOps: evita que Python use buffers en los logs.
# Esto hace que veas los prints en la consola de Docker al INSTANTE.
ENV PYTHONUNBUFFERED=1

# 4. Copiar únicamente tu script al contenedor
COPY main.py .

# 5. Comando por defecto para ejecutar el centinela
CMD ["python", "main.py"]
