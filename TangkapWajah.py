import cv2
import time

face_classifier = cv2.CascadeClassifier(
    'Haarcascades/haarcascade_frontalface_default.xml')
id = input("Masukkan ID : ")
a = 1


def face_detector(img, num):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img

    for (x, y, w, h) in faces:
        print(x, y, w, h)
        cv2.imwrite("DataSet/User."+str(id)+"." +
                    str(num) + ".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

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
