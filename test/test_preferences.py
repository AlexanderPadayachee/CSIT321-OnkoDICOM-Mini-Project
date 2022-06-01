import pytest
import os

from View.Preferences import *


def test_home_address_fail():
    """
    Test to ensure that the getHomeAddress method
    only outputs the home directory of the user
    """
    test_path = os.getcwd()
    assert str(getHomeAddress()) != test_path


def test_get_home_address():
    """
    Test to ensure that getHomeAddress returns
    the home directory as per the os of the user
    (e.g. 'C:/Users/alex')
    """
    test_path = os.path.expanduser('~')
    assert str(getHomeAddress()) == test_path


def test_database_create():
    databaseCreate()


def test_insert_data():
    insertData(1, 1)


def test_get_data_exists():
    """
    Test to see if something exists within getData
    """
    assert getData() != [(0, 0)]


def test_get_data():
    """
    Test to see if getData has an output
    """
    assert getData() == [(1, 1)]
