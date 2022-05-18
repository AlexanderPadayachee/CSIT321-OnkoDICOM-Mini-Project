import pytest
import os
import sys
import PySide6

from main.Main import main
from Controller.Controller import Controller
from PySide6 import QtCore


def test_case(qtbot):
    test_app = main.main()
    qtbot.addWidget(test_app)

    # click in the Greet button and make sure it updates the appropriate label
    qtbot.mouseClick(test_app.button_greet, QtCore.Qt.LeftButton)

    assert test_app.greet_label.text() == "Hello!"
