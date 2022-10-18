import random

import pandas as pd

# Changing to make interactive with inputs.

nail_base = ('Smoothing Base', 'Peely Base', 'Long Lasting Base')

# Boxes will be categorized as 'Metallics', 'Rainbow Holo', or 'Multichrome'.

nail_metallics = ('Gift Reciept', 'Cold Shoulder', 'Cheap Champagne', 'Mint Money', 'Fake Date')

nail_rainbow_holo = ('Blue Freezie', 'Purple Slushie', 'Magenta Jelly', 'Red Licorice', 'Orange Drink', 'Lemon Sucker', 'Green Taffy')

nail_multichrome = ('Chameleon Coat', "Blue Ain't Slick", 'Missed-Shift', 'Purple with Envy', "Cats' Evation")

# Toppers will be categoized as 'Holo Topper' and 'Unicorn Skin Topper'

nail_topper_holo = ('Flakie Holo Taco', 'Linear Holo Taco', 'Scattered Holo Taco')

nail_topper_unicorn = ('Aurora Unicorn Skin', 'Solar Unicorn Skin', 'Cosmic Unicorn Skin', 'Sonic Unicorn Skin', 'Galatic Unicorn Skin', 'Lunar Unicorn Skin')

nail_finishes = ('Glossy Taco', 'Super Glossy Taco', 'Matte Taco')

# Start program

print('Hello! We will be using Holo Taco nail polishes for this program.')

# Polish base choice 
def choose_base_polish(): 
    nail_base_random = random.choice(nail_base) 
    return nail_base_random

nail_base_choice = 'First, start with a base of ' + str(choose_base_polish()) + '.'

print(nail_base_choice)

# Main nail polish choice

def choose_metallics():
    nail_polish_random = random.choice(nail_metallics)
    return nail_polish_random

def choose_multichrome():
    nail_polish_random = random.choice(nail_multichrome)
    return nail_polish_random

def choose_holo():
    nail_holo_random = random.choice(nail_rainbow_holo)
    return nail_holo_random

def main_polish_choice():
    main_polish = (input('What main polish box would you like? Please choose: Metallics, Multichrome, or Rainbow Holo.\n'))

    if main_polish == 'Metallics':
        nail_polish_random = str(choose_metallics())
    elif main_polish == 'Multichrome':
        nail_polish_random = str(choose_multichrome())
    elif main_polish == 'Rainbow Holo':
        nail_polish_random = str(choose_holo())
    else:
        print('You have selected an incorrect option. Please Try again.\n')
        main_polish_choice()

    main_sentence = ('Okay, please use ' + nail_polish_random + 'for your main polish.')
    print(main_sentence)

main_polish_choice()

# Topper nail polish choice choice

def choose_holo_topper():
    topper_polish_random = random.choice(nail_topper_holo)
    return topper_polish_random

def choose_unicorn_topper():
    topper_polish_random = random.choice(nail_topper_unicorn)
    return topper_polish_random

def topper_polish_choice():
    topper_polish = (input('What nail polish topper type would you like? Please choose: Holo or Unicorn Skin'))

    if topper_polish == 'Holo':
        topper_polish_random = str(choose_holo_topper())
    elif topper_polish == 'Unicorn Skin':
        topper_polish_random = str(choose_unicorn_topper())
    else:
        print('You have selected an incorrect option. Please Try again.\n')
        topper_polish_choice()
    
    topper_sentence = ('Okay! Please use ' + topper_polish_random + 'for your topper polish.')
    print(topper_sentence)

topper_polish_choice()

# Finish polish function