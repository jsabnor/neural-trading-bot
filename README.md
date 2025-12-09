# Neural Trading Bot

Bot de trading automático usando redes neuronales (CNN-LSTM) para predecir movimientos de criptomonedas.

## 🎯 Modelos Optimizados

| Activo | Modelo | ROI 2024 | Drawdown | Estrategia |
|--------|--------|----------|----------|------------|
| BTC | `BTC_4h` | +73.49% | 36.84% | Especialista BTC+ETH |
| ETH | `GENERAL_4h_v2` | +58.24% | 42.80% | Generalista 7 pares |
| SOL | `SOL_GROUP_4h` | +60.11% | 52.99% | Grupo volátil |

## 📦 Instalación

```bash
# 1. Clonar repositorio
git clone <tu-repo>
cd neural-trading-bot

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables
cp .env.example .env
nano .env  # Editar con tus claves
```

## 🚀 Uso

### Entrenar Modelo
```bash
python -m neural_bot.cli train --name MI_MODELO --symbols BTC/USDT,ETH/USDT
```

### Backtest
```bash
# Backtest de un modelo en un símbolo específico
python -m neural_bot.cli backtest --model BTC_4h --symbol BTC/USDT --start-date 2024-01-01 --end-date 2024-12-31

# Backtest en múltiples símbolos
python -m neural_bot.cli backtest --model GENERAL_4h_v2 --symbols BTC/USDT,ETH/USDT --start-date 2024-01-01 --end-date 2024-12-31
```

### Ejecutar Bot (Paper Trading)
```bash
python bot_neural.py --model BTC_4h --symbols BTC/USDT --id BTC
```

### Listar Modelos Disponibles
```bash
python -m neural_bot.cli list
```

### Despliegue VPS
Ver instrucciones en `deploy/README_VPS.md`

## 📊 Estructura

```
neural-trading-bot/
├── bot_neural.py              # Bot principal
├── telegram_bot_handler.py    # Handler de Telegram
├── neural_bot/                # Paquete de estrategia
├── models/                    # Modelos entrenados
└── deploy/                    # Scripts de despliegue
```

## 📖 Documentación

- [Guía de Despliegue VPS](deploy/README_VPS.md)
- [Backtest Results](models/metrics_v1.json)

## ⚠️ Disclaimer

Este bot es para fines educativos. Operar en mercados financieros conlleva riesgo de pérdida de capital.
