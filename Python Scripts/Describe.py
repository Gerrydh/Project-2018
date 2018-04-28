# Ger Hanlon, 13.04.2018
# The describe function for the 2018 Iris Data-Set project

import pandas as pd # Import the panda library and reference it is pd- his library is used for data manipulation and analysis
import numpy as np # Import the numpy library and reference it is np- This library is useful for adding support for large, multi-dimensional 
                     # arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays 
import matplotlib as pl #Import the matplot library and reference it is pl- 
import matplotlib.pyplot as mpl #Import the plotting framework from matplot and reference it as mpl 

df = pd.read_csv('Iris head.csv') #read the csv file Iris Head into the dataframe(df)

print(df.describe()) #Print the describe function from the dataframe
