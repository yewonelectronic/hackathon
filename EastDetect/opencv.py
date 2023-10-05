import cv2
capture= cv2.VideoCapture(cv2.CAP_DSHOW+1)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

while cv2.waitKey(33)<0:
    ret,frame=capture.read()
    cv2.imshow("Video Frame",frame)

capture.release()
cv2.destroyAllwindows()