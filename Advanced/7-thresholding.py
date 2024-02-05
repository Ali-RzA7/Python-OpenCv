import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Kedi', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gri', gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # Gri tonlamalı görüntüyü belirli bir eşik değerine göre ikili bir görüntüye dönüştürür siyah ve beyaz olarak, görüntü, eşik değer, eşik değeri geçenlerin alacağı değer, eşikleme türü parametrelerini alır. 
cv.imshow('Thresh', thresh)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3) # Görüntü üzerindeki her pikselin eşik değerini, o pikselin çevresindeki komşu piksellerin değerlerine dayanarak belirlenir, görüntü, eşik değeri geçenlerin alacağı değer, eşikleme yöntemi, eşikleme türü, blok boyutu bu blok içindeki piksellerin değerlerine dayanarak belirlenir, eşik değerine eklenen sabit değer parametrelerini alır.  
cv.imshow('Adaptive Thresh', adaptive_thresh)


cv.waitKey(0)