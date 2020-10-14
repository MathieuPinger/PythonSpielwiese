# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:53:12 2020

Chapter 6 of Python Crashcourse: Dictionaries

@author: mathieu.pinger
"""

# a simple dictionary
favorite_pizza = {'Alan': 'Margharita',
                  'Peter': 'Funghi',
                  'Fungi': 'Funghi',
                  'David': 'Salami',
                  'Elizabeth': 'Veggie'}
# accessing values with brackets and get
favorite_pizza['Alan']
favorite_pizza.get('Peter', 'You did not ask this person!')

# for loops with .items and .key
for name, pizza in favorite_pizza.items():
    print(f"\n{name}'s favorite Pizza is {pizza}.")

print("People we've asked for their favorite pizza:")
for name in favorite_pizza.keys():
    print(name)
    
department = ['Peter', 'Fungi', 'David']

print("Favorite choices in our department:")
for name in favorite_pizza.keys():
    if name in department:
        pizza = favorite_pizza[name].title()
        print(f"\n{name} loves Pizza {pizza}.")
    else:
        print(f"\n{name} doesn't work in our department.")

# looping through dictionaries in order
for name in sorted(favorite_pizza.keys()):
    print(f"Thanks @{name}!")

# Looping through values in a dictionary
for pizza in favorite_pizza.values():
    print(pizza)


# Unique elements in a dictionary with set:
    for pizza in set(favorite_pizza.values()):
        print(pizza)
        
# Creating sets right away: braces and commas, no key/value-associations
pizzas = {"funghi", "proscuitto", "tonno"}

# dictionaries nested in lists
# let's create ten pizzas with random values
import random
topping_options = ['salami', 'funghi', 'tonno']
dough_options = ['italian', 'american']
cheese_options = ['mozzarella', 'gouda', 'gorgonzola']

orders = []
for order_number in range(20):
    new_order = {'number': order_number,
                 'dough': random.choice(dough_options),
                 'topping': random.sample(topping_options, random.choice([1,2,3])),
                 'cheese': random.choice(cheese_options)}
    orders.append(new_order)
    