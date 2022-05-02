import cv2
import numpy as np

class Img:
    """Image class used for color reading on maps"""
    def __init__(self, 
                 name: str,
                 filepath: str,
                 baseclr: list=[0,0,0],
                 topclr: list=[255,255,255],
                 filtertype: int=-1) -> None:
        # initializes variables as class attributes
        self.file = filepath
        self.base = np.array(baseclr)     # darker color
        self.top = np.array(topclr)       # lighter color 
        self.fltr = filtertype
        self.name = name

    def read(self):
        """reads and resizes the map image"""
        # reading and resizing
        self.img = cv2.imread(self.file, self.fltr)
        self.img = cv2.resize(self.img, (1020,660))   #20% is 660x1020
     
        # self.img = cv2.resize(self.img, (0,0), fx=0.2, fy = 0.2)   #20% is 660x1020
       
        # defines the image dimensions in x, y, and channels
        self.dim = self.img.shape

    def apply_mask(self):
        """creates mask and performs mask operation"""
        # defines the mask based on the base and top colors. 
        self.mask = cv2.inRange(self.img, self.base, self.top)
        
        # combines the image with itself, and applies the mask
        self.result = cv2.bitwise_and(self.img, self.img, mask=self.mask)

    def display_result(self):
        """Displays results and closes images upon key touch"""
        #displays the result and mask as an image file
        cv2.imshow(self.name, self.result)
        cv2.imshow(self.name + ' mask', self.mask)

        #Waits infinitely long, until any key is pressed which closes images.
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()