# CSIT321 OnkoDICOM Mini Project

Current state of code:
	Upon running and slecting a folder that contains dcm files, the dcm files are stored in the
	controller class attribute "self.dcmData" as an array of pydicom objects.
	The window also changes to the window that will act as the display window.

How to run
-
Install python on your machine\
Windows	- https://realpython.com/installing-python/#how-to-install-python-on-windows \
macOS	- https://realpython.com/installing-python/#how-to-install-python-on-macos \
linux	- https://realpython.com/installing-python/#how-to-install-python-on-linux

Ensure you are in the directory such that your terminal is at

	../CSIT321-OnkoDICOM-Mini-Project/

Now install the requirements, make sure the pre-requirements.txt are installed before requirements.txt
	
	pip install -r pre-requirements.txt
	pip install -r requirements.txt

The program should be good to go!

Running the program:

	python main.py


