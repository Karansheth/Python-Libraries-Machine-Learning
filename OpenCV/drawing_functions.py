import numpy as np
import cv2

#img = cv2.imread('lena.jpg',1)
img = np.zeros([512,512,3],np.uint8)

img = cv2.line(img,(0,0),(255,255),(0,0,255),4)
img = cv2.arrowedLine(img,(0,255),(255,255),(0,0,255),4)
img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),4)
img = cv2.circle(img,(447,63),63,(255,0,0),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV',(10,500),font,4,(0,255,255),5,cv2.LINE_AA)

cv2.imshow('Image-Frame',img)
cv2.waitKey(0)
cv2.destroyAllWindows()