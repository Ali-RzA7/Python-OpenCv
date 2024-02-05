import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Kedi', img)

b,g,r = cv.split(img) # Görünüyü oluşturan renk kanallarını ayırır.
cv.imshow('Mavi', b)
cv.imshow('Yeşil', g)
cv.imshow('Kırmızı', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r]) # Renk kanllarını birleştirir.
cv.imshow('Birleştirilmiş', merged)

cv.waitKey(0)