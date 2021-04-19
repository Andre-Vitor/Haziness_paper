# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 10:48:08 2021

@author: André Vitor
"""

import streamlit as st
import numpy as np
import cv2 as cv
import glob
from functions import *
import pandas as pd
import os


st.title('Haziness')

st.write("This web app calculates the Haziness measure.")
st.write("""
         It can also calculate RMS, Histogram Spread,
         Michelson, Weber and Rizzi metrics.
         """)

calc_rms = st.checkbox('RMS')
calc_Weber = st.checkbox('Weber')
calc_Michelson = st.checkbox('Michelson')
calc_Rizzi = st.checkbox('Rizzi')
calc_HS = st.checkbox('Histogram Spread')

N = st.number_input("Select number of iterations: ",min_value=1, step=1)
s = st.number_input("Select the size of the patches: ",min_value=1, step=1)

# import libraries
import streamlit as st
import tkinter as tk
from tkinter import filedialog

# Set up tkinter
root = tk.Tk()
root.withdraw()

# Make folder picker dialog appear on top of other windows
root.wm_attributes('-topmost', 1)

# Folder picker button
# st.title('Folder Picker')
# st.write('Please select a folder:')
# clicked = st.button('Folder')
# if clicked:
#     dirname = st.text_input('Selected folder:', filedialog.askdirectory(master=root))

# files = glob.glob(os.path.join(dirname,'/*'))
multiple_files = st.file_uploader("Select files: ",accept_multiple_files=True)
if multiple_files is None:
    st.text("No upload")
else:
    files = [file.name for file in multiple_files]
    st.text("\n".join(files))
# st.write(multiple_files[0].)
    
if len(files) == 0:
    print("""
The program couldn't identify the folder.
Please check if the name of the folder is 'Images'.
And it is not empty.
          """)

from PIL import Image, ImageOps
# st.image(multiple_files[0],use_column_width='auto')
values = []
for file in multiple_files:
#     file2 = file.split("\\")[1]
    print(f'Calculating for {file.name}')
#     file = cv.imread(file, 0)
    
    img = Image.open(file)
    img = ImageOps.grayscale(img)
    img = np.asarray(img)
    x, y = haziness_mean_std(img, N, s)
    values.append([file.name, round(x, 4), round(y, 4)])
st.write(values)
DF = pd.DataFrame(values,columns=["Name", "Value", "Std"])
st.write(DF)
# st.write(files)
# if agree:
#     st.write('Great!')


# N = int(input("Select number of iterations: "))
# s = int(input("Select the size of the patches: "))


# files = glob.glob('Test_images\*')
# if len(files) == 0:
#     print("""
# The program couldn't identify the folder.
# Please check if the name of the folder is 'Images'.
# And it is not empty.
#           """)

# files.sort()

# values = []
# for file in files:
#     file2 = file.split("\\")[1]
#     print(f'Calculating for {file2}')
#     file = cv.imread(file, 0)
#     x, y = haziness_mean_std(file, N, s)
#     values.append([file2, round(x, 4), round(y, 4)])
# # print(values)

# print('Done')
# DF = pd.DataFrame(values)
# header = ["Name", "Value", "Std"]
