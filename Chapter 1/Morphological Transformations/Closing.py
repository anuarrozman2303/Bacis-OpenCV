import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/closing.png', 0)
kernel = np.ones((5,5), np.uint8)

# Closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(121)
plt.imshow(img, 'gray')
plt.title('Original')

plt.subplot(122)
plt.imshow(closing, 'gray')
plt.title('Closing')

plt.show()