# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:49:36 2020

@author: Home Office
"""

things = ["starwars", "lotr", "startrek"]
mix = ["starwars", 2, 3, 4, "whatever"]

# append and concatenate

things.append("shutter island")
print(things)
things2 = things + mix
print(things2)

# insert

things.insert(1, "interstellar")
print(things)


# remove with del, pop and remove

del things[1]
print(things)

first_thing = things.pop(0)
print(first_thing)
print(things)

things.remove('startrek')
print(things)

# sort
things.append('planet of the apes')
print(sorted(things))
print(things)
print(things.reverse())