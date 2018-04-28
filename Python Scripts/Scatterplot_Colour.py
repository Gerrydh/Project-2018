import pandas as pd # Import the numpy library and reference it is np- This library is useful for adding support for large, multi-dimensional 
                     # arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays

import numpy as np #Import the panda library and reference it is pd- his library is used for data manipulation and analysis

import seaborn as sns #Import the seaborn library, this is useful for statistical graphs

import matplotlib.pyplot as plt #Import the matplot library and reference it is mpl

from sklearn.model_selection import train_test_split #Split arrays or matrices into random train and test subsets

df = pd.read_csv('Iris head.csv') #read the csv file Iris Head into the dataframe(df)

print(df.isnull().any()) #check if any of the values are not a number
Sepal Length    False
Sepal Width     False
Petal length    False
Petal Width     False
Species         False
dtype: bool

all_inputs =df[['Sepal Length', 'Sepal Width', 'Petal length', 'Petal Width']].values

all_classes = df['Species'].values

(train_inputs, test_inputs, train_classes, test_classes) =train_test_split(all_inputs, all_classes, train_size=0.7, random_state=1)
    
plt.show()
    
