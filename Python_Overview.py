# Python Basics

# Great Resource - https://www.w3schools.com/python/python_operators.asp

#Python runs on an interpreter system, meaning that code can be executed as soon as it is written

#Python can be treated in a procedural way, an object-oriented way or a functional way.

#The most recent major version of Python is Python 3

#Python uses new lines to complete a command, as opposed to other programming languages which often 
#use semicolons or parentheses.

#Python relies on indentation, using whitespace, to define scope; 
#such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

#Most content is from Jose Portilla's 'Python for Data Science and Machine Learning Bootcamp' course

#DATA TYPES

#Variable Assignment
# Can not start with number or special characters
name_of_var = 2
print(name_of_var) #2
x = 2.0
y = 3
print(x+y) #5.0

#Numbers
print(1 + 3) #4
print(2**4) #16
print(4/2) #2.0
print((2+3)*(5+5)) #50

#Strings
x = """Test""" 
print(x) #'Test'
print('You can put strings in single quotes')
print("You can also put strings in double quotes")
print("You can also 'wrap' single quotes in double quotes")

s = 'hello'
print('The fourth index of the string ' + s + ' is ' + s[4])

#Printing
num = 12
name = 'Sam'
print('My number is: {one}, and my name is: {two}'.format(one=num,two=name))

#Casting
#Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

#Casting Ints
#int() - constructs an integer number from an integer literal, 
# a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
print(int(1))   #1
print(int(2.8)) #2
print(int("3")) #3

#Casting Floats
#float() - constructs a float number from an integer literal, 
# a float literal or a string literal (providing the string represents a float or an integer)
print(float(1)) #1.0
print(float(2.8)) #2.8
print(float("3")) #3.0
print(float("4.2")) #4.2

#Casting Strings
#str() - constructs a string from a wide variety of data types, 
#including strings, integer literals and float literals
print(str("s1")) #'s1'
print(str(2))  #'2'
print(str(3.0)) #'3.0' 

"""
There are four collection data types in the Python programming language:
    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

#Lists
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets
list1 = [1,2,3,4]
print(list1)

my_list = ['a','b','c','d']
print(my_list)
my_list.append('e')
print(my_list)
print('The first element in my_list is ' + my_list[0])
my_list.append('NEW')
print(my_list)

#Can Nest lists wihin lists
my_list.append([10,11,12])
print(my_list)
print(my_list[6][2]) #12

#Dictionaries
#Dictionaries are used to store data values in key:value pairs
#As of Python version 3.7, dictionaries are ordered (items have a defined order that will not change)
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates
d = {'key1':'item1','key2':123}
print(d)

#To select an item in the dictionary, you insert the key:
print(d['key1']) #item1
print(d['key1'][1]) #t

#You can change values in a dictionary
d['key1'] = 'cheese'
print(d['key1']) #item1

# You cannot have 2 of the same key - this will only keep the second key
# d = {'key1':'item1','key1':123}
# print(d)

#You can also nest keys
e = {'k1':{'innerkey':[1,2,3]}}
print(e['k1']['innerkey'][0]) #1

#Tuples
#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are immutable (good for when you don't want the user to change the content)
#Tuples are written with round brackets.

t = (1,2,3)
print(t[0])

#You cannot change a value in a tuple (will return an error)
#t[0] = 'NEW'

#Sets
#A set is defined only by unique elements
#Sets are written with curly braces
#Sets are unorderd, unchangeable and unindexed
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#Once a set is created, you cannot change its items, but you can remove items and add new items.
x = {1,2,3} #{1,2,3}
y = {1,2,3,2,1,2,3,2,1} #{1,2,3}
print(x) 
print(y)
x.add(25)
print(x) #{1,2,3,25}

#Will not print
#print(x[1])

print(len(x))

z = set([1,2,3,4,3])
print(z)

#Booleans and Comparison Operators
#You can evaluate any expression in Python, and get one of two answers, True or False.
tru_val = True
false_val = False
print(tru_val) #True
print(1>2) #False

#Logic Operators
l = (1>2) and (2<3)
print('l is {}'.format(l)) #False

k = (1 > 2) or (2 < 3)
print('l is {}'.format(k)) #True

#If, elif, else statements
if 1 < 2:
    print('Yep!')
    
if 1<2:
    print('1 IS less than 2')
else:
    print('1 IS NOT less than 2')
    
if 1>2:
    print('1 IS greater than 2')
else:
    print('1 IS NOT greater than 2')
    
if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')
    
#For loops
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, 
#and works more like an iterator method as found in other object-orientated programming languages.
seq = [1,2,3,4,5,30]
for item in seq:
    print(item)
    
for item in seq:
    print('Yep')
    
#Break Statement - can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Continue - With the continue statement we can stop the current iteration of the loop, and continue with the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
#Range - To loop through a set of code a specified number of times, we can use the range() function
for x in range(6):
  print(x)
  
# Else in a for loop - The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for x in range(6):
  print(x)
else:
  print("Finally finished!") 
  
#While Loops

i = 1
while i < 5:
    print('hello')
    i=i+1
  
#Break
#With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 

#Range
#range() generates a range object
range(5)
list(range(5))
print(list(range(5)))

#List Comprehension
x = [1,2,3,4]
out = []
for item in x:
    out.append(item**2)
print(out)

print([item**2 for item in x])

#Functions
#A function is a block of code which only runs when it is called.
def my_function():
    """
        Docstring goes here.
    """
    print("Hello from my function")
    
my_function()

#Arguments
#Arguments are often shortened to args in Python documentations.
#You can add as many arguments as you want in a function, 
#just separate them with a comma.
def my_function(fname):
  print(fname + " Refsnes")
  
my_function("Emil")
  
"""
By default, a function must be called with the correct 
number of arguments. Meaning that if your function expects 
2 arguments, you have to call the function with 2 arguments, 
not more, and not less. 

If you do not know how many arguments that will be passed 
into your function, add a * before the parameter name in the 
function definition.
"""
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

"""
The phrase Keyword Arguments are often shortened to kwargs 
in Python documentations.
If you do not know how many keyword arguments that will be 
passed into your function, add two asterisk: 
** before the parameter name in the function definition.
"""
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

"""
The following example shows how to use a default parameter value.

If we call the function without argument, 
it uses the default value:
"""
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 

#Return Values
#To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9)) 

t = my_function(5)
print(t)

#Lambda Expressions
#A lambda function is a small anonymous function.
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6)) 

#The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

t = lambda var: var*2
t(5)

#Map and Filter
# Map - allows for you to apply a function to a sequence

def times2(var):
    return var*2

seq = [1,2,3,4,5]
map(times2,seq)
print(list(map(times2,seq)))

print(list(map(lambda var: var*2,seq)))


print(list(filter(lambda item: item%2 == 0,seq)))

#Methods

