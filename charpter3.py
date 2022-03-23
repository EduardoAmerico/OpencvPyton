import cv2

img = cv2.imread("Resources/carro.jpg")
print(img.shape)

imgResize = cv2.resize(img,(512,341))
print(imgResize.shape)

imgCrop = img[200:683, 250:850]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Crop", imgCrop)
cv2.waitKey(0)
