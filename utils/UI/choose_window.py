from PyQt5.QtWidgets import QDialog

from utils.UI.choose_ui import Ui_Form


class chooseWindow(QDialog):
    def __init__(self, widget):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.widget = widget
