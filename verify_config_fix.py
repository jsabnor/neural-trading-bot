import sys
import os

# Add project root to path
sys.path.append(os.getcwd())

try:
    from neural_bot.config import config
    print(f"✅ NeuralConfig loaded successfully.")
    print(f"MIN_TRAIN_SAMPLES = {config.MIN_TRAIN_SAMPLES}")
    
    if hasattr(config, 'MIN_TRAIN_SAMPLES'):
        print("✅ Attribute 'MIN_TRAIN_SAMPLES' exists.")
    else:
        print("❌ Attribute 'MIN_TRAIN_SAMPLES' is MISSING.")
        sys.exit(1)

except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
