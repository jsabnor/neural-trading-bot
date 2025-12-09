# 📊 Comparativa de Backtesting (2020-2025)

## Resumen Ejecutivo

El modelo `BTC_4h_v8` ha sido probado en 8 pares principales con resultados excepcionales en términos de ROI, aunque con niveles de riesgo (Drawdown) muy variados.

### 🏆 Top 3 Rendimiento (ROI)
1.  **BNB/USDT**: +243,143% (Sharpe: 6.40)
2.  **LINK/USDT**: +123,208% (Sharpe: 5.89)
3.  **ADA/USDT**: +42,146% (Sharpe: 2.62)

### 🛡️ Top 3 Seguridad (Menor Drawdown)
1.  **ETH/USDT**: 18.55% (ROI: 418%)
2.  **XRP/USDT**: 57.45% (ROI: 19,876%)
3.  **ADA/USDT**: 61.67% (ROI: 42,146%)

---

## Tabla Comparativa Detallada

| Símbolo | ROI Total | Win Rate | Max Drawdown | Sharpe Ratio | Trades | Calidad |
|:-------:|:---------:|:--------:|:------------:|:------------:|:------:|:-------:|
| **BNB** | **243,143%** | **81.77%** | 92.20% | 6.40 | 554 | 💎💎💎 |
| **LINK**| 123,208% | 57.94% | 84.22% | 5.89 | 882 | 💎💎 |
| **ADA** | 42,146% | 53.84% | 61.67% | 2.62 | 756 | 💎💎 |
| **SOL** | 20,763% | 64.78% | **94.32%** | **9.42** | 795 | 💎 |
| **XRP** | 19,876% | 56.43% | 57.45% | 1.32 | 645 | ⭐ |
| **AVAX**| 7,171% | 52.68% | 77.46% | 1.35 | 710 | ⭐ |
| **DOGE**| 7,047% | 50.80% | 82.53% | 1.22 | 750 | ⭐ |
| **ETH** | 418% | 69.23% | **18.55%** | 1.73 | 91 | 🛡️ |

---

## Análisis por Activo

### 💎 BNB/USDT (La Joya de la Corona)
*   **Rendimiento**: Absolutamente masivo. Un Win Rate del 81% es inaudito para este timeframe.
*   **Riesgo**: Drawdown extremo del 92%. Esto significa que en algún punto (probablemente 2022), el capital casi desapareció antes de recuperarse.
*   **Veredicto**: **Imprescindible**, pero requiere estómago de acero o una gestión de posición más conservadora (menor apalancamiento/capital).

### 💎 LINK/USDT (El Caballo de Batalla)
*   **Rendimiento**: ROI de 6 cifras con el mayor número de trades (882). Es un activo muy activo y rentable para este modelo.
*   **Riesgo**: Alto (84% DD), similar a BNB.
*   **Veredicto**: Excelente para compounding agresivo debido a la alta frecuencia de trades.

### 🛡️ ETH/USDT (El Refugio Seguro)
*   **Rendimiento**: Modesto comparado con las alts (418%), pero muy sólido.
*   **Riesgo**: El único con un Drawdown "seguro" (<20%).
*   **Veredicto**: Ideal para preservar capital. Debería ser la base estable del portafolio (ej: 40-50% del capital total).

### ⚠️ SOL, DOGE, AVAX (Alta Volatilidad)
*   **SOL**: Tiene el mejor Sharpe Ratio (9.42) lo que indica una rentabilidad ajustada al riesgo teórica increíble, PERO tiene el peor Drawdown (94%). Es "todo o nada".
*   **DOGE/AVAX**: ROIs decentes (7000%) pero con métricas de riesgo/recompensa peores que ADA o LINK.

---

## Recomendación de Portafolio (Live Trading)

Dado que vamos a operar en `MULTI` mode, sugiero una asignación de capital inversamente proporcional al riesgo (Drawdown), o usar un "Risk Parity" simplificado.

### Estrategia Sugerida: "Core & Satellite"

*   **Core (Estabilidad - 40% Capital)**
    *   **ETH**: 40% (Bajo riesgo, evita quiebras)

*   **Growth (Crecimiento - 40% Capital)**
    *   **BNB**: 15% (Alto WR, alto ROI)
    *   **ADA**: 15% (Buen balance ROI/DD)
    *   **LINK**: 10% (Alta frecuencia)

*   **Speculative (Alto Riesgo - 20% Capital)**
    *   **SOL**: 10% (Potencial explosivo)
    *   **XRP**: 10% (Diversificación)

### Ajustes de Configuración Recomendados

Para los activos con Drawdown > 80% (BNB, LINK, SOL, DOGE), considera reducir el `MAX_POSITION_SIZE` o ser más estricto con el Stop Loss en producción.

*   **ETH/ADA/XRP**: Configuración estándar.
*   **BNB/SOL/LINK**: Considerar `TRAILING_STOP_PCT` más ajustado (ej: 2% en vez de 3%) para asegurar ganancias antes en caídas violentas.
