from __future__ import print_function

import pandas as pd
from sqlalchemy import create_engine

# Create engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Query from pandas
df = pd.read_sql_query('SELECT * FROM Album', engine)
print('\nSelect all DataFrame: \n', df.head())

# INNER JOIN
df = pd.read_sql_query('SELECT Title, Name FROM Album INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId', engine)
print(df.head())

