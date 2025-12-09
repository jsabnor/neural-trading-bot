# Add L2 regularization support to model

import re

with open('neural_bot/strategy.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add import for regularizers at the top
if 'from keras import regularizers' not in content:
    # Find the keras imports section
    import_section = content.find('from keras import')
    if import_section != -1:
        # Add after existing keras imports
        content = content.replace(
            'from keras import layers, models, callbacks',
            'from keras import layers, models, callbacks, regularizers'
        )

# Add L2 regularization to Dense layers
# Find the Dense layers section in build_model
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

content = content.replace(old_dense, new_dense)

with open('neural_bot/strategy.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ L2 regularization added to model")
