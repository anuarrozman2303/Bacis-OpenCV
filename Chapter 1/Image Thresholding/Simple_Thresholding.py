# pixel value > threshold value = assigned 1 value (may be white)
# else assigned another value (may be black)
# Function: cv2.threshold(<image source>, <threshold value>, <maxVal>, <styles of threshold>)
# 1. Image source --> should be grayscale
# 2. Threshold value --> Classify pixel values
# 3. maxVal --> Value to be given if pixel value > threshold
# 4. styles of threshold --> cv2.THRESH_BINARY
#                        --> cv2.THRESH_BINARY_INV
#                        --> cv2.THRESH_TRUNC
#                        --> cv2.THRESH_TOZERO
#                        --> cv2.THRESH_TOZERO_INV

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/pokemon.jpg', 0)
ret,thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original', 'Binary', 'Binary_Inv', 'Trunc', 'Tozero', 'Tozero_Inv']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()