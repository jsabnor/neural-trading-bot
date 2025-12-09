# Add MARKET_REGIME_FEATURES to config.py

with open('neural_bot/config.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line with "# ================== ENTRENAMIENTO ==================" 
insert_index = None
for i, line in enumerate(lines):
    if '# ================== ENTRENAMIENTO ==================' in line:
        insert_index = i
        break

if insert_index is not None:
    # Insert MARKET_REGIME_FEATURES before ENTRENAMIENTO section
    new_lines = [
        "    # NUEVO: Features de régimen de mercado (MEJORA #1)\n",
        "    MARKET_REGIME_FEATURES = [\n",
        "        'trend_direction',    # Bull (1) vs Bear (0) market\n",
        "        'volatility_regime',  # Normalized volatility (0-1)\n",
        "        'trend_strength',     # Trending (1) vs Lateral (0)\n",
        "    ]\n",
        "    \n",
    ]
    
    lines = lines[:insert_index] + new_lines + lines[insert_index:]
    
    with open('neural_bot/config.py', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print("✅ MARKET_REGIME_FEATURES added to config.py")
else:
    print("❌ Could not find insertion point")
