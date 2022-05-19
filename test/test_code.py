import pytest
import os
import sys
import PySide6

from View.View import View
from Model.Model import Model
from Controller.Controller import Controller


def test_app():
    test_dir = sys.argv[0]
    test_application = PySide6.QtWidgets.QApplication(sys.argv)

    test_controller = Controller(test_dir)

    test_controller.showWindow()
    test_application.exec()





