# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:17:17 2020

Chapter 5 of Python Crashcourse

@author: mathieu.pinger
"""

### Some confusion with lists and atomic vectors
# This string is not globally changed by the upper method:
car = 'audi'
car.upper()
print(car)

# This list however is globally changed by the append method
cars = ['audi', 'BMW']
cars.append('peugeot')
print(cars)

# By the way, how to change the case of a string list?
# List comprehension:
cars = [brand.upper() for brand in cars]

# Conditional testing on local variables
car.upper() == 'AUDI' # True

# for with if
for brand in cars:
    if brand.lower() == 'audi':
        print(brand)

# conditional remove
cars = [brand for brand in cars if brand.lower() != 'audi']

# logical and/or
# finding elements in a list
cars.append('MERCEDES')
if 'BMW' in cars or 'MERCEDES' in cars:
    print('There are some expensive cars in the list')

if 'BMW' in cars and 'MERCEDES' in cars:
    print('There are many expensive cars in the list')
else:
    print("There's not that much in the list!")
    
# elements NOT in a list
cars.remove('BMW')
if 'BMW' not in cars:
    print("Get yourself a decent car!")

# Checking whether a list is not empty
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")