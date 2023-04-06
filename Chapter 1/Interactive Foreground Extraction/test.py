import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('F:/images/messi5.jpg')
RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

mask = np.zeros(RGB_img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (50,50,450,290)

cv.grabCut(RGB_img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
RGB_img = RGB_img*mask2[:,:,np.newaxis]
cv.imwrite('1',RGB_img)


# newmask is the mask image I manually labelled
# newmask = cv.imread('F:/images/newmask.jpg',0)

# wherever it is marked white (sure foreground), change mask=1
# wherever it is marked black (sure background), change mask=0
# mask[newmask == 0] = 0
# mask[newmask == 255] = 1
# mask, bgdModel, fgdModel = cv.grabCut(img,mask,None,bgdModel,fgdModel,5,cv.GC_INIT_WITH_MASK)
# mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')

# RGB_img = RGB_img*mask[:,:,np.newaxis]


plt.imshow(RGB_img)
plt.colorbar()
plt.show()
