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

    test_path = str(Path.home())
    assert str(getHomeAddress()) == test_path


def test_database_create():
    """
    Create the database to make sure testing can occur
    """
    databaseCreate()


def test_get_data_exists():
    """
    Test to see if something exists within the database
    """
    assert getData() != [(0, 0)]


def test_get_data_default_values():
    """
    Test default values for the database
    """
    assert getData() == [(1500, 500)]


def test_get_data():
    """
    Test to see if the data within the database is changed based on insertData
    """
    insertData(1, 1)
    assert getData() == [(1, 1)]
