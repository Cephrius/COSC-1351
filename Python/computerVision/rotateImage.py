import cv2
from cvzone.Utils import rotateImage  # Import rotateImage function from cvzone.Utils

# initialize the video capture
cap = cv2.VideoCapture(0) # capture video from the webcam

# start the loop to continuously get frames from the webcam
while True:

    # Read a frame from the webcam
    success, img = cap.read() # 'success' will be True if the frame is read successfully, 'img' will be None otherwise

    # Rotate the image by 60 degrees without keeping the original size
    imgRotate60 = rotateImage(img, 60, scale=1, keepSize=False) # Rotate the image by 60 degrees, not keeping the original size

    # Rotate the image by 60 degrees while keeping the original size
    imgRotate60KeepSize = rotateImage(img, 60, scale=1, keepSize=True) # Rotate the image by 60 degrees,  keeping the original size


    # Display the the rotate images
    cv2.imshow("imgRotate60", imgRotate60) # show the 60-degree rotated image without keeping the size
    # cv2.imshow("imageRotate60KeepSize", imgRotate60KeepSize) # show the 60-degree rotated image while keeping the size

    # wait for 1 millisecond between frames
    cv2.waitKey(1)  # Wait for 1 ms, during which any key press can be detected (not being used here)

