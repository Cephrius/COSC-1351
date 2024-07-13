import cv2
import cvzone

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read() # read the image data from the capture device


    #cv2.rectangle(img,(200,200),(500,400),(255,0,255),3)

    cvzone.cornerRect(img,(200,200,300,400),
                         l=30, t=5, rt=1,
                        colorR=(255, 0, 255), colorC = (0, 255, 0)
                      )

    cv2.imshow("Image",img) # show the image from the capture device
    cv2.waitKey(1) # give the capture device a bit of time to complete before continuing with the next operation on the capture device (delay)