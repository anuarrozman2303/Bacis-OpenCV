import cv2
import numpy as np
from matplotlib import image, pyplot as plt

# Perspective transformation - need 3x3 transformation matrix.
# Need 4 points on input image to find it and corresponding points on output image.

img = cv2.imread('F:/images/sudoku.jpg')
print(img.shape)

# this is coloured dot for finding points.
# use paint application to find the coordinates.
cv2.circle(img, (57,65), 5, (0,0,255), -1)
cv2.circle(img, (368,53), 5, (0,0,255), -1)
cv2.circle(img, (27,385), 5, (0,0,255), -1)
cv2.circle(img, (390,391), 5, (0,0,255), -1)

pts1 = np.float32([[57,65],
                   [368,53],
                   [27,385],
                   [390,391]])

pts2 = np.float32([[0,0],
                   [300,0],
                   [0,300],
                   [300,300]])

# cv2.getPerspectiveTransform(src,dst)
# src: coordinates in source image
# dst: coordinates in output image
M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (300,300))

plt.subplot(121)
plt.imshow(img)
plt.title('input')

plt.subplot(122)
plt.imshow(dst)
plt.title('output')

plt.show()
