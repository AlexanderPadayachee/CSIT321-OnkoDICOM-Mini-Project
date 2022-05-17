import os
import warnings
import sys
import platform
import logging
import PySide6
from Controller.Controller import Controller


# I did this to use pytest/CI on it, hope it's ok - Allen
def main():
    rootDir = sys.argv[0]
    logging.info("startup success")

    # GUI setup
    app = PySide6.QtWidgets.QApplication(sys.argv)

    mainController = Controller(rootDir)
    logging.info("GUI init Successful")

    mainController.showWindow()
    app.exec()
    logging.info("GUI exec Successful")


if __name__ == "__main__":
    main()

    sys.exit()
