from math import log10, sqrt
import numpy as np

class Measurement:
    def __init__(init):
        pass 

    def MSE(self, original, compressed, size):
        a = abs(np.subtract(original,compressed))
        b = 0
        for i in a:
            for j in i:
                b += (j**2)
        return b/(size[0]*size[1])
        # a = 0
        # for i in range(height-1):
        #     for j in range(width-1):
        #         a += ((compressed[i][j] - original[i][j])**2)
        # mse = a / (height*width)
        # return np.mean((original - compressed) ** 2)
    
    def PSNR(self, original, compressed, mse):
        # mse = np.mean((original - compressed) ** 2)
        if(mse == 0):   # MSE is zero means no noise is present in the signal .
            return 100
        max_pixel = 255.0
        psnr = 20 * log10(max_pixel / sqrt(mse))
        return psnr

    def NPCR():
        pass

    def UACI():
        pass

    def corr2(self, a,b):
        ''' Correlation coefficient between two pixels '''
        x = np.sum(a) / np.size(a)
        y = np.sum(b) / np.size(b)
        a = a - x
        b = b - y

        r = (a*b).sum() / sqrt((a*a).sum() * (b*b).sum());
        return r