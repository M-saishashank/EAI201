import numpy as np
import tensorflow as tf

true_slope = 8.0
true_intercept = 12.0

x_vals = np.linspace(0, 15, 200)
noise = np.random.normal(loc=0.0, scale=3.0, size=x_vals.shape)
y_vals = true_slope * x_vals + true_intercept + noise

regressor = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=(1,))
])

regressor.compile(optimizer='adam', loss='mean_squared_error')

training_log = regressor.fit(x_vals, y_vals, epochs=100, verbose=0)

weights, bias = regressor.layers[0].get_weights()

print("----- Comparison of Parameters -----")
print(f"Original slope: {true_slope:.2f}")
print(f"Original intercept: {true_intercept:.2f}")
print(f"Model estimated slope: {weights[0][0]:.2f}")
print(f"Model estimated intercept: {bias[0]:.2f}")

new_input = np.array([[20.0]])
predicted_output = regressor.predict(new_input)

print(f"\nPrediction for input x = {new_input[0][0]} → Predicted y = {predicted_output[0][0]:.2f}")
