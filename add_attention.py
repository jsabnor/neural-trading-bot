# Add Attention Layer with proper serialization to strategy.py

with open('neural_bot/strategy.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where to insert the AttentionLayer class (after imports, before NeuralTradingModel)
marker = "from sklearn.metrics import recall_score, f1_score"

attention_layer_code = """from sklearn.metrics import recall_score, f1_score


# MEJORA #3: Attention Layer con serialización correcta
@keras.saving.register_keras_serializable()
class AttentionLayer(layers.Layer):
    \"\"\"
    Attention mechanism para enfocar en partes importantes de la secuencia temporal
    \"\"\"
    def __init__(self, units=64, **kwargs):
        super().__init__(**kwargs)
        self.units = units
        self.W = None
        self.b = None
    
    def build(self, input_shape):
        self.W = self.add_weight(
            shape=(input_shape[-1], self.units),
            initializer='glorot_uniform',
            trainable=True,
            name='attention_W'
        )
        self.b = self.add_weight(
            shape=(self.units,),
            initializer='zeros',
            trainable=True,
            name='attention_b'
        )
        super().build(input_shape)
    
    def call(self, inputs):
        # Attention mechanism
        score = tf.nn.tanh(tf.matmul(inputs, self.W) + self.b)
        attention_weights = tf.nn.softmax(score, axis=1)
        context_vector = tf.reduce_sum(attention_weights * inputs, axis=1)
        return context_vector
    
    def get_config(self):
        config = super().get_config()
        config.update({"units": self.units})
        return config"""

content = content.replace(marker, attention_layer_code)

with open('neural_bot/strategy.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ AttentionLayer added with proper serialization")
