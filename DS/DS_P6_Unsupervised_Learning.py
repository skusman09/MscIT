
from numpy import where
from sklearn.datasets import make_classification
from matplotlib import pyplot
x,y = make_classification(n_samples=1000, n_features=2, n_informative= 2, n_redundant=0, n_clusters_per_class=1, random_state=4)
for class_value in range(2):
  row_ix = where(y==class_value)
  pyplot.scatter(x[row_ix,0],x[row_ix,1])
pyplot.show()

OGRAM USING MATPLOTLIB
from matplotlib import pyplot as plt

y= [10,5,6,5,4]
plt.hist(y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
y= np.array([25,65,74,25,65])
plt.pie(y)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x,y)
plt.grid()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
plt.style.use("_mpl-gallery")

y = [4.8,5.5,2.3,5.6,7.6,4.3,5.1,3.6]

fig, ax = plt.subplots()
ax.stairs(y, linewidth=2.5)
ax.set(xlim=(0,8), xticks=np.arange(4,8),
       ylim=(0,8), yticks=np.arange(4,8))
plt.show()