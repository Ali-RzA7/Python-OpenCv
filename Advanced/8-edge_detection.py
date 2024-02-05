import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Kedi', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


lap = cv.Laplacian(gray, cv.CV_64F) # Gri tonlamalı görüntü üzerindeki kontrast değişikliklerini tespit eder, görüntü, hesaplama sırasında kullanılacak veri tipi parametrelerini alır.
lap = np.uint8(np.absolute(lap)) # Görüntünün piksel değerlerini mutlak değer alarak sıfırdan farklı ve pozitif hale getirilir.
cv.imshow('Laplacian', lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # Gri tonlamalı görüntü üzerindeki kenarları ve gradyanları tespit etmeye yardımcı olur, görüntü, veri tipi, x yönündeki derece, y yönündeki derece parametrelerini alır.
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)