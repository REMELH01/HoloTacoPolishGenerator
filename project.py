import random

import pandas as pd

# Changing to make interactive with inputs.

nail_base = ('Smoothing Base', 'Peely Base', 'Long Lasting Base')

# Boxes will be categorized as 'Metalics', 'Rainbow Holo', or 'Multichrome'.

nail_metalics = ('Gift Reciept', 'Cold Shoulder', 'Cheap Champagne', 'Mint Money', 'Fake Date')

nail_rainbow_holo = ('Blue Freezie', 'Purple Slushie', 'Magenta Jelly', 'Red Licorice', 'Orange Drink', 'Lemon Sucker', 'Green Taffy')

nail_multichrome = ('Chameleon Coat', "Blue Ain't Slick", 'Missed-Shift', 'Purple with Envy', "Cats' Evation")

nail_toppers = ('Aurora Unicorn Skin', 'Solar Unicorn Skin', 'Cosmic Unicorn Skin', 'Flakie Holo Taco', 'Linear Holo Taco', 'Scattered Holo Taco', 'Sonic Unicorn Skin', 'Galatic Unicorn Skin', 'Lunar Unicorn Skin')

nail_finishes = ('Glossy Taco', 'Super Glossy Taco', 'Matte Taco')

polish_types = [nail_rainbow_holo, nail_metalics, nail_multichrome]

#start program

print('Hello! We will be using Holo Taco nail polishes for this program.')

def choose_base_polish(): 

    nail_base_random = random.choice(nail_base) 

nail_base_choice = 'First, start with a base of ' + str(choose_base_polish) + '.'

main_polish = (input('What main polish box would you like?'))

def choose_main_metalics():
    nail_metalics_random = random.choice(nail_metalics)

if nail_metalics == 'Metalics'
    metalics_sentence = 'Okay, please use ' + choose_main_metalics +'.'
    print(metalics_sentence)