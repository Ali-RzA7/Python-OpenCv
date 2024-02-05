import cv2 as cv

img = cv.imread('Photos/group 2.jpg')
cv.imshow('İnsanlar', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gri', gray)

haar_cascade = cv.CascadeClassifier('C:/Users/user/Desktop/npyt/Faces/haar_face.xml') # Önceden eğitilmiş Haar Cascade dosyalarını yüklemek için kullanılır.

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6) # Gri tonlamalı bir görüntüde belirli nesneleri tespit eder ve bu nesnelerin dikdörtgen koordinatlarını döndürür, görüntü, nesne boyut ölçeği, komşu dikdörtgenlerin sayısı parametrelerini alır. 

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Yüz', img)
cv.waitKey(0)