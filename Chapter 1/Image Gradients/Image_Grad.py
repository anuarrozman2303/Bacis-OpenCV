# Find image gradients / edges.
# Functions:
#   1. cv2.Sobel()
#   2. cv2.Scharr()
#   3. cv2.Lalacian()
# Gradient Filters (high pass filter):
#       a. Sobel
#       b. Scharr
#       c. Laplacian
# Sobel and Scharr Derivatives ---> Gaussian smoothing + Differentiation.
#                              ---> More resistant to noise.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/sudoku.jpg', 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(sobelX, cmap='gray')
plt.title('Sobel X')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y')
plt.xticks([])
plt.yticks([])

plt.show()
