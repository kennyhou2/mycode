import pandas as pd
import sqlite3

con = sqlite3.connect("challenge.db")

# Load the data into a DataFrame
thursday_df = pd.read_sql_query("SELECT * from thursday", con)

# Select only data for 2002
band1 = thursday_df[thursday_df.ID == 1]

# Write the new DataFrame to a new SQLite table
band1.to_sql("band1", con, if_exists="replace")

# Read sqlite query results into a pandas DataFrame
df = pd.read_sql_query("SELECT * from band1", con)

# Verify that result of SQL query is stored in the dataframe
print(df.head())

con.close()
