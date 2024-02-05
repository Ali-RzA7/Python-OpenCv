import cv2 as cv

img = cv.imread('Photos/cat.jpg') # Dosya yolundaki görüntüyü okur ve matrise çevirir.

cv.imshow('Kedi',img) # Görüntüyü ekranda göstermek için kullanılır. Pencerenin ismi ve matrisli görüntüyü parametre olarak alır.

cv.waitKey(0) # Kullanıcının bir tuşa basmasını bekler ve o tuşun ascıı değerini döndürür. parametre olarak süre alır. O süre içinde basılmazsa 0 döndürür. Belirli bir süre boyunca tuş beklemesi istenmiyorsa, genellikle 0 değeri kullanılır. 


# Video
capture = cv.VideoCapture('Videos/dog.mp4') # Video kaynaklarından gelen görüntü akışını çerçeve çerçeve okuyarak işler. Dosya yolu parametre olarak girilmişse dosya yolundaki videoyu işler. Eğerki 0 girilmişse bilgisayardaki birincil kameradan gelen görüntüleri işler.

while True:
    
    isTrue, frame = capture.read() # Video akışından bir çerçeve okur ve 2 değer döndürür. Birincisi çerçeve başarıyla okunduğunda True, okunmadığında False. İkinci olarak da çerçeveyi temsil eden bir görüntü matrisi döndürür.
    
    if not isTrue:
        break
    
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release() # Video akışını kapatır.
cv.destroyAllWindows() # Tüm pencereleri kapatır.

