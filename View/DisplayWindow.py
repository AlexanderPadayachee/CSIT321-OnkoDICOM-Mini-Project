from PySide6 import QtWidgets, QtCore, QtGui
from View.Preferences import *

class DisplayWindow(QtWidgets.QMainWindow):
    def __init__(self, view, controller, userPref):
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

    def resizeEvent(self, event):
        insertData(event.size().width(), event.size().height(), id=1)
        QtWidgets.QMainWindow.resizeEvent(self, event)