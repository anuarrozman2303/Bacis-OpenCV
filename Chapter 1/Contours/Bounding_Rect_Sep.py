import cv2
import matplotlib.pyplot as plt

australia = cv2.imread('F:/images/australia.png')
australia_grey = cv2.cvtColor(australia, cv2.COLOR_BGR2GRAY)

australia_thresh = cv2.threshold(australia_grey,226,255,cv2.THRESH_BINARY)[1]
australia_binary = cv2.bitwise_not(australia_thresh)

plt.imshow(australia_binary, cmap="gray", vmin=0, vmax=255)

# Generate variables
x1,y1,w,h = cv2.boundingRect(australia_binary)
x2 = x1+w
y2 = y1+h

# Draw bounding rectangle
start = (x1, y1)
end = (x2, y2)
colour = (255, 0, 0)
thickness = 1
rectangle_img = cv2.rectangle(australia, start, end, colour, thickness)
print("x1:", x1, "x2:", x2, "y1:", y1, "y2:", y2)
plt.imshow(rectangle_img, cmap="gray")

plt.show()

