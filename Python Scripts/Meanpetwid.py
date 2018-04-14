# Ger Hanlon, 14.04.2018
# Iris Data Analysis

# Calculate the mean of the petal widths
import numpy
import pandas

# read data file into array seperated by commas
data = numpy.genfromtxt('Iris head.csv', delimiter=',')

forthcol = data[:,3] # read column 3- the forth column

meanforthcol = numpy.mean(data[:,3])

print("Average of the forth column is: ", meanforthcol)

import matplotlib.pyplot as pl
pl.hist(forthcol) # prints a histogram detailing the Petal Widths
pl.show()
