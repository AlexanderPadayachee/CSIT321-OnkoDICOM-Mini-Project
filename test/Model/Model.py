import os
import logging
import glob
from pydicom import dcmread
from PIL import Image, ImageEnhance
import numpy as np

class Model:
    def __init__(self, Controller,rootDir = None):
        self.Controller = Controller
        self.rootDir = rootDir

    def OpenDicom(self, directory):
        strInput = directory + "/*.dcm"

        dirList = glob.glob(strInput)

        for i in dirList:
            ds = dcmread(i, force=True)
            try:
                temp = ds.get_item((0x0020,0x1041)).value
                self.Controller.dcmData.append(ds)
            except:
                self.Controller.dcmMisc.append(ds)
            #print(ds.get_item((0x0020,0x1041)).value)
        self.SortDicom()

    def SortDicom(self):
        self.Controller.dcmData.sort(key = lambda x:x.get_item((0x0020,0x1041)).value, reverse = False)

    # def findOrientations(self):
    #     for i in self.Controller.dcmData:
    #         print(i[0x20, 0x37])
    def DicomToImage(self, dicoms):
        images = []
        for i in dicoms:
            try:
                arr = i.pixel_array.astype(float)
                rescaled_im = (np.maximum(arr,0)/arr.max())*255
                final_image = np.uint8(rescaled_im)
                patientImage=Image.fromarray(final_image)
                images.append(patientImage)
            except:
                logging.info("Importing DICOM Files without pixel data")
        return(images)
