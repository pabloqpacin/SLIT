

"""
DESCRIPTION
Game for the user to guess a rendomly generated computer's secret number

LESSON
use functions, ...

BREAKDOWN-Intro
- Generate computer number with "random" package
- Have game running with the "guess" function

BREAKDOWN-Module
1 - Import python 'random' package
So that we can use 'functions' like "random.randint()".

BREAKDOWN-Function
2 - Define function "guess"
This is basically the whole thing, all we will print.
Operates with scripted data and user input (variables).

BREAKDOWN-next

"""


import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number beteween 1 and {x}: '))
        # print(guess)
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly.')


guess(10)