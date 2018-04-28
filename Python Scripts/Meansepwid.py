# Ger Hanlon, 10.04.2018
# Iris Data Analysis
# Calculate the mean of the sepal widths


import numpy #Import the panda library- his library is used for data manipulation and analysis
import pandas # Import the numpy library- This library is useful for adding support for large, multi-dimensional 
              # arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays

# read data file into array seperated by commas
data = numpy.genfromtxt('Iris head.csv', delimiter=',')

secondcol = data[:,1] # read column 1- the second column

meansecondcol = numpy.mean(data[:,1]) # call column 1 the meansecondcol be be referenced again

print("Average of the second column is: ", meansecondcol) #print the average of the second coulmn

import matplotlib.pyplot as pl #Import the plotting framework from matplot and reference it as mpl
pl.hist(secondcol) # prints a histogram detailing the Sepal Widths
pl.show()
