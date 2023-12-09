# B. Aim: Adaptive resonance theory.
import numpy as np
class ART1:
    def __init__(self, num_input, vigilance_parameter):
        self.num_input = num_input
        self.vigilance_parameter = vigilance_parameter
        self.weights = np.random.rand(num_input)
        self.reset()

    def reset(self):
        self.activation = 0
        self.category = -1

    def normalize(self, input_pattern):
        return input_pattern / input_pattern.sum()

    def match(self, input_pattern):
        return np.dot(self.weights, input_pattern)

    def train(self, input_pattern):
        normalized_pattern = self.normalize(input_pattern)
        self.activation = self.match(normalized_pattern)
        if self.activation >= self.vigilance_parameter:
            self.category = np.argmax(normalized_pattern)
        else:
            self.category = -1


# Example usage
if __name__ == "__main__":
    num_input = 4
    vigilance_parameter = 0.5
    art_network = ART1(num_input, vigilance_parameter)
  
    # Define training patterns and categories
    training_patterns = np.array([[0.1, 0.4, 0.2, 0.3],
                                  [0.6, 0.3, 0.4, 0.1],
                                  [0.2, 0.2, 0.3, 0.3]])
  
    for i, pattern in enumerate(training_patterns):
        art_network.train(pattern)
        print(f"Pattern {i + 1}: Category {art_network.category}")
        art_network.reset()

    # Test a new pattern for recognition
    test_pattern = np.array([0.5, 0.2, 0.3, 0.1])
    art_network.train(test_pattern)
    if art_network.category != -1:
        print(f"Test pattern belongs to Category {art_network.category}")
    else:
        print("Test pattern does not belong to any category")