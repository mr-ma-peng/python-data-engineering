import sqlite3
import pandas as pd

conn = sqlite3.connect('staff.db')
table_name = 'INSTRUCTOR'

query_statement = f'select * from {table_name}'
query_output = pd.read_sql(query_statement, conn)

print(query_output)

conn.close()
