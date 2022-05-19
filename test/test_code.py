import pytest
import os
import sys

from View.View import View
from Model.Model import Model
from Controller.Controller import Controller


def test_app(qtbot):
    test_app = View
    qtbot.addWidget(test_app)
    return test_app





