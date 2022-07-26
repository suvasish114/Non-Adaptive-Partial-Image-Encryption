# noise degression model
import numpy as np
from statistics import median

class Degreadation:
    def __init__(self, img, height, width, row =3):
        ''' constractor '''
        self.img = img          # original image
        self.height = height    # height of the original image
        self.width = width      # width of the original image
        self.row = row          # default row size

    def _neighbour(self, xc, yc, Q=1):
        ''' return a list of neighbour pixels '''
        order_of_filter = Q 
        nrow = int(self.row/2)
        list = []
        for a in range(-nrow, nrow+1):
            for b in range(-nrow, nrow+1):
                x = xc+b 
                y = yc+a 
                if x >= 0 and x <= self.width-1 and y >= 0  and y <= self.height-1:   # if pixel range inside image matrix
                    list.append(int(pow(self.img[x][y],order_of_filter)))
        return list 
    
    def medianFilter(self):
        ''' median filter '''
        degradated_img = self.img.copy()
        for a in range(self.width):
            for b in range(self.height):
                degradated_img[a][b] = int(median(self._neighbour(a,b)))

        return np.array(degradated_img, dtype=np.uint8)

