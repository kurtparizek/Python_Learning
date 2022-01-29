# NumPy Basics

# Great Resource - https://www.w3schools.com/python/numpy/default.asp

#NumPy is a Python library.
#NumPy is used for working with arrays.
#NumPy is short for "Numerical Python"

#Import the numpy library
import numpy as np

#The array object in NumPy is called ndarray
#We can create a NumPy ndarray object by using the array() function.
arr = np.array([1,2,3,4])
print(arr)
print(type(arr))

#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method
arr2 = np.array((1,2,3,4))
print(arr2)

arr2 = np.arange(0,10)
print(arr2)

arr2 = np.arange(0,11,2)
print(arr2)

arrz = np.zeros(3)
print(arrz)

arro = np.ones(3)
print(arro)

arr7 = np.linspace(0,10,50)
print(arr7)

#2-D Array
arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3)

arrz = np.zeros((5,5))
print(arrz)

arro = np.ones((3,3))
print(arro)

arre = np.eye(4)
print(arre)

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)

l = arr_2d[[[0],[2]],[[1],[2]]]
print(l) #[10,45]
print('#dims of l:',l.ndim)

#3-D Array - An array that has 2-D arrays (matrices) as its elements
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr4)

#NumPy Arrays provides the ndim attribute 
#that returns an integer that tells us how many dimensions the array have.
print(arr.ndim)
print(arr2.ndim)
print(arr3.ndim)
print('number of dimensions :', arr4.ndim)

#Indexing
#You can access an array element by referring to its index number.
print(arr2[1]) #2

#To access elements from 2-D arrays we can use comma 
# separated integers representing the dimension and the index of the element.
print(arr3[1,2]) #6

#Use negative indexing to access an array from the end.
arr5 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr5[1, -1]) #10

arr2d = np.zeros((10,10))
arr_length = arr2d.shape[1]
for i in range(arr_length):
    arr2d[i] = i
    
print(arr2d[[2,4,6,8]])

#Allows in any order
arr2d[[6,4,2,7]]

#Slicing Arrays
#Slicing in python means taking elements from one given index to another given index.
#If we don't pass start its considered 0
#If we don't pass end its considered length of array in that dimension
#If we don't pass step its considered 1
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #[2,3,4,5,6]
print(arr[:4]) #[1,2,3,4]

#Use the minus operator to refer to an index from the end:
print(arr[-3:-1]) #[5,6]
print(arr[1:5:2]) #[2,4]

#Return every other element from the entire array:
print(arr[::2]) 

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2[1,2:]) #[8,9,10]

arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr3)
print(arr3[0:2,2]) #[3,8]

#Broadcasting
arr9 = np.arange(0,11)
print(arr9)
arr9[6:] = 99
#Now note the changes also occur in our original array!
print(arr9)

#To get a copy, need to be explicit
arr_copy = arr9.copy()
print(arr_copy)

#Selection
arr10 = np.arange(1,11)
print(arr10>4) #[False False False False False True True True True True True]
bool_ar = arr10>4
print(arr10[bool_ar])

#Shape
#NumPy arrays have an attribute called shape that returns a
#tuple with each index having the number of corresponding elements.
arr11 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr11.shape) #(2,4)

#Re-Shape
arr12 = np.ones(12)
arr12 = arr12.reshape(4,3)
print(arr12)

#Use re-shape(-1) to flatten an array
arr13 = np.array([[1, 2, 3], [4, 5, 6]])
arr13 = arr12.reshape(-1)
print(arr13)

#Numpy Data Types
"""
Below is a list of all data types in NumPy and the characters used to represent them.

    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )
"""

#To return the type of an array, use dtype:
print(arr4.dtype)

#You can create arrays of specific data types:
arr5 = np.array([1, 2, 3, 4], dtype='S')
print(arr5)
print(arr5.dtype)

#Convert the data type of an existing array through using the astype function
#The astype function creates a copy of the array, and then allows you to specify the data type as a parameter
arr6 = np.array([1.1, 2.1, 3.1])
newarr = arr6.astype('i')
print(newarr)
print(newarr.dtype)

np_array = np.array([12,2,17,6,24])
py_list = np_array.tolist() #converting array back to list

#Iterating over Arrays

arr = np.array([1, 2, 3])

for x in arr:
  print(x) 
  
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)

#nditer
#The function nditer() is a helping function that can be used from very basic to very advanced iterations. 
for x in np.nditer(arr):
    print(x)

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x) 
  print(x.dtype)
  
#Joining
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr) 

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=0)
print(arr) 

#Splitting
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

#Searching Arrays
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x) #(array([3, 5, 6],)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x) 

#Sorting
#Note: This method returns a copy of the array, leaving the original array unchanged.
arr = np.array([3, 2, 0, 1])
print(np.sort(arr)) 

#Filtering
#Create a filter array that will return only values higher than 42:
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr) 
