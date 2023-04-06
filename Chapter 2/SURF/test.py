import numpy as np
import cv2 as cv

img = cv.imread('C:/Users/anuar/OneDrive/Pictures/opencvimage/chair.jpg')

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
surf = cv.xfeatures2d.SURF_create()

keypoints, descriptor = surf.detectAndCompute(img,None)

img = cv.drawKeypoints(img, keypoints,None)

cv.imshow("SURF", img)
cv.waitKey(0)
cv.destroyAllWindows
