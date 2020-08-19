{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np \n",
    "\n",
    "facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')\n",
    "rec = cv2.face.LBPHFaceRecognizer_create()\n",
    "rec.read('trainingData2.yml')\n",
    "\n",
    "\n",
    "fontFace = cv2.FONT_HERSHEY_SIMPLEX\n",
    "fontScale = 1\n",
    "fontColor = (0,0,255)\n",
    "\n",
    "\n",
    "cam = cv2.VideoCapture(r'E:\\Python\\ML\\testing_video.mp4')\n",
    "\n",
    "while(True):\n",
    "\tret,img = cam.read()\n",
    "\tgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)\n",
    "\tfaces = facedetect.detectMultiScale(gray,1.3,5)\n",
    "\n",
    "\tfor(x,y,w,h) in faces:\n",
    "\t\tcv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)\n",
    "\t\tid,conf = rec.predict(gray[y:y+h,x:x+w])\n",
    "\t\tcv2.putText(img,str(id),(x,y+h),fontFace,fontScale,fontColor)\n",
    "\n",
    "\t\t#cv2.putText(img,str(id)+'_'+str(conf),(x,y+h),fontFace,fontScale,fontColor)\n",
    "\n",
    "\tcv2.imshow(\"face\",img)\n",
    "\tif(cv2.waitKey(1)==ord('q')):\n",
    "\t\tbreak\n",
    "\n",
    "cam.release()\n",
    "cv2.destroyAllWindows()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
