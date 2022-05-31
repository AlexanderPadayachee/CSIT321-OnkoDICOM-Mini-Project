
class Model:
    def __init__(self, root_dir=None):
        self.root_dir = root_dir
        self.dcm_data = []  # DICOM files that contain pixel data are stored here as pydicom objects
        self.dcm_misc = []  # DICOM files that contain no pixel data are stored here as pydicom objects
        self.images = []  # DICOM images are stored here as PIL objects
