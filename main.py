from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

# create variables for running window
MainEvntThrd = QApplication([])

from utils.UI.startup_window import startupWindow
# from utils.choose_window import chooseWindow
from utils.UI.main_window import mainWindow

widget = QtWidgets.QStackedWidget()
widget.setFixedWidth(1650)
widget.setFixedHeight(950)

startup = startupWindow(widget)
# choose = chooseWindow(widget)
main = mainWindow(widget)

widget.addWidget(startup)
# widget.addWidget(choose)
widget.addWidget(main)

widget.show()
MainEvntThrd.exec()

