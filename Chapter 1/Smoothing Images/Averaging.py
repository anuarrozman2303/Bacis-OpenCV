# Take the average of all pixels under kernel area,
# Then replace the central element.
# Function: cv2.blur() or cv2.boxFilter()

from turtle import bgcolor
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/opencvlogo.jpg')
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

# Averaging
blur = cv2.blur(img, (5,5))
rgb_blur = cv2.cvtColor(blur, cv2.COLOR_BGR2RGBA)

# Print Images (Original and Blurred)
cv2.imshow('Original', rgb_img)
cv2.imshow('Blurred', rgb_blur)
cv2.waitKey(0)
cv2.destroyAllWindows