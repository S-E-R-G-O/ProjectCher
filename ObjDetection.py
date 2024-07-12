import cv2
import numpy as np
from Box import Box
from ObjectDetSet import ObjectRender


od = ObjectRender("Cars.mp4")


while True:

    cntr,frame,thresh = od.setting()


    detection = Box.detection_area(cntr)

    frame = Box.area(frame,detection)

    cv2.imshow('Tracker', frame)
    cv2.imshow('Mask', thresh)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
