import cv2 as cv

img = cv.imread('F:/images/australia.png',0)

ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]

# Moments : Calculate some features like center of mass and area of the object, etc.
# cv2.moments()
M = cv.moments(cnt)
print ('\n M =', M)

# From moments, we can extract data like area, centroid , etc.
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print('\n Centroid:')
print(' cx = ', cx)
print(' cy = ', cy)

# Area
# cv2.contourArea()
area = cv.contourArea(cnt)
print('\n Area = ', area)

# Perimeter
# cv2.arcLength()
perimeter = cv.arcLength(cnt,True)
print('\n Perimeter = ', perimeter)

# Approximation
epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)
print('\n Approximation = ', approx)

# Checking Convexity
k = cv.isContourConvex(cnt)
print('\n Checking Convexity = ', k)  
     

