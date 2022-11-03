import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("challenge.db")
df = pd.read_sql_query("SELECT * from thursday", con)

# Verify that result of SQL query is stored in the dataframe
print(df.head())

con.close()
