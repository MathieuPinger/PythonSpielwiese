# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 11:55:52 2020

@author: mathieu.pinger
"""

"""
Reading a file:
    * with open() and close(): Access file, assign it to a variable, then close
    
    * Safer: with, only keep the file open as long as needed
    
    * read() method
"""

# this imports file as singular string
with open('testnumbers.txt') as file_object:
          testnumbers = file_object.read()
print(testnumbers)

# Cooler version: import as list using list comprehension
#   rstrip strips off \n in every line of the file
with open('testnumbers.txt') as file_object:
          testnumbers = [line.rstrip('\n') for line in file_object]
print(testnumbers)
    
# This breaks the same code up into two bits:
    # assign file to a list containing newline characters
with open('testnumbers.txt') as file_object:
    lines = file_object.readlines()
print(lines)

# remove newline characters with rstrip
for line in lines:
    print(line.rstrip())
    
    
# Mash everything together
onestring = ''
for element in testnumbers:
    onestring += element

"""
Saving a file:
    * 'w' indicate write mode as opposed to read mode (the default)
"""
filename = 'output.txt'

with open(filename, 'w') as file:
    file.write(onestring)
    
"""
Exceptions are objects that occur when a code cannot be executed
    * each exception has a name
    * exceptions stop the program
    * try-except blocks can handle exceptions to continue

Very useful for handling user input!
"""
# dividing by zero: error!
# ZeroDivisionError
print(5/0)

try:
    print(5/0)
except ZeroDivisionError:
    print("Impossible.")

# Using try-except with user input
# multiple exceptions are allowed!
print("Enter two numbers for division.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero.")
    except ValueError:
        print("Please enter numbers!")
    else:
        print(answer)
    
"""
JSON file format
    * stores data in the same object format to share between programs
    * json.dump() and json.load() as functions
"""

# let's create a dictionary
favorite_foods = {'Mathieu': 'Pfannkuchen',
                  'Peter': 'Rosenkohl',
                  'David': 'Instant-Nudeln'}

# json.dump() to save
import json
with open('fav_foods.json', 'w') as f:
    json.dump(favorite_foods, f)
    
# json.load() to retrieve
with open('fav_foods.json') as f:
    copy_favfoods = json.load(f)