"""
Lesson: use variables and user input for string concatenation:
EXAMPLE - different ways to print a given variable
MADLIBS GAME - prints a script upon user input
Run the file in Terminal to play.
"""


print("    EXAMPLE: see some lines using the 'mateys' variable")

# variable example
supdawg = "mateys"

# different ways to print a variable
print("awe thanks " + supdawg + ", now that's it")
print("awe Gawd {}".format(supdawg) + ", this is fun")
print(f"yo {supdawg}, what's going on")


input("\nContinue? (press enter) \n")

# game begins hereo
print("    MADLIBS GAME: now you set the variables!")

# set new variables via user input
who = input("Who: ")
when = input("When: ")
where = input("Where: ")
act1 = input("Activity 1: ")
act2 = input("Activity 2: ")

# integrate variables in MADLIBS script
madlibs = f"    Sup dawg! Heard of {who}? Crazy shite aye!\n\
    So {when} {where}... Unbelievable.\n\
    Now {who} should either {act1} or {act2}, whaeva.\n\
    Well see you later Maricarmen 💃"

# print script aka Game
print(madlibs)