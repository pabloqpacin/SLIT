
"""
# 01-variables_madlibs.py
---
DESCRIPTION
Simple python game where the user is prompted to enter some information
that later will be integrated as variables within a scripted text.
---
GRAMMAR
Variables, f-strings, user input, ...
---
TWEAKS
- while following the original tutorial, the script here is radically different

"""




# TEST
print("\tTEST VARIABLES: 'updawg' is a variable written aside 🥵")
variable = "updawg"

print(f"yo what's {variable}?")                 # PREFERRED
print("yo what's " + variable + "?")
print("what's {}".format(variable) + "?")
 
input("\nContinue? (press enter) \n")



# GAME
print("\tMADLIBS: now ye set the variables and write tha scroll ✍🏽")

who = input("Who: ")
when = input("When: ")
where = input("Where: ")
act1 = input("Activity 1: to ")
act2 = input("Activity 2: ")

madlibs = f"    Sup dawg! Heard of {who}? Crazy shite aye!\n\
    So {when} {where}... Unbelievable.\n\
    Now {who} should either {act1} or {act2}, whaeva.\n\
    Well see ye later Maricarmen 💃"

print(madlibs)
