# Otsu's Binarization
# Automatically calculates a threshold value from image histogram for a bimodal image.
# Bimodal Image: Image whose histogram has two peaks).
# cv2.threshold() is used with extra flag --> cv2.THRESH_OTSU
# Threshold value = 0
# retVal --> return the optimal threshold value as second output.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/noisy2.png', 0)

# Global Thres
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Otsu's Thres
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's Thres after Gaussian Filter
blur = cv2.GaussianBlur(img, (5,5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Plot Images
images = [img, 0, th1,
          img, 0, th2, 
          blur, 0, th3]

titles = ['Original', 'Histogram', 'Global Thres (v=127)',
          'Original', 'Histogram', "Otsu's Thres",
          'Gaussian Filter', 'Histogram', "Otsu's Thres"]

for i in range(3):
    plt.subplot(3,3,i*3+1)
    plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(3,3,i*3+2)
    plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(3,3,i*3+3)
    plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2])
    plt.xticks([])
    plt.yticks([])

plt.show()
    
    