# 1. Usar una imagen oficial de Python ligera
FROM python:3.10-slim

# 2. Configurar el directorio de trabajo
WORKDIR /app

# 3. Evitar que Python use buffers (logs instantáneos)
ENV PYTHONUNBUFFERED=1

# 4. Copiar todo el directorio actual al contenedor
# Esto copia main.py, src/, data/ y demás necesario
COPY . .

# 5. Comando para ejecutar el centinela
CMD ["python", "main.py"]
