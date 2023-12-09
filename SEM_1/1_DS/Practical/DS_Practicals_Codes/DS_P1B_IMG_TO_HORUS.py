
# Image to HORUS Conversion
from skimage import io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
sInputFileName='/content/audi.jpg'
InputData = io.imread(sInputFileName, pilmode='RGBA')
plt.imshow(InputData)
InputData.shape
print('Input Data Values')
print('X: ',InputData.shape[0])
print('Y: ', InputData. shape[1])
print('RGBA: ', InputData.shape[2])
ProcessRawData=InputData.flatten()
y=InputData.shape[2] + 2
x=int(ProcessRawData.shape[0]/y)
ProcessData=pd.DataFrame(np.reshape(ProcessRawData, (x, y)))
ProcessRawData
ProcessData=pd.DataFrame(np.reshape(ProcessRawData, (x, y)))
sColumns= [ 'XAxis', 'YAxis', 'Red', 'Green', 'Blue','Aplha']
ProcessData.columns=sColumns
ProcessData
print('Rows: ',ProcessData.shape[0])
print('Columns :',ProcessData.shape[1])
OutputData = ProcessData
OutputData.to_csv('Image to HORUS.csv', index = False)