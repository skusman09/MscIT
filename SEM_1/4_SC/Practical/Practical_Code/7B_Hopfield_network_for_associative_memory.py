# B. Aim: Write a program for Hopfield network model for associative memory
import numpy as np

class HopfieldNetwork:
   def __init__(self, num_neurons):
       self.num_neurons = num_neurons
       self.weights = np.zeros((num_neurons, num_neurons))

   def train(self, patterns):
       num_patterns = len(patterns)
       for pattern in patterns:
           pattern = np.array(pattern)
           self.weights += np.outer(pattern, pattern)
       np.fill_diagonal(self.weights, 0)
       self.weights /= num_patterns

   def energy(self, state):
       return -0.5 * np.dot(state, np.dot(self.weights, state))

   def update_rule(self, state):
       h = np.dot(self.weights, state)
       return np.where(h >= 0, 1, -1)

# Example usage for the Hopfield network
if __name__ == "__main__":
    # Define the patterns to be stored
    patterns = [[1, 1, -1, -1], [-1, -1, 1, 1]]
    # Initialize the Hopfield network 
    num_neurons = len(patterns[0])
    hopfield_net = HopfieldNetwork(num_neurons)
    # Train the Hopfield network with the patterns
    hopfield_net.train(patterns)
    # Test the associative memory by recalling the patterns
    test_patterns = [[1, 1, 1, -1], [-1, 1, 1, 1]]
    for pattern in test_patterns:
        initial_state = np.array(pattern)
        iterations = 5
        print(f"Initial state: {initial_state}")
        for i in range(iterations):
            new_state = hopfield_net.update_rule(initial_state)
            print(f"Iteration {i + 1}: {new_state}")
            if np.array_equal(new_state, initial_state):
                print("Converged to a stable state.")
                break
            initial_state = new_state