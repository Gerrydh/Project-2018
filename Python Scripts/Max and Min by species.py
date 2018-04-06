# Ger Hanlon, 06.04.2018
# This code returns the smallest and the largest sepal and petal lenghts and widths by species
# https://stackoverflow.com/questions/49689028/python-iris-data-set-include-the-species/49689170#49689170

import pandas as pd  #Import Pandas
import numpy as np   # Import Numpy



df = pd.read_csv("iris head.csv")

print('The biggest and smallest Sepal Lenght is:', df.groupby(['Species'])['Sepal Length'].agg(['max','min']))
print('The biggest and smallest Sepal Width is:',df.groupby(['Species'])['Sepal Width'].agg(['max','min']))
print('The biggest and smallest Petal Lenght is:',df.groupby(['Species'])['Petal length'].agg(['max','min']))
print('The biggest and smallest Petal Width is:',df.groupby(['Species'])['Petal Width'].agg(['max','min']))
