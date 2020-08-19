
import pickle
import cv2
import numpy as np
from sklearn.cluster import DBSCAN
from imutils import build_montages
import os
from tqdm import tqdm


data = pickle.loads(open("enc.picke", "rb").read())
data=np.array(data)

encodings=[d['encodings'] for d in data]

clt = DBSCAN(metric="euclidean", n_jobs=-1)
clt.fit(encodings)

clt.labels_

labelIDs = np.unique(clt.labels_)
labelIDs

numUniqueFaces=len(np.where(labelIDs>-1)[0])

print("unique faces: {}".format(numUniqueFaces))


for labelID in tqdm(labelIDs):
    #print(labelID)
    idxs = np.where(clt.labels_ == labelID)[0]
    idxs = np.random.choice(idxs, size=min(25, len(idxs)),replace=False)
    faces = []
    path=r'face_samples/id'+str(labelID)
    if not os.path.exists(path):
        os.makedirs(path)
    for i in idxs:
        img=cv2.imread(data[i]["imgpath"])
        #(top, right, bottom, left) = data[i]["box"]
        #face = img[top:bottom, left:right]
        #face = cv2.resize(face, (96, 96))
        #faces.append(img)
        cv2.imwrite(path+"/"+str(i)+".jpeg",img)
    
    
#     montage = build_montages(faces, (96, 96), (5, 5))[0]
#     title = "Face ID #{}".format(labelID)
#     title = "Unknown Faces" if labelID == -1 else title
#     cv2.imshow(title, montage)
#     cv2.waitKey(0)