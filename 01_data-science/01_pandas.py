from __future__ import print_function

import numpy as np
import matplotlib as plt
import pandas as pd

df = pd.read_csv('librarians-by-msa.csv', index_col=0)
print(df.head())

# Print one column with all the observations
print('[INFO]: Printing a column as a Pandas Series')
data = df['area_name']
print(data, '\n Type: ', type(data))

# Print two columns as Pandas DataFrame
print('[INFO]: Printing two columns as a Pandas DataFrame')
data = df.loc[:, ['area_name', 'tot_emp']]
print(data, '\n Type: ', type(data))