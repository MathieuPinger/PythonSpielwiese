# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 15:13:07 2020

@author: mathieu.pinger
"""

# Function with optional arguments
# '' and none create optional arguments
# None acts as a logical False

def name_infos(first_name, last_name, middle_name='', age=None):
    info = {'first': first_name,
            'last': last_name,
            'middle': middle_name}
    if age:
        info['age'] = age
    return(info)

PI = name_infos('Peter', 'Kirsch', age=50)

print(PI)

# local vs global variables
# in Python, variables passed to functions can be globally changed
# if not desired, use [:] for slice copy

def create_stuff(letters, numbers):
    stuff =  {'letters': letters,
              'numbers': numbers}
    return(stuff) # local variable: without return, nothing happens

# slicing when variables are changed by the function
# This function removes elements from the first list:
not_preprocessed = ['VP_1', 'VP_2', 'VP_3']
preprocessed = []

def preprocessing(to_process, processed_list):
    while to_process:
        current_VP = to_process.pop()
        processed_list.append(current_VP)
        print(f"Preprocessing: {current_VP}.")
    
preprocessing(not_preprocessed, preprocessed)

# Using slicing, the first list stays untouched:
not_preprocessed = ['VP_1', 'VP_2', 'VP_3']
preprocessed = []
preprocessing(not_preprocessed[:], preprocessed)

# arbitrary number arguments creates tuples
def make_pizza(dough, cheese, *toppings):
    print("You ordered the following pizza:")
    print(f"\n{dough.title()} dough, {cheese} cheese,")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('italian', 'cheddar', 'tuna', 'bulgur', 'toenails')

# arbitrary keyword arguments create dictionaries
def make_pizza_dict(dough, cheese, **pizza_info):
    pizza_info['dough'] = dough
    pizza_info['cheese'] = cheese
    return(pizza_info)

pizza_orders = make_pizza_dict('Italian', 'Cheddar', fish='tuna', fruit='olives')
print(pizza_orders)