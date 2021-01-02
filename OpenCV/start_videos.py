import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
size = (640,480)
out = cv2.VideoWriter('output.avi',fourcc,fps,size)

while (cap.isOpened()):
    ret,frame = cap.read()

    if ret == True:
        #In order to get height and width of frame
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        out.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()
print(width,height)