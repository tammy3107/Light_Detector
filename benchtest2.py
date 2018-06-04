import cv2 
import numpy as np

port = 1
bg = cv2.createBackgroundSubtractorMOG2()
camera = cv2.VideoCapture(port)
while (camera.isOpened()):
	ret, img= camera.read()
	if ret:
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edge = cv2.Canny(gray,50,150,apertureSize=3)
	edge = cv2.GaussianBlur(gray,(5,5),0)
	ret, thresh = cv2.threshold(edge,225,255,cv2.THRESH_BINARY)
	thresh = cv2.erode(thresh,None,iterations=8)
	thresh = cv2.dilate(thresh,None,iterations=8)
	#bgmask = bg.apply(thresh)
	image,contours,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	#contours = 
	#bgmask = cv2.GaussianBlur(bgmask,(5,5),0)
	for cnt in contours:
	    if not (cv2.isContourConvex(cnt)):
		    hull = cv2.convexHull(cnt)
		    cv2.drawContours(img,[hull],-1,(0,255,0),2)
	cv2.imshow("test",img)
	k = cv2.waitKey(1)
	if k==27:
		break