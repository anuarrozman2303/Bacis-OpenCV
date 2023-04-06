# Importing the libraries
import cv2
from matplotlib import pyplot as plt

# Reading the image and converting into B/W
image = cv2.imread('C:/Users/anuar/OneDrive/Pictures/opencvimage/anuar.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Applying the function
fast = cv2.FastFeatureDetector_create()
fast.setNonmaxSuppression(False)


# Drawing the keypoints
kp = fast.detect(image,None)
img2 = cv2.drawKeypoints(image, kp, None, color=(255,0,0))

plt.subplot(121)
plt.imshow(image)
plt.title('Original')

plt.subplot(122)
plt.imshow(img2)
plt.title('FAST')
plt.show()