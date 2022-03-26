# general mathematical calculations
import numpy as np
from copy import copy as cpy

# function to convert decimal number to binary
def dec_to_bin(val):
    return str(bin(val).replace("0b", "")).zfill(8)

# function to convert binary number to decimal
def bin_to_dec(val):
    return int(str(val), 2)

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

# convert 1 in a matrix to 255
def convert_to_255(img):
    _img = cpy(img)
    _img[_img==1] = 255
    return _img

# bitplane composition
def bin_to_gray(img, height, width):
    for i in range(height):
        for j in range(width):
            img[i][j] = bin_to_dec(img[i][j])
    return img