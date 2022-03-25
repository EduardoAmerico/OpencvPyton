import cv2
import numpy as np

img = cv2.imread("Resources/Lenna.png")

hor = np.hstack((img,img))
ver = np.vstack((img,img))

cv2.imshow("horizontal", hor)
cv2.imshow("vertical", ver)
cv2.waitKey(0)

