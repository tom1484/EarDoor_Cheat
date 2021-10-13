import time
import base64
import io
from imageio import imread
from datetime import datetime

from PyQt5.QtGui import QImage, QPixmap


class Updater:
    def __init__(self, ui, database, sl_model):
        self.ui = ui
        self.database = database
        self.sl_model = sl_model

        self.time = -10

    def update(self, status, name, frame):
        if time.time() - self.time > 2:
            self.update_frame(frame)
            self.clear_identity()

            if status >= 0:
                self.time = time.time()
                if status >= 1:
                    self.update_identity(name)

    def clear_identity(self):
        # clear information
        self.ui.name_holder.setText('')
        self.ui.time_holder.setText('')
        self.ui.location_holder.setText('')

        self.sl_model.setStringList([])

        # clear image
        self.ui.picture_holder.setPixmap(QPixmap())

    def update_identity(self, name):
        # update database
        now = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")
        self.database.add_record(name, now)

        # update information
        self.ui.name_holder.setText(name)
        self.ui.time_holder.setText(now)
        self.ui.location_holder.setText("NTNU")

        # update records
        records = self.database.select_records(name)
        self.sl_model.setStringList(records)

        # update image
        raw = self.database.select_image(name)
        img = imread(io.BytesIO(base64.b64decode(raw)))
        img = QImage(img, img.shape[1], img.shape[0],
                     img.shape[1] * 3, QImage.Format_RGB888)
        img = QPixmap.fromImage(img)

        self.ui.picture_holder.setPixmap(img)

    def update_frame(self, frame):
        # convert image to QPixmap
        img = QImage(frame, frame.shape[1], frame.shape[0],
                     frame.shape[1] * 3, QImage.Format_RGB888)
        img = QPixmap.fromImage(img)

        # display image
        self.ui.camera_holder.setPixmap(img)
        self.ui.camera_holder.setScaledContents(True)
