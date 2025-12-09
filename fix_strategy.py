# Script para arreglar strategy.py corrupto

import re

# Leer archivo
with open('neural_bot/strategy.py', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# El problema está en extract_features - líneas 338-360
# Necesitamos reemplazar el método corrupto con la versión correcta

corrupted_section = '''    
    def extract_features(self, df, fit_scaler=False):
        """
        Extrae todas las features de un DataFrame OHLCV
        
            if name in df_features.columns:'''

fixed_section = '''    
    def extract_features(self, df, fit_scaler=False):
        """
        Extrae todas las features de un DataFrame OHLCV
        
        Args:
            df: DataFrame con columnas [timestamp, open, high, low, close, volume]
            fit_scaler: Si True, ajusta el scaler (solo para entrenamiento)
        
        Returns:
            np.array con features normalizadas, shape (n_samples, n_features)
        """
        # Calcular indicadores
        df_features = self.calculate_technical_indicators(df)
        df_features = self.calculate_price_features(df_features)
        df_features = self.calculate_market_regime(df_features)  # NUEVO: Régimen de mercado
        
        # Seleccionar columnas de features
        feature_cols = []

        # OHLCV básicos
        # feature_cols.extend(['open', 'high', 'low', 'close', 'volume']) # REMOVED: Non-stationary features
        # Solo usamos variaciones (returns, vol_change) ya incluidas en PRICE_FEATURES

        # Indicadores técnicos base
        for name in ['ema_fast', 'ema_slow', 'ema_trend', 'rsi', 'atr', 'adx']:
            if name in df_features.columns:'''

# Reemplazar
content = content.replace(corrupted_section, fixed_section)

# Guardar
with open('neural_bot/strategy.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Archivo reparado")
