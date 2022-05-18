import os
import warnings
import sys
import platform
import logging
import PySide6
from Controller.Controller import Controller


if __name__ == "__main__":
    rootDir = sys.argv[0]
    logging.info("startup success")

    # GUI setup
    app = PySide6.QtWidgets.QApplication(sys.argv)

    mainController = Controller(rootDir)
    logging.info("GUI init Successful")

    mainController.showWindow()
    app.exec()
    logging.info("GUI exec Successful")

    sys.exit()
