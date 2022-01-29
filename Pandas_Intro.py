# -*- coding: utf-8 -*-
#Pandas Introduction
#The name "Pandas" has a reference to both "Panel Data", 
# and "Python Data Analysis" and was created by Wes McKinney

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar) 

#Panda Series
#A Pandas Series is like a column in a table
#It is a one-dimensional array holding data of any type

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

#Indexing
myvar5 = pd.Series(calories, index = ["day1", "day2"])
print(myvar5)

#Panda DataFrames