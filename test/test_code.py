import pytest
import os
import sys

from Controller.Controller import Controller


def test_dicom_to_image():
    path = 'img/Pat01'
    fullpath = os.path.join(path, sys.argv[0])

    assert Controller(fullpath)





