import sqlite3
import pandas as pd

sql_connection = sqlite3.connect('Movies.db')
query_statement = "SELECT * FROM Top_50"
df = pd.read_sql(query_statement, sql_connection)
print(df)
