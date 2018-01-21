from __future__ import print_function

import pandas as pd
from sqlalchemy import create_engine
import urllib


params = urllib.quote_plus(
    "DRIVER={SQL Server Native Client 11.0};"
    "SERVER=DESKTOP-MAL7LCO;"
    "DATABASE=QtyT40I10D100K;"
    "UID=sssilvar;PWD=123Change"
)

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

# Query from pandas
df = pd.read_sql_query('SELECT * FROM DS WHERE [Quantity] = 10', engine)
print('\nSelect all DataFrame: \n', df.head())
print(df.info())
