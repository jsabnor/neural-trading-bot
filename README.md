# Neural Trading Bot

Bot de trading automático usando redes neuronales (CNN-LSTM) para predecir movimientos de criptomonedas.

## 🎯 Modelos Optimizados (2020-2025)

Resultados del backtest con el modelo `BTC_4h_v8`:

| Activo | ROI Total | Win Rate | Drawdown | Sharpe |
|--------|-----------|----------|----------|--------|
| **BNB** | +243,143% | 81.77% | 92.20% | 6.40 |
| **LINK**| +123,208% | 57.94% | 84.22% | 5.89 |
| **ADA** | +42,146% | 53.84% | 61.67% | 2.62 |
| **SOL** | +20,763% | 64.78% | 94.32% | 9.42 |
| **XRP** | +19,876% | 56.43% | 57.45% | 1.32 |
| **ETH** | +418% | 69.23% | 18.55% | 1.73 |

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
python -m neural_bot.cli train --name BTC_4h_v8 --symbols BTC/USDT --timeframe 4h
```

### Backtest
```bash
# Backtest de un modelo en un símbolo específico
python -m neural_bot.cli backtest --model BTC_4h_v8 --symbol ETH/USDT --start-date 2020-01-01 --end-date 2025-12-04
```

### Ejecutar Bot (Paper/Live)
```bash
# Modo Paper (Simulación)
python bot_neural.py --mode paper --model BTC_4h_v8 --id MULTI --symbols "ETH/USDT,SOL/USDT,DOGE/USDT,ADA/USDT,AVAX/USDT,BNB/USDT,LINK/USDT,XRP/USDT"

# Modo Live (Dinero Real)
python bot_neural.py --mode live --model BTC_4h_v8 --id MULTI --symbols "ETH/USDT,SOL/USDT,..."
```

### Bot de Telegram
```bash
python telegram_bot_handler.py
```

## 📖 Documentación

- [Guía de Instalación en VPS](docs/INSTALLATION_VPS.md)
- [Guía de Comandos](docs/COMMANDS.md)
- [Comparativa de Backtest](docs/BACKTEST_COMPARISON_2020-2025.md)

## 📊 Estructura

```
neural-trading-bot/
├── bot_neural.py              # Bot principal
├── telegram_bot_handler.py    # Handler de Telegram
├── neural_bot/                # Paquete de estrategia
├── models/                    # Modelos entrenados
├── docs/                      # Documentación
└── deploy/                    # Scripts de despliegue
```

## ⚠️ Disclaimer

Este bot es para fines educativos. Operar en mercados financieros conlleva riesgo de pérdida de capital.
