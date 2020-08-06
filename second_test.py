# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:13:20 2020

@author: mathieu.pinger
"""

print("what is going on")
print("cagatay is lol")

message = "I lIkE cHeEsE"
print(message)

print(message.title())
message = message.lower()
print(message)

first_name = "Mathieu"
last_name = "Pinger"

print(first_name + last_name)

numbers = [1,2,3]
print(numbers)
print(numbers[0])

# Format Function, F-strings
# {x} is replaced with the value of x
print(f"{first_name} {numbers[2]}")
print(f"{first_name.upper()}, {numbers}")

# tabs and newlines
message = "Can \n\tI \nhaz \n\tCheezeburgerz"
print(message)

# strip whitespace
toowhite = " Can \nI \nHaz cheezeburgerz? "
toowhite
toowhite.rstrip()
toowhite.strip()