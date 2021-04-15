# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:02:28 2021

@author: André Vitor
"""

import numpy as np
import cv2 as cv
import glob
from functions import *
import pandas as pd


if __name__ == "__main__":
    N = int(input("Select number of iterations: "))
    s = int(input("Select the size of the patches: "))
    
    files =  glob.glob('Images\*') 
    if len(files) == 0:
        print("""
    The program couldn't identify the folder.
    Please check if the name of the folder is 'Images'.
    And it is not empty.
              """)
              
    files.sort()
    
    values = []
    for file in files:
        print(f'Calculating for {file}')
        file = cv.imread(file,0)
        x, y = haziness_mean_std(file, N, s)
        values.append([round(x,4),round(y,4)])
    # print(values)
    
    print('Done')
    DF = pd.DataFrame(values)
    DF.to_csv("data.csv",index=False)



