# register.py
import cv2
from facerec import detect_faces

def registerCriminal(img, path, img_num):
    size = 2
    (im_width, im_height) = (112, 92)
    file_num = 2*img_num - 1

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detect_faces(gray)

    if(len(faces) > 0):
        # Taking the largest face detected
        faces = sorted(faces, key=lambda x: x[3], reverse=True)  # sort based on height of image
        face_i = faces[0]
        (x, y, w, h) = [v * size for v in face_i]

        face = gray[y:y + h, x:x + w]
        face = cv2.resize(face, (im_width, im_height))

        print("Saving training sample " + str(img_num)+".1")
        # Save image file
        cv2.imwrite('%s/%s.png' % (path, file_num), face)
        file_num += 1

        # Save flipped image
        print("Saving training sample " + str(img_num)+".2")
        face = cv2.flip(face, 1, 0)
        cv2.imwrite('%s/%s.png' % (path, file_num), face)

    else:
        # No face present
        print("img %d : Face is not present" % (img_num))
        return img_num

    return None