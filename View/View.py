"""View Class. This class handles the creation and updating of all GUI elements. Conforms to MVC """

from View.Preferences import *
from View.DisplayWindow import DisplayWindow
import logging


class View():
    def __init__(self, controller, root_dir=None):
        """init function for the view object"""
        databaseCreate()
        self.userPref = getData()
        # controller is referenced here, but only to create a communication between the view and the controller.
        # It is referenced in the init, and is not in any other functions.
        self.displayWindow = DisplayWindow(self, controller, self.userPref)
        logging.info("View object created successfully")

    @staticmethod
    def buttonTest():
        """Used to test widgets during development"""
        print("check")

    def show_main(self):
        """part of the QT gui system. Makes the display window visible"""
        self.displayWindow.show()

    def alert(self, string):
        """When the user needs to determine what happens after an error, this creates a dialog box"""
        logging.debug("Alert created for: {}".format(string))
        self.displayWindow.alert(string)
