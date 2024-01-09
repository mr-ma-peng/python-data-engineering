import pandas as pd

# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)

# print(s)
# print(s[2])
# print(s.iloc[3])
# print(s[1:4])
# print(s.values)


# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# print(df)
# print(df['Name'])
# print(df[['Age', 'City']])
# print(df[1:2])
print(df[df['Age'] > 30])
