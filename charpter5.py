import numpy as np

import cv2

img = cv2.imread("Resources/cartas2.jpg")

width, heigth = 250, 350
pts1 = np.float32([[342, 83], [548, 106], [291, 313], [515, 344]])
pts2 = np.float32([[0, 0], [width, 0], [0, heigth], [width, heigth]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, heigth))
# 343,79 291,313 548,106 515,344
cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)
