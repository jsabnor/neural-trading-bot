"""
Script de Análisis de Distribución de Datos
Verifica si los movimientos +2%/-2% son predecibles y cuál es la distribución real
"""

import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from collections import Counter

def analyze_symbol(symbol_file, lookahead=6, buy_threshold=0.01, sell_threshold=-0.01):
    """Analiza un archivo de datos de símbolo"""
    
    # Cargar datos
    df = pd.read_csv(symbol_file)
    
    # Asegurar que timestamp es datetime
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Calcular retorno futuro
    df['future_return'] = df['close'].shift(-lookahead) / df['close'] - 1
    
    # Clasificar según thresholds
    labels = []
    for ret in df['future_return']:
        if pd.isna(ret):
            labels.append(1)  # HOLD
        elif ret >= buy_threshold:
            labels.append(2)  # BUY
        elif ret <= sell_threshold:
            labels.append(0)  # SELL
        else:
            labels.append(1)  # HOLD
    
    df['label'] = labels
    
    # Contar distribución
    label_counts = Counter(labels)
    total = len(labels)
    
    return {
        'file': symbol_file.name,
        'total_samples': total,
        'sell_count': label_counts[0],
        'hold_count': label_counts[1],
        'buy_count': label_counts[2],
        'sell_pct': label_counts[0] / total * 100,
        'hold_pct': label_counts[1] / total * 100,
        'buy_pct': label_counts[2] / total * 100,
        'mean_return': df['future_return'].mean() * 100,
        'std_return': df['future_return'].std() * 100,
        'max_return': df['future_return'].max() * 100,
        'min_return': df['future_return'].min() * 100,
    }

def main():
    print("=" * 80)
    print("📊 ANÁLISIS DE DISTRIBUCIÓN DE DATOS")
    print("=" * 80)
    
    # Parámetros
    lookahead = 6  # 6 velas (6 horas en 1h, 24 horas en 4h)
    buy_threshold = 0.01   # +2%
    sell_threshold = -0.01  # -2%
    
    print(f"\nParámetros:")
    print(f"  Lookahead: {lookahead} velas")
    print(f"  BUY threshold: {buy_threshold*100:+.1f}%")
    print(f"  SELL threshold: {sell_threshold*100:+.1f}%")
    
    # Buscar archivos de datos
    data_dir = Path('data')
    csv_files = list(data_dir.glob('*_4h.csv'))
    
    if not csv_files:
        print("\n❌ No se encontraron archivos de datos en 'data/'")
        return
    
    print(f"\n📁 Archivos encontrados: {len(csv_files)}")
    
    # Analizar cada archivo
    results = []
    for csv_file in csv_files:
        try:
            result = analyze_symbol(csv_file, lookahead, buy_threshold, sell_threshold)
            results.append(result)
        except Exception as e:
            print(f"  ⚠️ Error en {csv_file.name}: {e}")
    
    # Mostrar resultados
    print("\n" + "=" * 80)
    print("RESULTADOS POR SÍMBOLO")
    print("=" * 80)
    
    for r in results:
        print(f"\n📈 {r['file']}")
        print(f"  Total muestras: {r['total_samples']:,}")
        print(f"  Distribución:")
        print(f"    SELL: {r['sell_count']:6,} ({r['sell_pct']:5.1f}%)")
        print(f"    HOLD: {r['hold_count']:6,} ({r['hold_pct']:5.1f}%)")
        print(f"    BUY:  {r['buy_count']:6,} ({r['buy_pct']:5.1f}%)")
        print(f"  Estadísticas de retorno:")
        print(f"    Media: {r['mean_return']:+.3f}%")
        print(f"    Std:   {r['std_return']:.3f}%")
        print(f"    Min:   {r['min_return']:+.2f}%")
        print(f"    Max:   {r['max_return']:+.2f}%")
    
    # Resumen global
    print("\n" + "=" * 80)
    print("RESUMEN GLOBAL")
    print("=" * 80)
    
    total_samples = sum(r['total_samples'] for r in results)
    total_sell = sum(r['sell_count'] for r in results)
    total_hold = sum(r['hold_count'] for r in results)
    total_buy = sum(r['buy_count'] for r in results)
    
    print(f"\nTotal muestras: {total_samples:,}")
    print(f"\nDistribución agregada:")
    print(f"  SELL: {total_sell:7,} ({total_sell/total_samples*100:5.1f}%)")
    print(f"  HOLD: {total_hold:7,} ({total_hold/total_samples*100:5.1f}%)")
    print(f"  BUY:  {total_buy:7,} ({total_buy/total_samples*100:5.1f}%)")
    
    # Diagnóstico
    print("\n" + "=" * 80)
    print("DIAGNÓSTICO")
    print("=" * 80)
    
    hold_pct = total_hold / total_samples * 100
    buy_sell_pct = (total_buy + total_sell) / total_samples * 100
    
    print(f"\n📊 Porcentaje de HOLD: {hold_pct:.1f}%")
    print(f"📊 Porcentaje de BUY+SELL: {buy_sell_pct:.1f}%")
    
    if hold_pct > 70:
        print("\n⚠️ PROBLEMA DETECTADO:")
        print(f"  HOLD representa {hold_pct:.1f}% de los datos")
        print(f"  Esto explica por qué el modelo predice HOLD siempre")
        print(f"\n💡 SOLUCIONES:")
        print(f"  1. Reducir thresholds a +1%/-1% para más señales BUY/SELL")
        print(f"  2. Cambiar a problema binario (BUY vs NO_BUY)")
        print(f"  3. Usar regresión en lugar de clasificación")
    elif hold_pct > 50:
        print("\n⚠️ ADVERTENCIA:")
        print(f"  HOLD representa {hold_pct:.1f}% de los datos")
        print(f"  Esto puede causar sesgo hacia HOLD")
        print(f"\n💡 RECOMENDACIÓN:")
        print(f"  Usar class weights agresivos o reducir thresholds")
    else:
        print("\n✅ DISTRIBUCIÓN ACEPTABLE:")
        print(f"  Las clases están relativamente balanceadas")
        print(f"  El problema puede estar en la arquitectura del modelo")
    
    # Verificar predictibilidad
    print("\n" + "=" * 80)
    print("ANÁLISIS DE PREDICTIBILIDAD")
    print("=" * 80)
    
    avg_std = np.mean([r['std_return'] for r in results])
    avg_mean = np.mean([r['mean_return'] for r in results])
    
    print(f"\nVolatilidad promedio: {avg_std:.2f}%")
    print(f"Retorno promedio: {avg_mean:+.3f}%")
    
    signal_to_noise = abs(buy_threshold * 100) / avg_std
    print(f"\nSignal-to-Noise Ratio: {signal_to_noise:.2f}")
    
    if signal_to_noise < 0.5:
        print("  ⚠️ Muy bajo - El threshold es menor que la volatilidad")
        print("  💡 Aumentar threshold o usar ventana más larga")
    elif signal_to_noise < 1.0:
        print("  ⚠️ Bajo - Difícil de predecir con alta precisión")
        print("  💡 Considerar features adicionales o modelo más complejo")
    else:
        print("  ✅ Aceptable - El threshold es significativo vs volatilidad")

if __name__ == '__main__':
    main()
