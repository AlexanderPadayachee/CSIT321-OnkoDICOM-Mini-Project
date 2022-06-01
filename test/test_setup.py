import pytest

from Controller.Setup import *


def test_log_setup():
    """
    Test to make sure that if the right
    parameters are met that 1 is returned
    """
    assert logSetup('TestOnkoLog.log') == 1



