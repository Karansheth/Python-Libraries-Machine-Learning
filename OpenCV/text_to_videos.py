import cv2
import numpy as np
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,3000)
cap.set(4,3000)

print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        mydate = str(datetime.datetime.now())
        frame = cv2.putText(frame,mydate,(10,50),font,2,(0,255,0),2,cv2.LINE_AA)
        cv2.imshow('Frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()