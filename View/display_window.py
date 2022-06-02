"""Defines the main window that the user interacts with."""
import logging
from PySide6 import QtWidgets, QtCore, QtGui
from View.preferences import insert_data


class DisplayWindow(QtWidgets.QMainWindow):
    """Window and widget creation"""

    def __init__(self, controller, user_pref):
        """init function, creates the qt objects and all widgets it contains"""
        super().__init__()
        self.layout_h = QtWidgets.QHBoxLayout()
        self.layout1 = QtWidgets.QVBoxLayout()
        self.button = QtWidgets.QPushButton("Select Directory")

        # Setup Widgets
        self.setWindowTitle("Mini Project Group 1 // DICOM DISPLAY")
        self.label = QtWidgets.QLabel(self)
        self.slider = QtWidgets.QSlider(self, QtCore.Qt.Horizontal)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.sliderMoved.connect(lambda: controller.update_image(self.slider.value()))
        self.slider.valueChanged.connect(lambda: controller.update_image(self.slider.value()))

        self.dicom_info = QtWidgets.QLabel(self)
        self.dicom_scroll = QtWidgets.QScrollArea()
        self.dicom_scroll.setWidget(self.dicom_info)
        self.dicom_scroll.setWidgetResizable(True)

        self.text_label = QtWidgets.QLabel(self)

        # Layout Creation
        self.layout1.setSpacing(5)
        self.layout_h.setSpacing(5)
        self.layout1.setContentsMargins(0, 0, 0, 0)
        self.layout1.addWidget(self.text_label)
        self.layout1.addWidget(self.label)
        self.layout1.addWidget(self.slider)
        self.layout_h.addLayout(self.layout1)
        self.layout_h.addWidget(self.dicom_scroll)
        widget = QtWidgets.QWidget()
        widget.setLayout(self.layout_h)
        self.setCentralWidget(widget)
        self.resize(QtCore.QSize(user_pref[0][0], user_pref[0][1]))

        # toolbar setup
        action1 = QtGui.QAction("&Open File", self)
        action1.triggered.connect(controller.directory_input)
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        file_menu.addAction(action1)
        file_menu.addSeparator()
        logging.info("Display window Created")

    def resizeEvent(self, event):
        """Updates sqlite database upon window resize"""
        insert_data(event.size().width(), event.size().height(), user_id=1)
        QtWidgets.QMainWindow.resizeEvent(self, event)
        logging.info("window resize")

    @staticmethod
    def alert(string_in):
        """Defines the error alert dialogue box"""
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setText("Error in Opening Dicom File: " + str(string_in))
        msg_box.setWindowTitle("DicomError")
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec()
        logging.info("alert box executed")
