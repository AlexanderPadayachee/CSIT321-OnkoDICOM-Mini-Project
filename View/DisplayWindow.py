"""Defines the main window that the user interacts with."""
from PySide6 import QtWidgets, QtCore, QtGui
from View.Preferences import *
import logging

class DisplayWindow(QtWidgets.QMainWindow):
    def __init__(self, view, controller, userPref):
        """init function, creates the qt objects and all widgets it contains"""
        super().__init__()
        self.layoutH = QtWidgets.QHBoxLayout()
        self.layout1 = QtWidgets.QVBoxLayout()
        self.button = QtWidgets.QPushButton("Select Directory")

        # Setup Widgets
        self.setWindowTitle("Mini Project Group 1 // DICOM DISPLAY")
        self.label = QtWidgets.QLabel(self)
        self.slider = QtWidgets.QSlider(self, QtCore.Qt.Horizontal)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.sliderMoved.connect(lambda: controller.update_image(self.slider.value()))
        self.slider.valueChanged.connect(lambda: controller.update_image(self.slider.value()))

        self.DicomInfo = QtWidgets.QLabel(self)
        self.dicomScroll = QtWidgets.QScrollArea()
        self.dicomScroll.setWidget(self.DicomInfo)
        self.dicomScroll.setWidgetResizable(True)

        self.textLabel = QtWidgets.QLabel(self)

        # Layout Creation
        self.layout1.setSpacing(5)
        self.layoutH.setSpacing(5)
        self.layout1.setContentsMargins(0, 0, 0, 0)
        self.layout1.addWidget(self.textLabel)
        self.layout1.addWidget(self.label)
        self.layout1.addWidget(self.slider)
        self.layoutH.addLayout(self.layout1)
        self.layoutH.addWidget(self.dicomScroll)
        widget = QtWidgets.QWidget()
        widget.setLayout(self.layoutH)
        self.setCentralWidget(widget)
        self.resize(QtCore.QSize(userPref[0][0], userPref[0][1]))

        # toolbar setup
        Action1 = QtGui.QAction("&Open File", self)
        Action1.triggered.connect(controller.directory_input)
        menu = self.menuBar()
        fileMenu = menu.addMenu("&File")
        fileMenu.addAction(Action1)
        fileMenu.addSeparator()
        logging.info("Display window Created")

    def resizeEvent(self, event):
        """Updates sqlite database upon window resize"""
        insertData(event.size().width(), event.size().height(), id=1)
        QtWidgets.QMainWindow.resizeEvent(self, event)
        logging.info("window resize")

    def alert(self, stringIn):
        """Defines the error alert dialogue box"""
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText("Error in Opening Dicom File: " + str(stringIn))
        msgBox.setWindowTitle("DicomError")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()
        logging.info("alert box executed")