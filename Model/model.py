"""Contains all data structures that the GUI requires"""
import logging


class Model:
    """Holds data structures for GUI"""
    def __init__(self, root_dir=None):
        """Init defines the data structures. They are referenced from
        the controller to keep this class as minimal as possible """
        self.root_dir = root_dir
        self.dcm_data = []  # DICOM files as pydicom objects
        self.dcm_misc = []  # DICOM files as pydicom objects
        self.images = []  # DICOM images as PIL objects
        logging.info("Model class created")

    def return_dcm(self):
        """returns model data structure of dicom objects"""
        return self.dcm_data

    def return_images(self):
        """returns model data structure of dicom bitmaps"""
        return self.images
