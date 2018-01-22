from __future__ import print_function

import pandas as pd

# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read all sheets in excel: xl
xl = pd.read_excel(url, sheet_name=None)

# Print the sheetnames
keys = xl.keys()

for i, key in enumerate(keys):
    print('The key number %d is %s \n' %(i+1, key))

# Print the head of the first sheet (using its name NOT its index)
print(xl[keys[0]].head())
