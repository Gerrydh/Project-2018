# Ger Hanlon, 10.04.2018
# Iris Data Analysis

# Calculate the mean of the sepal length
import numpy
import pandas

# read data file into array seperated by commas
data = numpy.genfromtxt('Iris head.csv', delimiter=',')

firstcol = data[:,0] # read column 0- the first column

meanfirstcol = numpy.mean(data[:,0])

print("Average of the first column is: ", meanfirstcol)

import matplotlib.pyplot as pl
pl.hist(firstcol) # prints a histogram detailing the Sepal Lengths
pl.show()
