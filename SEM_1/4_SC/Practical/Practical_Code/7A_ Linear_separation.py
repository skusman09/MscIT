# Practical no 7
# A. Aim: Write a program for Linear separation in python.
import numpy as np

# Perceptron class for linear separation
class Perceptron:
    def __init__(self, num_features):
        self.weights = np.zeros(num_features)
        self.bias = 0.0

    def predict(self, inputs):
        weighted_sum = np.dot(self.weights, inputs) + self.bias
        return 1 if weighted_sum >= 0 else 0
    
    def train(self, training_data, labels, learning_rate, epochs):
        for epoch in range(epochs):
            for i in range(len(training_data)):
                inputs = training_data[i]
                label = labels[i]
                prediction = self.predict(inputs)
                if prediction != label:
                    update = (label - prediction) * learning_rate
                    self.weights += update * inputs
                    self.bias += update
    
# Example usage for linear separation
if __name__ == "__main__":
    # Define training data and labels for a simple linearly separable problem
    training_data = np.array([[1, 2], [2, 3], [3, 1], [4, 4], [5, 5], [6, 4]])
    labels = np.array([0, 0, 0, 1, 1, 1])
    
    # Create a Perceptron instance
    num_features = training_data.shape[1]
    perceptron = Perceptron(num_features)
    
    # Train the Perceptron with the training data
    learning_rate = 0.1
    epochs = 100
    perceptron.train(training_data, labels, learning_rate, epochs)
    
    # Test the trained Perceptron with new data points
    test_data = np.array([[2, 2], [4, 3], [5, 6]])
    for data_point in test_data:
        prediction = perceptron.predict(data_point)
        print(f"Prediction for {data_point}: Class {prediction}")