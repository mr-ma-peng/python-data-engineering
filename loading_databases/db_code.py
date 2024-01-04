import sqlite3
import pandas as pd

conn = sqlite3.connect('staff.db')

table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CODE']

file_path = '//loading_databases/INSTRUCTOR.csv'
df = pd.read_csv(file_path)

df.to_sql(table_name, conn, if_exists='replace', index=False)
print('table {} created'.format(table_name))

query_statement = f'select * from {table_name}'
query_output = pd.read_sql(query_statement, conn)

print(query_output)

conn.close()
