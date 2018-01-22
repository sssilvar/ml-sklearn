from __future__ import print_function

import urllib
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


# Set plot style
plt.style.use('ggplot')

# Set up the parameters of the connection
# (You can also use DRIVER={SQL Server Native Client 11.0})
params = urllib.quote_plus(
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-MAL7LCO;"
    "DATABASE=QtyT40I10D100K;"
    "UID=sssilvar;PWD=123Change"
)

# Create an engine for SQL Server using params
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

# Query from pandas
df = pd.read_sql_query('SELECT * FROM DS WHERE ([CustomerID] = 83 AND [Quantity] > 6)', engine)
print('\nSelect all DataFrame: \n', df.head())
print(df.info())
df.hist('Quantity')
plt.show()
