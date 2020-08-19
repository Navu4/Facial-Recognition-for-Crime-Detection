import numpy as np 
import cv2

def detect():
    
    facedetect = cv2.CascadeClassifier(r'E:\Python\ML\Criminal Detection using Encoding Technique\haarcascade_frontalface_default.xml')
    #cam = cv2.VideoCapture(0)
    cam = cv2.VideoCapture(r'E:\Python\ML\Criminal Detection using Encoding Technique\testing_video.mp4')
    sampleNum = 0


    while(True):
        ret,img = cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray,1.3,5)

        for(x,y,w,h) in faces:
            sampleNum+=1
            cv2.imwrite('dataset/'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.waitKey(1)
        cv2.imshow('face',img)
        cv2.waitKey(1)
        if(sampleNum>100):
            break

    cam.release()
    cv2.destroyAllWindows()
    
    
detect()   