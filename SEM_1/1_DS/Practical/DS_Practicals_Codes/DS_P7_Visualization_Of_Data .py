
# To Perform Visualization Of Data 

# Step 1
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import warnings
warnings.filterwarnings('ignore')
boston_df=pd.read_csv('/content/boston.csv')
print(boston_df)

# Step 2
plt.figure(figsize=(10,5))
sns.boxplot(x = boston_df.Price)
plt.title('Boxplot for MEDV')
plt.show() 

# Step 3
ax2 = sns.countplot(x='CHAS', data=boston_df)
ax2.set_title('Number of homes near the charles river')

# Step 4
boston_df.loc[(boston_df["AGE"]<35),"AGE_GROUP"] = "35 years and younger"
boston_df.loc[(boston_df["AGE"]<35) & (boston_df["AGE"]<70) ,"AGE_GROUP"]="Between 35 years abd 70 Years"
boston_df.loc[(boston_df["AGE"]>=70),"AGE_GROUP"] = "70 years and older"
plt.figure(figsize=(10,5))
sns.boxplot(x=boston_df.Price, y=boston_df.AGE_GROUP, data=boston_df)
plt.title("BOXPLOT FOR THE MEDV VARIABLE VS THE AGE VARIABLE")
plt.show()

ax4 = sns.scatterplot(y='NOX', x="INDUS", data=boston_df)
ax4.set_title("Nitric oxide concentration per proportion of no-retail business acres per town")

plt.figure(figsize=(10,5))
sns.distplot(a=boston_df.PTRATIO, bins=10, kde=False, color="red")
plt.title("HISTOGRAM FOR THE PUPIL TO TEACHER PATIO VARIABLE")
plt.show()