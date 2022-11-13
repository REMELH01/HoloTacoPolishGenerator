import random
from time import sleep

seconds = 2
sleep(seconds)

## Lists here
# Changing to make interactive with inputs.

nail_base = ('Smoothing Base', 'Peely Base', 'Long Lasting Base')

# Main polishes will be categorized as 'Metallics', 'Rainbow Holo', or 'Multichrome'.

nail_metallics = ('Gift Reciept', 'Cold Shoulder', 'Cheap Champagne', 'Mint Money', 'Fake Date')

nail_rainbow_holo = ('Blue Freezie', 'Purple Slushie', 'Magenta Jelly', 'Red Licorice', 'Orange Drink', 'Lemon Sucker', 'Green Taffy')

nail_multichrome = ('Chameleon Coat', "Blue Ain't Slick", 'Missed-Shift', 'Purple with Envy', "Cats' Evation")

# Toppers will be categoized as 'Holo Topper' and 'Unicorn Skin Topper'

nail_topper_holo = ('Flakie Holo Taco', 'Linear Holo Taco', 'Scattered Holo Taco')

nail_topper_unicorn = ('Aurora Unicorn Skin', 'Solar Unicorn Skin', 'Cosmic Unicorn Skin', 'Sonic Unicorn Skin', 'Galatic Unicorn Skin', 'Lunar Unicorn Skin')

nail_finishes = ('Glossy Taco', 'Super Glossy Taco', 'Matte Taco')


# Polish base choice 

def choose_base_polish(): 
    nail_base_random = random.choice(nail_base) 
    return nail_base_random

nail_base_choice = 'First, start with a base of ' + str(choose_base_polish()) + '.'


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
    nail_polish_random = None
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

    main_sentence = ('Okay, please use ' + str(nail_polish_random) + ' for your main polish.')
    if nail_polish_random is not None:
            print(main_sentence)


# Topper nail polish choice choice

def choose_holo_topper():
    topper_polish_random = random.choice(nail_topper_holo)
    return topper_polish_random

def choose_unicorn_topper():
    topper_polish_random = random.choice(nail_topper_unicorn)
    return topper_polish_random

def topper_polish_choice():
    topper_polish_random = None
    topper_polish = (input('What nail polish topper type would you like? Please choose: Holo or Unicorn Skin\n'))

    if topper_polish == 'Holo':
        topper_polish_random = str(choose_holo_topper())
    elif topper_polish == 'Unicorn Skin':
        topper_polish_random = str(choose_unicorn_topper())
    else:
        print('You have selected an incorrect option. Please Try again.\n')
        topper_polish_choice()
    
    topper_sentence = ('Okay! Please use ' + str(topper_polish_random) + ' for your topper polish.')
    if topper_polish_random is not None:
            print(topper_sentence)


# Finish polish function

def choose_finish_polish(): 
    nail_finish_random = random.choice(nail_finishes) 
    return nail_finish_random

nail_finish_choice = 'Finally, end with a finish of ' + str(choose_finish_polish()) + '.'


# Program here

if __name__ == '__main__':
    # Start program
    print('Hello! We will be using Holo Taco nail polishes for this program.')
    sleep(2)
    # Polish base random choice
    print(nail_base_choice)
    sleep(2)
    # Main polish user choice
    main_polish_choice()
    sleep(2)
    # Topper polish user choice 
    topper_polish_choice()
    sleep(2)
    # Nail finish 
    print(nail_finish_choice)
    sleep(2)
    #Ending program notes
    print('Thank you for using this program.')
    sleep(2)
    print('Please remember to give your nails plenty of time to dry.')
    sleep(2)
    print('Enjoy your fun new look!')
    sleep(2)