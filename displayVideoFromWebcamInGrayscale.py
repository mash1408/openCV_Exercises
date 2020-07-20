# script in openCV to open webcam and render facetime in grayscale mode
import cv2

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (800, 400))
    # convert each frame to grayscale
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', gray)
    cv2.waitKey(1)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()