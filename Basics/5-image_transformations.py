import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Kedi', img)

def translate(img, x, y):
    transmat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, transmat, dimensions) # Görüntüye dönüşümler uygular, görüntü, dönüştürme yapabilmek için affiin matrisi, çıkış boyutu parametrelerini alır.

translated = translate(img, -50, 50)
cv.imshow('Translated', translated)

def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # Döndürme işlemi için kullanılacak affin matrisi oluşturur, döndürme noktası, döndürme açısı, ölçek parametrelerini alır. 
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions) # Affin matrisi ile görüntüyü döndürür, görüntü, affin matrisi, çıkış boyutlarını parametre olarakk alır.

rotated = rotate(img, 45)
cv.imshow('Döndürülmüş', rotated)

flip = cv.flip(img, -1) # Görüntüyü belirli bir eksen etrafında çevirmeyi sağlar, görüntü, çevirme kodu parametrelerini alır.
cv.imshow('Flip', flip)


cv.waitKey(0)