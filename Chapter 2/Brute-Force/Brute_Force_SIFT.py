import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('C:/Users/anuar/OneDrive/Pictures/opencvimage/a.jpg',0) # queryImage
img2 = cv2.imread('C:/Users/anuar/OneDrive/Pictures/opencvimage/b.jpg',0) # trainImage

gray1= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# Initiate SIFT detector
sift = cv2.SIFT()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detect(gray1,None)
kp2, des2 = sift.detect(gray2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,flags=2)

plt.imshow(img3),plt.show()