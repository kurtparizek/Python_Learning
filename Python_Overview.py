# Python Basics

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
t[0] = 'NEW'

#Sets

#Booleans
#You can evaluate any expression in Python, and get one of two answers, True or False.
tru_val = True
false_val = False
print(tru_val) #True
print(1>2) #False

"""
    Booleans
    Comparison Operators
    if, elif, else Statements
    for Loops
    while Loops
    range()
    list comprehension
    functions
    lambda expressions
    map and filter
    methods
"""



