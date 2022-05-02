import cv2   # openCV computer vision for python
import numpy as np 
from bgr_to_hsv import bgr_to_hsv

img = cv2.imread('color_detection_map/SOLAR.jpg', -1)   # -1: default, 1: color (filter transparent)
img = cv2.resize(img, (0,0), fx=0.2, fy = 0.2)         # 20%= 660x1020
dimenions = img.shape
# print(dimenions)
# print(img[330][510])

darkpurp = np.array([340,0,0])
red = np.array([0,100,255])

darkred = np.array([0,0,0]) # bgr_to_hsv([0, 0, 51])                     # create a single numpy 1D pixel array  (type in BGR values). function converts to hsv  
lightyellow = np.array([71,255,255]) # bgr_to_hsv([204,255,204]) 

print(type(darkred), darkred, type(lightyellow), lightyellow)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print(img_hsv[600-210][300])
mask = cv2.inRange(img_hsv, darkred, lightyellow)

result = cv2.bitwise_and(img, img, mask=mask)    #source1, source2, mask.    if pixel is source1 is in range of mask, keep. else, black 


cv2.imshow('Image', result) 
# cv2.imshow('Image2', mask)
# cv2.imshow('Image3', img_hsv) 


cv2.waitKey(0)   # wait infinity , skip on key press
cv2.destroyAllWindows()       # close window on key press 



# cv2.imwrite("")
# cv2."    "     IMREAD_COLOR  - no transparency   IMREAD_GRAYSCALE   - grayscale        IMREAD_UNCHANGED     - including alpha channel
# in terminal: python -m pydoc FUNCTIONNAME             <- displays description of function