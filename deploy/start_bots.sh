#!/bin/bash

# Asegurar que estamos en el directorio raíz del proyecto
# Obtener el directorio donde está este script (deploy/) y subir un nivel
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

echo "📂 Directorio de trabajo: $(pwd)"

# Usar directamente el python del entorno virtual
PYTHON_CMD="venv/bin/python"

# Verificar que existe
if [ ! -f "$PYTHON_CMD" ]; then
    echo "❌ Error: No se encuentra $PYTHON_CMD"
    echo "   Asegúrate de haber creado el entorno virtual: python3 -m venv venv"
    exit 1
fi

echo "🚀 Iniciando Bots Neuronales..."
echo "   🐍 Usando Python: $PYTHON_CMD"

# 1. Neural Bot MULTI (Todos los pares)
echo "   - Iniciando Neural Bot MULTI..."
# Lista de símbolos soportados
SYMBOLS="ETH/USDT,SOL/USDT,DOGE/USDT,ADA/USDT,AVAX/USDT,BNB/USDT,LINK/USDT,XRP/USDT"

nohup $PYTHON_CMD -u bot_neural.py --mode paper --model BTC_4h_v8 --id MULTI --symbols "$SYMBOLS" > log_neural_multi.txt 2>&1 &
echo $! > pid_neural_multi.txt

# 2. Telegram Bot (Manejador)
echo "   - Iniciando Telegram Bot..."
nohup $PYTHON_CMD -u telegram_bot_handler.py > log_telegram.txt 2>&1 &
echo $! > pid_telegram.txt

echo "✅ Todos los servicios iniciados en segundo plano."
echo "   Logs disponibles en: log_neural_multi.txt, log_telegram.txt"
