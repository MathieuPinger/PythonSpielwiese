# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:55:09 2020

@author: mathieu.pinger
"""

"""Input"""

# Chunk to clear console
try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    pass


# Input lets user type something and save the value
mood = input("How are you? Enter here: ")

# multi-line input
name = input("What's your name? ")
prompt = (f"Hello {name}! \nWe have a special offer for you!")
prompt += ("How much are you willing to pay? Only enter a number: ")
richness = input(prompt)

# turning str to int
richness = int(richness)
if richness > 50:
    print("We might have something very unique for you!")
else:
    new_richness = input("Go get more money you peasant! Or enter a new value: ")
    
# modulo operator and round to ten

def round_to_ten(x):
    return int(round(x / 10.0)) * 10

new_richness = int(new_richness)
if new_richness % 10 == 0:
    print(f"Thanks for the money, we'll take your {new_richness}!")
else:
    rounded_richness = round_to_ten(new_richness)
    prompt2 = ("We'll have to round this to the next ten...")
    prompt2 += (f"Are you okay with spending {rounded_richness}? (y/n)")
    answer = input(prompt2)
    
if answer == 'y':
    print("Thank you, we give you nothing, byeeee!")
elif answer == 'n':
    print("Well then off you go, byeeee!")
else:
    print("Was that so difficult?!")
    
"""while loops"""

# with flag
prompt = "How much do you want to pay? Enter a number: "
prompt += "Or enter 'q' to quit."

active = True
while active:
    answer = input(prompt)

    if answer == 'q':
        active = False
    elif int(answer) > 99:
        print("OK that's enough, bye!")
        active = False
    elif int(answer) < 100:
        print("Hmm we need a lil bit more!")

