# Image Pyramid
# 2 types: 
#   1. Gaussian Pyramid
#   2. Laplacian Pyramid
# Functions: 
#   1. cv2.pyrUp()
#   2. cv2.pyrDown()

import cv2
from cv2 import pyrDown
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('F:/images/pokemon.jpg')

layer = img.copy()

for i in range(4):
    plt.subplot(2,2,i+1)
    
    #pyrdown function
    layer = cv2.pyrDown(layer)
    
    cv2.imshow('pyrDown', layer)
    cv2.waitKey(0)
    
cv2.destroyAllWindows
    

