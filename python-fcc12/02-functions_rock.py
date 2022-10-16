"""
# 02-functions_rock.py
---
DESCRIPTION
Simple python terminal game to play 'rock, paper, scissors' with the machine.
---
GRAMMAR
Along with the 'random' module, we use functions, variables, user input and if-statements.
---
TWEAKS
While following the original tutorial, we also include custom elements: 
- custom text strings
- cheat keyword to bypass the game's rules
---
TO-DO
- make it best-of-three
- if game ends in tie, run the function automatically

"""


# Required module
import random


# Main function containing the two core variables
def play():
    computer = random.choice(["r", "p", "s"])
    print(computer)                                 # un-commented for TESTING
    user = input("Wakey-wakey! 🔫 Shoot aye: 'r' for rock, 'p' for paper, 's' for scissors --- ").lower()

    if user == computer:
        return "T'was a tie duh, shoot again plz"

    # side function called; if True returns the 'user yay' string
    if win_fun(user, computer):
        return 'W for the hooman yay!'
    return 'Computer dominance mf!'                 # ---so 'else' wasn't needed because...we're in a function (?)---


# Side function addressing how R, P and S interact (ie. conditions met = True = user win, the opposite otherwise)
def win_fun(user, computer):
    if (user == "r" and computer == "s") \
        or (user == "p" and computer == "r") \
        or (user == "s" and computer == "p") \
        or (user == "tusupervieja"):                # CLASSIC CHEAT KEYWORD
        return True

print(play())
