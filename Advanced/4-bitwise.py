import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('Dikdörtgen', rectangle)
cv.imshow('Daire', circle)

bitwise_and = cv.bitwise_and(rectangle, circle) # İki görüntünün piksel düzeyindeki karşılıklı olan piksellerini AND işlemi uygular, görüntü1, görüntü2 yi parametre olarak alır.
cv.imshow('Bitwise AND', bitwise_and)

bitwise_or = cv.bitwise_or(rectangle, circle) # İki görüntünün piksel düzeyindeki karşılıklı olan piksellerini OR işlemi uygular, görüntü1, görüntü2 yi parametre olarak alır.
cv.imshow('Bitwise OR', bitwise_or)

bitwise_xor = cv.bitwise_xor(rectangle, circle) # İki görüntünün piksel düzeyindeki karşılıklı olan piksellerini XOR işlemi uygular farklı ise 1 diğer hallerde 0, görüntü1, görüntü2 yi parametre olarak alır.
cv.imshow('Bitwise XOR', bitwise_xor)

bitwise_not = cv.bitwise_not(circle) # Görüntünün piksel düzeyinde tersini alır, görüntüyü parametre olarak alır
cv.imshow('Circle NOT', bitwise_not)

cv.waitKey(0)