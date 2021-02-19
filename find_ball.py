import cv2
import numpy as np
img=cv2.imread('D:/python/LUCA_2/football.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i=-1;
for c in contours:
    i=i+1
    # if hierarchy[0][i][2]!=-1:
    # 计算最小封闭圆形的中心和半径
    (x, y), radius = cv2.minEnclosingCircle(c)
    # 转换成整数
    center = (int(x), int(y))
    radius = int(radius)
    # 画出圆形
    img = cv2.circle(img, center, radius, (0, 255, 0), 1)
cv2.drawContours(img, contours, -1, (0, 0, 0), 1)
cv2.imshow("contours", img)
cv2.waitKey()
cv2.destroyAllWindows()