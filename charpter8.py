import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getContours(img):
    conturs, hieranchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in conturs:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 500:
            cv2.drawContours(imgConturs, cnt, -1, (255, 0, 0), 3)
            permiter = cv2.arcLength(cnt, True)
            # print(permiter)
            aprox = cv2.approxPolyDP(cnt, 0.02 * permiter, True)
            # print(len(aprox))
            objectCorner = len(aprox)
            x, y, w, h = cv2.boundingRect(aprox)

            if objectCorner == 3:
                objectType = "Try"
            elif objectCorner == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05: objectType = "Square"
                else: objectType = "Rectangle"
            elif objectCorner > 4: objectType = "Circle";
            else:
                objectType = "None"

            cv2.rectangle(imgConturs, (x, y), (x + w, y + h), (0, 255, 0))
            cv2.putText(imgConturs, objectType,
                        (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0, 0, 0), 2)


img = cv2.imread("Resources/shapes.png")
imgConturs = img.copy()
imgBlank = np.zeros_like(img)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCany = cv2.Canny(imgBlur, 50, 50)

getContours(imgCany)

imgStack = stackImages(0.8, ([img, imgGray, imgBlur], [imgCany, imgConturs, imgBlank]))
cv2.imshow("Output", imgStack)

cv2.waitKey(0)
