import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Kedi', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # Renkli bir görüntüyü gri tonlamalı görüntüye çevirir, Dönüştürülecek görüntü, dönüşüm için kullanılacak kod. COLOR_XXX2YYY XXX başlangıç renk uzayını, YYY hedef renk uzayını temsil eder.
cv.imshow('Gri', gray)

blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT) # Görüntüyü yumuşatır, görüntü, filtre boyutu, kenar pikseller için kullanılacak olan sınır modu. 
cv.imshow('Blur', blur)

canny = cv.Canny(img, 75, 175) #Kenar tespitit için kullanılır, görüntü, kenar pikselleri için alt eşik değeri, kenar pikselleri için üst eşik değeri, eğer pikselin gradyan değeri üst eşik değerinden büyükse güçlü kenar pikselidir, alt ve üst eişk değeri arasında ie zayıf, alt eşikten küçüksekenar piksle oalrak kabul edilmez. Gradyan renk veya parlaklık değerlerinin değişimini ifade eder.
cv.imshow('Kenar', canny)

dilated = cv.dilate(canny, (7, 7), iterations=3) # Beyaz nesneleri genişletir. Görüntü, işlem için kullanılacak olan kernel boyutu bu genişleme boyutunu ve şeklini belirler, işlemin kaç kez tekrarlanacağını ifade eden sayıyı parametre olarak alır.
cv.imshow('Genişletilmiş', dilated)

eroded = cv.erode(dilated, (7, 7), iterations=3) # Beyaz nesneleri daraltır, görüntü, işlem için kullanılacak olan kernel boyutu bu genişleme boyutunu ve şeklini belirler, işlemin kaç kez tekrarlanacağını ifade eden sayıyı parametre olarak alır.
cv.imshow('Daraltılmış', eroded)

cv.waitKey(0)

