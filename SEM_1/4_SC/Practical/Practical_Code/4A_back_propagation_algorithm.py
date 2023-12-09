import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Define the neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights with random values
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = 0.1

        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)

    def feedforward(self, X):
        self.hidden_layer_input = np.dot(X, self.weights_input_hidden)
        self.hidden_layer_output = sigmoid(self.hidden_layer_input)
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output)
        self.output_layer_output = sigmoid(self.output_layer_input)

    def backward(self, X, y):
        # Calculate the error
        self.error = y - self.output_layer_output

        # Calculate the delta for the output layer
        delta_output = self.error * sigmoid_derivative(self.output_layer_output)

        # Calculate the error for the hidden layer
        self.hidden_layer_error = delta_output.dot(self.weights_hidden_output.T)

        # Calculate the delta for the hidden layer
        delta_hidden = self.hidden_layer_error * sigmoid_derivative(self.hidden_layer_output)

        # Update the weights
        self.weights_hidden_output += self.hidden_layer_output.T.dot(delta_output) * self.learning_rate
        self.weights_input_hidden += X.T.dot(delta_hidden) * self.learning_rate

    def train(self, X, y, epochs):
        for _ in range(epochs):
            self.feedforward(X)
            self.backward(X, y)

    def predict(self, X):
        self.feedforward(X)
        return self.output_layer_output

if __name__ == "__main__":
    # Define the XOR function dataset
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Create and train the neural network
    neural_network = NeuralNetwork(2, 4, 1)
    neural_network.train(X, y, epochs=10000)

    # Make predictions
    predictions = neural_network.predict(X)

    print("Predictions:")
    print(predictions)

