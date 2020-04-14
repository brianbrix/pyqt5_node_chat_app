import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

import main
from PyQt5 import QtWidgets, QtCore


class Call_Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.chat()

    def chat(self):
        self.frame = QWebEngineView(self.ui.centralwidget)
        self.frame.setObjectName("frame")
        self.ui.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame.load(QUrl("http://localhost:8080"))

app = QApplication(sys.argv)
c = Call_Main()
c.show()
app.exec_()
