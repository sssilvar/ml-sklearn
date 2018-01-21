from __future__ import print_function

import pandas as pd
from sqlalchemy import create_engine

# Create an engige SQLite
engine = create_engine('sqlite:///Chinook.sqlite')


def get_df_from_db(cmd):
    """
    It gets a command to be executed through the global engine
    :param cmd: a SQL query command.
    """
    global engine
    with engine.connect() as con:
        rs = con.execute(cmd)
        df = pd.DataFrame(rs.fetchall())
        df.columns = rs.keys()
    return df


# Get everything
df = get_df_from_db('SELECT * FROM Album')
print('Everything: \n', df.head())

# Get Title and order it by ArtistId
df = get_df_from_db('SELECT * FROM Album ORDER BY ArtistId')
print('Everything ordered by ArtistId: \n', df.head())

# Get Title and Name and order it by ArtistId
df = get_df_from_db('SELECT * FROM Artist')
print('Title and other ordered by ArtistId: \n', df.head())

# INNER JOIN Album.ArtistId with Artist.ArtistId
df = get_df_from_db('SELECT Title, Name FROM Album INNER JOIN Artist on Album.ArtistId = Artist.ArtistId')
print('Title and Artist Name joined:\n', df.head())
