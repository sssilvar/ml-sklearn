from __future__ import print_function

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Create DataFrame from csv
df = pd.read_csv('../datasets/dob_job_application_filings_subset.csv')

print(df.info())

# Clean data a bit
df['initial_cost'] = df['Initial Cost'].str.replace('$', '').astype(float)
df.drop(columns='Initial Cost', axis=1)

# # Plot a histogram of 'Existing Zoning Sqft' column
# df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)
# df.boxplot(column='initial_cost', by='Borough', rot=90)
# plt.show()
# plt.clf()
