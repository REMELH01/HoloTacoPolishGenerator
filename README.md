# Holo Taco Nail Polish Generator 

## Description 
This project is a nail polish generator using nail polishes made and sold by Holo Taco. It will use random to first select a base polish and the finishing polish, and it will use random to select the main polish and topper polish based on the user's input. If the user inputs something that is not one of the listed options, it will tell the user to try again until the user correctly inputs an option. The goal is to give the user an effortless way to choose their next nail polish look without having to choose themselves. 

## Interpreting the Polishes
In this project, there are 4 categories for the nail polishes: Base, Main, Topper, and Finish. Of these, the Main nail polish has 3 sub-categories (Metallics, Rainbow Holo, and Multichrome) and the Topper polishes have 2-sub-categories (Holo and Unicorn Skin). Overall, the Main polish type has the most nail polishes in it, with there being 17 in total. The sub-category with the most nail polishes was Rainbow Holo, with 7 nail polishes. The Base and Finish categories were tied for having the least nail polishes, each only having 3. While there are several custom functions choosing the nail polishes, there are 2 types: 1 that only randomizes a single list (used for all the lists), and the other being one that returns a single polish from the sub-categories based off the user's input. using 'if', 'elif' and 'else' statements. The latter includes a feature that starts the function over again if the user incorrectly enters something. 

## Technologies 
- Python 
- Matplotlib
- Statistics

## Getting Started 
1. Clone 'https://github.com/REMELH01/HoloTacoPolishGenerator' 
2. Make sure you have matplotlib installed.
3. Respond to the inputs within the program when it begins. 

## Features 
1. Includes lists of data in the form of nail polish names, separated by the type of nail polish it is. 
2. Uses custom functions to randomize a nail polish based on the type of polish it is, as well as randoizing between multiple lists depending on what the user's input is. 
3. Analyzes the nail polish numbers using built-in Python features.
4. Prints statements with custom responses based off the user’s input.
5. Vizualizes the amount of nail polishes in the program using matplotlib.  
6. Includes a README explaining the generator and its functions. 

## Limitations 
Holo Taco is a vastly expanding brand of nail polish created by Cristine Rotenberg, also known as simplynailogical on YouTube. This program only includes a small percentage of the nail polishes made and produced by Holo Taco. The only polishes included in this program are the ones personally owned by the creator of the program. 

## Obstacles 
There are some nail polishes included in this program that, unless previously owned, are no longer available for purchase, as they were limited addition nail polishes sold by Holo Taco. Additionally, since Holo Taco is a rapidly growing brand, they are consistently putting out new nail polishes. As such, the program is not up to date on the most recent collections released by Holo Taco. 

## To Do:
Going forward after Code Louisville: 
1. Add an interactive GUI (potentially using tkinter). 
2. Add more of the nail polishes created by Holo Taco. 
3. Better define the nail polish types, rather than using the basic type. 
4. When the polish choices are given (whether randomized or based off the user’s input), have the sentence also state which collection the polish was a part of. 

## License  
Holo Taco is a trademarked company owned by Cristine Rotenberg. 

### For Code Louisville: 
This project was created in part for fulfillment of Data Analysis Pathway 1.