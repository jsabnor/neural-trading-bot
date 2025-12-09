    @staticmethod
    def label_data(df):
        """
        Etiqueta datos usando UMBRALES FIJOS o DINÁMICOS ATR
        
        Soporta dos modos:
        - Binario: BUY vs NO_BUY (más simple, mejor para aprendizaje)
        - Ternario: SELL vs HOLD vs BUY (más complejo)
        
        Ventajas sobre percentiles:
        - Consistente entre símbolos
        - Simétrico (BUY y SELL tratados igual)
        - Fácil de entender y ajustar
        - No depende de la distribución de datos
        
        Returns:
            np.array de labels: 
            - Binario: 0=NO_BUY, 1=BUY
            - Ternario: 0=SELL, 1=HOLD, 2=BUY
        """
        lookahead = config.LABEL_LOOKAHEAD
        binary_mode = config.USE_BINARY_CLASSIFICATION
        
        # Usar umbrales fijos, dinámicos ATR, o percentiles según configuración
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
            buy_threshold = config.LABEL_BUY_THRESHOLD    # +1.0%
            sell_threshold = config.LABEL_SELL_THRESHOLD  # -1.0%
            use_dynamic_atr = False
            
            if binary_mode:
                print(f"📊 Etiquetado BINARIO con umbrales fijos:")
                print(f"   BUY:    retorno >= {buy_threshold*100:+.1f}%")
                print(f"   NO_BUY: retorno < {buy_threshold*100:+.1f}%")
            else:
                print(f"📊 Etiquetado TERNARIO con umbrales fijos:")
                print(f"   BUY:  retorno >= {buy_threshold*100:+.1f}%")
                print(f"   SELL: retorno <= {sell_threshold*100:+.1f}%")
                print(f"   HOLD: entre {sell_threshold*100:+.1f}% y {buy_threshold*100:+.1f}%")
            
        else:
            # ESTRATEGIA ANTIGUA: Percentiles dinámicos (DEPRECADA)
            print("⚠️ Usando estrategia de percentiles (DEPRECADA)")
            min_movement = 0.010
            
        labels = []
        
        # Calcular etiquetas
        for i in range(len(df)):
            # Últimas velas no tienen futuro suficiente
            if i >= len(df) - lookahead:
                labels.append(1 if binary_mode else 1)  # NO_BUY o HOLD
                continue
            
            current_price = df.iloc[i]['close']
            
            if hasattr(config, 'USE_DYNAMIC_ATR_THRESHOLDS') and config.USE_DYNAMIC_ATR_THRESHOLDS:
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
                
                # Aplicar etiquetado con umbrales (dinámicos o fijos)
                if binary_mode:
                    # MODO BINARIO: BUY vs NO_BUY
                    if return_pct >= buy_threshold:
                        labels.append(1)  # BUY
                    else:
                        labels.append(0)  # NO_BUY
                else:
                    # MODO TERNARIO: SELL/HOLD/BUY
                    if return_pct >= buy_threshold:
                        labels.append(2)  # BUY
                    elif return_pct <= sell_threshold:
                        labels.append(0)  # SELL
                    else:
                        labels.append(1)  # HOLD
                        
            elif config.USE_FIXED_THRESHOLDS:
                # NUEVA ESTRATEGIA: Comparar precio futuro directo con umbrales fijos
                future_price = df.iloc[i + lookahead]['close']
                return_pct = (future_price - current_price) / current_price
                
                if binary_mode:
                    # MODO BINARIO: BUY vs NO_BUY
                    if return_pct >= buy_threshold:
                        labels.append(1)  # BUY
                    else:
                        labels.append(0)  # NO_BUY
                else:
                    # MODO TERNARIO: SELL/HOLD/BUY
                    if return_pct >= buy_threshold:
                        labels.append(2)  # BUY
                    elif return_pct <= sell_threshold:
                        labels.append(0)  # SELL
                    else:
                        labels.append(1)  # HOLD
                    
            else:
                # ANTIGUA ESTRATEGIA: Percentiles (mantener por compatibilidad)
                future_prices = df.iloc[i+1:i+lookahead+1]['close']
                max_gain = (future_prices.max() - current_price) / current_price
                max_loss = (future_prices.min() - current_price) / current_price
                
                if abs(max_gain) > abs(max_loss):
                    future_return = max_gain
                else:
                    future_return = max_loss
                
                # Usar percentiles si hay suficientes datos
                if abs(future_return) < min_movement:
                    labels.append(0 if binary_mode else 1)  # NO_BUY o HOLD
                elif future_return >= min_movement:
                    labels.append(1 if binary_mode else 2)  # BUY
                elif future_return <= -min_movement:
                    labels.append(0)  # NO_BUY o SELL
                else:
                    labels.append(0 if binary_mode else 1)  # NO_BUY o HOLD
        
        labels_array = np.array(labels)
        
        # Mostrar estadísticas de etiquetado
        from collections import Counter
        label_counts = Counter(labels_array)
        total = len(labels_array)
        
        print(f"\n📊 Distribución de etiquetas generadas:")
        if binary_mode:
            print(f"   NO_BUY (0): {label_counts[0]:5d} ({label_counts[0]/total*100:5.1f}%)")
            print(f"   BUY    (1): {label_counts[1]:5d} ({label_counts[1]/total*100:5.1f}%)")
        else:
            print(f"   SELL (0): {label_counts[0]:5d} ({label_counts[0]/total*100:5.1f}%)")
            print(f"   HOLD (1): {label_counts[1]:5d} ({label_counts[1]/total*100:5.1f}%)")
            print(f"   BUY  (2): {label_counts[2]:5d} ({label_counts[2]/total*100:5.1f}%)")
        print(f"   Total:    {total:5d}")
        
        return labels_array
