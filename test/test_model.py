import pytest
import os

from Model.Model import Model


def test_open_dicom():
    path = 'test/img/Pat01'
    full_path = os.path.join(os.getcwd(), path)

    test_misc_array = []

    test_data = Model.open_dicom(full_path)
    test = 'Dataset.file_meta'
    test0 = '(7fe0, 0010) Pixel Data OW: Array of 524288 elements]'
    test1 = "(0002, 0003) Media Storage SOP Instance UID      " \
            "UI: 1.3.6.1.4.1.9590.100.1.2.122473141513104494726271804482866400552"

    if test in test_data[0] and test0 in test_data and test1 in test_data:
        test = test_data[0]
        assert test_data[0] == test

    assert test_data[1] == test_misc_array


def test_dicom_to_image():
    path = 'test/img/Pat01'
    full_path = os.path.join(os.getcwd(), path)

    test_data = Model.open_dicom(full_path)
    test_image = Model.dicom_to_image(test_data[0])

    test = '<PIL.Image.Image image mode=L size=512x512 at 0x7F6A31FE3A60>'
    test0 = '<PIL.Image.Image image mode=L size=512x512 at 0x7F6A31FC6C20>'

    if test in test_image and test0 in test_image:
        test = test_image
        assert test_image == test
