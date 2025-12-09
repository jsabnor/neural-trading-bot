# 🚀 Neural Trading Bot - Guía de Instalación en VPS

## Requisitos del Sistema

- **OS**: Ubuntu 20.04+ o Debian 11+
- **RAM**: Mínimo 2GB (4GB recomendado)
- **CPU**: 2 cores mínimo
- **Disco**: 10GB libres
- **Python**: 3.10+

---

## 1. Preparar el Servidor

```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependencias del sistema
sudo apt install -y python3 python3-pip python3-venv git screen htop

# Verificar versión de Python
python3 --version  # Debe ser 3.10+
```

---

## 2. Clonar el Proyecto

```bash
# Crear directorio de trabajo
mkdir -p ~/bots && cd ~/bots

# Clonar repositorio (reemplaza con tu repo)
git clone https://github.com/tu-usuario/neural-trading-bot.git
cd neural-trading-bot
```

---

## 3. Configurar Entorno Virtual

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno
source venv/bin/activate

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. Configurar Variables de Entorno

```bash
# Copiar template
cp .env.example .env

# Editar configuración
nano .env
```

### Contenido del archivo `.env`:

```env
# API Keys de Binance
BINANCE_API_KEY=tu_api_key_aqui
BINANCE_API_SECRET=tu_api_secret_aqui

# Telegram
TELEGRAM_BOT_TOKEN=tu_bot_token_de_botfather
TELEGRAM_CHAT_ID=tu_chat_id
TELEGRAM_AUTHORIZED_USERS=tu_chat_id

# Modo de Trading
TRADING_MODE=paper

# Capital por par
CAPITAL_PER_PAIR=50.0

# Timeframe
TIMEFRAME=4h
```

---

## 5. Subir Modelos Entrenados

El error "Directorio del modelo no existe" ocurre porque los modelos entrenados en tu PC no están en el VPS. Debes subirlos.

Desde tu **PC LOCAL** (PowerShell o Terminal), ejecuta:

```bash
# Subir el modelo BTC_4h_v8 (reemplaza usuario@ip_vps)
scp -r models/BTC_4h_v8 usuario@ip_vps:~/bots/neural-trading-bot/models/
```

O si usas **FileZilla**:
1. Conéctate a tu VPS por SFTP.
2. Navega a `~/bots/neural-trading-bot/models/`.
3. Sube la carpeta `BTC_4h_v8` desde tu PC.

---

## 6. Verificar Instalación

```bash
# Verificar que los modelos existen
ls models/

# Probar backtest
python -m neural_bot.cli backtest --model BTC_4h_v8 --symbol ETH/USDT --start-date 2024-01-01 --end-date 2024-12-01
```

---

## 6. Ejecutar el Bot

### Opción A: Screen (recomendado para VPS)

```bash
# Crear sesión screen para el bot
screen -S neural_bot

# Activar entorno e iniciar bot
source venv/bin/activate
python bot_neural.py --mode paper --model BTC_4h_v8 --id MULTI --symbols "ETH/USDT,SOL/USDT,DOGE/USDT"

# Desconectar de screen: Ctrl+A, luego D
# Reconectar: screen -r neural_bot
```

### Bot de Telegram (otra sesión screen):

```bash
screen -S telegram_bot
source venv/bin/activate
python telegram_bot_handler.py

# Desconectar: Ctrl+A, D
```

---

## 7. Configurar Servicio (Systemd)

Para que el bot se ejecute automáticamente al reiniciar el VPS y se recupere de fallos, configuramos un servicio.

1. **Editar el archivo de servicio:**
   
   El archivo `deploy/neural-bot.service` ya tiene una plantilla. Edítalo para asegurar que el usuario y rutas sean correctos:

   ```bash
   nano deploy/neural-bot.service
   ```
   
   *Verifica que `User=j0s3m4` y las rutas `/home/j0s3m4/...` coincidan con tu usuario real.*

2. **Instalar el servicio:**

   ```bash
   # Copiar al directorio de systemd
   sudo cp deploy/neural-bot.service /etc/systemd/system/

   # Recargar daemon
   sudo systemctl daemon-reload

   # Habilitar inicio automático
   sudo systemctl enable neural-bot

   # Iniciar servicio
   sudo systemctl start neural-bot
   ```

3. **Verificar estado:**

   ```bash
   sudo systemctl status neural-bot
   ```

4. **Ver logs:**

   ```bash
   # Logs del servicio
   journalctl -u neural-bot -f

   # Logs de los bots (en la carpeta del proyecto)
   tail -f log_neural_multi.txt
   ```

---

## 8. Monitoreo

```bash
# Ver logs en tiempo real (systemd)
sudo journalctl -u neural-bot -f

# Ver logs screen
screen -r neural_bot

# Estado del sistema
htop
```

---

## 9. Cambiar a Modo Live

⚠️ **ADVERTENCIA**: Solo después de probar extensivamente en paper.

```bash
# Editar .env
nano .env
# Cambiar: TRADING_MODE=live

# O usar argumento
python bot_neural.py --mode live --model BTC_4h_v8 --id MULTI --symbols "ETH/USDT,SOL/USDT"
```

---

## 10. Actualizar el Bot

```bash
# Detener bot
sudo systemctl stop neural-bot
# o Ctrl+C en screen

# Actualizar código
git pull origin main

# Reinstalar dependencias
source venv/bin/activate
pip install -r requirements.txt

# Reiniciar
sudo systemctl start neural-bot
```

---

## Troubleshooting

### Error: "Claves API no configuradas"
- Verifica que `.env` existe y tiene `BINANCE_API_KEY` y `BINANCE_API_SECRET`

### Error: "Modelo no encontrado"
- Verifica que existe `models/BTC_4h_v8/` con los archivos del modelo

### Telegram no envía mensajes
- Verifica `TELEGRAM_BOT_TOKEN` y `TELEGRAM_CHAT_ID` en `.env`
- Asegúrate de haber iniciado conversación con el bot

### Bot se detiene
- Revisa logs: `sudo journalctl -u neural-bot -n 100`
- El servicio systemd lo reiniciará automáticamente
