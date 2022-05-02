from Img import Img
import numpy as np
import cv2

solar = Img('solar','color_detection_map/SOLAR.jpg', [0,0,0],[50,50,255], -1)
pland = Img('pland','color_detection_map/PUBLIC_LAND.jpg', [0,0,0],[50,50,255], -1)

solar.read()
pland.read()

solar.apply_mask()
pland.apply_mask()

solar.display_result()
pland.display_result()

cv2.waitKey(0)
cv2.destroyAllWindows()



""" Hori = np.concatenate((solar.result, pland.result), axis = 1)
Hori2 = np.concatenate((solar.mask, pland.mask), axis = 1)

cv2.imshow('H', Hori)
cv2.imshow('V', Hori2)

cv2.waitKey(0)
cv2.destroyAllWindows() """