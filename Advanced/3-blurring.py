import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Kedi', img)

average = cv.blur(img, (3,3)) # Görüntü üzerinde bir bulanıklık uygular, görüntü, bulanıklık boyutunu parametre olaral alır.
cv.imshow('Avarege Blur', average)

median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median) # Her bir pikselin çevresindeki bir bölgenin piksel değerleri üzerinden ortanca değeri alarak bulanıklık işlemi gerçekleştirir, görüntü, ortanca değeri hesaplanırken kullanılacak bölgenin boyutunu parametre olarak alır.

bilateral = cv.bilateralFilter(img, 50, 55, 55) # Bir görüntü üzerinde hem uzamsal hem de renk tabanlı bir filtreleme yapar, görüntü, filtre çapı, renk benzerliği, pikselin çevresindeki komşu piksellerle olan benzerlik parametrelerini alır.
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)