import os
import warnings
import sys
import platform
import logging
import PySide6
from Controller.Controller import Controller

if __name__ == "__main__":
    log = logging.getLogger()
    # logging setup
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.getLogger().setLevel(logging.DEBUG)
    logging.basicConfig(filename="OnkoLog.log", format="%(asctime)s %(levelname)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")

    # ROOT DIRECTORY SETUP (not used in code, but is nice to have)
    root_dir = sys.argv[0]
    logging.info("startup success")

    # GUI setup
    #
    app = PySide6.QtWidgets.QApplication(sys.argv)

    main_controller = Controller(root_dir)
    logging.info("GUI init Successful")

    main_controller.show_window()

    # Run GUI
    app.exec()

    # Code below will run when the GUI is closed

    logging.info("GUI exec Successful")
    logging.info("END SESSION \n\n")

    sys.exit()
