"""Contains all functions that concern the sqlite database"""

from pathlib import Path
import sqlite3
from os import path, makedirs
import logging


def get_home_address():
    """get the home address (e.g. 'C:/Users/alex')"""
    logging.debug("home address at: %s", Path.home())
    return Path.home()


def database_create():
    """Creates the database and directory depending on what exists"""
    home = get_home_address()
    db_address = ".OnkoMiniproject"
    full_path = path.join(home, db_address, 'Onko.db')
    partial_path = path.join(home, db_address)

    if not path.exists(partial_path):
        logging.debug("Path in home directory non-existent. Making directory")
        makedirs(partial_path)
    if not path.exists(full_path):
        logging.debug("database file non-existant. Making file")
        conn = sqlite3.connect(full_path)
        conn.execute('''CREATE TABLE USER_PREFERENCES
                     (ID INT(3) PRIMARY KEY    NOT NULL,
                     WIDTH          INT(5)    NOT NULL,
                     HEIGHT         INT(5)     NOT NULL);''')
        logging.debug("inserting default values: 1500, 500")
        sql = "INSERT INTO " \
              "USER_PREFERENCES (ID, WIDTH, HEIGHT) " \
              "VALUES ({},{},{})".format(1, 1500, 500)
        conn.execute(sql)
        conn.commit()
        conn.close()
        logging.info("database creation successful")


def insert_data(width, height, user_id=1):
    """Updates the sqlite database"""
    home = get_home_address()
    db_address = ".OnkoMiniproject"
    full_path = path.join(home, db_address, 'Onko.db')
    if path.exists(full_path):
        logging.debug("Database file found. updating now")
        conn = sqlite3.connect(full_path)
        sql = "UPDATE USER_PREFERENCES " \
              "set WIDTH = {}, HEIGHT = {} WHERE ID = {}".format(width, height, user_id)
        conn.execute(sql)
        conn.commit()
        conn.close()
    else:
        logging.debug("no database file found. Creating now")
        database_create()
        insert_data(width, height)


def get_data(user_id=1):
    """executes the select statement to get the data from the database"""
    home = get_home_address()
    db_address = ".OnkoMiniproject"
    full_path = path.join(home, db_address, 'Onko.db')
    if path.exists(full_path):
        conn = sqlite3.connect(full_path)
        sql = "SELECT WIDTH, HEIGHT FROM USER_PREFERENCES WHERE ID = {}".format(user_id)
        cursor = conn.execute(sql)
        out = []
        for i in cursor:
            out.append(i)
        logging.debug("sql select successful")
        return out

    logging.debug("no database file found. Creating now")
    database_create()
    return get_data()
