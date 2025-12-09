# Fix all imports in strategy.py

with open('neural_bot/strategy.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find where to insert TensorFlow imports (after the docstring)
insert_idx = None
for i, line in enumerate(lines):
    if '"""' in line and i > 10:  # End of docstring
        insert_idx = i + 1
        break

if insert_idx:
    # TensorFlow imports to add
    tf_imports = """
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path
import json
import joblib
import warnings
warnings.filterwarnings('ignore')

# TensorFlow/Keras
try:
    import tensorflow as tf
    from tensorflow import keras
    from keras import layers, models, callbacks, regularizers
except ImportError:
    print("⚠️ TensorFlow no está instalado. Instala con: pip install tensorflow")
    print("   Para solo CPU: pip install tensorflow-cpu")
    exit(1)

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix

"""
    
    # Remove old broken imports (lines after docstring until we find a class or proper import)
    new_lines = lines[:insert_idx]
    new_lines.append(tf_imports)
    
    # Skip lines until we find "# Local imports" or a class definition
    skip_until = insert_idx
    for i in range(insert_idx, len(lines)):
        if '# Local imports' in lines[i] or 'class ' in lines[i]:
            skip_until = i
            break
    
    new_lines.extend(lines[skip_until:])
    
    with open('neural_bot/strategy.py', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("✅ All imports fixed!")
else:
    print("❌ Could not find insertion point")
