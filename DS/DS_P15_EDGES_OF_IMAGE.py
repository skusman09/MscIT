import sys
import os
import matplotlib.pyplot as plt
from PIL import Image
sPicNameIn="/content/drive/MyDrive/DS_PRACTICAL_NOTES/1.png"
sPicNameOut="/content/audi.png"
imageIn = Image.open(sPicNameIn)
fig1 = plt.figure(figsize=(10, 10))
mask = imageIn.convert("L")
fig1.suptitle('Audi R8', fontsize=20)
imgplot = plt.imshow(imageIn)
th = 49
imageOut = mask.point(lambda i: i < th and 255)
imageOut.save(sPicNameOut)
imageTest = Image.open(sPicNameOut)
fig2=plt.figure(figsize=(10, 10))
fig2.suptitle('Audi R8 Edge', fontsize=20)
imgplot = plt.imshow(imageTest)