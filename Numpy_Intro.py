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

#2-D Array
arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3)

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