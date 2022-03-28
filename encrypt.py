# encryption related functions
import cv2 as cv
from calculation import *
import numpy as np

# bitplane decompostition
# return: a list of 8 bitplane images from MSB to LSB
def bitplane_decomposition(original, height, width):
    ret, bitplane8 = cv.threshold(original, 127, 255, cv.THRESH_BINARY)
    ret, bitplane7 = cv.threshold(original, 127, 255, cv.THRESH_BINARY)
    ret, bitplane6 = cv.threshold(original, 127, 255, cv.THRESH_BINARY)
    ret, bitplane5 = cv.threshold(original, 127, 255, cv.THRESH_BINARY)
    ret, bitplane4 = cv.threshold(original, 127, 255, cv.THRESH_BINARY)
    ret, bitplane3 = cv.threshold(original, 127, 255, cv.THRESH_BINARY)
    ret, bitplane2 = cv.threshold(original, 127, 255, cv.THRESH_BINARY)
    ret, bitplane1 = cv.threshold(original, 127, 255, cv.THRESH_BINARY)
    bitplanes = [bitplane8, bitplane7, bitplane6, bitplane5, bitplane4, bitplane3, bitplane2, bitplane1]

    for a in range(8):
        for i in range(height):
            for j in range(width):
                bin_val = dec_to_bin(original[i,j])
                if str(bin_val)[a] == '1':
                    bitplanes[a][i,j] = 1
                else:
                    bitplanes[a][i,j] = 0
    return np.array(bitplanes)


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