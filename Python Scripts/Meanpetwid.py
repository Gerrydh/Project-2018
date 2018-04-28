# Ger Hanlon, 14.04.2018
# Iris Data Analysis
# Calculate the mean of the petal widths


import numpy #Import the panda library- his library is used for data manipulation and analysis
import pandas # Import the numpy library- This library is useful for adding support for large, multi-dimensional 
              # arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays

# read data file into array seperated by commas
data = numpy.genfromtxt('Iris head.csv', delimiter=',')

forthcol = data[:,3] # read column 3- the forth column

meanforthcol = numpy.mean(data[:,3]) # Reference this column as meancolforth

print("Average of the forth column is: ", meanforthcol) #print the mean of the forth column

import matplotlib.pyplot as pl #Import the plotting framework from matplot and reference it as mpl
pl.hist(forthcol) # prints a histogram detailing the Petal Widths
pl.show()
