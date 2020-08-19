{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import os\n",
    "import numpy as np\n",
    "\n",
    "def faceDetection(test_img):\n",
    "    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)#convert color image to grayscale\n",
    "    face_haar_cascade=cv2.CascadeClassifier(r'E:\\Python\\ML\\Criminal Detection using Encoding Technique\\haarcascade_frontalface_default.xml')#Load haar classifier\n",
    "    faces=face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbors=5)#detectMultiScale returns rectangles\n",
    "\n",
    "    return faces,gray_img\n",
    "\n",
    "def labels_for_training_data(directory):\n",
    "    faces=[]\n",
    "    faceID=[]\n",
    "\n",
    "    for path,subdirnames,filenames in os.walk('E:\\Python\\ML\\Criminal Detection using Encoding Technique\\data'):\n",
    "        for filename in filenames:\n",
    "            if filename.startswith(\".\"):\n",
    "                print(\"Skipping system file\")#Skipping files that startwith .\n",
    "                continue\n",
    "\n",
    "            id=os.path.basename(path)#fetching subdirectory names\n",
    "            img_path=os.path.join(path,filename)#fetching image path\n",
    "            print(\"img_path:\",img_path)\n",
    "            print(\"id:\",id)\n",
    "            test_img=cv2.imread(img_path)#loading each image one by one\n",
    "            if test_img is None:\n",
    "                print(\"Image not loaded properly\")\n",
    "                continue\n",
    "            faces_rect,gray_img=faceDetection(test_img)#Calling faceDetection function to return faces detected in particular image\n",
    "            if len(faces_rect)!=1:\n",
    "                continue #Since we are assuming only single person images are being fed to classifier\n",
    "            (x,y,w,h)=faces_rect[0]\n",
    "            roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from grayscale image\n",
    "            faces.append(roi_gray)\n",
    "            faceID.append(int(id[-1]))\n",
    "    return faces,faceID\n",
    "\n",
    "def train_classifier(faces,faceID):\n",
    "    face_recognizer=cv2.face.LBPHFaceRecognizer_create()\n",
    "    face_recognizer.train(faces,np.array(faceID))\n",
    "    return face_recognizer\n",
    "\n",
    "\n",
    "faces,faceID=labels_for_training_data('E:\\Python\\ML\\Criminal Detection using Encoding Technique\\data')\n",
    "face_recognizer=train_classifier(faces,faceID)\n",
    "face_recognizer.write('trainingData2.yml')"
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
