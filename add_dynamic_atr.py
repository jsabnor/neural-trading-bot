# Add dynamic ATR threshold logic to DataLabeler.label_data()

with open('neural_bot/strategy.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the section where we set thresholds
old_code = """        # Usar umbrales fijos o percentiles según configuración
        if config.USE_FIXED_THRESHOLDS:
            # ESTRATEGIA NUEVA: Umbrales fijos
            buy_threshold = config.LABEL_BUY_THRESHOLD    # +2.0%
            sell_threshold = config.LABEL_SELL_THRESHOLD  # -2.0%
            
            if binary_mode:
                print(f"📊 Etiquetado BINARIO con umbrales fijos:")
                print(f"   BUY:    retorno >= {buy_threshold*100:+.1f}%")
                print(f"   NO_BUY: retorno < {buy_threshold*100:+.1f}%")
            else:
                print(f"📊 Etiquetado TERNARIO con umbrales fijos:")
                print(f"   BUY:  retorno >= {buy_threshold*100:+.1f}%")
                print(f"   SELL: retorno <= {sell_threshold*100:+.1f}%")
                print(f"   HOLD: entre {sell_threshold*100:+.1f}% y {buy_threshold*100:+.1f}%")"""

new_code = """        # Usar umbrales fijos, dinámicos ATR, o percentiles según configuración
        if hasattr(config, 'USE_DYNAMIC_ATR_THRESHOLDS') and config.USE_DYNAMIC_ATR_THRESHOLDS:
            # MEJORA #2: Umbrales dinámicos basados en ATR
            print(f"📊 Etiquetado con UMBRALES DINÁMICOS ATR:")
            print(f"   ATR Multiplier BUY:  {config.ATR_MULTIPLIER_BUY}x")
            print(f"   ATR Multiplier SELL: {config.ATR_MULTIPLIER_SELL}x")
            print(f"   ATR Period: {config.ATR_PERIOD}")
            
            # Calcular ATR si no existe
            if 'atr' not in df.columns:
                period = config.ATR_PERIOD
                high_low = df['high'] - df['low']
                high_close = np.abs(df['high'] - df['close'].shift())
                low_close = np.abs(df['low'] - df['close'].shift())
                ranges = pd.concat([high_low, high_close, low_close], axis=1)
                true_range = ranges.max(axis=1)
                df['atr'] = true_range.rolling(window=period).mean()
            
            # Los umbrales serán calculados por vela (dinámicos)
            buy_threshold = None  # Se calcula en el loop
            sell_threshold = None  # Se calcula en el loop
            use_dynamic_atr = True
            
        elif config.USE_FIXED_THRESHOLDS:
            # ESTRATEGIA NUEVA: Umbrales fijos
            buy_threshold = config.LABEL_BUY_THRESHOLD    # +2.0%
            sell_threshold = config.LABEL_SELL_THRESHOLD  # -2.0%
            use_dynamic_atr = False
            
            if binary_mode:
                print(f"📊 Etiquetado BINARIO con umbrales fijos:")
                print(f"   BUY:    retorno >= {buy_threshold*100:+.1f}%")
                print(f"   NO_BUY: retorno < {buy_threshold*100:+.1f}%")
            else:
                print(f"📊 Etiquetado TERNARIO con umbrales fijos:")
                print(f"   BUY:  retorno >= {buy_threshold*100:+.1f}%")
                print(f"   SELL: retorno <= {sell_threshold*100:+.1f}%")
                print(f"   HOLD: entre {sell_threshold*100:+.1f}% y {buy_threshold*100:+.1f}%")"""

content = content.replace(old_code, new_code)

# Now update the loop to use dynamic thresholds
old_loop = """            if config.USE_FIXED_THRESHOLDS:
                # NUEVA ESTRATEGIA: Comparar precio futuro directo
                future_price = df.iloc[i + lookahead]['close']
                return_pct = (future_price - current_price) / current_price"""

new_loop = """            if hasattr(config, 'USE_DYNAMIC_ATR_THRESHOLDS') and config.USE_DYNAMIC_ATR_THRESHOLDS:
                # MEJORA #2: Umbrales dinámicos basados en ATR
                future_price = df.iloc[i + lookahead]['close']
                return_pct = (future_price - current_price) / current_price
                
                # Calcular umbrales dinámicos para esta vela
                atr_value = df.iloc[i]['atr']
                if pd.isna(atr_value) or atr_value == 0:
                    # Si no hay ATR, usar umbrales fijos como fallback
                    buy_threshold = config.LABEL_BUY_THRESHOLD
                    sell_threshold = config.LABEL_SELL_THRESHOLD
                else:
                    # Umbral dinámico: k * ATR / precio
                    buy_threshold = (config.ATR_MULTIPLIER_BUY * atr_value) / current_price
                    sell_threshold = -(config.ATR_MULTIPLIER_SELL * atr_value) / current_price
                
            elif config.USE_FIXED_THRESHOLDS:
                # NUEVA ESTRATEGIA: Comparar precio futuro directo
                future_price = df.iloc[i + lookahead]['close']
                return_pct = (future_price - current_price) / current_price"""

content = content.replace(old_loop, new_loop)

with open('neural_bot/strategy.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Dynamic ATR threshold logic added to DataLabeler")
