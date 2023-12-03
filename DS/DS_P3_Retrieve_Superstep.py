
# Understand Retrieve Superstep 
import os
import pandas as pd
sFileName = "/content/IP_DATA_CORE.csv"
IP_DATA_ALL = pd.read_csv(sFileName,header = 0,low_memory = False, usecols = ['Country','Place.Name','Latitude','Longitude'])
IP_DATA_ALL.rename(columns = {'Place.Name': 'Place_Name'}, inplace = True)
dropDuplicates = IP_DATA_ALL.drop_duplicates(subset = None, keep = 'first', inplace = False)
print('Rows :',dropDuplicates.shape[0])
print('Columns :',dropDuplicates.shape[1])
retrieve_outPutFile = 'Retrieve_Router_Location.csv'
dropDuplicates.to_csv(retrieve_outPutFile, index = False)
print('Done...!!')