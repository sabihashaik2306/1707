import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#
def sigmoid_derivative(x):
    return x * (1 - x)


X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])


y = np.array([[0],
              [1],
              [1],
              [0]])


np.random.seed(42)


input_layer_neurons = 2
hidden_layer_neurons = 2
output_neurons = 1


wh = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
bh = np.random.uniform(size=(1, hidden_layer_neurons))
wout = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))


learning_rate = 0.1
epochs = 10000


for i in range(epochs):
   
    hidden_layer_input = np.dot(X, wh) + bh
    hidden_layer_activations = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_activations, wout) + bout
    output = sigmoid(output_layer_input)

   
    error = y - output
    d_output = error * sigmoid_derivative(output)

    error_hidden_layer = d_output.dot(wout.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_activations)

   
    wout += hidden_layer_activations.T.dot(d_output) * learning_rate
    bout += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    wh += X.T.dot(d_hidden_layer) * learning_rate
    bh += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

print("Final output after training:\n", output)
