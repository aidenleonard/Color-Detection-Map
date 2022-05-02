import cv2   # openCV computer vision for python
import numpy as np 
from bgr_to_hsv import bgr_to_hsv
from Img import Img

solar = Img('color_detection_map/SOLAR.jpg', [0,0,0],[50,50,255], -1)
print(solar)

solar.read()
print(solar)
solar.apply_mask()
solar.display_result()

#darkred = np.array([0, 0, 0])                    
#red = np.array([50,50,255]) 

#black = np.array([0,0,0])
#nearblack = np.array([10,10,10])

   #source1, source2, mask.    if pixel is source1 is in range of mask, keep. else, black 



# cv2.imshow('Image3', img_hsv) 

   # wait infinity , skip on key press
      # close window on key press 



# cv2.imwrite("")
# cv2."    "     IMREAD_COLOR  - no transparency   IMREAD_GRAYSCALE   - grayscale        IMREAD_UNCHANGED     - including alpha channel
# in terminal: python -m pydoc FUNCTIONNAME             <- displays description of function