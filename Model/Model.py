import os
import logging
import glob
from pydicom import dcmread
from PIL import Image, ImageEnhance
import numpy as np

class Model:
    def __init__(self, Controller,rootDir = None):
        self.rootDir = rootDir

    @staticmethod
    def OpenDicom(directory):
        strInput = directory + "/*.dcm"

        dirList = glob.glob(strInput)
        TempDcmArray = []
        TempMiscArray = []
        for i in dirList:
            ds = dcmread(i, force=True)
            try:
                temp = ds.get_item((0x0020,0x1041)).value
                TempDcmArray.append(ds)
            except:
                TempMiscArray.append(ds)
            #print(ds.get_item((0x0020,0x1041)).value)
        SortDicom(TempDcmArray)
        return([TempDcmArray, TempMiscArray])

    @staticmethod
    def SortDicom(array):
        array.sort(key = lambda x:x.get_item((0x0020,0x1041)).value, reverse = False)
        return(array)

    @staticmethod
    def DicomToImage(dicoms):
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
