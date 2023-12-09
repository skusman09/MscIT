import numpy as np

# Define the sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Define the neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate):
        # Initialize network architecture and weights
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.learning_rate = learning_rate

        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))

    def forward(self, x):
        # Calculate hidden layer input and output
        self.hidden_input = np.dot(x, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)

        # Calculate output layer input and output
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.output = sigmoid(self.output_input)

    def backward(self, x, y):
        # Compute the loss and gradients
        loss = y - self.output
        delta_output = loss * sigmoid_derivative(self.output)
        hidden_error = delta_output.dot(self.weights_hidden_output.T)
        delta_hidden = hidden_error * sigmoid_derivative(self.hidden_output)

        # Update weights and biases
        self.weights_hidden_output += self.hidden_output.T.dot(delta_output) * self.learning_rate
        self.bias_output += np.sum(delta_output, axis=0, keepdims=True) * self.learning_rate
        self.weights_input_hidden += x.T.dot(delta_hidden) * self.learning_rate
        self.bias_hidden += np.sum(delta_hidden, axis=0, keepdims=True) * self.learning_rate

    def train(self, x, y, epochs):
        for _ in range(epochs):
            self.forward(x)
            self.backward(x, y)

    def predict(self, x):
        self.forward(x)
        return self.output

if __name__ == "__main__":
    # Define the XOR function dataset
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Create and train the neural network
    neural_network = NeuralNetwork(input_size=2, hidden_size=4, output_size=1, learning_rate=0.1)
    neural_network.train(X, y, epochs=10000)

    # Make predictions
    predictions = neural_network.predict(X)

    print("Predictions:")
    print(predictions)
