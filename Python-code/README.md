# Python OpenCV
### This is a demo trained and test on a single video. By changing the Path of the input Training and Testing video's the "LBPHFaceRecognizer" will be able to recognize the faces of the characters in video streams
Task 1: Analyze a 30 second- 1 min video, and capture faces of the people in the same.

Task 2 Analyze another video to see how many of the persons in the first video are seen again in the second video and at what times.

Task 3 if the above technology is used for thousands of videos gathered from hundreds of intelligence sources, with cross-checks across all videos, really significant information on patterns in any form of organized crime can be identified.


### Steps to Run :
- Capturing faces from the training video using haarcascode_frontalface_default.xml.

face_detection.py

- Created the 128-d embeddings i.e. Feature Vectors for each face in the dataset and stored it in eci.picke file.

Encoding_dataset_into_different_folders.py

-Then cluster the images by comparing the Feature Vectors into different folders using "DBSCAN clustering".

final_encoding.py

- Train the model "LBPHFaceRecognizer" using the labelled images that we clustered in previous step.

Face_Recog_Train_CR.py

- Using "LBPHFaceRecognizer", recognize the faces of the characters in video streams.

Face_Recog_Test_CR.py
