# -*- coding: utf-8 -*-
#Pandas Introduction
#The name "Pandas" has a reference to both "Panel Data", 
# and "Python Data Analysis" and was created by Wes McKinney

import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar) 

#Panda Series
#A Pandas Series is like a column in a table
#It is a one-dimensional array holding data of any type
#Like a numpy array, but is indexed

a = [1,2,3]
myvar2 = pd.Series(a)
print(myvar2)

print(myvar2[0])

#With the index argument, you can name your own labels
b = [1, 7, 2]

myvar3 = pd.Series(b, index = ["x", "y", "z"])
print(myvar3)
print(myvar3["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar4 = pd.Series(calories)
print(myvar4)

func_Series = pd.Series([sum,print,len])

ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
ser2 = pd.Series([1,2,3,4],['USA','China','USSR','Japan'])
print(ser1)

print(ser1['USA'])
print(ser1[0])

sum_series = ser1+ser2
print(sum_series)

#Indexing
myvar5 = pd.Series(calories, index = ["day1", "day2"])
print(myvar5)

#Panda DataFrames
df = pd.DataFrame(randn(5,4),
                  ['A','B','C','D','E'],
                  ['W','X','Y','Z'])

#Selecting Columns
print(df['W'])
print(df[['W','Z']])
print(df.W)

#Creating a new column
df['new'] = df['W'] + df['Y']

#Drop does not happen inplace (false by default) - must set to True
df.drop('new',axis=1, inplace=True)

df.drop('E',axis=0,inplace=True)

print(df.shape)

#Selecting Rows - note: rows are also data series
print(df.loc['A'])
#Indexed based location
print(df.iloc[1])

print(df.loc['B']['Y'])
print(df.loc[['A','B'],['W','Y']])
print(df.iloc[0:2,0:2])

