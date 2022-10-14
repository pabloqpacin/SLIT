#!/bin/bash


<<Introduction
Hello world.
Now this is a basic "guess the number" game.
I put it together guessing what to do cuz I didn't look anything up.
So let's break it down.
Introduction


<<Breakdown1
1 - with the variable $guessme we set the secret number, 
which may be any number between 0-1000 using '$RANDOM' & '%'.
2 - print instructions for the user.
3 - you could print the number itself for testing purposes.
4 - time for user input, which becomes the variable $meguess.
Recap:
$meguess = user input
$guessme = secret number
Breakdown1

<<Breakdown2
5 - RESULTS LOOP
So now for as long as the two variables don't match
(ie. the user hasn't guessed the number),
there's gonna be a loop situation.
5.1 - LONG GUESS
We declare an if statement inside the loop,
thereof a user guess greater than the secret number
will return the designated message "nope, too high".
And the script will ask for user input again.
5.2 - SHORT GUESS
Now the opposite, a guess lower than the secret number
will return the message "nope, too low", and ask for user input again.
The loop will be on until the guess is successful.
5.3 - GUESSED IT
When the two variables match, the loop will break
and the script will return the secret number.
Breakdown2

<<Tweak
# As a personal note, I should work on the computer feedback,
that is, after each guess the computer will return all numbers
the user has tried.
Look up the FCC12 project for ideas.
Tweak


# 1 - number to guess
guessme=$(($RANDOM%1000))

# 2 - instructions for the user
echo '
Guess mey (1/1000)'

# 3 - print secret number (DON'T)
echo $guessme | lolcat

# 4 - user guess
read meguess

# 5 - GAME'S ON
while [ $meguess != $guessme ]
do
    # 5.1
    if [ $meguess -gt $guessme ]
    then echo "yeah nope... too high"
        # echo "so far you've tried: $meguess"
        read meguess
    # 5.2
    elif [ $meguess -lt $guessme ]
    then echo "yeah nope... too low"
        # echo "so far you've tried: $meguess"
        read meguess
    fi
#5.3
done
    echo "yay t'was"
    echo -e "\t $guessme" | lolcat
