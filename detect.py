import cv2
import numpy as np
from ultralytics import YOLO
from ultralytics.engine.results import Results


class DetectObject:
    def __init__(self, model: YOLO):
        self.model = model

    def detect(self, image_bytes: bytes):
        image = np.frombuffer(image_bytes, dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        results: Results = self.model.predict(image, save=True)
