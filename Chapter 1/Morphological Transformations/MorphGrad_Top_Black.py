import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/gradient.png', 0)
kernel = np.ones((5,5), np.uint8)
kernel_2 = np.ones((9,9), np.uint8)

# Gradient
# The result will look like the outline of the object.
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Top Hat
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel_2)

# Black Hat
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel_2)

plt.subplot(141)
plt.imshow(img, 'gray')
plt.title('Original')

plt.subplot(142)
plt.imshow(gradient, 'gray')
plt.title('Closing')

plt.subplot(143)
plt.imshow(tophat, 'gray')
plt.title('Top Hat')

plt.subplot(144)
plt.imshow(blackhat, 'gray')
plt.title('Black Hat')

plt.show()