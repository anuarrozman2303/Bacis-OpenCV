#Transformation functions:
# 1. cv.warpAffine - 2x3 transformation matrix.
# 2. cv.warpPerspective - 3x3 transformation matrix.

# Scaling = Resizing image.
# cv.resize()

# Interpolation methods:
# 1. cv.INTER_AREA - shrinking
# 2. cv.INTER_CUBIC - (slow)
# 3. cv.INTER_LINEAR - zooming

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/pokemon.jpg')
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

res = cv2.resize(RGB_img, None, fx=2, fy=2, interpolation= cv2.INTER_CUBIC)

plt.subplot(121)
plt.title('Original')
plt.imshow(RGB_img)

plt.subplot(122)
plt.title('Scale')
plt.imshow(res)

plt.show()