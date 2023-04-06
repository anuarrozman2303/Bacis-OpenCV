import cv2
import numpy as np

img = cv2.imread('F:/images/noisy2.png', 0)
blur = cv2.GaussianBlur(img,(5,5),0)

# Find normalized_hist, and its cumulative distr function
hist = cv2.calcHist([blur],[0],None,[256],[0,256])
hist_norm = hist.ravel()/hist.sum()

Q = hist_norm.cumsum()
bins = np.arange(256)
fn_min = np.inf
thresh = -1

for i in range(1,256):
    # Probabilities
    p1, p2 = np.hsplit(hist_norm,[i])
    
    # Cum sum of classes
    q1, q2 = Q[i], Q[255] - Q[i]
    
    if q1 < 1.e-6 or q2 < 1.e-6:
        continue
    
    # Weights
    b1, b2 = np.hsplit(bins,[i])
    
    # Find means and variances
    m1 = np.sum(p1 * b1) / q1 
    m2 = np.sum(p2 * b2) / q2
    
    v1 = np.sum(((b1 - m1) ** 2) * p1 / q1)
    v2 = np.sum(((b2 - m2) ** 2) * p2 / q2)
    
    # Calculate minimization function
    fn = v1 * q1 + v2 * q2
    if fn < fn_min:
        fn_min = fn
        thresh = i

# Find Otsu's thres value
ret, otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("{} {}". format(thresh,ret))