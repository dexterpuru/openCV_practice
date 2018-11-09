import cv2
import numpy as np

img = cv2.imread("bookpage.jpg")

greyscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(greyscaled, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(greyscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('original', img)
cv2.imshow('greyscaled', greyscaled)
cv2.imshow('gaus', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()

