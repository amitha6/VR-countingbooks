import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
image = cv.imread("CountBooks_BookShelf.jpg")
image = cv.resize(image, (960, 540))
#cv.imshow("Edge_Books", image)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (9, 9), 0)
canny = cv.Canny(blur, 10, 150)
lines1 = cv.HoughLinesP(canny, 1, np.pi/180, 90, minLineLength=100, maxLineGap=40)
count = 0
""" for line in lines1:
    x1, y1, x2, y2 = line[0]
    if(x1 == x2) or (y2-y1)/(x2-x1) > 3.372 or (y2-y1)/(x2-x1) < -3.372:
        count += 1
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
count = 0 """
lines2 = cv.HoughLines(canny, 1, np.pi/180, 130)
for line in lines2:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000 *(-b))
    y1 = int(y0 + 1000 *(a))
    x2 = int(x0 - 1000 *(-b))
    y2 = int(y0 - 1000 *(a))
    if(x1 == x2) or (y2-y1)/(x2-x1) > 3.372 or (y2-y1)/(x2-x1) < -3.372:
        count += 1
    cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2) 


lsd = cv.createLineSegmentDetector(0)
lines = lsd.detect(canny)[0] #Position 0 of the returned tuple are the detected lines
#Draw detected lines in the image 
img = lsd.drawSegments(canny,lines)
print(len(lines2))
print(count)
cv.imshow("lines_Books", image)

#cols = image.shape[1]
#horizontal_size = cols // 30
# Create structure element for extracting horizontal lines through morphology operations
#horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))
# Apply morphology operations
#image = cv.erode(image, horizontalStructure)
#image = cv.dilate(image, horizontalStructure)
# Show extracted horizontal lines
#cv.show_wait_destroy("horizontal", image)
""" rows = image.shape[0]
verticalsize = rows // 30
# Create structure element for extracting vertical lines through morphology operations
verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))
# Apply morphology operations
image = cv.erode(image, verticalStructure)
image = cv.dilate(image, verticalStructure)
# Show extracted vertical lines
#show_wait_destroy("vertical", image)
cv.imshow("lines_Books", image)  """
cv.waitKey(0)