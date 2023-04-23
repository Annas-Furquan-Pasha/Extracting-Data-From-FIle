# Extracting data from file

import pandas as pd

filename = 'data1.csv'

data = pd.read_csv(filename)

print('printing complete data frame')
print(data , end='\n\n')

print('printing first five items in data frame')
print(data.head(), end='\n\n')

print('printing first 10 items in data frame')
print(data.head(10), end='\n\n')

print('printing last 5 items in data frame')
print(data.tail(), end='\n\n')

print('printing last 10 items in data frame')
print(data.tail(10), end='\n\n')