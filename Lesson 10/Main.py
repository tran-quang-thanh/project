import Webcam
import cv2

test = Webcam.webcam()

test.thread_webcam()

while True:
    frame = test.get_currentframe()
    cv2.imshow("Threadmain", frame)
    cv2.waitKey(10)