
"""
05-stringy_hangman.py
---
DESCRIPTION
The classic hangman game - A word is withdrawn from a pool
and its letters are engineered to interact with user input
(user input == letters to guess the random word).
---
GRAMMAR
'Random' module for random choices, side file 'WORDS' as pool,
module 'string' for solid operations with strings and letters.
Other than that, f-strings, while-loops, if-statements, etc.
---
TWEAKS
- thorough commenting
- custom text for sassier dialogue
- few key variables set to be printed for testing purposes
---
TO-DO
- valid words only if 5+ letters
- sharpen 'string' module usage
- have LETTERS printed alphabetically
"""



# Required modUles
import random
import string
from words import words


# Greetings
print("\n👊 Supp broe, new game aye. Throw in letters till you guess da WORD 👻")



# (1) This function determines the secret word (all snippets are explained aside)
def get_valid_word(words):                                                                              # function handling the words pool:
    word = random.choice(words)                                                                         # randomly chooses a word from the pool,
    while "-" in word or " " in word:                                                                   # but if it has dashes or spaces:
        word = random.choice(words)                                                                     # loop iterates to find one without.
    return word.upper()                                                                                 # when found, it is returned in uppercase



# (2) Now let's build the game!
def hangman():                                                                                          # core game function:
    lives = 7                                                                                           # (may be any integer) 
    alphabet = set(string.ascii_uppercase)                                                              # tracks all possible letters 
    word = get_valid_word(words)                                                                        # result of (1) function
    word_letters = set(word)                                                                            # tracks letters in 'word'
    used_letters = set()                                                                                # tracks letters via user input
    print(f"\n-Alphabet: {alphabet} \n-Word: {word} \n-Letters: {word_letters} \n")
    # Let's TEST all those variables and see what are we working with! (COMMENT IT TO PLAY PROPERLY!)
    

    while len(word_letters) > 0 and lives > 0:                                                          # LOOP ON while letters and lives LEFT

        print(f"~~~~~~~~~~~~~~~~~~\n\
📝 M8 u have {lives} lives left and used dis letters: ", " ".join(used_letters))

        # next line turns word letters into "-" and used letters into letters!!
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("DA WORD: ", " ".join(word_list))

        # user input in the loop:
        user_letter = input("YO LETTER: ").upper()
        
        # if letter is in word and hasn't been used yet
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            # if letter is not in word
            else:
                lives = lives - 1
                print(f"👉 Dawg letter '{user_letter}' ain't in da word!\n")
    
        # if letter is already used
        elif user_letter in used_letters:
            print("👉 Yo wakey-wakey, u've already tried that. Go on aye!\n")

        # if input is invalid
        else:
            print("👉 Invalid character, try again dawg!\n")


    # when LOOP breaks (ie. no lives or word_letters LEFT)...
    print("\n~~~~~~~~~~~~~~~~~~\n")
    if lives == 0:
        print(f"  YE DIED MF, get yo shit 2gether. 💩 The word was '{word}' btw!\n")
    else:
        print(f"  HOLY SMOKES ye did it!! Ye nerd guessed the word '{word}'!! 🤓\n")


hangman()
