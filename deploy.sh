#!/bin/bash

# 1. Correr el Parser de Python
echo "--- Iniciando Auditoría de Logs ---"
python3 main.py --file data/sample.log

# 2. Verificar si la Blacklist cambió
if git status --porcelain data/blacklist.txt | grep -q "M"; then
    echo "--- ¡Nuevas amenazas detectadas! Actualizando Red ---"
    
    cd terraform
    terraform init
    terraform apply -auto-approve
    
    echo "--- Mitigación Completada ---"
else
    echo "--- No se detectaron nuevas amenazas. Sistema Seguro ---"
fi
