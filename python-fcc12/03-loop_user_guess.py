"""
DESCRIPTION
Game for the user to guess a random number (CHEATS included)

LESSON:
functions, variables, f-Strings, while-loops, if-statements, ...

BREAKDOWN
- Import RANDOM module
- Define core GAME function with a not-yet-defined X parameter.
    - var1 --> SECRET_NUMBER
    Randomly generated integer between 1 and X (X is later defined as 10).
    - var2 --> USER_GUESS
    Must have a value different from whatever SECRET_NUMBER may be, so it's set to 0 (could be 11, 20k, 5M...).
    - WHILE loop --> expressing the two variables don't match (and CHEATS ain't used)
        - var2 --> USER GUESS
        Integer '0' is updated with user input; f-String includes the later defined NOT_DEFINED value.
        - if USER is CHEAT, print so and break loop!
        - if USER too low, print so.
        - if USER too high, print so.
    The loop iterates (is ON) until the variables match, breaking it as expressed above.
    - PRINT --> yay message when the loop is broken, returning the actual SECRET_NUMBER.
- GAME parameter X defined
Parameter X is defined as the integer 10, but any other number works...
as long as the variable USER_GUESS integer is initially NOT in the range 1-X!

"""



import random

def game(x):

    secret_number = random.randint(1, x)
    user_guess = 0

    while (user_guess != secret_number) and (user_guess != 420):
        user_guess = int(input(f"Guess a number between 1 and {x}: "))
        if user_guess == 420:
            print("-- You sneaky ass, dare to play and claim a W in range 1-1M 💀 --")
            continue
        if user_guess < secret_number:
            print("Yo guess again, too low aye.") 
        if user_guess > secret_number:
            print("Yo guess again, too high aye.")

    print(f"Congrats m8, u've noicely guessed tha number {secret_number} yay!")

# define X parameter
game(10)
