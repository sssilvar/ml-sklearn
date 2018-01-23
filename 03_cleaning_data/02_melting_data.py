from __future__ import print_function

import pandas as pd
import os

# Assign dataset path
dataset_path = os.path.join('..', 'datasets', 'airquality.csv')

# Load dataset as DataFrame and print its head
airquality = pd.read_csv(dataset_path)
print('\n[  OK  ] === Non-melted DataFrame === \n', airquality.head())

# Melt others but Month and Day and print its head
airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')
print('\n[  OK  ] === Melted DataFrame === \n', airquality_melt.head())

# Pivot the DataFrame and print the head again
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')
print('\n[  OK  ] === Pivoted back DataFrame == \n', airquality_pivot.head())

# Reset index (disable hierarchical indexing)
airquality_pivot = airquality_pivot.reset_index()
print('\n[  OK  ] === Pivoted back DataFrame (Index reset) == \n', airquality_pivot.head())

# Add a duplicated data
airquality = airquality.append([42.0, 191, 7.6, 69, 5, 1])

#
