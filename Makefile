# Valores por defecto para que nunca falle
FILE ?= logs.txt
THRESHOLD ?= 5

.PHONY: run-parser
# ... el resto sigue igual ...

.PHONY: run-parser

# Ejemplo: make run-parser FILE=logs.txt THRESHOLD=10
run-parser:
	python3 src/parser/main.py --file $(FILE) --threshold $(THRESHOLD)
