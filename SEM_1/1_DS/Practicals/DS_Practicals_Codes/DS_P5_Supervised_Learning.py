# To predict the price of any item using supervised learning algorithm.
# (Linear Regression)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Load the Dataset
df=pd.read_csv("/content/PotatoPrice.csv")
print(df)

#DATA VISUALIZATION
%matplotlib inline
plt.xlabel("Potato in Kg")
plt.ylabel("Price in Rupees")
plt.scatter(df.potato_kg,df.price)
X=df[["potato_kg"]]
Y=df["price"]
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
print("X_train", X_train)
print("X_test", X_test)
print("Y_train", Y_train)
print("Y_test", Y_test)

#Train Dataset using model
reg = LinearRegression()
reg.fit(x_train, y_train)
print('Trained Dataset: ', reg.predict(x_test))

#ACCURACY OF THE MODEL
print('ACCURACY:', reg.score(x_test,y_test))

#Take the user input
x=input("Enter the potato quantity in kg: \n")
array=np.array(x)
fvalu=array.astype(np.float)
fvalu_2D=([[fvalu]])
my_prediction=reg.predict(fvalu_2D)
price=np.array(my_prediction)
price=price.item()
print('So',x,'Kilogram potato price is ',price,' Rupees')