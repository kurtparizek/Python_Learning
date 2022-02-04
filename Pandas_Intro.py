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
print(type(df['W']))

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

booldf = df > 0
print(booldf)
booldf = df[booldf]
print(booldf)

#Returns only the rows that are true:
print(df[df['W']>0])
print(df[df['W']>0]['X'])
print(df[df['W']>0][['Y','X']])

#Doing multiple comparisons at once:
# df[(df['W']>0) and (df['Y']>1)] #Will return an error
multi_col_compare = df[(df['W']>0) & (df['Y']<1)]

#Resetting the matrix - must do in-place if you want to make it permanent
print(df.reset_index())

newind = 'CA NY WY OR'.split()
df['States'] = newind
df.set_index('States')

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df2 = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df2.loc['G1'].loc(1))
df2.index.names = ['Groups','Num']
print(df2.xs('G1'))
print(df2.xs(1,level='Num'))

#Dealing with NaNs
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df3 = pd.DataFrame(d)
print(df3)

#Will drop all of the rows that have a NaN
print(df3.dropna())
print(df3.dropna(thresh=2))
print(df3.fillna(value='FILL VALUE'))

print(df3['A'].fillna(value=df3['A'].mean()))

#Groupby
#Groupby allows you to group rows bassed off of a column and then perform
#an aggregrate function on them
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df4 = pd.DataFrame(data)
byComp = df4.groupby('Company')
print(byComp.mean())
print(byComp.sum().loc['FB'])
print(byComp.count())
print(byComp.describe())

#Merging, joining and Concatenating

#Reading in Data
#To read in an excel file
df5 = pd.read_excel("sales_data.xlsx",sheet_name = "Orders", index_col="Row ID") 
#pd.read_csv() to read in a csv file

print(df5.head())
print(df5.columns)
#To get the data types of the columns
print(df5.dtypes)
# To get information related to numerical columns:
print(df5.describe())
df5["Per Unit Sale"] = df5["Sales"]/df5["Quantity"]

#To convert back to excel
#pd5.to_Excel("data_2.xlsx",index=False)

#Changing data types of columns
df5["Postal Code"] = df5["Postal Code"].astype(str)

#Dealing with date and time
df5["Order Date"] = pd.to_datetime(df5["Order Date"],errors="raise",format="%Y-%m-%d")
df5["month"] = df5["Order Date"].dt.month

df5["String date"] = df5["Order Date"].dt.strftime("%b-%Y")