import numpy as np
import cv2

img = cv2.imread('capture.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

greyscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(greyscaled, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(greyscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval2, otsu = cv2.threshold(greyscaled, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('orignal', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()