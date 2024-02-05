import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('C:/Users/user/Desktop/npyt/Faces/haar_face.xml')

people = ['Ben Afflek', 'Jerry Seinfield']
features = np.load('C:/Users/user/Desktop/npyt/features.npy', allow_pickle=True)
labels = np.load('C:/Users/user/Desktop/npyt/labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read('C:/Users/user/Desktop/npyt/face_trained.yml')

img = cv.imread('C:/Users/user/Desktop/npyt/Faces_val/jerrY_seinfield/1 (3).jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Etiket = {people[label]} oranı {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Person', img)

cv.waitKey(0)