from __future__ import print_function

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Create DataFrame from csv
df = pd.read_csv('dob_job_application_filings_subset.csv')

print(df.info())


# Plot a histogram of 'Existing Zoning Sqft' column
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)
plt.show()
