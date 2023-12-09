
# UNDERSTAND THE USE OF DATA CLEANING
#                OR
# To perform classification using SVM

import pandas as pd
df=pd.read_csv("/content/credit.csv", encoding='latin-1')
df
# Remove all rows with null values
df.dropna(inplace =True)
print(df.to_string())
# convert to date
df['trdate'] = pd.to_datetime(df['trdate'])
print(df.to_string())