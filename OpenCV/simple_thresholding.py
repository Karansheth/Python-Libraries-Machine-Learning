import numpy as np
import cv2

img = cv2.imread('gradient.png',0)

ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret2,th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret3,th3 = cv2.threshold(img,200,255,cv2.THRESH_TRUNC) #Here value of original image will remain same till 200 but if greater than that it would become 200 itself
ret4,th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO) #Here value will change to 0 if it is less than 127 but if bigger than that than it will remain same
ret5,th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('Image',img)
cv2.imshow('Binary Threshold',th1)
cv2.imshow('Binary Threshold Inverse',th2)
cv2.imshow('Trunc Threshold',th3)
cv2.imshow('Threshold to Zero',th4)
cv2.imshow('Threshold to Zero Inverse',th5)

cv2.waitKey(0)
cv2.destroyAllWindows()