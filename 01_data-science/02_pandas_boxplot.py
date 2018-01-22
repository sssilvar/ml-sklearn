from __future__ import print_function

import pandas as pd
import matplotlib.pyplot as plt

# Set plot style
plt.style.use('ggplot')

# Load DataFrame
df = pd.read_csv('librarians-by-msa.csv', index_col=0)

# Create a boxplot from jobs per state
df.boxplot('jobs_1000', 'prim_state', rot=60)
plt.show()
