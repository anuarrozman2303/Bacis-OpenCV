import cv2
import matplotlib.pyplot as plt

australia = cv2.imread('F:/images/australia.png')
australia_grey = cv2.cvtColor(australia, cv2.COLOR_BGR2GRAY)

australia_thresh = cv2.threshold(australia_grey,226,255,cv2.THRESH_BINARY)[1]
australia_binary = cv2.bitwise_not(australia_thresh)

plt.imshow(australia_binary, cmap="gray", vmin=0, vmax=255)

# Multiple objects
result = australia.copy()
contours = cv2.findContours(australia_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
colour = (255, 0, 0)
thickness = 1
i = 0
for cntr in contours:
    x1,y1,w,h = cv2.boundingRect(cntr)
    x2 = x1+w
    y2 = y1+h
    cv2.rectangle(result, (x1, y1), (x2, y2), colour, thickness)
    print("Object:", i+1, "x1:", x1, "x2:", x2, "y1:", y1, "y2:", y2)
    i += 1
    
plt.imshow(result)
plt.show()