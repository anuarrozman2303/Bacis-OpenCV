# Canny Edge Detection
# Function: cv2.Canny()
# Multi-stage algorithm:
#   1. Noise reduction --> remove noise 
#   2. Finding intensity gradient --> Get gradient magnitude and direction 
#   3. Non-max suppression --> Full scan to remove unwanted pixels
#   4. Hysteresis Thresholding --> Decides which are all edges are really edges or not.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:\OpenCV\images\sakura.jpg', 0)
# cv2.Canny(<image source>, <minVal>, <maxVal>)
edges = cv2.Canny(img, 100, 200)

edges_2 = cv2.Canny(img, 500, 700)

edges_3 = cv2.Canny(img, 800, 1000)

plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(222)
plt.imshow(edges, cmap='gray')
plt.title('Edge Image(1)')
plt.xticks([])
plt.yticks([])

plt.subplot(223)
plt.imshow(edges_2, cmap='gray')
plt.title('Edge Image(2)')
plt.xticks([])
plt.yticks([])

plt.subplot(224)
plt.imshow(edges_3, cmap='gray')
plt.title('Edge Image(3)')
plt.xticks([])
plt.yticks([])

plt.show()