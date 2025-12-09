"""
Configuración del Sistema Neural de Trading

Define todos los parámetros del modelo, entrenamiento y aprendizaje continuo.
Configuración modular y bien documentada para fácil ajuste de hiperparámetros.
"""

from pathlib import Path


class NeuralConfig:
    """Configuración centralizada de la estrategia neuronal"""
    
    # ================== ARQUITECTURA DEL MODELO ==================
    
    # Ventana de lookback (cuántas velas históricas usar para predecir)
    LOOKBACK_WINDOW = 60  # 60 velas para contexto temporal
    LABEL_LOOKAHEAD = 6   # Velas a futuro para etiquetado
    
    # Estrategia de etiquetado
    USE_FIXED_THRESHOLDS = True   # True = umbrales fijos, False = percentiles dinámicos
    LABEL_BUY_THRESHOLD = 0.01    # +1.0% = BUY (umbral fijo)
    LABEL_SELL_THRESHOLD = -0.01  # -1.0% = SELL (umbral fijo)
    
    # Umbrales dinámicos basados en ATR
    USE_DYNAMIC_ATR_THRESHOLDS = True
    ATR_MULTIPLIER_BUY = 0.5
    ATR_MULTIPLIER_SELL = 0.5
    ATR_PERIOD = 14
    
    # Modo de clasificación
    USE_BINARY_CLASSIFICATION = False  # TERNARIO: SELL/HOLD/BUY
    
    # ================== MODELO AMPLIADO ==================
    
    # CNN: Detecta patrones locales en precios
    CNN_FILTERS = [128, 256, 512]   # AMPLIADO: Más capacidad
    CNN_KERNEL_SIZE = 3
    
    # LSTM: Captura dependencias temporales
    LSTM_UNITS = 256          # AMPLIADO: Más memoria temporal
    LSTM_DROPOUT = 0.5        # AUMENTADO: Más regularización
    
    # Attention Layer
    USE_ATTENTION = True
    ATTENTION_UNITS = 128    # AMPLIADO
    
    # Capas densas finales
    DENSE_UNITS = [512, 256, 128]  # AMPLIADO: 3 capas
    DENSE_DROPOUT = 0.6       # AUMENTADO: Más regularización
    
    # L2 Regularization
    USE_L2_REGULARIZATION = True
    L2_LAMBDA = 0.0005
    
    # Salida: 3 clases (SELL, HOLD, BUY)
    NUM_CLASSES = 3
    
    # ================== FEATURES ==================
    
    TECHNICAL_INDICATORS = {
        'ema_fast': 12,
        'ema_slow': 26,
        'ema_trend': 200,
        'rsi': 14,
        'atr': 14,
        'adx': 14,
        'macd_fast': 12,
        'macd_slow': 26,
        'macd_signal': 9,
        'bb_period': 20,
        'bb_std': 2,
        'stoch_k': 14,
        'stoch_d': 3,
        'cci': 20,
    }
    
    PRICE_FEATURES = [
        'returns', 'log_returns', 'volatility',
        'hl_ratio', 'oc_ratio', 'volume_change',
    ]
    
    VOLUME_FEATURES = ['vwap', 'obv', 'volume_ratio']
    
    CROSS_FEATURES = [
        'ema_cross', 'price_to_ema_fast', 'price_to_ema_slow',
    ]
    
    MARKET_REGIME_FEATURES = [
        'trend_direction', 'volatility_regime', 'trend_strength',
    ]
    
    # ================== ENTRENAMIENTO ==================
    
    INITIAL_EPOCHS = 100
    BATCH_SIZE = 64
    LEARNING_RATE = 0.0003
    
    USE_LR_SCHEDULE = True
    LR_PATIENCE = 5
    LR_FACTOR = 0.5
    LR_MIN = 0.00001
    
    INCREMENTAL_EPOCHS = 15
    VALIDATION_SPLIT = 0.3
    EARLY_STOPPING_PATIENCE = 15
    RETRAIN_INTERVAL_HOURS = 24
    
    MIN_PERFORMANCE_THRESHOLD = 0.52
    MIN_SHARPE_RATIO = 0.5
    MAX_DRAWDOWN_THRESHOLD = 0.20
    MIN_TRADES_FOR_EVALUATION = 10
    
    # ================== GESTIÓN DE MODELOS ==================
    
    MODELS_DIR = 'models'
    CHECKPOINTS_DIR = 'models/checkpoints'
    LOGS_DIR = 'models/logs'
    
    MODEL_NAME_FORMAT = 'neural_model_v{version}.keras'
    CONFIG_NAME_FORMAT = 'scaler_v{version}.pkl'
    METRICS_NAME_FORMAT = 'metrics_v{version}.json'
    MODELS_INDEX_FILE = 'models/models_index.json'
    MAX_VERSIONS_TO_KEEP = 5
    
    # ================== SEÑALES DE TRADING ==================
    
    MIN_CONFIDENCE_BUY = 0.55    # Umbral mínimo de confianza para BUY
    MIN_CONFIDENCE_SELL = 0.55   # Umbral mínimo de confianza para SELL
    
    # ================== GESTIÓN DE RIESGO ==================
    
    STOP_LOSS_PCT = -0.04         # Stop Loss: -4%
    TAKE_PROFIT_PCT = 0.08        # Take Profit: +8% (2x Stop Loss = R:R 1:2)
    TRAILING_STOP_PCT = 0.03      # Trailing Stop: -3% desde máximo
    TRAILING_ACTIVATION_PCT = 0.01 # Activar trailing cuando ganancias > 1%
    
    # ================== BACKTESTING ==================
    
    USE_COMPOUNDING = True        # Reinvertir ganancias (True) o tamaño fijo (False)
    INITIAL_CAPITAL = 50.0        # Capital inicial por símbolo
    MAX_POSITION_SIZE = 10000.0   # Límite máximo de posición para evitar crecimiento irreal
    
    CLASS_LABELS = {
        0: 'NO_BUY',
        1: 'BUY'
    } if USE_BINARY_CLASSIFICATION else {
        0: 'SELL',
        1: 'HOLD',
        2: 'BUY'
    }
    
    USE_AUTO_CLASS_WEIGHTS = False
    
    CLASS_WEIGHTS = {
        0: 0.1,
        1: 5,
    } if USE_BINARY_CLASSIFICATION else {
        0: 0.5,   # SELL
        1: 0.3,   # HOLD
        2: 5.0,   # BUY - Alto para forzar aprendizaje
    }
    
    # ================== DATA ==================
    
    FILTER_LATERAL_MARKETS = False
    MIN_ADX_FOR_TRAINING = 25
    LATERAL_DATA_RATIO = 0.6
    MIN_TRAIN_SAMPLES = 1000
    
    DEFAULT_SYMBOLS = ['ETH/USDT', 'BTC/USDT', 'SOL/USDT', 'XRP/USDT', 'ADA/USDT', 'DOGE/USDT', 'LINK/USDT', 'BNB/USDT']
    DEFAULT_TIMEFRAME = '4h'
    
    # ================== OPTIMIZACIÓN ==================
    
    OPTIMIZER = 'adam'
    LOSS_FUNCTION = 'sparse_categorical_crossentropy'
    
    USE_FOCAL_LOSS = True        # ACTIVADO
    FOCAL_LOSS_GAMMA = 2.0
    FOCAL_LOSS_ALPHA = 0.5
    
    METRICS = ['accuracy']
    
    # ================== DEBUG ==================
    
    VERBOSE = 1
    RANDOM_SEED = 42
    
    # ================== MÉTODOS HELPER ==================
    
    @classmethod
    def ensure_directories(cls):
        Path(cls.MODELS_DIR).mkdir(parents=True, exist_ok=True)
        Path(cls.CHECKPOINTS_DIR).mkdir(parents=True, exist_ok=True)
        Path(cls.LOGS_DIR).mkdir(parents=True, exist_ok=True)
    
    @classmethod
    def get_model_path(cls, name):
        return Path(cls.MODELS_DIR) / name
    
    @classmethod
    def validate_config(cls):
        issues = []
        if cls.LOOKBACK_WINDOW < 10:
            issues.append("LOOKBACK_WINDOW muy pequeño (< 10)")
        if cls.VALIDATION_SPLIT < 0 or cls.VALIDATION_SPLIT >= 1:
            issues.append("VALIDATION_SPLIT debe estar entre 0 y 1")
        if cls.MIN_CONFIDENCE_BUY < 0 or cls.MIN_CONFIDENCE_BUY > 1:
            issues.append("MIN_CONFIDENCE_BUY debe estar entre 0 y 1")
        return issues


# Instancia global de configuración
config = NeuralConfig()
