

"""
COMMENT-TIME
- Import RANDOM module
- Define core game in PLAY function
    - variable USER for the user input, which is read after the premise-question
    - variable COMPUTER for the AI random choice (either R, P or S)
    - then if both variables match, print the TIE thing
    - now for the win/lose system we need the second function below, IS_WIN, to be called
        - once defined, we have it run here; if True, return the USER WIN thing
        - if it isn't True, the PLAY function just returns COMPUTER WIN 
- Define game mechanics (win/lose) in IS_WIN function
    - establish IS_WIN as True if the variables USER and COMPUTER take values that would mean USER victory (eg. USER r > COMPUTER)
    - nonetheless, we also include the classic keyword "tusupervieja"
- Now we just print the core PLAY function and that's the game!
Thanks for reading and I hope you like it!

"""


"""
TO-TWEAK:
- if TIE, run PLAY again automatically

"""





import random


def play():
    user = input("Wakey-wakey, shoot aye! 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "Boring tie, just shoot again"

    if is_win(user, computer):
        return 'W for the hooman yay!'

    # kinda else, meaning IS_WIN ain't True
    return 'Computer dominance mf!'

# return true if user wins: r > s, s > p, p > r
def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
        or (user == 'p' and computer == 'r') or (user == 'tusupervieja'):
        return True

print(play())
