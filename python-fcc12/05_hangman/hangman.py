"""
05-..._hangman.py
---
DESCRIPTION
tricks to capitalize all input for the program to process such input correctly
---
GRAMMAR
Imported 'random', side file 'words' and its purposeful variable as well as the 'string' module.
Now used the classic 'random.choice()', 
---
TWEAKS
...
---
TO-DO
- valid words ONLY 5+ letters
"""



"""
OJO CON LO DEL ALPHABET (29:00)


"""







# Required modUles
import random
from words import words
import string


# Greetings
print("\n👊 Supp broe, new game aye. Throw in letters till you guess da WORD 👻")



# (1) Retrieve a valid word to play with
def get_valid_word(words):                      # function works with imported 'words' variable
    word = random.choice(words)                 # OK variable 'word' is defined as a random choice
    while "-" in word or " " in word:           # while that 'word' has dashes or spaces,
        word = random.choice(words)             # keep iteratating for another word
    return word.upper()                         # finally return valid 'word' in capital letters



# (2) Build the game!
def hangman():
    word = get_valid_word(words)                # 'word' variable is again defined as the result of such function
    word_letters = set(word)                    # breaking down the letters in 'word'
    alphabet = set(string.ascii_uppercase)      # (!)
    used_letters = set()                        # variable to keep track of the user input

    lives = 9                                   # can be changed!
    print(f"-- {word} 😡 --")                  # un-commented for TESTING
    
    while len(word_letters) > 0 and lives > 0:      # if there are lives and letters left, LOOP ON!
        # what current word is (ie W - R D)
        print("\n~~~~~~~~~~~~~~~~~~\n")
        print(f"📝 Yo u've got --{lives}-- lives left and used da letters: ", ' '.join(used_letters))    # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('DA WORD: ', ' '.join(word_list))
        


        user_letter = input("YO LETTER: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # takes away a life if wrong
                print(f"\tDawg letter '{user_letter}' ain't in da word!")
    
        elif user_letter in used_letters:
            print("\tYo wakey-wakey, u've already tried that. Go on aye!")

        else:
            print("\tInvalid character, try again dawg!")

    print("\n~~~~~~~~~~~~~~~~~~\n")

    # when LOOP breaks (ie. 'lives' and 'word_letters' = 0)...
    if lives == 0:
        print(f"  YE DIED MF, get yo shit 2gether. 💩 The word was '{word}' btw!\n")
    else:
        print(f"  HOLY SMOKES ye did it!! Ye nerd guessed the word '{word}'!! 🤓\n")

hangman()