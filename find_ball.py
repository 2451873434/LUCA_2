import cv2
import numpy as np
import os
paths='D:/python/LUCA_2/ball/'
dirs=os.listdir(paths)
for file in dirs:
    img = cv2.imread(paths+file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)  # 用高斯滤波处理原图像降噪
    canny = cv2.Canny(blur, 100, 200)  # 50是最小阈值,150是最大阈值
    circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, 500, param1=100, param2=50, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:  # 遍历矩阵每一行的数据
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 2)
    cv2.imwrite('D:/python/LUCA_2/ball_found/'+file, img)