import cv2


class Camera:
    def __init__(self, cam_idx, width, height):
        self.camera = cv2.VideoCapture(cam_idx)
        self.width = width
        self.height = height

    def capture(self):
        ret, frame = self.camera.read()
        if not ret:
            return None
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # set image center
        h, w = frame.shape[:2]
        mid_y = h // 2
        mid_x = w // 2

        # adjust image dimension
        r_res = self.width / self.height
        r = w / h

        if r > r_res:
            w = int(h * r_res)
        elif r < r_res:
            h = int(w / r_res)

        # set crop area
        y1 = mid_y - h // 2
        y2 = mid_y + h // 2
        x1 = mid_x - w // 2
        x2 = mid_x + w // 2

        frame = frame[y1:y2, x1:x2]
        frame = cv2.resize(frame, (self.width, self.height))

        return frame

