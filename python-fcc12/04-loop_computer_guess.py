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









import random


print("\n    Now ye think of a number 1-1000 and let the computer guess it!\n\
-- Enter 'h', 'l' or 'aye' to give feedback to the machine 🧠 --\n")


def game(x):

    low = 1
    high = x
    feedback = "sup dawg"
    
    while feedback != "aye":
        # print(low, high)    # un-comment to see how LOW and HIGH are updated through the LOOP
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # "guess = high" works the same-ish
            break
        feedback = input(f"Is {guess} too high or too low? \
Am I just right dawg? ").lower()    # ".lower()" ensures "input" is lowercase
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"\n    Ha-ha get rekt hooman, \
me the machine has guessed yo number {guess} 🙃 ")


game(1000)