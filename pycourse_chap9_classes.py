# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 13:29:07 2020

@author: mathieu.pinger
"""

class Restaurant:
    """Stores information on a restaurant and prints it"""
    
    # initialize object, always include Self!
    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.name = name
        self.cuisine_type = cuisine_type
        
    # methods = functions attached to an object
    def describe_restaurant(self):
        """Print the restaurant info"""
        print(f"{self.name} offers {self.cuisine_type} food.")
        
    def open_restaurant(self):
        """Indicate the restaurant is open"""
        print(f"{self.name} is open!")
        
laperla = Restaurant('La Perla', 'italian')


# calling class methods:
laperla.describe_restaurant()
laperla.open_restaurant()

# tuple of objects: loop over class methods
gianni = Restaurant('Ristorante da Gianni', 'italian')
amara = Restaurant('Amara', 'kurdish')

restaurants = {gianni, amara, laperla}

for infos in restaurants:
    infos.describe_restaurant()
    
# Change attribute values in three ways
# classes can have default values!

class Restaurant:
    """Stores information on a restaurant and prints it"""
    
    # initialize object, always include Self!
    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # default value doesn't need to be added to init
        
    # methods = functions attached to an object
    def describe_restaurant(self):
        """Print the restaurant info"""
        print(f"{self.name} offers {self.cuisine_type} food.")
        
    def open_restaurant(self):
        """Indicate the restaurant is open"""
        print(f"{self.name} is open!")
        
    def set_number_served(self, update):
        """Change the number of served dishes"""
        if update > self.number_served:
            self.number_served = update
            print(f"Number of served tables: {self.number_served}")
        else:
            print("Error: New value must be increment to old value.")
            
    def increment_number_served(self, increment):
        """Add a number to number_served"""
        if increment > 0:
            self.number_served += increment
            print(f"Number of served tables: {self.number_served}")
        else:
            print("Error: Enter positive increment.")
            
laperla = Restaurant('La Perla', 'italian')

# change values with a. direct attribute, b. set method, c. increment method
laperla.number_served = 5
laperla.increment_number_served(1)
laperla.set_number_served(9)

# Child classes

class IceCreamStand(Restaurant):
    """Child class of Restaurant with list of available ice cream flavors"""
    """ also add new attribute: number of tables"""
    """ cuisine type is "Icecream" by default"""
    
    # default value needs to be positioned after *args
    # inherit full __init__ from Restaurant, but set cuisine to default
    # flavors as a tuple
    
    def __init__(self, name, tables, *flavors, cuisine_type = 'Icecream'):
        """Inherit attributes from parent class"""
        super().__init__(name, cuisine_type)
        self.tables = tables # add new attribute
        self.flavors = flavors

    def describe_restaurant(self):
        print(f"{self.name} offers {self.cuisine_type} food.")
        print("This stand offers the following flavors:")
        # print flavors without brackets
        print(*self.flavors, sep = ', ')
    
dajerry = IceCreamStand("Da Jerry", 5, "vanilla", "strawberry")
dajerry.describe_restaurant()
