from PySide6 import QtWidgets
from PySide6 import QtCore
import logging


class View:
    def __init__(self, Controller, rootDir = None):
        self.Controller = Controller
        self.rootDir = rootDir

        self.Controller.mainWindow.setWindowTitle("Mini Project Group 1")
        self.Controller.mainWindow.setFixedSize(QtCore.QSize(600, 300))
        self.Controller.button = QtWidgets.QPushButton("Select Directory")

        self.Controller.mainWindow.setMenuWidget(self.Controller.button)
        self.Controller.button.clicked.connect(self.Controller.directroyInput)

        self.Controller.displayWindow.setWindowTitle("Mini Project Group 1 // DICOM DISPLAY")
        self.Controller.displayWindow.setFixedSize(QtCore.QSize(600, 300))



    def ViewToggle(self):
        self.Controller.mainWindow.close()
        self.Controller.displayWindow.show()