
from View.Preferences import *
from View.DisplayWindow import DisplayWindow

class View():
    def __init__(self, controller, root_dir=None):
        databaseCreate()
        self.userPref = getData()
        # controller is referenced here, but only to create a communication between the view and the controller.
        # It is referenced in the init, and is not in any other functions.
        self.displayWindow = DisplayWindow(self,controller, self.userPref)



    def ButtonTest(self):
        print("check")


    def show_main(self):  # View Function
        self.displayWindow.show()

    def alert(self, stringIn):
        self.displayWindow.alert(stringIn)