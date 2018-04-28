# Ger Hanlon, 10.04.2018
# Iris Data Analysis
# Calculate the mean of the sepal length


import numpy #Import the panda library- his library is used for data manipulation and analysis
import pandas # Import the numpy library- This library is useful for adding support for large, multi-dimensional 
              # arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays

# read data file into array seperated by commas
data = numpy.genfromtxt('Iris head.csv', delimiter=',')

firstcol = data[:,0] # read column 0- the first column

meanfirstcol = numpy.mean(data[:,0]) # call column 0 meanfirstcol to be referenced later

print("Average of the first column is: ", meanfirstcol) # print the mean of the first column

import matplotlib.pyplot as pl #Import the plotting framework from matplot and reference it as mpl
pl.hist(firstcol) # prints a histogram detailing the Sepal Lengths
pl.show()
