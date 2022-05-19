from PySide6 import QtWidgets
from PySide6 import QtCore
from Model.Model import Model
from View.View import View
import logging
import numpy as np
import PIL

import sys


class Controller:
    def __init__(self, rootDir=None):
        self.rootDir = rootDir

        self.Model = Model(self, self.rootDir)
        self.View = View(self, self.rootDir)
        self.dcmData = []
        self.dcmMisc = []
        self.images = []

    def showWindow(self):
        self.View.showMain()

    def directroyInput(self):
        dlg = QtWidgets.QFileDialog(self.View.mainWindow)
        dlg.setFileMode(QtWidgets.QFileDialog.Directory)
        foldernames = QtCore.QStringListModel
        if dlg.exec():
            foldernames = dlg.selectedFiles()
        # print(foldernames[0])

        if len(foldernames) < 1 or len(foldernames) > 1:
            logging.warning("File Selection Error. Maintaining Current View State")
        else:
            self.dcmData = []
            self.dcmMisc = []
            OpenData = self.Model.OpenDicom(foldernames[0])
            self.dcmData = OpenData[0]
            self.dcmMisc = OpenData[1]

            if len(self.dcmData) > 0:
                self.images = self.Model.DicomToImage(self.dcmData)
                self.View.viewImage(self.images[0])
                logging.info("Image Array Length = " + str(len(self.images)))
                logging.info("Dicom Array Length = " + str(len(self.dcmData)))
                self.View.ViewToggle(self.dcmData, self.images)
            else:
                logging.warning("No Dicom Files Found in Folder. Maintaining Current View State")
                return (-1)

    # def DisplayDicom(self):
