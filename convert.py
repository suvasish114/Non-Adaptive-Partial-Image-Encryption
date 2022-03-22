import cv2

def bgr_to_rgb(img):
    b,g,r = cv2.split(img)
    return cv2.merge([r,g,b])

def dec_to_bin(val):
    return str(bin(val).replace("0b", "")).zfill(8)

def bin_to_dec(val):
    return int(val, 2)