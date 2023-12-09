# HISTOGRAM USING MATPLOTLIB
# importing matplotlib module
from matplotlib import pyplot as plt
# Y-axis values
y = [10, 5, 8, 4, 2]
# Function to plot histogram
plt.hist(y)
# Function to show the plot
plt.show()


##############PIE CHARTS###################
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()


###########PIE CHART WITH LABEL############
import matplotlib.pyplot as plt
labels = 'apple', 'banana', 'cherry', 'durian', 'elderberries', 'figs', 'grapes'
sizes= [32, 20, 15, 10, 10, 8, 5]
p = plt.pie (sizes, labels=labels, explode=(0.07, 0, 0, 0, 0, 0, 0),
             autopct='%1.1fXX', startangle=130, shadow=True)
plt.axis('equal')
for i, (apple, banana, cherry, durian, elderberries, figs, grapes) in enumerate(p):
  if i > 0:
    apple.set_fontsize(12)
    banana.set_fontsize(12)
    cherry.set_fontsize(12)
    durian.set_fontsize(12)
    elderberries.set_fontsize(12)
    figs.set_fontsize(12)
    grapes.set_fontsize(12)
plt.show()


###########ADDING GRID LINES TO PLOT###################
import numpy as np
import matplotlib.pyplot as plt
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid()
plt.show()

###################STAIRS VALUE#######################
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')
# make data
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]
# plot
fig, ax = plt.subplots()
ax. stairs(y, linewidth=2.5)
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
plt.show()