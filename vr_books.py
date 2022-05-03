import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
image = cv.imread("CountBooks_BookShelf.jpg")
image = cv.resize(image, (960, 540))
#cv.imshow("Edge_Books", image)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (15, 15), 0)
canny = cv.Canny(blur, 10, 150)
#ret, thresh = cv.threshold(blur, 150, 300, cv.THRESH_BINARY)
dilated = cv.dilate(canny, (2, 2), iterations=0)
#_, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
#kernal = np.ones((2, 2), np.uint8)
#dilated = cv.dilate(thresh, kernal, iterations=2)
(cnt, hierarchy) = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(image, cnt, -1, (0, 255, 0), 4)
print(str(len(cnt)))
cv.imshow("coun", image)
cv.waitKey(0)
