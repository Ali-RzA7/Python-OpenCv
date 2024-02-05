import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('blank', blank)

blank[200:300, 300:400] = 0,255,0 # Belirtilen piksellere 0,255,0 renk değeri atanır yani yeşil. 
cv.imshow('Yeşil', blank)

cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2) # Görüntü üzerine dikdörtgen çizer. Çizilecek görüntü, dikdörtgenin sol üst köşesinin koordinaları, dikdörtgenin sağ alt köşesinin koordinaları, rengi RGB formatında, thickness çizginin kalınlığı.
cv.imshow('Dikdörtgen', blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=2) # Görüntü üzerine daire çizer. Çizilecek görüntü, dairenin merkez koordinatları, yarıçapı, rengi, çizgnin kalınlğını parametre olarak alır.
cv.imshow('Daire', blank)

cv.line(blank, (0, 0), (250, 250), (120, 120, 120), thickness=3) # Görüntü üzerine çizgi çizer. Çizilecek görüntü, çizginin bir ucunun koordinatları, diğer ucununkoordinatları, rengi, çizginin kalınlığını parametre olarak alır.
cv.imshow('Çizgi', blank)

cv.putText(blank, 'Yazi', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2) # Görüntü üzerine metin ekler, Yazılacak görüntü, yazılacak metin, metnin koordinatları, yazı tipi, yazının büyüklüğü, rengi, metnin kalınlığını parametre olarak alır.
cv.imshow('Metin', blank)

cv.waitKey(0)