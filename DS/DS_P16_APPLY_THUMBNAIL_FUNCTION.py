import sys
import os
import matplotlib.pyplot as plt
from PIL import Image
spicName = '/content/drive/MyDrive/DS_PRACTICAL_NOTES/1.png'
nSize = 4
img = Image.open(spicName)
plt.figure(figsize=(nSize, nSize))
sTitle = "Unchanges"
plt.title(sTitle)
imgplot = plt.imshow(img)

from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("/content/drive/MyDrive/DS_PRACTICAL_NOTES/1.png")

img.thumbnail((64, 64), Image.ANTIALIAS)

nSize = 10
sTitle = "Resized"
plt.figure(figsize=(nSize, nSize))
plt.title(sTitle)
imgplot = plt.imshow(img)

nSize = 10
sTitle = "Resized with Bi-Cubic"
plt.figure(figsize=(nSize, nSize))
plt.title(sTitle)
imgplot = plt.imshow(img, interpolation="bicubic")
print('### Done!! #########')