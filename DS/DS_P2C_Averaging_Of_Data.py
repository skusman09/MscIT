import pandas as pd
InputFileName = 'IP_DATA_CORE.csv'
OutputFileName = 'Retrieve_Router_Location.csv'
sFileName = '/content/IP_DATA_CORE.csv'
IP_DATA_ALL = pd.read_csv(sFileName,header=0,low_memory=False,usecols=['Country','Place.Name','Latitude','Longitude'], encoding="latin-1")

IP_DATA_ALL.rename(columns={'Place.Name': 'Place_Name'}, inplace=True)
AllData = IP_DATA_ALL[['Country', 'Place_Name','Latitude']]
print(AllData)
MeanData = AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()
print(MeanData)