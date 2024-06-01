import numpy as np
from PIL import Image

img = Image.open('Photo.jpg')
img.show()
Idata = np.array(img)
print(Idata)

pixelMap=img.load()
pixelNew=img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if (pixelMap[i,j][0]>=0 and pixelMap[i,j][0]<=63):
            pixelNew[i,j]=(10,255,20)
        elif (pixelMap[i,j][0]>=64 and pixelMap[i,j][0]<=127):
            pixelNew[i,j]=(30,255,54)
        elif (pixelMap[i,j][0]>=128 and pixelMap[i,j][0]<=191):
            pixelNew[i,j]=(40,255,89)
        elif (pixelMap[i,j][0]>=192 and pixelMap[i,j][0]<=255):
            pixelNew[i,j]=(50,255,10)
img.show("Photo1.jpg")