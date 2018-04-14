# Ger Hanlon, 10.04.2018
# Iris Data Analysis

# Calculate the mean of the sepal widths
import numpy
import pandas

# read data file into array seperated by commas
data = numpy.genfromtxt('Iris head.csv', delimiter=',')

secondcol = data[:,1] # read column 1- the second column

meansecondcol = numpy.mean(data[:,1])

print("Average of the first column is: ", meansecondcol)

import matplotlib.pyplot as pl
pl.hist(secondcol) # prints a histogram detailing the Sepal Widths
pl.show()
