from PySide6 import QtWidgets
from PySide6 import QtCore
from Model.Model import Model
from View.View import View
import logging
import numpy as np
import PIL

import sys


class Controller:
    def __init__(self, root_dir=None):
        # setup attributes and create model and view
        self.root_dir = root_dir
        self.Model = Model(self.root_dir)
        self.View = View(self, self.root_dir)
        self.dcm_data = []  # DICOM files that contain pixel data are stored here as pydicom objects
        self.dcm_misc = []  # DICOM files that contain no pixel data are stored here as pydicom objects
        self.images = []  # DICOM images are stored here as PIL objects

    def show_window(self):  # self-explanatory
        self.View.show_main()

    def directory_input(self):
        # This function runs the file input GUI and processes the data in the folder selected
        dlg = QtWidgets.QFileDialog(self.View.mainWindow)
        dlg.setFileMode(QtWidgets.QFileDialog.Directory)
        folder_names = QtCore.QStringListModel
        if dlg.exec():
            folder_names = dlg.selectedFiles()

        if len(folder_names) < 1 or len(folder_names) > 1:
            logging.warning("File Selection Error. Maintaining Current View State")
        else:
            # clear dicom data
            self.dcm_data = []
            self.dcm_misc = []
            open_data = self.Model.open_dicom(folder_names[0])
            self.dcm_data = open_data[0]
            self.dcm_misc = open_data[1]

            if len(self.dcm_data) > 0:
                self.images = self.Model.dicom_to_image(self.dcm_data)  # call to model function
                self.View.view_image(self.images[0])  # call to view function
                logging.info("Image Array Length = " + str(len(self.images)))
                logging.info("Dicom Array Length = " + str(len(self.dcm_data)))
                self.View.view_toggle(self.dcm_data, self.images)  # call to view function
            else:
                logging.warning("No Dicom Files Found in Folder. Maintaining Current View State")
                return -1
