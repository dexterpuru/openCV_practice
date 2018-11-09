import cv2
import numpy as np

img1 = cv2.imread('background.jpg')
img2 = cv2.imread('Python.jpg')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2grey = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2grey, 220, 250, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

#add = img1 + img2
#add = cv2.add(img1, img2)

#weighted = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)

#cv2.imshow('weighted', weighted)
#cv2.imshow('mask', mask)

cv2.imshow('res', img1)
#cv2.imshow('dst', dst)
#cv2.imshow('img2_fg', img2_fg)
#cv2.imshow('img1_bg', img1_bg)
#cv2.imshow('mask_inv', mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()