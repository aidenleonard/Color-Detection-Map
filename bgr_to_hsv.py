import cv2
import numpy as np

def bgr_to_hsv(rbg: list=[0,0,0]) -> 'np 1D array':
    """takes a 1D array with blue, green, and red values and converts them to a 1D HSV numpy array"""
    rbg_numpy = np.array([[rbg]], dtype=np.uint8)
    hsv_pixel = cv2.cvtColor(rbg_numpy, cv2.COLOR_BGR2HSV)  # must take 3D numpy array as input
    return hsv_pixel[0][0]  # returns 1D numpy array 

