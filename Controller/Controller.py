from PySide6 import QtWidgets
from PySide6 import QtCore
from Model.Model import Model, open_dicom, dicom_to_image
from View.View import View
import logging
import numpy as np
import PIL

import sys


class Controller:
    def __init__(self, root_dir=None):
        self.root_dir = root_dir

        self.Model = Model(self, self.root_dir)
        self.View = View(self, self.root_dir)
        self.dcm_data = []
        self.dcmMisc = []
        self.images = []

    def show_window(self):
        self.View.show_main()

    def directory_input(self):
        dlg = QtWidgets.QFileDialog(self.View.mainWindow)
        dlg.setFileMode(QtWidgets.QFileDialog.Directory)
        folder_names = QtCore.QStringListModel
        if dlg.exec():
            folder_names = dlg.selectedFiles()
        # print(folder_names[0])

        if len(folder_names) < 1 or len(folder_names) > 1:
            logging.warning("File Selection Error. Maintaining Current View State")
        else:
            self.dcm_data = []
            self.dcmMisc = []
            open_data = open_dicom(folder_names[0])
            self.dcm_data = open_data[0]
            self.dcmMisc = open_data[1]

            if len(self.dcm_data) > 0:
                self.images = dicom_to_image(self.dcm_data)
                self.View.view_image(self.images[0])
                logging.info("Image Array Length = " + str(len(self.images)))
                logging.info("Dicom Array Length = " + str(len(self.dcm_data)))
                self.View.view_toggle(self.dcm_data, self.images)
            else:
                logging.warning("No Dicom Files Found in Folder. Maintaining Current View State")
                return -1

    # def DisplayDicom(self):
