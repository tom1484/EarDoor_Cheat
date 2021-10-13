import darknet as dn
import cv2


class YOLO:
    def __init__(self, cfg_path, data_path, weights_path):
        self.network, self.class_names, self.class_colors = dn.load_network(cfg_path, data_path, weights_path)
        self.width = dn.network_width(self.network)
        self.height = dn.network_height(self.network)

    def detect(self, frame):
        darknet_image = dn.make_image(self.width, self.height, 3)
        img_resized = cv2.resize(frame, (self.width, self.height),
                                 interpolation=cv2.INTER_LINEAR)

        # get image ratios to convert bounding boxes to proper size
        img_height, img_width, _ = frame.shape
        width_ratio = img_width / self.width
        height_ratio = img_height / self.height

        # run model on darknet style image to get detections
        dn.copy_image_from_bytes(darknet_image, img_resized.tobytes())
        detections = dn.detect_image(self.network, self.class_names, darknet_image)
        dn.free_image(darknet_image)

        results = []
        for label, confidence, bbox in detections:
            if float(confidence) <= 99.0:
                continue

            left, top, right, bottom = dn.bbox2points(bbox)
            # print((bottom - top) * (right - left))
            if (bottom - top) * (right - left) < 18000:
                continue

            disX = ((right + left) / 2 - self.width / 2) / self.width
            disY = ((bottom + top) / 2 - self.height / 2) / self.height
            if abs(disX) > 0.15 or abs(disY) > 0.15:
                continue

            left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), \
                                       int(right * width_ratio), int(bottom * height_ratio)

            results.append((confidence, (left, top, right, bottom)))

        if len(results) > 0:
            return max(results)[1]
        else:
            return None
