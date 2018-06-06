import cv2
import numpy as np
import time

lower = np.array([0, 0, 0])
higher = np.array([255, 255, 117])


def Scan(a, m, n):
    count = 0
    for i in range(m, n + 64 + 1):
        for j in range(m, n + 64 + 1):
            if a[i, j] >= 200:
                count += 1
    if count >= 64 * 64 / 2:
        return True
    return False

a = time.time()
def Test():
    start_time = a
    frame = cap.read()[1]
    frame = cv2.flip(frame, 1)
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    binImage = cv2.inRange(hsvImage, lower, higher)
    # print(Scan(binImage, 10, 10))
    cv2.imshow("binImg", binImage)
    cv2.waitKey(50)
    def Time(a,b):
        d = b - a
        print(d)
        if 1.5 > d > 1:
            return True
        elif d > 1.5:
            b = a
            Time(a,b)
    if Time(start_time,time.time()):
        print(Scan(binImage,10,10))
    else:
        return False

cap = cv2.VideoCapture(0)
while True:
    # frame = cap.read()[1]
    # frame = cv2.flip(frame, 1)
    # hsvImage = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    # binImage = cv2.inRange(hsvImage, lower, higher)
    # print(Scan(binImage, 10, 10))
    # cv2.imshow("binImg", binImage)
    # cv2.waitKey(30)
    Test()






