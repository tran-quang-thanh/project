import cv2
from threading import Thread


class webcam():

    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame = self.cap.read()[1]

    def update(self):
        while(True):
            self.frame = self.cap.read()[1]
            cv2.imshow("Thread1", self.frame)
            cv2.waitKey(1)

    def thread_webcam(self):
        Thread(None, self.update).start()

    def get_currentframe(self):
        return self.frame