import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    
    width = int(frame.shape[1] * scale) # Çerçevenin genişliğini scale ile çarparak yeni genişlik değeri elde edilir.
    height = int(frame.shape[0] * scale) # çerçevenin yüksekliğimi scale ile çarparak yeni yükseklik değeri elde edilir.
    
    dimensions = (width, height) # Yeni boyutlar değişkende tutuldu.
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) # Ölçeklendirme veya boyut değiştirme işlemlemlerinde kullanılır. Çerçeve, yeni boyutlar ve boyutlandırma sırasında kullanılacak olan yöntem. Burada INTER_AREA kullanıldı. Piksellerin ortalamsını alarak yeni pikselin değerini üretir.

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    
    isTrue, frame = capture.read() 
    frame_resized = rescaleFrame(frame)
    
    if not isTrue:
        break
    
    cv.imshow('Video', frame)
    cv.imshow('Boyutlandırılmış', frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()