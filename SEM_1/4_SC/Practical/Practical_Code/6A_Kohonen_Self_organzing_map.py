# Practical no. 6
# A. Aim: Kohonen Self organizing map using python

from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt
# Generate sample data (you can replace this with your own dataset)
data = np.random.rand(100, 2)
# Define the SOM dimensions (grid size) and the input dimensionality
grid_size = (10, 10)
input_dim = 2
# Initialize the SOM
som = MiniSom(grid_size[0], grid_size[1], input_dim, sigma=1.0, learning_rate=0.5)
# Train the SOM with the data
som.train(data, 100) # 100 iterations, you can adjust this number
# Create a map of the winning neurons
win_map = som.win_map(data)
# Visualize the SOM
plt.figure(figsize=(10, 10))
plt.pcolor(som.distance_map().T, cmap='bone_r') # Plot the distance map
# Mark the winning neurons on the map
for position, values in win_map.items():
 x, y = position
 plt.scatter(x + 0.5, y + 0.5, s=100, color='red', edgecolor='black')
 plt.text(x + 0.5, y + 0.5, str(len(values)), fontsize=12, ha='center', va='center')
plt.title('Kohonen Self-Organizing Map')
plt.show()