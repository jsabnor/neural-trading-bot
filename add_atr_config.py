# Add dynamic ATR threshold configuration

with open('neural_bot/config.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the section after LABEL_SELL_THRESHOLD
marker = "    LABEL_SELL_THRESHOLD = -0.005  # -2.0% = SELL (umbral fijo)\n    # Nota: Entre -2% y +2% = HOLD"

new_config = """    LABEL_SELL_THRESHOLD = -0.005  # -2.0% = SELL (umbral fijo)
    # Nota: Entre -2% y +2% = HOLD
    
    # NUEVO: Umbrales dinámicos basados en ATR (MEJORA #2)
    USE_DYNAMIC_ATR_THRESHOLDS = False  # True = usar ATR, False = usar umbrales fijos
    ATR_MULTIPLIER_BUY = 1.5   # Multiplicador de ATR para umbral BUY
    ATR_MULTIPLIER_SELL = 1.5  # Multiplicador de ATR para umbral SELL
    ATR_PERIOD = 14            # Período para calcular ATR"""

content = content.replace(marker, new_config)

with open('neural_bot/config.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Dynamic ATR threshold config added")
