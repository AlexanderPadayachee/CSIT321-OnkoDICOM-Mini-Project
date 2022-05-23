import pytest
import os
import sys
import PySide6

from Controller.Controller import Controller


def test_controller():
    test_dir = sys.argv[0]

    assert Controller(test_dir)






