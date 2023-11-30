import sys
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
sPicName='/content/drive/MyDrive/DS_PRACTICAL_NOTES/1.png'
t=0
img=mpimg.imread(sPicName)
print('Size:', img.shape)
plt.figure(figsize=(10, 10))
t+=1
sTitle= '(' + str(t) + ') Original'
plt.title(sTitle)
plt.imshow(img)
plt.show()
for c in range(img.shape[2]):
    t+=1
    plt.figure(figsize=(10, 10))
    sTitle= '(' + str(t) + ') Channel:' + str(c)
    plt.title(sTitle)
    lum_img = img[:,:,c]
    plt.imshow(lum_img)
    plt.show()