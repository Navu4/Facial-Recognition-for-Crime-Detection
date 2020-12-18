# Python OpenCV
### This is a demo trained and test on a single video. By changing the Path of the input Training and Testing video's the "LBPHFaceRecognizer" will be able to recognize the faces of the characters in video streams
Task 1: Analyze a 30 second- 1 min video, and capture faces of the people in the same.

Task 2 Analyze another video to see how many of the persons in the first video are seen again in the second video and at what times.

Task 3 if the above technology is used for thousands of videos gathered from hundreds of intelligence sources, with cross-checks across all videos, really significant information on patterns in any form of organized crime can be identified.


### Steps to Run :
- Capturing faces from the training video using haarcascode_frontalface_default.xml.
> [Face Detection](https://github.com/Navu4/Facial-Recognition-for-Crime-Detection/blob/master/Python-code/face_detection.py) 

- Created the 128-d embeddings i.e. Feature Vectors for each face in the dataset and stored it in eci.picke file.
> [Encoding_dataset_into_different_folders](https://github.com/Navu4/Facial-Recognition-for-Crime-Detection/blob/master/Python-code/Encoding_dataset_into_different_folders.py)

- Then cluster the images by comparing the Feature Vectors into different folders using "DBSCAN clustering".
> [Encoding](https://github.com/Navu4/Facial-Recognition-for-Crime-Detection/blob/master/Python-code/final_encoding.py)

- Train the model "LBPHFaceRecognizer" using the labelled images that we clustered in previous step.

> [Face Recog Train](https://github.com/Navu4/Facial-Recognition-for-Crime-Detection/blob/master/Python-code/FaceRecog_Train.py)

- Using "LBPHFaceRecognizer", recognize the faces of the characters in video streams.
> [Face Recog Test](https://github.com/Navu4/Facial-Recognition-for-Crime-Detection/blob/master/Python-code/FaceRecog_Test.py)
