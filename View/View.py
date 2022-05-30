from PySide6 import QtWidgets, QtCore, QtGui
import logging
import PIL
from PIL.ImageQt import ImageQt
import io


class View:
    # very messy, doesn't conform to MVC or QT standards. Each window should be its own class
    def __init__(self, controller, root_dir=None):
        # controller is referenced here, but only to create a communication between the view and the controller.
        # It is referenced in the init, and is not in any other functions. this should be replaced by the parent call.

        self.root_dir = root_dir
        self.displayWindow = QtWidgets.QMainWindow()

        # toolbar setup
        Action1 = QtGui.QAction("&Open File", self.displayWindow)
        Action1.triggered.connect(controller.directory_input)
        menu = self.displayWindow.menuBar()
        fileMenu = menu.addMenu("&File")
        fileMenu.addAction(Action1)
        fileMenu.addSeparator()
        self.layoutH = QtWidgets.QHBoxLayout()
        self.layout1 = QtWidgets.QVBoxLayout()
        self.button = QtWidgets.QPushButton("Select Directory")

        # Setup Widgets
        self.displayWindow.setWindowTitle("Mini Project Group 1 // DICOM DISPLAY")
        self.label = QtWidgets.QLabel(self.displayWindow)
        self.slider = QtWidgets.QSlider(self.displayWindow, QtCore.Qt.Horizontal)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.sliderMoved.connect(lambda: controller.update_image(self.slider.value()))
        self.slider.valueChanged.connect(lambda: controller.update_image(self.slider.value()))

        self.DicomInfo = QtWidgets.QLabel(self.displayWindow)
        self.dicomScroll = QtWidgets.QScrollArea()
        self.dicomScroll.setWidget(self.DicomInfo)
        self.dicomScroll.setWidgetResizable(True)

        self.textLabel = QtWidgets.QLabel(self.displayWindow)

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
        self.displayWindow.setCentralWidget(widget)
        self.displayWindow.resize(QtCore.QSize(1500, 500))


    def ButtonTest(self):
        print("check")



    def show_main(self):  # View Function
        self.displayWindow.show()

