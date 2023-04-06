import cv2
import numpy as np

img = cv2.imread('F:/images/pokemon.jpg',0)
rows, cols = img.shape

# cols-1 and rows-1 are the coordinate limits

M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv2.warpAffine(img, M, (cols,rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows
