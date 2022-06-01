"""Contains all functions that concern the sqlite database"""

from pathlib import Path
import sqlite3
from os import path, makedirs
import logging


def getHomeAddress():
    """get the home address (e.g. 'C:/Users/alex')"""
    logging.debug("home address at: {}".format(Path.home()))
    return Path.home()


def databaseCreate():
    """Creates the database and directory depending on what exists"""
    home = getHomeAddress()
    dbAddress = ".OnkoMiniproject"
    fullPath = path.join(home, dbAddress, 'Onko.db')
    partialPath = path.join(home, dbAddress)

    if not path.exists(partialPath):
        logging.debug("Path in home directory non-existent. Making directory")
        makedirs(partialPath)
    if not path.exists(fullPath):
        logging.debug("database file non-existant. Making file")
        conn = sqlite3.connect(fullPath)
        conn.execute('''CREATE TABLE USER_PREFERENCES
                     (ID INT(3) PRIMARY KEY    NOT NULL,
                     WIDTH          INT(5)    NOT NULL,
                     HEIGHT         INT(5)     NOT NULL);''')
        logging.debug("inserting default values: 1500, 500")
        sql = "INSERT INTO USER_PREFERENCES (ID, WIDTH, HEIGHT) VALUES ({},{},{})".format(1, 1500, 500)
        conn.execute(sql)
        conn.commit()
        conn.close()
        logging.info("database creation successful")


def insertData(width, height, id=1):
    """Updates the sqlite database"""
    home = getHomeAddress()
    dbAddress = ".OnkoMiniproject"
    fullPath = path.join(home, dbAddress, 'Onko.db')
    if path.exists(fullPath):
        logging.debug("Database file found. updating now")
        conn = sqlite3.connect(fullPath)
        sql = "UPDATE USER_PREFERENCES set WIDTH = {}, HEIGHT = {} WHERE ID = {}".format(width, height, id)
        conn.execute(sql)
        conn.commit()
        conn.close()
    else:
        logging.debug("no database file found. Creating now")
        databaseCreate()
        insertData(width, height)


def getData(id=1):
    """executes the select statement to get the data from the database"""
    home = getHomeAddress()
    dbAddress = ".OnkoMiniproject"
    fullPath = path.join(home, dbAddress, 'Onko.db')
    if path.exists(fullPath):
        conn = sqlite3.connect(fullPath)
        sql = "SELECT WIDTH, HEIGHT FROM USER_PREFERENCES WHERE ID = {}".format(id)
        cursor = conn.execute(sql)
        out = []
        for i in cursor:
            out.append(i)
        logging.debug("sql select successful")
        return out
    else:
        logging.debug("no database file found. Creating now")
        databaseCreate()
        return getData()
