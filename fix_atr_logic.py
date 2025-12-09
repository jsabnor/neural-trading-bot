# Fix the corrupted ATR logic in strategy.py

with open('neural_bot/strategy.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the problematic section (around line 620)
# We need to find where the ATR calculation is and fix the missing else clause

fixed_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # Check if we're at the problematic section
    if 'atr_value = df.iloc[i][\'atr\']' in line:
        # Add the current line
        fixed_lines.append(line)
        i += 1
        
        # Add the if statement
        fixed_lines.append(lines[i])  # if pd.isna...
        i += 1
        
        # Add the comment and threshold assignments
        while i < len(lines) and 'sell_threshold = config.LABEL_SELL_THRESHOLD' not in lines[i]:
            fixed_lines.append(lines[i])
            i += 1
        
        if i < len(lines):
            fixed_lines.append(lines[i])  # sell_threshold line
            i += 1
        
        # Add the ELSE clause that was missing
        fixed_lines.append('                else:\n')
        fixed_lines.append('                    # Umbral dinámico: k * ATR / precio\n')
        fixed_lines.append('                    buy_threshold = (config.ATR_MULTIPLIER_BUY * atr_value) / current_price\n')
        fixed_lines.append('                    sell_threshold = -(config.ATR_MULTIPLIER_SELL * atr_value) / current_price\n')
        fixed_lines.append('                \n')
        
        # Skip any malformed lines until we find the labeling logic
        while i < len(lines) and 'if binary_mode:' not in lines[i]:
            i += 1
        
        # Now add the rest normally
        continue
    
    fixed_lines.append(line)
    i += 1

with open('neural_bot/strategy.py', 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

print("✅ Fixed ATR logic in strategy.py")
