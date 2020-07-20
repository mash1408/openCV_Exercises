import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.ones((400, 400, 3), dtype = 'uint8')
img.fill(255)

e = img.copy()
# calculating the  center of img
(x, y) = (int(img.shape[1]/2), int(img.shape[0]/2))
startAngle = 0
  
endAngle = 360

circle = cv2.ellipse(e,(x,y),(25,40),0,startAngle,endAngle,(0, 0, 255),3)
''' first argument is image, center position, axislength,startANgle ,EndAngle color and thickness 
'''
cv2.imshow('ELLIPSE', e)
cv2.waitKey(0)
cv2.destroyAllWindows()