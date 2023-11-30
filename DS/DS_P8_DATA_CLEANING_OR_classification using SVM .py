import pandas as pd
df=pd.read_csv("/content/credit.csv", encoding='latin-1')
df

df.dropna(inplace =True)
print(df.to_string())

df['trdate'] = pd.to_datetime(df['trdate'])
print(df.to_string())