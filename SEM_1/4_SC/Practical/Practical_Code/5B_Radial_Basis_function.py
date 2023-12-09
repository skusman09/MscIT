# Practical No.5B
# B. Aim: Write a program for Radial Basis function.
# Source code:

import numpy as np
import matplotlib.pyplot as plt

# Define the Radial Basis Function (Gaussian) as an activation function
def radial_basis_function(x, c, sigma):
    return np.exp(-((x - c) ** 2) / (2 * sigma ** 2))

# Generate sample data and target function (sine function)
x = np.linspace(0, 2 * np.pi, 100)
y_target = np.sin(x)

# Choose RBF centers and spread (sigma)
num_centers = 5
centers = np.linspace(0, 2 * np.pi, num_centers)
sigma = (max(centers) - min(centers)) / (2 * num_centers)

# Compute the RBF activations for each data point
rbf_activations = np.zeros((len(x), num_centers))
for i in range(len(x)):
    for j in range(num_centers):
        rbf_activations[i, j] = radial_basis_function(x[i], centers[j], sigma)

# Learn the weights using linear regression (pseudo-inverse method)
weights = np.linalg.pinv(rbf_activations).dot(y_target)

# Calculate the RBF network's output
y_approximated = rbf_activations.dot(weights)

# Plot the results
plt.figure()
plt.plot(x, y_target, label="Target Function (sin(x)")
plt.plot(x, y_approximated, label="RBF Approximation")
plt.scatter(centers, np.sin(centers), c='red', marker='o', label="RBF Centers")
plt.legend()
plt.title("Radial Basis Function Approximation")
plt.show()