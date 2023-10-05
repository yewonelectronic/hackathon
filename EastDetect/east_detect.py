import cv2
import numpy as np
from imutils.object_detection import non_max_suppression
import pytesseract
from PIL import Image, ImageOps

min_confidence = 0.5
'''file_name = "noexam.jpg"'''

east_decorator = 'frozen_east_text_detection.pb'

frame_size = 320
padding = 0.05

def textROI(image):
    # load the input image and grab the image dimensions
    orig = image.copy()
    (origH, origW) = image.shape[:2]
 
    # 자동차 이미지를 잘라오게 되면 자동차의 크기에 따라 이미지의 사이즈가 달라지기 때문에(정사각형이 아니기 때문에) 
    # 번호판 글씨가 왜곡(늘려지거나 줄여지는 현상)될 수 있다(번호판은 차의 중앙에 있다)
    # 그러므로 늘리거나 줄임없이 정사각형 이미지로(320x320) 잘라내기 위해 다음 작업을 실행한다.
    rW = origW / float(frame_size)
    rH = origH / float(frame_size)
    newW = int(origW / rH)
    center = int(newW / 2)
    start = center - int(frame_size / 2)

    # resize the image and grab the new image dimensions
    image = cv2.resize(image, (newW, frame_size))  
    scale_image = image[0:frame_size, start:start+frame_size]
    (H, W) = scale_image.shape[:2]

    
    cv2.imshow("orig", orig)
    #cv2.imshow("resize", image)
    #cv2.imshow("scale_image", scale_image)
    
    # define the two output layer names for the EAST detector model 
    layerNames = [
            "feature_fusion/Conv_7/Sigmoid",
            "feature_fusion/concat_3"]
    
    # load the pre-trained EAST text detector
    net = cv2.dnn.readNet(east_decorator)

    # construct a blob from the image 
    blob = cv2.dnn.blobFromImage(image, 1.0, (frame_size, frame_size),
            (123.68, 116.78, 103.94), swapRB=True, crop=False)
    net.setInput(blob)
    (scores, geometry) = net.forward(layerNames)

    (numRows, numCols) = scores.shape[2:4]
    rects = []
    confidences = []

    # loop over the number of rows
    for y in range(0, numRows):
        # extract the scores (probabilities)
        scoresData = scores[0, 0, y]
        xData0 = geometry[0, 0, y]
        xData1 = geometry[0, 1, y]
        xData2 = geometry[0, 2, y]
        xData3 = geometry[0, 3, y]
        anglesData = geometry[0, 4, y]

        # loop over the number of columns
        for x in range(0, numCols):

                if scoresData[x] < min_confidence:
                        continue

                (offsetX, offsetY) = (x * 4.0, y * 4.0)

                angle = anglesData[x]
                cos = np.cos(angle)
                sin = np.sin(angle)

                h = xData0[x] + xData2[x]
                w = xData1[x] + xData3[x]

                endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
                endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
                startX = int(endX - w)
                startY = int(endY - h)

                rects.append((startX, startY, endX, endY))
                confidences.append(scoresData[x])
    
    # apply non-maxima suppression 
    boxes = non_max_suppression(np.array(rects), probs=confidences)

    # initialize the list of results
    results = []

    # loop over the bounding boxes
    for (startX, startY, endX, endY) in boxes:

            startX = int(startX * rW)
            startY = int(startY * rH)
            endX = int(endX * rW)
            endY = int(endY * rH)

            dX = int((endX - startX) * padding)
            dY = int((endY - startY) * padding)

            startX = max(0, startX - dX)
            startY = max(0, startY - dY)
            endX = min(origW, endX + (dX * 2))
            endY = min(origH, endY + (dY * 2))

            # extract the actual padded ROI
            return ([startX, startY, endX, endY], orig[startY:endY, startX:endX])


CAM_ID = 0
def capture(camid = CAM_ID):

    cam= cv2.VideoCapture(cv2.CAP_DSHOW+1)

    if cam.isOpened() == False:
        print ('cant open the cam (%d)' % camid)
        return None

    ret, frame = cam.read()
    if frame is None:
        print ('frame is not exist')
        return None

    # png로 압축 없이 영상 저장 
    cv2.imwrite('example.jpg',frame, params=[cv2.IMWRITE_PNG_COMPRESSION,0])

#이미지 저장
    cam.release()
    
capture()
img = cv2.imread('example.jpg')        
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
#size = (224, 224)
#img = ImageOps.fit(img, size, Image.ANTIALIAS)
    #cv2.imwrite('save_image.jpg', src)

    # display the resized image
#cv2.imshow("img",img)
'''img=cv2.imread(file_name)'''
# Loading image
img_copy=img.copy()
([startX,startY,endX,endY], text_image) = textROI(img)
cv2.imshow('plate_img',text_image)#가장 중요함!

##############색깔인식 시작 ver1Z
img_hsv = cv2.cvtColor(text_image, cv2.COLOR_BGR2HSV) # cvtColor 함수를 이용하여 hsv 색공간으로 변환

lower_blue = (80, 60, 60) # hsv 이미지에서 바이너리 이미지로 생성 , 적당한 값 30
upper_blue = (140, 250, 250)
elec_range = cv2.inRange(img_hsv, lower_blue, upper_blue) # 범위내의 픽셀들은 흰색, 나머지 검은색
elec_image = cv2.imshow('electronic_license_plate', elec_range)
################# ver2
#elec_range = cv2.inRange(text_image, (80, 60, 60), (130, 200, 200)) # 전기자동차 번호판 색상 인식 픽셀 범위 설정(하이퍼 파라미터)
#elec_image = cv2.imshow('electronic_license_plate', elec_range)

cv2.waitKey(0)

isElectronic = 0 
notElectronic = 0

for y in range(endY-startY):
    for x in range(endX-startX):
        if elec_range[y, x] >= 50: # 픽셀 값이 1 이상이면 전기차로 가정
            isElectronic += 1
        else:
            notElectronic += 1
                                  
print(isElectronic, notElectronic)
            
if 3*isElectronic >= notElectronic: # 10배(하이퍼 파라미터) 이상 차이가 나면 전기자동차로 인식
    print("전기 자동차가 검출되었습니다.")

else:
    print("전기 자동차가 아닙니다.")
cv2.waitKey(0)   
cv2.destroyAllWindows()
