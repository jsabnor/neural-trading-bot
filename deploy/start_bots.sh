#!/bin/bash

# Detectar Python
PYTHON_CMD="python"
if [ -d "venv" ]; then
    source venv/bin/activate
    # Asegurar que usamos el python del venv
    if [ -f "venv/bin/python" ]; then
        PYTHON_CMD="venv/bin/python"
    fi
elif command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
fi

echo "🚀 Iniciando Bots Neuronales..."
echo "   🐍 Usando Python: $PYTHON_CMD"

# 1. Neural Bot MULTI (Todos los pares)
echo "   - Iniciando Neural Bot MULTI..."
# Lista de símbolos soportados
SYMBOLS="ETH/USDT,SOL/USDT,DOGE/USDT,ADA/USDT,AVAX/USDT,BNB/USDT,LINK/USDT,XRP/USDT"

nohup $PYTHON_CMD bot_neural.py --mode paper --model BTC_4h_v8 --id MULTI --symbols "$SYMBOLS" > log_neural_multi.txt 2>&1 &
echo $! > pid_neural_multi.txt

# 2. Telegram Bot (Manejador)
echo "   - Iniciando Telegram Bot..."
nohup $PYTHON_CMD telegram_bot_handler.py > log_telegram.txt 2>&1 &
echo $! > pid_telegram.txt

echo "✅ Todos los servicios iniciados en segundo plano."
echo "   Logs disponibles en: log_neural_multi.txt, log_telegram.txt"
