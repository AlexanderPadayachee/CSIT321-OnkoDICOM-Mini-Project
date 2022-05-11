from code import interact
import glob
import os
import tkinter
from matplotlib.collections import PolyCollection
import numpy as np
import pydicom as dicom
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import imageio
from IPython import display
from skimage import img_as_ubyte
import plotly
from plotly.graph_objs import *

def load_scan(path):
    slices = [dicom.dcmread(path + '/' + s) for s in os.listdir(path)]
    slices = [s for s in slices if 'SliceLocation' in s]
    slices.sort(key = lambda x: int(x.InstanceNumber))
    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)
    for s in slices:
        s.SliceThickness = slice_thickness
    return slices

def get_pixels_hu(scans):
    image = np.stack([s.pixel_array for s in scans])
    image = image.astype(np.int16)
    # Set outside-of-scan pixels to 0
    # The intercept is usually -1024, so air is approximately 0
    image[image == -2000] = 0
    
    # Convert to Hounsfield units (HU)
    intercept = scans[0].RescaleIntercept
    slope = scans[0].RescaleSlope
    
    if slope != 1:
        image = slope * image.astype(np.float64)
        image = image.astype(np.int16)
        
    image += np.int16(intercept)
    
    return np.array(image, dtype=np.int16)

def get_file_path():
    global file_path
    # Open directory of dicom files 
    file_path = filedialog.askdirectory(
        title = "Select A Patient Directory" 
    )
    # Open single dicom files 
    # file_path = filedialog.askopenfilename(
    #     title = "Select A File", 
    #     filetypes = (("Dicom Files", "*.dcm"), ("All Files", "*.*"))
    # )     
    l1 = Label(
        window, 
        text = "Dicom image: ").pack()
    
window = Tk()
window.geometry("600x600")

# # Creating a button to search the file
b1 = Button(window, height = 2, width = 10, text = "Open Folder", command = get_file_path).pack()

window.mainloop()

patient_path = file_path 
patient_dicom = load_scan(patient_path)
patient_pixels = get_pixels_hu(patient_dicom)

imageio.mimsave('./pat001.gif', patient_pixels, duration=0.1)
display.Image('./pat001.gif', format='png')

# plt.figure(1)
# plt.title('Dicom File')
# x = dicom.dcmread(file_path)
# plt.imshow(x.pixel_array, cmap=plt.cm.bone)
# plt.show()

# x = dicom.dcmread(file_path)
# plt.imshow(x.pixel_array, cmap=plt.cm.gray)
# plt.show()