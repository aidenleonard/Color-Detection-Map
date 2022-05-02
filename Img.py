import cv2
import numpy as np

class Img:
    """Image class used for color reading on maps"""
    def __init__(self, 
                 filepath,
                 baseclr: list=[0,0,0],
                 topclr: list=[255,255,255],
                 filtertype: int=-1) -> None:
        self.file = filepath
        self.base = np.array(baseclr)     # darker color
        self.top = np.array(topclr)       # lighter color 
        self.fltr = filtertype

    def read(self):
        self.img = cv2.imread(self.file, self.fltr)
        self.img = cv2.resize(self.img, (0,0), fx=0.2, fy = 0.2)   #20% is 660x1020
        self.dim = self.img.shape

    def apply_mask(self):
        self.mask = cv2.inRange(self.img, self.base, self.top)
        self.result = cv2.bitwise_and(self.img, self.img, mask=self.mask)

    def display_result(self):
        cv2.imshow('Result', self.result)
        cv2.imshow('Mask', self.mask)
        cv2.waitKey(0)
        cv2.destroyAllWindows()