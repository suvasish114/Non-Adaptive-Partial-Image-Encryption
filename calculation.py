# general mathematical calculations
import numpy as np
import cv2 as cv

# function to convert decimal number to binary
def dec_to_bin(val):
    return str(bin(val).replace("0b", "")).zfill(8)

# function to convert binary number to decimal
def bin_to_dec(val):
    return int(val, 2)

# function to generate random number using arnold cat map formula
def arnold_cat_map(u, a):
    return u*a*(1-a)

# function to get random matrix using arnold cat map formula
def get_random_matrix(u, a, b, row, column):
    mat = []
    x = a
    y = b
    for i in range(row):
        temp = []
        for j in range(column):
            if x>y:
                temp.append(1)
            else:
                temp.append(0)
            x = arnold_cat_map(u, x)
            y = arnold_cat_map(u, y)
        mat.append(temp)
    return x,y,mat

# XOR two matrix
def xor_matrix(matrix1, matrix2):
    return np.bitwise_xor(matrix1, matrix2)

# bitplane decompostition
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

    return bitplane8, bitplane7, bitplane6, bitplane5, bitplane4, bitplane3, bitplane2, bitplane1

# bitplane composition
def bitplane_composition(bitplanes, height, width):
    pass