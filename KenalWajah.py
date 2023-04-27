import cv2
import os
import time
from PIL import Image

face_classifier = cv2.CascadeClassifier(
    'Haarcascades/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('Training/trainner.yml')
font_face = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 255)
a = 1


def face_detector(img, num):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        id, conf = recognizer.predict(gray[y:y+h, x:x+w])
        if id == 1:
            name = "Jevon"

        cv2.putText(frame, name, (x+w, y+h), font_face, font_scale, font_color)
        print(x, y, w, h)
        cv2.imwrite("DataSet/User."+str(name)+"." +
                    str(num) + ".jpg", gray[y:y+h, x:x+w])

    return img


cap = cv2.VideoCapture(3)
while True:
    a += 1
    ret, frame = cap.read()
    cv2.imshow('Our Face Extractor', face_detector(frame, a))
    cv2.waitKey(1)
    if a > 24:  # 13 is the Enter Key
        break


cap.release()
cv2.destroyAllWindows()
