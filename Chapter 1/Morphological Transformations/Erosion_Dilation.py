# Erosion
# Erodes the boundaries of foreground object.
# Always try to keep foreground white.
# Removing small white noises.
# --------------------------------------------
# Dilation = pposite of erosion.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/j.png', 0)
kernel = np.ones((5,5), np.uint8)

# Erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(erosion, kernel, iterations=1)

plt.subplot(131)
plt.imshow(img, 'gray')
plt.title('Original')

plt.subplot(132)
plt.imshow(erosion, 'gray')
plt.title('Erosion')

plt.subplot(133)
plt.imshow(dilation, 'gray')
plt.title('Dilation')

plt.show()