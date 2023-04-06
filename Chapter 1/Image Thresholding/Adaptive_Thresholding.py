# Adaptive Thresholding
# The algo calculate the threshold for a small region of the image.

import cv2
from cv2 import THRESH_BINARY
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/sudoku.jpg',0)
img = cv2.medianBlur(img, 5)

ret,th1 = cv2.threshold(img,127,255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ['Original', 'Global Thres (v=127)', 'Adaptive Mean Thres', 'Adaptive Gaussian Thres']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()