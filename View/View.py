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

        self.mainWindow = QtWidgets.QMainWindow()
        self.displayWindow = QtWidgets.QMainWindow()

        self.layoutH = QtWidgets.QHBoxLayout()
        self.layout1 = QtWidgets.QVBoxLayout()
        self.mainWindow.setWindowTitle("Mini Project Group 1")
        # self.mainWindow.setFixedSize(QtCore.QSize(600, 600))
        self.button = QtWidgets.QPushButton("Select Directory")

        self.mainWindow.setMenuWidget(self.button)
        self.button.clicked.connect(controller.directory_input)

        self.displayWindow.setWindowTitle("Mini Project Group 1 // DICOM DISPLAY")
        # self.displayWindow.setFixedSize(QtCore.QSize(1000, 1000))
        self.label = QtWidgets.QLabel(self.displayWindow)
        self.slider = QtWidgets.QSlider(self.displayWindow, QtCore.Qt.Horizontal)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.sliderMoved.connect(self.update_image)
        self.slider.valueChanged.connect(self.update_image)

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

        # the next attribute setups are disgusting and don't make sense. Data should not be stored in the view object.
        # If you find a way to send data from the Controller to the view when an event listener in the view is
        # triggered please implement it here.
        # It is static data though and will not change state when running the code.
        self.dcm_data = []
        self.images = []

    def view_toggle(self, dcm_data, images):
        self.images = images
        self.dcm_data = dcm_data
        self.mainWindow.close()
        self.displayWindow.show()
        text1 = "Scan Position:   " + str(dcm_data[0].get_item((0x0020, 0x1041)).value) + "\n"
        text2 = "Series Position:  0"

        self.textLabel.setText(text1 + text2)

        self.slider.setMinimum(1)
        self.slider.setMaximum(len(dcm_data))
        self.slider.setValue(1)
        self.slider.setSingleStep(1)
        self.update_image(True)

        self.displayWindow.resize(QtCore.QSize(1600, 500))

    def view_image(self, picture):
        data = ImageQt(picture)
        pix = QtGui.QPixmap.fromImage(data)
        self.label.setPixmap(pix)

    def update_image(self, force_init=False):
        index = int(self.slider.value() - 1)
        if force_init is True:
            index = 0
        image = self.images[index]
        self.view_image(image)
        text1 = "Scan Position:   " + str(self.dcm_data[index].get_item((0x0020, 0x1041)).value) + "\n"
        text2 = "Series Position: " + str(index + 1)

        self.textLabel.setText(text1 + text2)
        self.DicomInfo.setText(str(self.dcm_data[index]))

    def show_main(self):
        self.mainWindow.show()
