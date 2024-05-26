import cv2
# from final_encoding import *

def detect(path):
    facedetect = cv2.CascadeClassifier(r'C:\Users\hp\Documents\GitHub\Face-Recognition-For-Criminal-Detection-GUi\haarcascade_frontalface_default.xml')
    #cam = cv2.VideoCapture(0)
    cam = cv2.VideoCapture(path)
    sampleNum = 0
   
    while sampleNum <= 100:
        ret, img = cam.read()
        if not ret:
            break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

     for (x, y, w, h) in faces:
            sampleNum += 1
            cv2.imwrite(f'dataset/{sampleNum}.jpg', gray[y:y+h, x:x+w])
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if sampleNum > 100:
                break

    cv2.imshow('face', img)
        if cv2.waitKey(1) & 0xFF == ord('q') or sampleNum > 100:
            break
    cam.release()
    cv2.destroyAllWindows()
