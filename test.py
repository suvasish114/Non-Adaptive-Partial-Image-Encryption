# testing
from calculation import *
import numpy as np

x = 0.78
y = 0.98
if __name__ == '__main__':
    x1 = x
    y1 = y
    a = 0
    # for i in range(100):
    #     a += 1
    #     x,y,rand = PRBG(x,y)
    #     print('{} {}'.format(x,y))
    #     print('{}'.format(rand), end=' ')
    #     if a%4 == 0:
    #         print(' ', end='')
    #     if a == 32:
    #         a = 0
    #         print()
    # print()

    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(horizontal_adj(mat,3,3))

    
