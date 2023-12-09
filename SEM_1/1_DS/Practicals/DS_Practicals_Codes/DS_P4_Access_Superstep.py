# PRACTICAL-4
# TO UNDERSTAND THE USE OF ASSESS SUPERSTEP

#1. REPLACING NAN VALUES WITH MEAN
print('#1. REPLACING NAN VALUES WITH MEAN')
import pandas as pd
import numpy as np
df = pd.DataFrame([[10, np.nan, 30, 40], [7, 14, 21, 28], [55, np.nan, 8, 12],
 [15, 14, np.nan, 8], [7, 1, 1, np.nan], [np.nan, 4, 9, 2]],
 columns=['Apple', 'Orange', 'Banana', 'Pear'],
 index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
 'Basket5', 'Basket6'])
print("#################################")
print("THE ORIGINAL VALUES")
print(df)
print("REPLACING THE  VALUES WITH MEAN")
df.fillna(df.mean(),inplace=True)
df

#2.REPLACING NAN VALUES WITH MEDIAN
print('\n#2.REPLACING NAN VALUES WITH MEDIAN')
import pandas as pd
import numpy as np
df = pd.DataFrame([[10, np.nan, 30, 40], [7, 14, 21, 28], [55, np.nan, 8, 12],
 [15, 14, np.nan, 8], [7, 1, 1, np.nan], [np.nan, 4, 9, 2]],
 columns=['Apple', 'Orange', 'Banana', 'Pear'],
 index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
 'Basket5', 'Basket6'])
print("#################################")
print("THE ORIGINAL VALUES")
print(df)
print("REPLACING THE  VALUES WITH MEAN")
df.fillna(df.median(),inplace=True)
df

#3.REPLACING NAN VALUES WITH MODE
print('\n#3.REPLACING NAN VALUES WITH MODE')
import pandas as pd
import numpy as np
df = pd.DataFrame([[10, np.nan, 30, 40], [7, 14, 21, 28], [55, np.nan, 8, 12],
 [15, 14, np.nan, 8], [7, 1, 1, np.nan], [np.nan, 4, 9, 2]],
 columns=['Apple', 'Orange', 'Banana', 'Pear'],
 index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
 'Basket5', 'Basket6'])
print("#################################")
print("THE ORIGINAL VALUES")
print(df)
print("REPLACING THE  VALUES WITH MEAN")
for column in df.columns:
  df[column].fillna(df[column].mode()[0], inplace=True)
df

#4.REPLACING NAN VALUES WITH MINIMUM
print('\n#4.REPLACING NAN VALUES WITH MINIMUM')
import pandas as pd
import numpy as np
df = pd.DataFrame([[10, np.nan, 30, 40], [7, 14, 21, 28], [55, np.nan, 8, 12],
 [15, 14, np.nan, 8], [7, 1, 1, np.nan], [np.nan, 4, 9, 2]],
 columns=['Apple', 'Orange', 'Banana', 'Pear'],
 index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
 'Basket5', 'Basket6'])
print("#################################")
print("THE ORIGINAL VALUES")
print(df)
print("REPLACING THE  VALUES WITH MEAN")
df.fillna(df.min(),inplace=True)
df