#!/bin/bash

# Asegurar que estamos en el directorio raíz del proyecto
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

echo "🛑 Deteniendo servicios..."

# Función para matar proceso por archivo PID
kill_process() {
    if [ -f "$1" ]; then
        pid=$(cat "$1")
        if ps -p $pid > /dev/null; then
            kill $pid
            echo "   - Proceso $pid detenido ($1)"
        else
            echo "   - Proceso $pid no encontrado ($1)"
        fi
        rm "$1"
    else
        echo "   ℹ️ No se encontró archivo PID: $1"
    fi
}

kill_process "pid_neural_multi.txt"
kill_process "pid_telegram.txt"

# Limpieza adicional por si acaso (opcional, cuidado si hay otros python corriendo)
# pkill -f "bot_neural.py"
# pkill -f "telegram_bot_handler.py"

echo "✅ Servicios detenidos."
