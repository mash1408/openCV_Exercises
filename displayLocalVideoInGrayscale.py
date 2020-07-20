
# openCV code that scans .mp4 files in the trpository or root dir 
# and plays the video file in grayscale mode
# untested on windows OS 
import cv2
import glob

videosPath=glob.glob("*.mp4")
print("Videos in your current directory :")

for videoName in videosPath :
    print(videoName)

getVideo=int(input("Select video number"))
print("Selecting Video :"+videosPath[getVideo-1])


video = cv2.VideoCapture('piper.mp4')
''' Cv2 has function VideoCapture which Capture video from Camera
    Argument Zero(0) means Capture from Laptop 
    
    Here I am running a True Loop which means Capture till Video is there 
'''

while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (800, 400))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('video', gray)
    cv2.waitKey(1)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()