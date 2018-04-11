# Ger Hanlon, 10.04.2018
# Iris Data Analysis, this script can be run in ipython and shows the mean of the first column.
# ipython can also be edited interactively to return the max or the min values of the first column with a graph from matplotlib

# Calculate the mean of each column
import numpy
import pandas


# read data file into array
data = numpy.genfromtxt('Iris head.csv', delimiter=',')



firstcol = data[:,0]

meanfirstcol = numpy.mean(data[:,0])

print("Average of the first column is: ", meanfirstcol)

import matplotlib.pyplot as pl
pl.hist(firstcol)
pl.show()
