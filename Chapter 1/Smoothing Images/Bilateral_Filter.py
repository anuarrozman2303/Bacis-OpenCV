# Bilateral filter effective in noise removal while keeping edges sharp.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/bilat_filter.jpg',)

# Bilateral Filtering
bilat_filter = cv2.bilateralFilter(img, 9, 75, 75)

# Print Images (Original and Blurred)
plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGBA))
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(cv2.cvtColor(bilat_filter, cv2.COLOR_BGR2RGBA))
plt.title('Blurred')
plt.xticks([])
plt.yticks([])

plt.show()