import cv2

from utils.YOLO import YOLO
from utils.CNN import CNN


class Recognizer:
    def __init__(self):
        self.yolo = YOLO("cfg/yolov4-tiny-obj.cfg", "cfg/ear.data", "models/yolov4-tiny-obj_final.weights")
        # self.yolo = YOLO("cfg/yolov4-tiny-obj.cfg", "cfg/ear.data", "models/yolov4_last.weights")
        self.cnn = CNN()

        self.names = ['Employee1', 'Employee2', 'Cannot Recognize']

    def detect(self, frame):
        # try:
        # get yolo detection results
        detection = self.yolo.detect(frame)
        if detection is not None:
            left, top, right, bottom = detection

            id, value = self.cnn.detect()
            name = self.names[id - 1]

            if id == 1:
                frame = cv2.putText(frame, name, (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
                frame = cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 4)
                return 1, name, frame
            elif id == 2:
                frame = cv2.putText(frame, name, (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
                frame = cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 4)
                return 1, name, frame
            elif id == 3:
                frame = cv2.putText(frame, name, (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 4)
                frame = cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 4)
                return 0, None, frame

        return -1, None, frame



