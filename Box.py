import cv2
import numpy as np

class Box():
    GREEN = (100, 255, 0)
    RED = (0, 0, 255)
    detected_area = 500
    frames_count = 0
    id = 0

    def __init__(self, x ,y ,w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.id = Box.id
        Box.id += 1

    def shape(self):
        return self.x, self.y, self.w, self.h

    def rectangle(self):
        return self.x, self.y, self.x +self.w, self.y+self.h

    @classmethod
    def detection_area(cls, cntr):
        detection = []
        if len(cntr) != 0:
            for cnt in cntr:
                area = cv2.contourArea(cnt)
                if area > cls.detected_area:
                    x, y, w, h = cv2.boundingRect(cnt)
                    detection.append(Box(x, y, w, h))

        return detection

    @classmethod
    def area(cls, frame, boxes):
        if len(boxes) > 0:
            for box in boxes:
                print('id ', cls.id, 'coordinate', box.shape())
                x, y, w, h = box.shape()
                cx = x + w // 2
                cy = y + h // 2
                cv2.rectangle(frame, (x, y), (x + w, y + h), cls.GREEN, 2)
                cv2.circle(frame, (cx, cy), 2, cls.RED, 3)
        return frame














