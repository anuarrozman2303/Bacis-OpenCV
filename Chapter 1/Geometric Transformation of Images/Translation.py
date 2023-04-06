import numpy as np
import cv2

# Translation = Shifting Object's Location

# Read image
img = cv2.imread('F:/images/pokemon.jpg',0)

rows,cols = img.shape


M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows

