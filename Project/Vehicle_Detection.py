from pickle import FALSE
import cv2
from ipykernel import kernel_protocol_version
import numpy as np

cap = cv2.VideoCapture('D:\\UniKL MIIT\\Computer Vision\\Project\\sample1.mp4')

stop_sign = cv2.CascadeClassifier('D:/UniKL MIIT/Computer Vision/Assignment1_RoadSign/cascade_stop_sign.xml')

bgobject = cv2.createBackgroundSubtractorMOG2(varThreshold=100,detectShadows=True)

kernel = None

while (1):
    #read video frame by frame
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.1, 5)

    # Detect the stop sign, x,y = origin points, w = width, h = height
    for (x, y, w, h) in stop_sign_scaled:
        # Draw rectangle around the stop sign
        stop_sign_rectangle = cv2.rectangle(frame, (x,y),
                                            (x+w, y+h),
                                            (0, 255, 0), 3)
        # Write "BERHENTI" on the bottom of the rectangle
        stop_sign_text = cv2.putText(img=stop_sign_rectangle,
                                     text="Berhenti",
                                     org=(x, y-10),
                                     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                     fontScale=1, color=(0, 0, 255),
                                     thickness=2, lineType=cv2.LINE_4)
      
    #apply bgobject kat every frame
    fgmask = bgobject.apply(frame)
    
    #thresholding , get rid of shadows
    _, fgmask = cv2.threshold(fgmask, 250, 255, cv2.THRESH_BINARY)
    
    fgmask = cv2.erode(fgmask,kernel, iterations=1)
    fgmask = cv2.dilate(fgmask,kernel, iterations=2)
    
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    frameCopy = frame.copy()
    
    for cnt in contours:
        if cv2.contourArea(cnt) > 900:
            
            x, y, width, height = cv2.boundingRect(cnt)
            
            cv2.rectangle(frameCopy, (x , y), (x + width, y + height),(0, 0, 255), 2)
            
            cv2.putText(frameCopy, 'Vehicle', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,255,0), 1, cv2.LINE_AA)
            
    fgpart = cv2.bitwise_and(frame,frame, mask=fgmask)
    
    stacked = np.hstack((frame,fgpart, frameCopy))
    
    cv2.imshow('Stacked', cv2.resize(stacked, None, fx=0.7, fy=0.7))
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
    
    