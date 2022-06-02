"""View Class. This class handles the creation and updating of
all GUI elements. Conforms to MVC
Pylint score is 0/10 for missing imports, but imports work
fine"""

import logging
from View.preferences import database_create, get_data
from View.display_window import DisplayWindow


class View():
    """View Class. creates window and takes commands from controller"""
    def __init__(self, controller):
        """init function for the view object"""
        database_create()
        self.user_pref = get_data()
        # controller is referenced here, but only to create a
        # communication between the view and the controller.
        # It is referenced in the init, and is not in any other functions.
        self.display_window = DisplayWindow(controller, self.user_pref)
        logging.info("View object created successfully")

    @staticmethod
    def button_test():
        """Used to test widgets during development"""
        print("check")

    def show_main(self):
        """part of the QT gui system. Makes the display window visible"""
        self.display_window.show()

    def alert(self, string):
        """When the user needs to determine what happens after an
        error, this creates a dialog box"""
        logging.debug("Alert created for: %s", string)
        self.display_window.alert(string)
