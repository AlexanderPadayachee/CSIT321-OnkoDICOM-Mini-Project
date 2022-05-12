import os
import glob
from pydicom import dcmread

class Model:
    def __init__(self, Controller,rootDir = None):
        self.Controller = Controller
        self.rootDir = rootDir

    def OpenDicom(self, directory):
        strInput = directory + "/*.dcm"

        dirList = glob.glob(strInput)

        for i in dirList:
            ds = dcmread(i, force=True)
            self.Controller.dcmData.append(ds)

