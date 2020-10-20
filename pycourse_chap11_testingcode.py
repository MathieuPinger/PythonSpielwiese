# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:55:23 2020

@author: mathieu.pinger
"""

"""Testing codes with unittests"""

# write a function
def city_country(city, country):
    """Prints a string in the format 'City, Country'"""
    full_string = f"{city}, {country}"
    return full_string.title()

# create unittest
import unittest

class test_cities(unittest.TestCase):
    """Test for city_country"""
    
    def test_city_country(self):
        """Do entries like "london" and "united kingdom" work?"""
        formatted_string = city_country('london', 'united kingdom')
        self.assertEqual(formatted_string, 'London, United Kingdom')
        
    def test_city_country_population(self):
        """Do entries like 'london', 'united kingdom' and '500000' work?"""
        formatted_string = city_country('london', 'uk', '50000000')
        self.assertEqual(formatted_string, 'London, Uk - 50000000')
        
if __name__ == '__main__':
    unittest.main()
    
# rework function
# setting population to '' makes test pass again: optional argument
# also shows error that occurs if no "if else" is added
def city_country(city, country, population=''):
    """Prints a string in the format 'City, Country'"""
    if population:
        full_string = f"{city}, {country} - {population}"
    else:
        full_string = f"{city}, {country}"
    return full_string.title()

""" Testing a class with setUp"""
# new class
class Employee:
    """Takes first name, last name, and salary.
    Stores each of these as attributes.
    Add money to the salary."""
    def __init__(self, first_name, last_name, salary):
        """ Initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
    def give_raise(self, amount = 5000):
        self.new_salary = self.salary + amount
        print(f"New salary: {self.new_salary}")

class test_employees(unittest.TestCase):
    """Test for Class Employee"""
    
    def setUp(self):
        """Create an employee"""
        self.example = Employee("Herbert", "Trulla", 6000)
        
    def test_give_default_raise(self):
        """Test default give_raise"""
        self.example.give_raise()
        self.assertEqual(self.example.new_salary, 11000)
        
    def test_give_custom_raise(self):
        """Test custom give_raise"""
        self.example.give_raise(2000)
        self.assertEqual(self.example.new_salary, 8000)

if __name__ == '__main__':
    unittest.main()