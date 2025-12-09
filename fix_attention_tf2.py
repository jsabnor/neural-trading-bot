# Fix AttentionLayer serialization for TensorFlow 2.x compatibility

with open('neural_bot/strategy.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the problematic decorator with TensorFlow 2.x compatible version
old_attention = """@keras.saving.register_keras_serializable()
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

new_attention = """class AttentionLayer(layers.Layer):
    \"\"\"
    Attention mechanism para enfocar en partes importantes de la secuencia temporal
    Compatible con TensorFlow 2.x save/load
    \"\"\"
    def __init__(self, units=64, **kwargs):
        super().__init__(**kwargs)
        self.units = units
    
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
        return config
    
    @classmethod
    def from_config(cls, config):
        return cls(**config)"""

content = content.replace(old_attention, new_attention)

with open('neural_bot/strategy.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ AttentionLayer fixed for TensorFlow 2.x compatibility")
