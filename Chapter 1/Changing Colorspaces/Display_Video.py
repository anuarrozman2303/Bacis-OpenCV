import cv2
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file nameq
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('F:\images\pikachu.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
    
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    
    # Take each frame
    _, frame = cap.read()
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define range of the colors in HSV
    lower_yellow = np.array([21,202,225])
    upper_yellow = np.array([31,212,295])
    lower_orange = np.array([9,224,237])
    upper_orange = np.array([-1,214,194])
  
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    mask_1 = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask_1)
    
    # Display the resulting frame
    cv2.imshow('Frame',frame)
    cv2.imshow('Mask',mask)
    cv2.imshow('Mask_1',mask_1)
    cv2.imshow('Res',res)

    # Press Q on keyboard to  exit
    if cv2.waitKey(0) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()