

###################____2B____################
import numpy as np

print("****** XOR CODE *********")

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
  return x * (1 - x)

try:
  A = int(input("Enter 1st Binary Input(0,1): "))
  B = int(input("Enter 2nd Binary Input (0,1): "))

  if A in [0, 1] and B in [0, 1]:
    # Create the XOR truth table
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Initialize the network parameters
    input_size = 2
    hidden_size = 2
    output_size = 1
    hidden_weight = np.random.uniform(size=(input_size, hidden_size))
    hidden_bias = np.random.uniform(size=(1, hidden_size))
    output_weights = np.random.uniform(size=(hidden_size, output_size))
    output_bias = np.random.uniform(size=(1, output_size))

    # Forward pass
    hidden_layer_input = np.dot(x, hidden_weight) + hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, output_weights) + output_bias
    output_layer_output = sigmoid(output_layer_input)

    # Print the output
    print(f"XOR({A}, {B}) = {(output_layer_output[0][0])}")
  else:
    print("Invalid Input. Please enter 0 or 1 for binary input.")

except:
  print("Invalid input.")
