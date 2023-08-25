import cv2 as cv
import cv2 as cv
import numpy as np
img = cv.imread('P2 Nâng Cao/co viet nam.jpg')
window_name = 'show_img'
cv.namedWindow(window_name, cv.WINDOW_NORMAL)

cv.imshow('show_img', img)
cv.waitKey(0)
