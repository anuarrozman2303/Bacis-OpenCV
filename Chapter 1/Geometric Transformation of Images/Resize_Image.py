from turtle import width
import cv2
from matplotlib import scale

img = cv2.imread('F:/images/pokemon.jpg', cv2.IMREAD_UNCHANGED)

print ('Original Dimension: ', img.shape)

scale_percent = 60
width = int(img.shape[1] * scale_percent/100)
height = int(img.shape[0] * scale_percent/100)
dim = (width,height)

resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print ('Resized Dimensions: ', resized.shape)

cv2.imshow("Resized Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows