# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:36:14 2020

@author: mathieu.pinger

Let's create a program that asks users for some information:
    ID, Age, Number of Siblings
Save data into json file.

If JSON (= ID.json) exists already:
    Load json file and continue with next question (Favorite Food) + append.
If JSON doesn't exist:
    Ask for initial data and save.
"""

# Chunk to clear console
try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    pass


import json

""" Enter user ID and raise error if not integer value"""


def get_user_id():
    """ Prompt for entering User ID in the correct format.
    Returns correct User ID."""
    
    # flag for while-Loop: continue until correct ID format is entered
    incorrect_id = True
    while incorrect_id:
        print("Press 'q' to quit.")
        user_input = input("Please enter your ID here:")
        if user_input == 'q':
            break
        # check numeric input
        try:
            int(user_input)
        except ValueError:
            print("Please enter a numeric ID!")
        else:
            # check length of input = 5
            if len(user_input) != 5:
                print("Please enter 5 numbers as your ID.")
            else:
                # safe user_id
                user_id = user_input
                incorrect_id = False
                return user_id
    


# Function: Load file
def load_user_info(user_id):
    """Load stored user info if available"""
    
    filename = f"{user_id}.json"
    try:
        with open(filename) as f:
            user_info = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user_info
        
# Function: enter initial userinfo
def first_user_info(user_id):
    """Create a dictionary with first user info"""
    active = True
    print("Press 'q' in any question to quit.")
    while active:
        # ask for age and siblings, controlling for data type
        age = input("Please enter your age (in numbers): ")
        if age == 'q':
            break
        try:
            int(age)
        except ValueError:
            age = input("Error: Please enter a number: ")
            if age == 'q':
                break
        
        siblings = input("How many siblings do you have? If none, enter 0: ")
        if siblings == 'q':
            break
        try:
            int(siblings)
        except ValueError:
            siblings = input("Error: Please enter a number: ")
            if siblings == 'q':
                break
        
        # generate user info dictionary
        user_info = {'ID': user_id,
                     'age': age,
                     'siblings': siblings}
        return(user_info)
        active = False


# Function: enter second userinfo
def second_user_info(user_info):
    """Add another question to user info"""
    print("Press 'q' to quit.")
    active = True
    while active:
        favorite_food = input("What is your favorite food? ")
        if favorite_food == 'q':
            break
        user_info['favorite_food'] = favorite_food
        return user_info
        active = False
    

# Complete function
def user_info():
    """Create user ID, look for available data and create or add data"""
    active = True
    while active:
        # create user ID
        user_id = get_user_id()
        
        # Look for stored user data
        if user_id:
            user_info = load_user_info(user_id)
        if user_info:
            if 'favorite_food' in user_info:
                print("You have already completed the survey.")
                break
            else:
                print("Found data matching ID. Adding new data:")
                user_info = second_user_info(user_info)

        else:    
            print("No user data found!")
            print("Initializing new data.")
            user_info = first_user_info(user_id)
        
        filename = f"{user_id}.json"
        with open(filename, 'w') as f:
            json.dump(user_info, f)
        active = False