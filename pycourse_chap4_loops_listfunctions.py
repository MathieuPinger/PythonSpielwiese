# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:06:05 2020

Chapter 4 of Python Crash Course

@author: mathieu.pinger
"""

""" Slicing vs Assigning """

# Assigning a new variable name to a list does NOT CREATE A NEW LIST!
list_1 = ['a', 'b', 'c']
list_2 = list_1
print(list_2)
# list_1 and list_2 point to the same object: both are changed
list_1.append('d')
print(list_2)

# Copy a list with full indexing [:]
list_3 = list_1[:]
print(list_3)
list_1.pop(-1)
list_3

# Slicing (indexing)
# starts at 0!
print(list_3[1])
print(list_3[1:3])
print(list_3[0:4])

# omit first value for "all elements until Xth value"
print(list_3[:3])
# omit second value for "all elements from Xth value
print(list_3[3:])

""" loops and loop comprehensions """
# loops with indentation and colon
list_4 = []
for element in list_3:
    list_4.append(element.title())

num_list =  []
for value in range(10,101,10):
    num_list.append(value ** 2)

# list comprehensions
num_list_2 = [value-33 for value in num_list]

""" tuples """
# Tuples are lists whose items cannot be reassigned
# Create them with parentheses and always a comma
tuple_1 = (1,2,3)
# give error messages:
tuple_1.append(4)
tuple_1[0] = 2

# but tuples can be reassigned as a whole
tuple_1 = (2,3,4)
