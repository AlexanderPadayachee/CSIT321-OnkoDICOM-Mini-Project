import pytest
import os
import sys
import PySide6

from Controller.Controller import Controller


def test_controller():
    test_dir = sys.argv[0]

    # core dump if this is not in the code
    test_application = PySide6.QtWidgets.QApplication(sys.argv)

    assert Controller(test_dir)






