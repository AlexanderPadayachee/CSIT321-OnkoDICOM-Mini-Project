from pathlib import Path
import sqlite3
from os import path, makedirs


def getHomeAddress():
    return Path.home()


def databaseCreate():
    home = getHomeAddress()
    dbAddress = ".OnkoMiniproject"
    fullPath = path.join(home, dbAddress, 'Onko.db')
    partialPath = path.join(home, dbAddress)

    if not path.exists(partialPath):
        makedirs(partialPath)
    if not path.exists(fullPath):
        conn = sqlite3.connect(fullPath)
        conn.execute('''CREATE TABLE USER_PREFERENCES
                     (ID INT(3) PRIMARY KEY    NOT NULL,
                     WIDTH          INT(5)    NOT NULL,
                     HEIGHT         INT(5)     NOT NULL);''')
        sql = "INSERT INTO USER_PREFERENCES (ID, WIDTH, HEIGHT) VALUES ({},{},{})".format(1, 1500, 500)
        conn.execute(sql)
        conn.commit()
        conn.close()


def insertData(width, height, id=1):
    home = getHomeAddress()
    dbAddress = ".OnkoMiniproject"
    fullPath = path.join(home, dbAddress, 'Onko.db')
    if path.exists(fullPath):
        conn = sqlite3.connect(fullPath)
        sql = "UPDATE USER_PREFERENCES set WIDTH = {}, HEIGHT = {} WHERE ID = {}".format(width, height, id)
        conn.execute(sql)
        conn.commit()
        conn.close()

def getData(id=1):
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
        return out
