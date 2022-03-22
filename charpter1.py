import cv2

# Imagem Import
# print("Packge imported!")
#
# img = cv2.imread("Resources/Lenna.png")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# Video Import

cap = cv2.VideoCapture("Resources/VideoTeste.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
