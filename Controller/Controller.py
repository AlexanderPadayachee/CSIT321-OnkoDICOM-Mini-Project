from PySide6 import QtWidgets
from PySide6 import QtCore
from Model.Model import Model
from View.View import View
import logging
import numpy as np
import PIL

import sys
class Controller:
    def __init__(self, rootDir = None):
        self.rootDir = rootDir

        self.Model = Model(self ,self.rootDir)
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
        #print(foldernames[0])

        if len(foldernames) < 1 or len(foldernames) > 1:
            logging.warning("File Selection Error. Maintaining Current View State")
        else:
            self.dcmData = []
            self.dcmMisc = []
            self.Model.OpenDicom(foldernames[0])
            #print(self.dcmData[10])
            if len(self.dcmData) > 0:
                self.images = self.Model.DicomToImage(self.dcmData)
                self.View.viewImage(self.images[0])
                self.View.ViewToggle()
            else:
                logging.warning("No Dicom Files Found in Folder. Maintaining Current View State")
                return(-1)


    def close(self):
        self.close()

    #def DisplayDicom(self):







