import os
import logging
import glob
from pydicom import dcmread
from PIL import Image, ImageEnhance
import numpy as np


def dicom_to_image(dicom):
    images = []
    for i in dicom:
        try:
            arr = i.pixel_array.astype(float)
            rescaled_im = (np.maximum(arr, 0) / arr.max()) * 255
            final_image = np.uint8(rescaled_im)
            patient_image = Image.fromarray(final_image)
            images.append(patient_image)
        finally:
            logging.info("Importing DICOM Files without pixel data")
    return images


def sort_dicom(array):
    array.sort(key=lambda x: x.get_item((0x0020, 0x1041)).value, reverse=False)
    return array


def open_dicom(directory):
    str_input = directory + "/*.dcm"

    dir_list = glob.glob(str_input)
    temp_dcm_array = []
    temp_misc_array = []
    for i in dir_list:
        ds = dcmread(i, force=True)
        try:
            temp = ds.get_item((0x0020, 0x1041)).value
            temp_dcm_array.append(ds)
        finally:
            temp_misc_array.append(ds)
        # print(ds.get_item((0x0020,0x1041)).value)
    sort_dicom(temp_dcm_array)
    return [temp_dcm_array, temp_misc_array]


class Model:
    def __init__(self, controller, root_dir=None):
        self.root_dir = root_dir
