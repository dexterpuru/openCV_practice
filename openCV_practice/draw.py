import numpy as np
import cv2

img = cv2.imread('th.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (250, 250), (255, 0, 255), 15)
cv2.rectangle(img, (15, 25), (200, 150), (255, 0, 255), 5)
cv2.circle(img, (100, 63), 55, (255, 0, 150), -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
#pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (255, 150, 45), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts!!', (0, 130), font, 1, (255, 150, 0), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()