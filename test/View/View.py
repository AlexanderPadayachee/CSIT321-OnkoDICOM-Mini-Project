from PySide6 import QtWidgets, QtCore, QtGui
import logging
import PIL
from PIL.ImageQt import ImageQt
import io




class View:
    def __init__(self, Controller, rootDir = None):
        self.Controller = Controller
        self.rootDir = rootDir

        self.mainWindow = QtWidgets.QMainWindow()
        self.displayWindow = QtWidgets.QMainWindow()

        self.layoutH = QtWidgets.QHBoxLayout()
        self.layout1 = QtWidgets.QVBoxLayout()
        self.mainWindow.setWindowTitle("Mini Project Group 1")
        #self.mainWindow.setFixedSize(QtCore.QSize(600, 600))
        self.button = QtWidgets.QPushButton("Select Directory")

        self.mainWindow.setMenuWidget(self.button)
        self.button.clicked.connect(self.Controller.directroyInput)

        self.displayWindow.setWindowTitle("Mini Project Group 1 // DICOM DISPLAY")
        #self.displayWindow.setFixedSize(QtCore.QSize(1000, 1000))
        self.label = QtWidgets.QLabel(self.displayWindow)
        self.slider = QtWidgets.QSlider(self.displayWindow, QtCore.Qt.Horizontal)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.sliderMoved.connect(self.UpdateImage)
        self.slider.valueChanged.connect(self.UpdateImage)

        self.DicomInfo = QtWidgets.QLabel(self.displayWindow)
        self.dicomScroll = QtWidgets.QScrollArea()
        self.dicomScroll.setWidget(self.DicomInfo)
        self.dicomScroll.setWidgetResizable(True)


        self.textLabel = QtWidgets.QLabel(self.displayWindow)

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




    def ViewToggle(self):
        self.mainWindow.close()
        self.displayWindow.show()
        text1 = "Scan Position:   " + str(self.Controller.dcmData[0].get_item((0x0020, 0x1041)).value) + "\n"
        text2 = "Series Position:  0"

        self.textLabel.setText(text1 + text2)

        self.slider.setMinimum(1)
        self.slider.setMaximum(len(self.Controller.dcmData))
        self.slider.setValue(1)
        self.slider.setSingleStep(1)
        self.UpdateImage(True)
        self.displayWindow.resize(QtCore.QSize(1600, 500))
        #self.displayWindow.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.displayWindow.rect().center())

        #self.displayWindow.setFixedSize(self.displayWindow.sizeHint())



    def viewImage(self, picture):
        data = ImageQt(picture)
        pix = QtGui.QPixmap.fromImage(data)
        self.label.setPixmap(pix)

    def UpdateImage(self, forceInit = False):
        index = int(self.slider.value() - 1)
        if(forceInit == True):
            index = 0
        image = self.Controller.images[index]
        self.viewImage(image)
        text1 = "Scan Position:   " + str(self.Controller.dcmData[index].get_item((0x0020, 0x1041)).value) + "\n"
        text2 = "Series Position: " + str(index + 1)

        self.textLabel.setText(text1+text2)
        self.DicomInfo.setText(str(self.Controller.dcmData[index]))





    def showMain(self):
        self.mainWindow.show()


