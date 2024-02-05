import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Kedi', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gri', gray)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Mask', masked)


gray_hist = cv.calcHist([gray], [0], masked, [256], [0,256]) # Görüntüdeki piksel değerlerinin histogramını hesaplamak için kullanılır, görüntü, renk kanalı (gri için 0, renkli için 0, 1, 2), mask bölgesi, içereceği bölme sayısı, renk kanalı değerleri parametrelerini alır. 
plt.figure()
plt.title('Gri Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


plt.figure()
plt.title('Renkli Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)