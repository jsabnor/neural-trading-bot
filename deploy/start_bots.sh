#!/bin/bash

# Activar entorno virtual si existe
if [ -d "venv" ]; then
    source venv/bin/activate
fi

echo "🚀 Iniciando Bots Neuronales..."

# 1. Neural Bot MULTI (Todos los pares)
echo "   - Iniciando Neural Bot MULTI..."
# Lista de símbolos soportados
SYMBOLS="ETH/USDT,SOL/USDT,DOGE/USDT,ADA/USDT,AVAX/USDT,BNB/USDT,LINK/USDT,XRP/USDT"

nohup python bot_neural.py --mode paper --model BTC_4h_v8 --id MULTI --symbols "$SYMBOLS" > log_neural_multi.txt 2>&1 &
echo $! > pid_neural_multi.txt

# 2. Telegram Bot (Manejador)
echo "   - Iniciando Telegram Bot..."
nohup python telegram_bot_handler.py > log_telegram.txt 2>&1 &
echo $! > pid_telegram.txt

echo "✅ Todos los servicios iniciados en segundo plano."
echo "   Logs disponibles en: log_neural_multi.txt, log_telegram.txt"
