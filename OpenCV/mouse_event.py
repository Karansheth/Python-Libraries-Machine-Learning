import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorimg = np.zeros((512,512,3),np.uint8)
        mycolorimg[:] = [blue,green,red] 
        cv2.imshow('Color',mycolorimg)

        #cv2.circle(img,(x,y),3,(0,0,255),-1)
        #points.append((x,y))
        #if len(points)>=2:
            #cv2.line(img,points[-1],points[-2],(255,0,0),5)
        #cv2.imshow('Image',img)

        #print(x,', ',y)
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #strxy = str(x) + ', ' + str(y)
        #cv2.putText(img,strxy,(x,y),font,1,(255,255,0),2)
        #cv2.imshow('Image',img)

    """
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img,strBGR,(x,y),font,1,(0,255,255),2)
        cv2.imshow('Image',img)
    """
#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('lena.jpg',-1)
points = []
cv2.imshow('Image',img)
cv2.setMouseCallback('Image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()