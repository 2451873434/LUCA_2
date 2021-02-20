import cv2
import numpy as np
import os

img = cv2.imread('D:/python/LUCA_2/ball/basketball1.jpg')
# dst = cv2.pyrMeanShiftFiltering(img, 10, 30)#均值偏移滤波
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),1)
# blur=cv2.medianBlur(gray,5)
# blur = cv2.GaussianBlur(gray, (3, 3), 0)  # 用高斯滤波处理原图像降噪
# canny = cv2.Canny(blur, 100, 300)  # 50是最小阈值,150是最大阈值
# circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=0, maxRadius=0)
# circles = np.uint16(np.around(circles))
# for i in circles[0, :]:  # 遍历矩阵每一行的数据
#     cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
#     cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 2)
# cv2.imwrite('D:/python/LUCA_2/ball_found/basketball1.jpg', img)
cv2.imshow('123',img)
cv2.waitKey()