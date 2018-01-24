from __future__ import print_function

import pandas as pd
import urllib
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Set plot style to ggplot
plt.style.use('ggplot')

# Assign server url
params = urllib.quote_plus(
    "DRIVER={SQL Server}"
    "SERVER=mssqlserver.c8cjbzkwrzed.us-west-2.rds.amazonaws.com"
    "DATABASE=machine"
    "UID=sssilvar;PWD=123Change"
)

# Create engine
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

# Query from pandas

df = pd.read_sql('SELECT * FROM iris', engine)

df.hist(column=[df.keys()], bins=20, xrot=60)
plt.show()
