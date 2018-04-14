# Ger Hanlon, 14.04.2018
# Iris Data Analysis

# Calculate the mean of the petal lengths
import numpy
import pandas

# read data file into array seperated by commas
data = numpy.genfromtxt('Iris head.csv', delimiter=',')

thirdcol = data[:,2] # read column 2- the thrid column

meanthirdcol = numpy.mean(data[:,2])

print("Average of the third column is: ", meanthirdcol)

import matplotlib.pyplot as pl
pl.hist(thirdcol) # prints a histogram detailing the Petal Lengths
pl.show()
