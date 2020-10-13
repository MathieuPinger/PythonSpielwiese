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

# delete with numerical indexing
# del is a STATEMENT
del things[1]
print(things)

# Popped out slices can be reassigned!
# pop is a METHOD
first_thing = things.pop(0)
print(first_thing)
print(things)

# delete by specifying the value
things.remove('startrek')
print(things)
# what happens with multiple values?
# it only removes the first element that matches the string
thingies = ['a', 'a', 'b', 'a', 'c']
thingies.remove('a')
print(thingies)

# sort

# permanently: with sort
things = ["starwars", "lotr", "startrek"]
things.sort()
print(things)

# temporarily: with sorted
things.append('planet of the apes')
print(sorted(things))
print(things)
print(things.reverse())

# Lengths
len(things)
