import numpy as np
import cv2

img = cv2.imread('lena.jpg',-1)
#0 - Grayscale
#1 - RGB channel
#-1 - Alpha channel


cv2.imshow('Frame-1',img)
k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k == ord('f'):
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()