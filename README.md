# CSIT321 OnkoDICOM Mini Project

quick MVC refresher -https://www.youtube.com/watch?v=DUg2SWWK18I&ab_channel=WebDevSimplified

Model - interacts with database (DICOM file), returns data to controller. Handles validation, saving and updating of data.
View - Presents data. Should nevere send/recive data to and from model.
Controller - All user requests flow through here. Minimal amount of code.


Current state of code:
	Upon running and slecting a folder that contains dcm files, the dcm files are stored in the
	controller class attribute "self.dcmData" as an array of pydicom objects.
	The window also changes to the window that will act as the display window.


