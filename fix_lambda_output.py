# Fix Lambda layer in Attention mechanism

with open('neural_bot/strategy.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the Lambda layer without output_shape
old_lambda = "x = layers.Lambda(lambda xin: tf.reduce_sum(xin, axis=1))(x)"
new_lambda = "x = layers.Lambda(lambda xin: tf.reduce_sum(xin, axis=1), output_shape=(config.LSTM_UNITS,))(x)"

content = content.replace(old_lambda, new_lambda)

with open('neural_bot/strategy.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Lambda layer fixed with output_shape")
