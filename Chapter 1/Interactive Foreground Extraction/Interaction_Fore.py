# foreground extraction using GrabCut algorithm

import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('F:/images/db.jpg')
RGB_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# create a simple mask image similar to the loaded image, with the shape and return type
mask = np.zeros(RGB_img.shape[:2], np.uint8)

# specify the background and foreground model
# using numpy the array is constructed of 1 row
# and 65 columns, and all array elements are 0
# Data type for the array is np.float64 (default)
backgroundModel = np.zeros((1, 65), np.float64)
foregroundModel = np.zeros((1, 65), np.float64)

# define the Region of Interest (ROI) as the coordinates of the rectangle
# where the values are entered as (startingPoint_x, startingPoint_y, width, height)
rectangle = (20, 100, 150, 150)
# rectangle = (50,50,450,290)

# apply the grabcut algorithm with appropriate
# values as parameters, number of iterations = 3
# cv2.GC_INIT_WITH_RECT is used because of the rectangle mode is used
cv2.grabCut(RGB_img, mask, rectangle,
			backgroundModel, foregroundModel,
			3, cv2.GC_INIT_WITH_RECT)

# In the new mask image, pixels will be marked with four flags
# four flags denote the background / foreground mask is changed, 
# all the 0 and 2 pixels are converted to the background
# mask is changed, all the 1 and 3 pixels are now the part of the foreground
mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')

# The final mask is multiplied with
# the input image to give the segmented image.
RGB_img = RGB_img * mask2[:, :, np.newaxis]

# output
plt.subplot(121)
plt.imshow(image)
plt.title('Original')

plt.subplot(122)
plt.imshow(RGB_img)
plt.title('grabCut')
plt.show()