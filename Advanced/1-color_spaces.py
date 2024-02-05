import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Kedi', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gri', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV) # HSV renk uzayına çevirir.
cv.imshow('HSV', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB) # Lab renk uzayına çevirir.
cv.imshow('LAB', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB) # RGB renk uzayına çevirir.
cv.imshow('RGB', rgb)

cv.waitKey(0)