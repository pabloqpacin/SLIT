"""
(context: [03](https://github.com/pabloqpacin/SLIT/blob/main/python-fcc12/03-loop_user_guess.py))
BREAKDOWN
- Import RANDOM module.
- Print instructions.
- Define core GAME function with a later-defined X parameter.
    - var1 --> LOW end of numbers' range, in this case 1
    - var2 --> HIGH end of number's range, in this case 1000 (X parameter later defined as 1000)
    - var3 --> our FEEDBACK to the guessing computer, current value is irrelevant
    - WHILE loop --> as long as FEEDBACK is not "AYE"...
        - IF - LOW and HIGH don't match...
        (currently 1 and 1000, soon to be UPDATED in the LOOP)
            - var4 (GUESS) is generated --> RANDOM number between LOW and HIGH
        - ELSE... (!!!)
            - var4 GUESS becomes the var1 LOW (now LOW is the RANDOM number) (!!!)
        - var3 FEEDBACK becomes the user input because...
        - if FEEDBACK is "h", the var2 HIGH becomes GUESS-1
        - if FEEDBACK is "l", the var1 LOW becomes GUESS+1
        Let's explain that: (!!!)
    - finally, when FEEDBACK becomes "AYE" the LOOP breaks and the YAY f-String is printed.
- lastly, the GAME parameter X is defined as 1000, which in turns translates into the var2 HIGH.
"""



"""

HEAVILY IMPROVED THE LOW=HIGH THING + NOW LOOP BREAKS CUZ COMPUTER KNOWZ
ADDED hostname STUFF (socket!)

---

we never tell the computer our secret number so we need to play fair and give the right feedback

"""




# Required modules
import random
import socket
import getpass


username = getpass.getuser()
hostname = socket.gethostname()


# Instructions
print("\n    Now ye think of a number 1-1000 and let the computer guess it!\n\
-- Enter 'h', 'l' or 'aye' to give feedback to the machine 🧠 --\n")


# Core GAME function
def game(x):                                            # X is defined at the bottom  

    low = 1                                             # LOW begins as 1 but will be updated
    high = x                                            # HIGH is now 1000, soon to be updated
    feedback = "sup dawg"                               # whatever, it matters when LOOP is iterating
    
    while feedback != "aye":                            # until we tell the computer they're right...
        print(low, high)                                # given range, un-commented for TESTING
        
        guess = random.randint(low, high)               # computer GUESS is random in the given range
        if low == high:                                 # if range is narrowed down to a SINGLE number
            guess = low    # guess=high OK too          # computer GUESS becomes that single number
            break                                       # and the LOOP breaks 
        
        feedback = input(f"Is {guess} \
too high or too low? Am I just right dawg? ").lower()   # FEEDBACK = user input as per instructions

        if feedback == "h":                             # if we declare the GUESS to be too high
            high = guess - 1                            # then HIGH becomes the GUESS - 1
        elif feedback == "l":                           # now if GUESS is too low
            low = guess + 1                             # LOW becomes the GUESS + 1, hence narrowing the range


# As it iterates upon fair feedback, the computer should narrow down the range soon enough,
# f feedback is given correctly, the computer should eventually narrow down the range enough
    # to return a correct GUESS (while if the GUESS can only be one number, the computer will know)

    # Either of those two possibilities break the loop and lead to this message 
    print(f"\n    Ha-ha get rekt {username}, \
your computer {hostname} has guessed yo number {guess} 🙃 ")

# We define here the value of X (--I don't seem to grasp this logic yet--)
game(1000)