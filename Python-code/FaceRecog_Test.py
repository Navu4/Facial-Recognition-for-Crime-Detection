import cv2
import numpy as np 


facedetect =cv2.CascadeClassifier(r'E:\Python\ML\Criminal Detection using Encoding Technique\haarcascade_frontalface_default.xml')#Load haar classifier

# facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


rec = cv2.face.LBPHFaceRecognizer_create()
rec.read('trainingData2.yml')


fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (0,0,255)


cam = cv2.VideoCapture(r'E:\Python\ML\Criminal Detection using Encoding Technique\testing_video.mp4')

length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))

while(length):
	ret,img = cam.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = facedetect.detectMultiScale(gray,1.3,5)
	length = length - 1
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		id,conf = rec.predict(gray[y:y+h,x:x+w])
		cv2.putText(img,str(id),(x,y+h),fontFace,fontScale,fontColor)

		#cv2.putText(img,str(id)+'_'+str(conf),(x,y+h),fontFace,fontScale,fontColor)

	cv2.imshow("face",img)
	if(cv2.waitKey(1)==ord('q')):
		break

cam.release()
cv2.destroyAllWindows()
