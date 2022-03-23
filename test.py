# testing
from calculation import *
import numpy as np

u = 3.57
x = 0.78
y = 0.98

if __name__ == '__main__':
    x,y,mat1 = get_random_matrix(u,x,y,4,4)
    x,y,mat2 = get_random_matrix(u,x,y,4,4)
    print(mat1)
    print(mat2)
    print(xor_matrix(mat1, mat2))
    