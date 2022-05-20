import pytest
import os

from Model.Model import open_dicom, dicom_to_image


def test_open_dicom():
    path = 'img/Pat01'
    full_path = os.path.join(os.getcwd(), path)

    assert open_dicom(full_path)


def test_dicom_to_image():
    path = 'img/Pat01'
    full_path = os.path.join(os.getcwd(), path)

    test_data = open_dicom(full_path)
    test_dcm_data = test_data[0]

    assert dicom_to_image(test_dcm_data)
