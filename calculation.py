# general mathematical calculations
import numpy as np
from copy import copy as cpy

u = 3.57

# function to convert decimal number to binary
def dec_to_bin(val):
    return str(bin(val).replace("0b", "")).zfill(8)

# function to convert binary number to decimal
def bin_to_dec(val):
    return int(str(val), 2)

# function to generate random number using arnold cat map formula
def arnold_cat_map(u, a):
    return u*a*(1-a)

'''
pseudo random number generator
param:
    x: float
        initial value of x
    y: float
        initial value of y
return:
    x: float
        next value of x
    y: float
        next value of y
    number: int
        a random number between 1 and 0
'''
def PRBG(x, y):
    x1 = float("{:.2f}".format(u*x*(1-x)))
    y1 = float("{:.2f}".format(u*y*(1-y)))
    if x1>=y1:
        return x1,y1,1
    else:
        return x1,y1,0

'''
Param
    x: float
        a value in float to generate random number
    y: float
        a value in float to generate random number
    height: int
        pixel height of the original image
    width: int
        pixel width of the original image
Return
    x: float
        last generated value of x
    y: float
        last generated value of y
    final: list of list
        random 2D binary matrix
'''
def get_random_matrix(x, y, height, width):
    final = []
    for i in range(height):
        temp = []
        for j in range(width):
            x,y,n = PRBG(x, y)
            temp.append(n)
        final.append(temp)
    return x,y,np.array(final, dtype=np.uint8)

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

# matrix xor
def xor_matrix(mat1, mat2):
    return np.bitwise_xor(mat1, mat2)


def horizontal_adj(img, height, width):
    for i in range(height):
        for j in range(width-1):
            img[i][j] = img[i][j+1]
        if i!=height-1:
            img[i][width-1]=img[i+1][0]
    img[height-1][width-1]=0
    return np.array(img, dtype=np.uint8)


'''
calculate entropy of the given image
'''
def entropy(pic):
    p =np.array([(pic--v).sum() for v in range (256)])
    p= p/p.sum()
    #compute e= -sum(p(si)*log2(p(si))
    e=-(p*np.log2(p)).sum()
    return e
