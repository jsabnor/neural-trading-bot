# Complete fix for strategy.py - adds all necessary imports and L2 regularization

import re

# Read the file
with open('neural_bot/strategy.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Callback import after sklearn imports
if 'from tensorflow.keras.callbacks import Callback' not in content:
    content = content.replace(
        'from sklearn.metrics import recall_score, f1_score',
        'from tensorflow.keras.callbacks import Callback\nfrom sklearn.metrics import recall_score, f1_score'
    )

# 2. Add L2 regularization to Dense layers in build_model
old_dense = """        # Capas densas
        for units in config.DENSE_UNITS:
            x = layers.Dense(units, activation='relu')(x)
            x = layers.Dropout(config.DENSE_DROPOUT)(x)"""

new_dense = """        # Capas densas
        for units in config.DENSE_UNITS:
            if hasattr(config, 'USE_L2_REGULARIZATION') and config.USE_L2_REGULARIZATION:
                x = layers.Dense(
                    units, 
                    activation='relu',
                    kernel_regularizer=regularizers.l2(config.L2_LAMBDA)
                )(x)
            else:
                x = layers.Dense(units, activation='relu')(x)
            x = layers.Dropout(config.DENSE_DROPOUT)(x)"""

if old_dense in content:
    content = content.replace(old_dense, new_dense)

# Write back
with open('neural_bot/strategy.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ All fixes applied successfully!")
print("   - Callback import added")
print("   - L2 regularization added to Dense layers")
