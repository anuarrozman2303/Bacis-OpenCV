# Function: cv2.GaussianBlur()

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/opencvlogo.jpg',)

# Gaussian Blur
blur = cv2.GaussianBlur(img, (5,5), 0)

# Print Images (Original and Blurred)
plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGBA))
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGBA))
plt.title('Blurred')
plt.xticks([])
plt.yticks([])

plt.show()