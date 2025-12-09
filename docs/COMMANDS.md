# 📚 Neural Trading Bot - Documentación de Comandos

## Índice

1. [CLI de Gestión de Modelos](#1-cli-de-gestión-de-modelos)
2. [Bot de Trading](#2-bot-de-trading)
3. [Bot de Telegram](#3-bot-de-telegram)
4. [Configuración](#4-configuración)

---

## 1. CLI de Gestión de Modelos

```bash
python -m neural_bot.cli <comando> [opciones]
```

### Comandos Disponibles

#### `list` - Listar modelos

```bash
python -m neural_bot.cli list
```

Muestra todos los modelos entrenados disponibles.

---

#### `info` - Información del modelo

```bash
python -m neural_bot.cli info --model <nombre_modelo>
```

| Opción | Descripción |
|--------|-------------|
| `--model` | Nombre del modelo (ej: BTC_4h_v8) |

---

#### `backtest` - Ejecutar backtesting

```bash
python -m neural_bot.cli backtest --model <modelo> --symbol <par> --start-date <fecha> --end-date <fecha>
```

| Opción | Descripción | Ejemplo |
|--------|-------------|---------|
| `--model` | Nombre del modelo | `BTC_4h_v8` |
| `--symbol` | Par de trading | `ETH/USDT` |
| `--start-date` | Fecha inicio | `2020-01-01` |
| `--end-date` | Fecha fin | `2025-12-01` |

**Ejemplos:**

```bash
# Backtest ETH 2020-2025
python -m neural_bot.cli backtest --model BTC_4h_v8 --symbol ETH/USDT --start-date 2020-01-01 --end-date 2025-12-04

# Backtest SOL último año
python -m neural_bot.cli backtest --model BTC_4h_v8 --symbol SOL/USDT --start-date 2024-01-01 --end-date 2025-12-04
```

---

#### `train` - Entrenar modelo

```bash
python -m neural_bot.cli train --symbol <par> --timeframe <tf> --name <nombre>
```

| Opción | Descripción | Default |
|--------|-------------|---------|
| `--symbol` | Par para entrenamiento | BTC/USDT |
| `--timeframe` | Timeframe | 4h |
| `--name` | Nombre del modelo | Auto-generado |
| `--epochs` | Épocas de entrenamiento | 100 |

---

#### `set-default` - Establecer modelo por defecto

```bash
python -m neural_bot.cli set-default --model <nombre>
```

---

#### `delete` - Eliminar modelo

```bash
python -m neural_bot.cli delete --model <nombre>
```

---

## 2. Bot de Trading

```bash
python bot_neural.py [opciones]
```

### Opciones

| Opción | Descripción | Valores | Requerido |
|--------|-------------|---------|-----------|
| `--mode` | Modo de trading | `paper`, `live` | No (usa .env) |
| `--model` | Modelo a usar | Nombre modelo | No (usa default) |
| `--id` | ID del bot | String | **Sí** |
| `--symbols` | Pares a tradear | Lista separada por comas | No |

### Ejemplos

```bash
# Paper trading con múltiples pares
python bot_neural.py --mode paper --model BTC_4h_v8 --id MULTI --symbols "ETH/USDT,SOL/USDT,DOGE/USDT"

# Paper trading solo ETH
python bot_neural.py --mode paper --model BTC_4h_v8 --id ETH --symbols ETH/USDT

# Live trading (¡CUIDADO!)
python bot_neural.py --mode live --model BTC_4h_v8 --id LIVE --symbols "ETH/USDT,BTC/USDT"
```

### Archivos Generados

| Archivo | Descripción |
|---------|-------------|
| `bot_state_neural_<ID>.json` | Estado del bot (posiciones, equity) |
| `trades_neural_<ID>.csv` | Historial de trades |

---

## 3. Bot de Telegram

### Iniciar Bot Interactivo

```bash
python telegram_bot_handler.py
```

### Comandos de Telegram

| Comando | Descripción |
|---------|-------------|
| `/start` | Menú principal con botones |
| `/status` | Estado de todos los bots |
| `/posiciones` | Posiciones abiertas con PnL |
| `/help` | Ayuda y comandos disponibles |

### Botones del Menú

- **📊 Estado** - Resumen de bots activos
- **💼 Posiciones** - Posiciones abiertas
- **📈 Reportes** - Reportes de rendimiento
  - ADX Bot
  - EMA Bot
  - Neural Bot

---

## 4. Configuración

### Archivo `.env`

```env
# === API BINANCE ===
BINANCE_API_KEY=tu_api_key
BINANCE_API_SECRET=tu_api_secret

# === TELEGRAM ===
TELEGRAM_BOT_TOKEN=token_de_botfather
TELEGRAM_CHAT_ID=tu_chat_id
TELEGRAM_AUTHORIZED_USERS=chat_id1,chat_id2

# === TRADING ===
TRADING_MODE=paper          # paper | live
CAPITAL_PER_PAIR=50.0       # Capital por par en USDT
TIMEFRAME=4h                # Timeframe del bot

# === SÍMBOLOS (opcional) ===
SYMBOLS=ETH/USDT,SOL/USDT,DOGE/USDT

# === GESTIÓN DE RIESGO (opcional) ===
STOP_LOSS_PCT=0.04          # 4%
TAKE_PROFIT_PCT=0.08        # 8%
TRAILING_STOP_PCT=0.03      # 3%
```

---

### Archivo `config.py` (raíz)

Configuración para `bot_neural.py`:

| Variable | Valor Default | Descripción |
|----------|---------------|-------------|
| `STOP_LOSS_PCT` | 0.04 | Stop Loss 4% |
| `TAKE_PROFIT_PCT` | 0.08 | Take Profit 8% |
| `TRAILING_STOP_PCT` | 0.03 | Trailing Stop 3% |
| `CAPITAL_PER_PAIR` | 50.0 | Capital USDT por par |
| `MIN_EQUITY` | 10.0 | Capital mínimo para operar |

---

### Archivo `neural_bot/config.py`

Configuración para backtesting:

| Variable | Valor Default | Descripción |
|----------|---------------|-------------|
| `MIN_CONFIDENCE_BUY` | 0.55 | Confianza mínima para BUY |
| `MIN_CONFIDENCE_SELL` | 0.55 | Confianza mínima para SELL |
| `STOP_LOSS_PCT` | -0.04 | Stop Loss -4% |
| `TAKE_PROFIT_PCT` | 0.08 | Take Profit +8% |
| `TRAILING_STOP_PCT` | 0.03 | Trailing Stop -3% |
| `USE_COMPOUNDING` | True | Reinvertir ganancias |
| `MAX_POSITION_SIZE` | 10000.0 | Cap máximo de posición |

---

## 5. Resultados del Backtest

### Métricas Reportadas

| Métrica | Descripción |
|---------|-------------|
| **Total Trades** | Número de operaciones ejecutadas |
| **Win Rate** | % de trades ganadores |
| **ROI** | Retorno sobre inversión total |
| **Final Capital** | Capital final después del período |
| **Max Drawdown** | Máxima caída desde máximo |
| **Sharpe Ratio** | Rendimiento ajustado por riesgo |

### Rendimiento por Símbolo (2020-2025)

| Símbolo | Win Rate | ROI | Max DD |
|---------|----------|-----|--------|
| ETH/USDT | 69% | +418% | 19% |
| SOL/USDT | 65% | +20,764% | 94% |
| DOGE/USDT | 51% | +7,047% | 83% |
| ADA/USDT | 48% | +15,973% | 60% |
| BTC/USDT | 69% | +14% | 8% |

---

## 6. Arquitectura del Sistema

```
neural-trading-bot/
├── bot_neural.py           # Bot principal (paper/live)
├── config.py               # Configuración bot live
├── telegram_notifier.py    # Notificaciones automáticas
├── telegram_bot_handler.py # Bot interactivo Telegram
├── data_cache.py          # Cache de datos OHLCV
├── .env                   # Variables de entorno
│
├── neural_bot/            # Módulo principal
│   ├── __init__.py
│   ├── cli.py            # Interfaz de comandos
│   ├── config.py         # Configuración backtest
│   ├── strategy.py       # Estrategia neuronal
│   ├── backtest.py       # Motor de backtesting
│   └── ...
│
├── models/               # Modelos entrenados
│   └── BTC_4h_v8/
│       ├── model.keras
│       ├── scaler.pkl
│       └── metadata.json
│
├── data/                 # Cache de datos OHLCV
│   └── *.csv
│
└── docs/                 # Documentación
    ├── INSTALLATION_VPS.md
    └── COMMANDS.md
```
