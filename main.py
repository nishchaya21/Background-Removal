import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
segmentor = SelfiSegmentation(1)
fpsReader = cvzone.FPS()
# imgBg = cv2.imread('Images/1.jpg')
listImg = os.listdir("Images")
print(listImg)
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'Images/{imgPath}')
    imgList.append(img)
print(len(imgList))
indexImg = 0
while True:
    success, img = cap.read()
    # imgOut = segmentor.removeBG(img, (255,0,0), threshold = 0.8)      # colour background
    # imgOut = segmentor.removeBG(img, imgBg, threshold = 0.8)      # single image background
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold = 0.8)    # multiple colour backgrounds
    imgStack = cvzone.stackImages([img,imgOut], 2, 1)
    _, imgStack = fpsReader.update(imgStack)
    print(indexImg)
    cv2.imshow("Image", imgStack)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(imgList)-1:
            indexImg += 1
    elif key == ord('q'):
        break