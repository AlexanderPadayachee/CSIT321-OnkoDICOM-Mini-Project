from PySide6 import QtWidgets, QtCore, QtGui
import logging
import PIL
from PIL.ImageQt import ImageQt
import io




class View:
    def __init__(self, Controller, rootDir = None):
        self.Controller = Controller
        self.rootDir = rootDir

        self.Controller.layout1 = QtWidgets.QVBoxLayout()

        self.Controller.mainWindow.setWindowTitle("Mini Project Group 1")
        self.Controller.mainWindow.setFixedSize(QtCore.QSize(600, 600))
        self.Controller.button = QtWidgets.QPushButton("Select Directory")

        self.Controller.mainWindow.setMenuWidget(self.Controller.button)
        self.Controller.button.clicked.connect(self.Controller.directroyInput)

        # self.Controller.buttonCor = QtWidgets.QPushButton("Coronal view")
        # self.Controller.buttonTrans = QtWidgets.QPushButton("Axial / Transverse view")
        # self.Controller.buttonSag = QtWidgets.QPushButton("Sagittal view")

        self.Controller.displayWindow.setWindowTitle("Mini Project Group 1 // DICOM DISPLAY")
        self.Controller.displayWindow.setFixedSize(QtCore.QSize(600, 600))
        self.Controller.label = QtWidgets.QLabel(self.Controller.displayWindow)
        #self.Controller.displayWindow.setCentralWidget(self.Controller.label)
        self.Controller.slider = QtWidgets.QSlider(self.Controller.displayWindow, QtCore.Qt.Horizontal)
        self.Controller.slider.setOrientation(QtCore.Qt.Horizontal)
        self.Controller.slider.sliderMoved.connect(self.UpdateImage)
        self.Controller.slider.valueChanged.connect(self.UpdateImage)

        #QtWidgets.QStatusBar(self.Controller.displayWindow)
        #self.Controller.displayWindow.setCentralWidget(self.Controller.slider)
        self.Controller.textLabel = QtWidgets.QLabel(self.Controller.displayWindow)

        self.Controller.layout1.addWidget(self.Controller.textLabel)
        self.Controller.layout1.addWidget(self.Controller.label)
        self.Controller.layout1.addWidget(self.Controller.slider)

        widget = QtWidgets.QWidget()
        widget.setLayout(self.Controller.layout1)
        self.Controller.displayWindow.setCentralWidget(widget)




    def ViewToggle(self):
        self.Controller.mainWindow.close()
        self.Controller.displayWindow.show()
        self.Controller.textLabel.setText("Scan Position: " + str(self.Controller.dcmData[0].get_item((0x0020, 0x1041)).value))

        self.Controller.slider.setMinimum(1)
        self.Controller.slider.setMaximum(len(self.Controller.dcmData))
        self.Controller.slider.setValue(0)
        self.Controller.slider.setSingleStep(1)



    def viewImage(self, picture):
        data = ImageQt(picture)
        pix = QtGui.QPixmap.fromImage(data)
        self.Controller.label.setPixmap(pix)

    def UpdateImage(self):
        #print(self.Controller.slider.value())
        index = self.Controller.slider.value() - 1
        if(index < 0 or index == None):
            return (-1)
        else:
            image = self.Controller.images[index]
            self.viewImage(image)
            self.Controller.textLabel.setText(
                "Scan Position: " + str(self.Controller.dcmData[index].get_item((0x0020, 0x1041)).value))

