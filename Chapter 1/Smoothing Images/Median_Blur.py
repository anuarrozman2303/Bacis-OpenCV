# Take median of all pixels under kernel area.
# Central element is replaced with this median value.
# Central element is replaced by some pixel value in image.
# Reduce the noice effectively.
# Function: cv2.medianBlur()

# Added 50% noise to original image and applied median blur.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/med_blur.jpg',)

# Median Blur
med_blur = cv2.medianBlur(img, 5)

# Print Images (Original and Blurred)
plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGBA))
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(cv2.cvtColor(med_blur, cv2.COLOR_BGR2RGBA))
plt.title('Blurred')
plt.xticks([])
plt.yticks([])

plt.show()