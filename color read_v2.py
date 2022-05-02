import cv2   # openCV computer vision for python
import numpy as np 
from bgr_to_hsv import bgr_to_hsv



img = cv2.imread('color_detection_map/SOLAR.jpg', -1)   # -1: default, 1: color (filter transparent)
img = cv2.resize(img, (0,0), fx=0.2, fy = 0.2)         # 20%= 660x1020
dimenions = img.shape
# print(dimenions)
# print(img[330][510])


darkred = np.array([0, 0, 0])                     # create a single numpy 1D pixel array  (type in BGR values). function converts to hsv  
red = np.array([50,50,255]) 

black = np.array([0,0,0])
nearblack = np.array([10,10,10])

# print(type(darkred), darkred, type(red), red)

# img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(img, darkred, red)
mask_outline = cv2.inRange(img, black, nearblack)


result = cv2.bitwise_and(img, img, mask=mask)    #source1, source2, mask.    if pixel is source1 is in range of mask, keep. else, black 


background = cv2.bitwise_and(img, img, mask=mask_outline)

cv2.imshow('Image', result) 
cv2.imshow('Image2', mask)
cv2.imshow('outline', mask_outline)
# cv2.imshow('Image3', img_hsv) 


cv2.waitKey(0)   # wait infinity , skip on key press
cv2.destroyAllWindows()       # close window on key press 



# cv2.imwrite("")
# cv2."    "     IMREAD_COLOR  - no transparency   IMREAD_GRAYSCALE   - grayscale        IMREAD_UNCHANGED     - including alpha channel
# in terminal: python -m pydoc FUNCTIONNAME             <- displays description of function