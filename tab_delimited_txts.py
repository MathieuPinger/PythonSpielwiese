# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 11:15:44 2020

@author: mathieu.pinger
code by Jason K. Moore https://gist.github.com/moorepants/5136538#file-tab-delimited-py
"""

# Creates a txt file
x = range(10)
funcs = [lambda x: x**2, lambda x: x / 5.0, lambda x: x**3, lambda x: x + 3]
lines = 'x\tx^2\tx/5\tx^3\tx+3\n'
for row in x:
    lines += str(row)
    for col in funcs:
        lines += '\t' + str(col(row))
    if row != 9:
        lines += '\n'
with open('test.txt', 'w') as f:
    f.write(lines)


from numpy import array

f = open('test.txt', 'r') # open the file for reading
data = []
for row_num, line in enumerate(f):
    # Remove the new line at the end and then split the string based on
    # tabs. This creates a python list of the values.
    values = line.strip().split('\t')
    if row_num == 0: # first line is the header
         header = values
    else:
        data.append([float(v) for v in values])
# convert to numpy array        
basic_data = array(data)
f.close() # close the file

# one-liner without headers
from numpy import loadtxt

np_data = loadtxt('test.txt', delimiter='\t', skiprows=1) # skips header
print(np_data)

# with pandas
from pandas import read_csv

pandas_data = read_csv('test.txt', delimiter='\t')
print(pandas_data)