from __future__ import print_function

import matplotlib.pyplot as plt
import pandas as pd

# Set plt style
plt.style.use('ggplot')

# Assign url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Read the file into a DataFrame and print its head
df = pd.read_csv(url, sep=';')
print(df.head())

# Plot first colum of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()
