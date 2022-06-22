# encryption related functions

import cv2 as cv
from conversion import *
import numpy as np

class Encryption:
    def __init__(self):
        pass

    def bitplane_decomposition(self, original, height, width):          # bitplane decomposition from the original image
        bitplanes = []
        for i in range(8):
            ret, bitplane = cv.threshold(original, 127, 255, cv.THRESH_BINARY)
            bitplanes.append(bitplane)

        for i in range(8):
            for a in range(height):
                for b in range(width):
                    bin_val = dec_to_bin(original[a][b])
                    if str(bin_val)[i] == '1':
                        bitplanes[i][a][b] = 1
                    else:
                        bitplanes[i][a][b] = 0
        return np.array(bitplanes, dtype=np.uint8)

# compose image from bitplane images and cipher images
def cipher_image_composition(bitplane_images, height, width):
    final = []

    # combining process
    for i in range(7):
        if i==0:
            for j in range(height):
                temp = []
                for k in range(width):
                    temp.append(int(str(bitplane_images[i][j][k])+str(bitplane_images[i+1][j][k])))
                final.append(temp)
        else:
            for j in range(height):
                temp = []
                for k in range(width):
                    temp.append(int(str(final[j][k])+str(bitplane_images[i+1][j][k])))
                final[j] = temp

    # converting binary pixels to decimal
    for i in range(height):
        for j in range(width):
            final[i][j] = bin_to_dec(final[i][j])
    return np.array(final, dtype=np.uint8)