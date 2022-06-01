import pytest
import os

from View.Preferences import *


def test_home_address_not_current_directory():
    test_path = os.getcwd()
    assert str(getHomeAddress()) != test_path


def test_get_home_address():
    test_path = os.path.expanduser('~')
    assert str(getHomeAddress()) == test_path


def test_database_create():
    databaseCreate()


def test_insert_data():
    insertData(1, 1)


def test_get_data():
    test_out = getData()
    print(test_out)
    assert test_out
