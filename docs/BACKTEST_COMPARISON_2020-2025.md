# 📊 Comparativa de Backtesting (2020-2025)

## Resumen Ejecutivo

El modelo `BTC_4h_v8` ha sido probado en 9 pares principales con resultados muy dispares: algunos activos muestran un ROI absolutamente explosivo, mientras que otros destacan por su seguridad y bajo drawdown. La combinación de ambos perfiles es clave para construir un portafolio equilibrado.

### 🏆 Top 3 Rendimiento (ROI)
1. **SOL/USDT**: +294,778% (Sharpe: 9.31)
2. **LINK/USDT**: +86,350% (Sharpe: 5.05)
3. **BNB/USDT**: +19,850% (Sharpe: 6.25)

### 🛡️ Top 3 Seguridad (Menor Drawdown)
1. **BTC/USDT**: 8.65% (ROI: 11.37%)
2. **ETH/USDT**: 19.05% (ROI: 332%)
3. **XRP/USDT**: 60.36% (ROI: 7,469%)

---

## Tabla Comparativa Detallada

| Símbolo | ROI Total | Win Rate | Max Drawdown | Sharpe Ratio | Trades | Calidad |
|:-------:|:---------:|:--------:|:------------:|:------------:|:------:|:-------:|
| **SOL** | **294,778%** | 63.86% | **93.83%** | **9.31** | 797 | 💎 |
| **LINK**| 86,350% | 57.64% | 77.61% | 5.05 | 883 | 💎💎 |
| **BNB** | 19,850% | **79.42%** | 91.47% | 6.25 | 554 | 💎💎 |
| **XRP** | 7,469% | 55.49% | 60.36% | 1.39 | 647 | ⭐ |
| **ADA** | 7,844% | 53.37% | 68.79% | 1.34 | 757 | ⭐ |
| **DOGE**| 1,500% | 50.66% | 88.01% | 0.95 | 752 | ⭐ |
| **AVAX**| 1,390% | 52.39% | 86.53% | 1.06 | 712 | ⭐ |
| **ETH** | 332% | 64.84% | **19.05%** | 1.54 | 91 | 🛡️ |
| **BTC** | 11% | **69.23%** | **8.65%** | 0.37 | 13 | 🛡️ |

---

## Análisis por Activo

### 💎 SOL/USDT (Explosivo pero extremo)
- **Rendimiento**: ROI descomunal, el mayor de todos los activos.
- **Riesgo**: Drawdown cercano al 94%, lo que implica riesgo de casi desaparición del capital en fases adversas.
- **Veredicto**: Activo especulativo puro, ideal para una pequeña fracción del portafolio.

### 💎 LINK/USDT (Caballo de batalla)
- **Rendimiento**: ROI altísimo con gran número de trades (883).
- **Riesgo**: Drawdown elevado (77%), pero compensado por Sharpe sólido.
- **Veredicto**: Excelente para compounding agresivo, aunque requiere gestión estricta de riesgo.

### 💎 BNB/USDT (Alta eficiencia)
- **Rendimiento**: ROI muy alto y Win Rate excepcional (79%).
- **Riesgo**: Drawdown superior al 90%, lo que exige stops ajustados.
- **Veredicto**: Gran candidato para crecimiento, pero con control de exposición.

### 🛡️ ETH/USDT (Refugio seguro)
- **Rendimiento**: ROI moderado (332%), pero consistente.
- **Riesgo**: Drawdown bajo (19%), lo que lo convierte en uno de los más estables.
- **Veredicto**: Base sólida del portafolio, ideal para preservar capital.

### 🛡️ BTC/USDT (Máxima estabilidad)
- **Rendimiento**: ROI muy bajo (11%), pero con el menor drawdown (8.6%).
- **Riesgo**: Prácticamente nulo comparado con las alts.
- **Veredicto**: Activo defensivo, útil como ancla de seguridad.

### ⭐ XRP/USDT
- **Rendimiento**: ROI notable (7,469%).
- **Riesgo**: Drawdown medio-alto (60%).
- **Veredicto**: Buen balance riesgo/beneficio, puede diversificar la parte especulativa.

### ⭐ ADA/USDT
- **Rendimiento**: ROI similar a XRP (7,844%).
- **Riesgo**: Drawdown algo más alto (68%).
- **Veredicto**: Complemento de crecimiento, aunque menos eficiente que LINK o BNB.

### ⭐ DOGE/USDT y AVAX/USDT
- **Rendimiento**: ROI decente (1,500% y 1,390%).
- **Riesgo**: Drawdowns muy altos (>85%).
- **Veredicto**: Activos secundarios, solo para diversificación mínima.

---

## Recomendación de Portafolio (Live Trading)

### Estrategia Sugerida: "Core & Satellite"

- **Core (Estabilidad - 40% Capital)**
  - **ETH**: 25% (bajo riesgo, ROI consistente).
  - **BTC**: 15% (máxima seguridad).

- **Growth (Crecimiento - 40% Capital)**
  - **LINK**: 15% (alta frecuencia y ROI).
  - **BNB**: 15% (alto Win Rate).
  - **ADA/XRP**: 10% (balance riesgo/beneficio).

- **Speculative (Alto Riesgo - 20% Capital)**
  - **SOL**: 15% (potencial explosivo).
  - **DOGE/AVAX**: 5% (diversificación especulativa).

---

## Ajustes de Configuración Recomendados

- **Activos con Drawdown >80% (SOL, BNB, DOGE, AVAX)**  
  Reducir `MAX_POSITION_SIZE` y aplicar `TRAILING_STOP_PCT` más ajustado (ej. 2%).
  
- **Activos estables (ETH, BTC)**  
  Configuración estándar, sin necesidad de stops agresivos.

- **Activos intermedios (LINK, ADA, XRP)**  
  Stops moderados (2.5–3%) para balancear riesgo y capturar beneficios.

---
