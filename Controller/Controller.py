from PySide6 import QtWidgets
from PySide6 import QtCore
from Model.Model import Model
from View.View import View
import numpy as np
import PIL
from PIL.ImageQt import ImageQt
from PySide6 import QtGui
import sys
import os
import logging
import glob
from pydicom import dcmread
from PIL import Image, ImageEnhance


class Controller:
    def __init__(self, root_dir=None):
        # setup attributes and create model and view
        self.root_dir = root_dir
        self.Model = Model(self.root_dir)
        self.View = View(self, self.root_dir)

    def show_window(self):  # self-explanatory
        self.View.show_main()

    def directory_input(self):
        # This function runs the file input GUI and processes the data in the folder selected
        self.Model.dcm_data = []
        self.Model.dcm_misc = []
        self.Model.images = []
        dlg = QtWidgets.QFileDialog(self.View.displayWindow)
        dlg.setFileMode(QtWidgets.QFileDialog.Directory)
        folder_names = QtCore.QStringListModel
        if dlg.exec():
            folder_names = dlg.selectedFiles()

        if len(folder_names) < 1 or len(folder_names) > 1:
            logging.warning("File Selection Error. Maintaining Current View State")
        else:
            # clear dicom data
            self.Model.dcm_data = []
            self.Model.dcm_misc = []
            open_data = self.open_dicom(folder_names[0])
            self.Model.dcm_data = open_data[0]
            self.Model.dcm_misc = open_data[1]

            if len(self.Model.dcm_data) > 0:
                self.Model.images = self.dicom_to_image(self.Model.dcm_data)  # call to model function
                self.view_image(self.Model.images[0])  # call to view function
                logging.info("Image Array Length = " + str(len(self.Model.images)))
                logging.info("Dicom Array Length = " + str(len(self.Model.dcm_data)))
                self.view_toggle()  # call to view function
            else:
                logging.warning("No Dicom Files Found in Folder. Maintaining Current View State")
                return -1

    def update_image(self, value, force_init=False):
        index = int(value - 1)
        if force_init is True:
            index = 0
        image = self.Model.images[index]
        self.view_image(image)
        text1 = "Scan Position:   " + str(self.Model.dcm_data[index].get_item((0x0020, 0x1041)).value) + "\n"
        text2 = "Series Position: " + str(index + 1)

        self.View.textLabel.setText(text1 + text2)
        self.View.DicomInfo.setText(str(self.Model.dcm_data[index]))

    def view_toggle(self):
        text1 = "Scan Position:   " + str(self.Model.dcm_data[0].get_item((0x0020, 0x1041)).value) + "\n"
        text2 = "Series Position:  0"

        self.View.textLabel.setText(text1 + text2)
        self.View.slider.setMinimum(1)
        self.View.slider.setMaximum(len(self.Model.dcm_data))
        self.View.slider.setValue(1)
        self.View.slider.setSingleStep(1)
        self.update_image(True)
        self.View.displayWindow.resize(QtCore.QSize(1500, 500))

    def view_image(self, picture):
        data = ImageQt(picture)
        pix = QtGui.QPixmap.fromImage(data)
        self.View.label.setPixmap(pix)

    def open_dicom(self, directory):
        str_input = directory + "/*.dcm"

        dir_list = glob.glob(str_input)
        temp_dcm_array = []
        temp_misc_array = []
        for i in dir_list:
            ds = dcmread(i, force=True)
            try:
                temp = ds.get_item((0x0020, 0x1041)).value
                temp_dcm_array.append(ds)
            except:
                temp_misc_array.append(ds)
            # print(ds.get_item((0x0020,0x1041)).value)
        temp_dcm_array = self.sort_dicom(temp_dcm_array)
        self.Model.dcm_data = temp_dcm_array
        self.Model.dcm_misc = temp_misc_array
        return [temp_dcm_array, temp_misc_array]

    def sort_dicom(self, array):
        array.sort(key=lambda x: float(x.get_item((0x0020, 0x1041)).value), reverse=True)
        return array

    def dicom_to_image(self, dicom):
        images = []
        for i in dicom:
            try:
                arr = i.pixel_array.astype(float)
                rescaled_im = (np.maximum(arr, 0) / arr.max()) * 255
                final_image = np.uint8(rescaled_im)
                patient_image = Image.fromarray(final_image)
                images.append(patient_image)
                if(sys.getsizeof(images) >= 500000000):
                    logging.warning("Image processing aborted(files to large)")
                    break
            except:
                logging.info("Importing DICOM Files without pixel data")
        logging.debug("Size of Image Array = " + str(sys.getsizeof(images)))
        self.Model.images = images
        return images