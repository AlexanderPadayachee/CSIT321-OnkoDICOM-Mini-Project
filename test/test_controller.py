import pytest
import os
import glob

from pydicom import dcmread
from Controller.Controller import *


def test_sort_dicom_empty():
    """
    Test that if nothing is inputted nothing
    is returned
    """
    test_data = []
    assert Controller.sort_dicom(test_data) == []


def test_sort_dicom():
    """
    Test to see if the dicom file is being
    arranged properly with the method
    sort_dicom
    """
    test_input = os.path.join(os.getcwd(), 'img/*.dcm')
    test_data = []
    dir_list = glob.glob(test_input)

    for i in dir_list:
        ds = dcmread(i, force=True)
        ds.get_item((0x0020, 0x1041)).value
        test_data.append(ds)

    if "(0002, 0000) File Meta Information Group Length" in str(Controller.sort_dicom(test_data)):
        assert True
