
"""
# 03-loop_user_guess.py
---
DESCRIPTION
Basic python game where the user should guess secret number the computer has "thought".
---
GRAMMAR
Including the 'random' module and the use of functions, variables,
f-Strings, while-loops and if-statements, in a rally compact way.
Besides, we actually include the 'getpass' module for custom dialogue.
---
TWEAKS
- cheat keyword (scripted integer)
- custom sassy text
- usage of environment values with the 'socket' and 'getpass' modules
"""

# AWKWARD SYNTAX BREAKDOWN
# - Function's parameter 'X' is defined aside, at the end of the script (currently defined as 20)
# - Variable 'secret_number' will take a value randomly generated between '1' and 'X'
# - Variable 'user_guess' can be any integer outside of 'secret_number' range (eg. 0, 200, 5000, etc.)
# - Now WHILE the GUESS doesn't match with 'secret_number' (that's the case rn) and the input isn't '420':
#     - A message is displayed with the instructions and from now on the GUESS may be whatever the integer entered by the user
#     - IF our guess is '420', a message is displayed and the LOOP is bypassed!!
#     - IF GUESS is lower than secret_number, we are given such feedback.
#     - IF GUESS is higher, similar feedback is given.
# - Now WHEN the LOOP is broken, the 'YAY' message is displayed.
# - Function's parameter 'X' is defined here --because...---

""


# Required module
import random
import getpass

you = getpass.getuser()


# Greetings
print(f"\nGreetings '{you}'. Let's play a game, shall we? 🎲") 


# Game's function (X parameter defined in the last line)
def game(x):

    secret_number = random.randint(1, x)
    user_guess = 0
    print(f"--😡 {secret_number}--")        # DELETE!                 

    while (user_guess != secret_number) and (user_guess != 420):
        user_guess = int(input(f"\nGuess me secret number between 1 and {x}: "))
        if user_guess == 420:
            print("\n-- You sneaky ass, dare to play and claim a W in range 1-1M 💀 --")
            continue                        # --same as 'break'?--
        if user_guess < secret_number:
            print("  Yo guess again, too low aye.") 
        if user_guess > secret_number:
            print("  Yo guess again, too high aye.")

    print(f"\n\tDamn it took long... Noice, u've guessed da number {secret_number} yay! 🧙\n")


# define X parameter
game(20)
