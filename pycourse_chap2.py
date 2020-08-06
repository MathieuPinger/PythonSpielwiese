# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:35:38 2020

@author: Mathieu Pinger
"""

# Python Crash Course, Exercises 2.3-2.7

# 2.3 Personal Message (and some format + newlines)
name = "Cagatay Guersoy"
message = f"Look {name}! I'm learning Python"
print(message)
message1 = "Look "
message2 = "I'm learning Python"
print("{0} {1}\n{2}".format(message1, name, message2))
print("Look {0}\n\tI'm learning Python".format(name))

# 2.4 Name Cases
print(name.lower())
print(name.upper())
print(name.title())

# 2.5 Quote
quote = 'Morgenstern: "In allem pulsieren, an nichts sich verlieren"'
print(quote)

# 2.6 Another quote
name = "Morgenstern"
message = f'{name}: "In allem pulsieren etc pp"'
print(message)