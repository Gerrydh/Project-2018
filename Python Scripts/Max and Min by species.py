# Ger Hanlon, 06.04.2018
# This code returns the smallest and the largest sepal and petal lenghts and widths by species
# https://stackoverflow.com/questions/49689028/python-iris-data-set-include-the-species/49689170#49689170

import pandas as pd  # Import the panda library and reference it is pd- This library is used for data manipulation and analysis
import numpy as np   # Import the numpy library and reference it is np- This library is useful for adding support for large, multi-dimensional 
                     # arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.



df = pd.read_csv("iris head.csv") #read the csv file Iris Head into the dataframe(df)

print('The biggest and smallest Sepal Lenght is:', df.groupby(['Species'])['Sepal Length'].agg(['max','min'])) #Prints the biggest and smallest sepal lenghts including the species
print('The biggest and smallest Sepal Width is:',df.groupby(['Species'])['Sepal Width'].agg(['max','min'])) #Prints the biggest and smallest sepal widths including the species
print('The biggest and smallest Petal Lenght is:',df.groupby(['Species'])['Petal length'].agg(['max','min'])) #Prints the biggest and smallest petal lenghts including the species
print('The biggest and smallest Petal Width is:',df.groupby(['Species'])['Petal Width'].agg(['max','min'])) #Prints the biggest and smallest petal widths including the species
