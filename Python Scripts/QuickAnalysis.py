import numpy as np #Import the panda library and reference it is pd- his library is used for data manipulation and analysis
import scipy as sp # Import the scipy library and reference it as sp, this library is useful for efficient numerical routines 
                   #such as routines for numerical integration and optimization.
import pandas as pd # Import the numpy library and reference it is np- This library is useful for adding support for large, multi-dimensional 
                     # arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import matplotlib as mpl #Import the matplot library and reference it is mpl
import seaborn as sns #Import the seaborn library, this is useful for statistical graphs

df = pd.read_csv('Iris head.csv'): #read the csv file Iris Head into the dataframe(df)

Print(df.mean()) # Return the mean or average from the dataframe
Print(df.median()) # Return the median from the dataframe
Print(df.std()) # Return the standard deviation from the datafram
