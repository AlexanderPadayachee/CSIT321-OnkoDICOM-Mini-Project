import pytest
import os

from View.Preferences import *


def test_get_home_address():
    assert getHomeAddress()


def test_database_create():
    databaseCreate()


def test_insert_data():
    insertData(1, 1)


def test_get_data():
    assert getData(1)
