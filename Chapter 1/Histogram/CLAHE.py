import numpy as np
import cv2

img = cv2.imread('F:/images/clahe.jpg',0)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.imshow('Clahe',cl1)
cv2.waitKey(0)
cv2.destroyAllWindows()

