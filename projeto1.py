import cv2
import numpy as np

frameWidth = 640
frameHeigth = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeigth)
cap.set(10, 130)

myColors = [[169, 179, 147, 255, 98, 255], [0, 125, 174, 255, 127, 255]]
myColorsValues =[[0,0,255],[255,0,0]]


def getContours(img):
    conturs, hieranchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in conturs:
        area = cv2.contourArea(cnt)
        if area > 300:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            permiter = cv2.arcLength(cnt, True)
            aprox = cv2.approxPolyDP(cnt, 0.02 * permiter, True)
            x, y, w, h = cv2.boundingRect(aprox)
    return x + w // 2, y


def findColor(img, myColors, myColorsValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    for color in myColors:
        lower = np.array([color[0], color[2], color[4]])
        upper = np.array([color[1], color[3], color[5]])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorsValues[count], cv2.FILLED)
        count+=1
        # cv2.imshow(str(color[0]), mask)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    findColor(img, myColors, myColorsValues)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
