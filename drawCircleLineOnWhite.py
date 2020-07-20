import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.ones((400, 400, 3), dtype = 'uint8')
img.fill(255)


(x, y) = (int(img.shape[1]/2), int(img.shape[0]/2))

d = img.copy()

line_1 = cv2.line(d, (50,50), (350,350), (0, 0, 255), 3)

line_ = cv2.line(d, (50,350), (350,50), (0, 0, 255), 3)

rectangle_1 = cv2.rectangle(d,(50, 50), (350, 350), (0, 0, 255), 3)

circle_ = cv2.circle(d, (x,y), (60), (0, 0, 255), 3)

circle_1 = cv2.circle(d, (x,y), (120), (0, 0, 255), 3)

cv2.imshow('combiined', d)
cv2.waitKey(0)
cv2.destroyAllWindows()