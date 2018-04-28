# Ger Hanlon, 14.04.2018
# Iris Data Analysis
# Calculate the mean of the petal lengths


import numpy #Import the panda library- his library is used for data manipulation and analysis
import pandas # Import the numpy library- This library is useful for adding support for large, multi-dimensional 
              # arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays

# read data file into array seperated by commas
data = numpy.genfromtxt('Iris head.csv', delimiter=',')

thirdcol = data[:,2] # read column 2- the thrid column

meanthirdcol = numpy.mean(data[:,2]) # call column 3 meanthirdcol to be referenced again

print("Average of the third column is: ", meanthirdcol) # return the mean of this column

import matplotlib.pyplot as pl #Import the plotting framework from matplot and reference it as mpl
pl.hist(thirdcol) # prints a histogram detailing the Petal Lengths
pl.show()
