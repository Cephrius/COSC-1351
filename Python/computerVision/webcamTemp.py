import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read() # read the image data from the capture device
    cv2.imshow("Image",img) # show the image from the capture device
    cv2.waitKey(1) # give the capture device a bit of time to complete before continuing with the next operation on the capture device (delay)