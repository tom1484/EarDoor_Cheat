from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox

from utils.UI.startup_ui import Ui_Form


class startupWindow(QDialog):
    def __init__(self, widget):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.widget = widget

        self.ui.account.returnPressed.connect(self.ui.key.setFocus)
        self.ui.key.returnPressed.connect(self.login)
        self.ui.login_button.clicked.connect(self.login)

    def login(self):
        if self.ui.account.text() == "tom1484" and self.ui.key.text() == "12345678":
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Login Failed")
            msg.setText("Wrong username or password!")
            msg.setStandardButtons(QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Cancel)
            msg.exec()
