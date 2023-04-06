# Opening
# Opening is just another name of erosion followed by dilation.
# Remove small blobs from an image.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/blob.jpg', 0)
kernel = np.ones((5,5), np.uint8)

# Erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(erosion, kernel, iterations=1)

# Opening
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

plt.subplot(121)
plt.imshow(img, 'gray')
plt.title('Original')

plt.subplot(122)
plt.imshow(opening, 'gray')
plt.title('Opening')

plt.show()