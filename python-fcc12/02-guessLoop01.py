

"""
DESCRIPTION
Game for the user to guess a rendomly generated computer's secret number

LESSON
use functions, loops

BREAKDOWN-Intro
- Generate computer number with "random" package
- Have game running with the "guess" function

BREAKDOWN-Module
1 - Import python 'random' package
So that we can use 'functions' like "random.randint()".

BREAKDOWN-Function
2 - Define function "guess" (or any other name) to equal "x" (secret number)
This is basically the whole thing, all that will be printed.
Operates with scripted data and user input (variables).

BREAKDOWN-next
have random number equal any random integer between 1 and any (x)

BREAKDOWN-WhileLoop
Used to receive computer feedback and keep guessing until we guess "x".
ITERATION (condition): our guess is not the secret number
"""


"""
BREAKDOWN
- import random module
- define function "meguess", which will be the user input 
"x" stands for the max number and it's established after the function
- generate secret number
- "guess=0" because IT NEEDS TO BE LIKE THAT wtf
- while loop, with a clear expression (condition)
expression: our guess doesn't match the secret number

"""



""""
YO remember Python is a scripting language so it's read top-to-bottom"""








# import this python module to use its functions
import random

# we define the function 'myguess' as a 'notdefined' value
def myguess(notdefined):
# we set the variable 'randomnumber' to equal...
    # a random integer between 1 and the 'notdefined' value
    randomnumber = random.randint(1, notdefined)
# now the function 'myguess' is like a variable and we updated it from...
    # a 'notdefined' value to equal 0, then to 1k, it doesn't matter,
    # as long as it allows us to start the loop below 
    myguess = 0
    myguess = 1000
# we set the game's loop expressing that the core function is NOT the random number
    # To that end, we've set it to a value 
    # that the main function (1k atm) is at the moment differ
    while myguess != randomnumber:
        myguess = int(input(f"Guess a number between 1 and {notdefined}: "))
        if myguess < randomnumber:
            print("Sorrey, guess again. Too low aye.") 
        if myguess > randomnumber:
            print("Sorrey, guess again. Too high aye.")

    print(f"Yay, congrats. You have guessed the number {randomnumber} correctly!")

myguess(10)
# establishing the max





# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f'Guess a number between 1 and {x}: '))
#         # print(guess)
#         if guess < random_number:
#             print('Sorry, guess again. Too low.')
#         elif guess > random_number:
#             print('Sorry, guess again. Too high.')

#     print(f'Yay, congrats. You have guessed the number {random_number} correctly.')


# guess(10)