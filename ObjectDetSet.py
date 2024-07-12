import cv2

class ObjectRender:

    def __init__(self,video_path):
        self.mog = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
        self.stream = cv2.VideoCapture(video_path)

    def __del__(self):
        self.stream.release()

    def setting(self):
        ret, frame = self.stream.read()

        if not ret:
           raise Exception("Empty File")

        mask = self.mog.apply(frame)
        _, thresh = cv2.threshold(mask, 250, 255, cv2.THRESH_BINARY)

        #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        #mask_eroded = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        thresh = cv2.medianBlur(thresh, 15)
        thresh = cv2.dilate(thresh, None, iterations=4)

        cntr, hirarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        return cntr, frame, thresh