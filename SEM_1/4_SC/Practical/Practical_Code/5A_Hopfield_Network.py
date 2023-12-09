# Practical No.5A
# Aim: Write a program for Hopfield Network.
# Source code:

import numpy as np

class HopfieldNetwork:
    def __init__(self, pattern_size):
        self.pattern_size = pattern_size
        self.weights = np.zeros((pattern_size, pattern_size))

    def train(self, patterns):
        for i in range(self.pattern_size):
            for j in range(i, self.pattern_size):
                if i != j:
                    weight = 0
                    for pattern in patterns:
                        weight += pattern[i] * pattern[j]
                    self.weights[i][j] = weight
                    self.weights[j][i] = weight

    def recall(self, pattern):
        for _ in range(10):  # Repeat the process several times for convergence
            for i in range(self.pattern_size):
                activation = 0
                for j in range(self.pattern_size):
                    activation += self.weights[i][j] * pattern[j]
                pattern[i] = 1 if activation > 0 else -1
        return pattern

if __name__ == "__main__":
    pattern_size = 9
    patterns = [
        np.array([-1, 1, 1, -1, 1, -1, -1, 1, -1]),
        np.array([1, 1, 1, -1, -1, -1, 1, 1, 1]),
        np.array([1, -1, 1, 1, -1, 1, 1, -1, 1])
    ]

    hopfield_net = HopfieldNetwork(pattern_size)
    hopfield_net.train(patterns)

    # Test the network by recalling patterns
    for pattern in patterns:
        recalled_pattern = hopfield_net.recall(pattern.copy())
        print("Original Pattern:")
        print(pattern.reshape(3, 3))
        print("Recalled Pattern:")
        print(recalled_pattern.reshape(3, 3),"\n")