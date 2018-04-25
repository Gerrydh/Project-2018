In [1]: import pandas as pd

In [2]: import pandas as pd

In [3]: import numpy as np

In [4]: import seaborn as sns

In [5]: import seaborn as sns

In [6]: import matplotlib.pyplot as plt

In [7]: from sklearn.model_selection import train_test_split

In [8]: df = pd.read_csv('Iris head.csv')

In [9]: print(df.isnull().any())
Sepal Length    False
Sepal Width     False
Petal length    False
Petal Width     False
Species         False
dtype: bool

In [10]: all_inputs =df[['Sepal Length', 'Sepal Width', 'Petal lengt
    ...: h', 'Petal Width']].values

In [11]: all_classes = df['Species'].values

In [12]: (train_inputs, test_inputs, train_classes, test_classes) =
    ...: train_test_split(all_inputs, all_classes, train_size=0.7, r
    ...: andom_state=1)
    
In [15]: plt.show()
    
