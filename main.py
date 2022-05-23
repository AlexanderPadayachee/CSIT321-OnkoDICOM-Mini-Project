import os
import warnings
import sys
import platform
import logging
import PySide6
from Controller.Controller import Controller


if __name__ == "__main__":

    #logging setup
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(filename  = "OnkoLog.log", format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")

    # ROOT DIRECTORY SETUP (not used in code, but is nice to have)
    rootDir = sys.argv[0]
    logging.info("startup success")


    ## GUI setup
    app = PySide6.QtWidgets.QApplication(sys.argv)

    mainController = Controller(rootDir)
    logging.info("GUI init Successful")

    mainController.showWindow()

    # Run GUI
    app.exec()

    #Code below will run when the GUI is closed

    logging.info("GUI exec Successful")
    logging.info("END SESSION \n\n")

    sys.exit()
