# Add market regime features to extract_features method

with open('neural_bot/strategy.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the marker where we need to add the code
marker = "            if 'dist_to_trend' in df_features.columns:\n                feature_cols.append('dist_to_trend')"

new_code = """            if 'dist_to_trend' in df_features.columns:
                feature_cols.append('dist_to_trend')

        # Market regime features (NUEVO - MEJORA #1)
        if hasattr(config, 'MARKET_REGIME_FEATURES'):
            for name in config.MARKET_REGIME_FEATURES:
                if name in df_features.columns:
                    feature_cols.append(name)"""

content = content.replace(marker, new_code)

with open('neural_bot/strategy.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Market regime features integrated into extract_features")
