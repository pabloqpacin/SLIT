"""
# 04-loop_computer_guess.py
---
Building from [03](https://github.com/pabloqpacin/SLIT/blob/main/python-fcc12/03-loop_user_guess.py)
---
DESCRIPTION
Python game where the user thinks a number (1-1000 or any range)
and the computer narrows down that range to guess our secret number.
We never declare our number, giving instead fair feedback to the guessing computer.
---
GRAMMAR
Besides using if-statements, f-strings, while-loops and the 'random' module,
we now introduce the 'socket' and 'getpass' modules, addressing environment_variables.
---
TWEAKS
Taking distance from the original tutorial, we've performed the following tweaks:
- included modules 'socket' and 'getpass' for custom f-strings
- thoroughly commented and explained all relevant code snippets
- reworked most of the printed text strings for sassier dialogue
- improved syntax for the `if low == high:` statement (ln 55)
    - now the loop also breaks if there's only one number to guess, hence declaring W for the machine
---
TO-DO
- devise cheats to bypass the while-loop and its 'yay' message

"""


# Required modules
import random
import socket
import getpass


username = getpass.getuser()
hostname = socket.gethostname()


# Instructions
print(f"\nNow ye think of a number 1-1000 and let your calcul8r {hostname} guess it!\n\
-- Enter 'h', 'l' or 'aye' to give feedback to the machine 🧠 --")


# Core GAME function
def game(x):                                            # X is defined at the bottom  

    low = 1                                             # LOW begins as 1 but will be updated
    high = x                                            # HIGH is now 1000, soon to be updated
    feedback = "sup dawg"                               # whatever, it matters when LOOP is iterating
    
    while feedback != "aye":                            # until we tell the computer they're right...
        print(f"\nI guess between {low} and {high}...")                                # given range, un-commented for TESTING
        guess = random.randint(low, high)               # computer GUESS is random in the given range
        
        if low == high:                                 # if range is narrowed down to a SINGLE number
            guess = low    # guess=high OK too          # computer GUESS becomes that single number
            break                                       # and the LOOP breaks 
        
        feedback = input(f"Hey, is {guess} \
too high or too low? Am I just right dawg? ").lower()   # FEEDBACK = user input as per instructions

        if feedback == "l":                             # if our FEEDBACK means for GUESS to be too low,
            low = guess + 1                             # then LOW becomes that random GUESS + 1
        elif feedback == "h":                           # and if GUESS is reported as too high,
            high = guess - 1                            # HIGH becomes that GUESS - 1


    # fair feedback + loop iterations + variables updating = guessing range narrowed down 
    # when 1 possible guess or correct guess --> loop breaks leading to f-string below [^1] 
    print(f"\n    Ha-ha get rekt {username}, computer takes the W. T'was {guess}, easy guess 🙃 ")


# Here we define the value of X (--tho I don't seem to grasp this logic just yet--)
game(1000)




# [^1] As we provide fair feedback, the loop iterates and the variables are updated,
# steadily narrowing down the range for guesses until the loop is broken because
# there's only one possible guess or the last guess is actually correct.