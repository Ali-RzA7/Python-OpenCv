import cv2 as cv
import numpy as np


img = cv.imread('Photos/cat.jpg')
cv.imshow('Kedi', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gri', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 50, 175)
cv.imshow('Kenar', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # Kenarları tespit edilmiş görüntüdeki bir nesnenin dış hatlarını bulmayı sağlar, görüntü, nesnenin dış hatlarını bulma modu, nesnenin dış hatlarına yaklaşım metodu parametrelerini alır.

cv.drawContours(blank, contours, -1, (0,0,255), 1) # Tespit edilen dış hatları çizer, görüntü, nesnenin dış hatlarının listesi, index (-1 hepsini çizer), renk, kalınlık parametrelerini alır.
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)