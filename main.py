import os
import warnings
import sys
import platform
import logging
import PySide6
from Controller.Controller import Controller

if __name__ == "__main__":
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(filename="OnkoLog.log", format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")

    root_dir = sys.argv[0]
    logging.info("startup success")

    # GUI setup
    app = PySide6.QtWidgets.QApplication(sys.argv)

    mainController = Controller(root_dir)
    logging.info("GUI init Successful")

    mainController.show_window()
    app.exec()
    logging.info("GUI exec Successful")
    logging.info("END SESSION \n\n")

    sys.exit()
