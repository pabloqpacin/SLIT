#!/bin/bash


# First battle user VS machine
echo "
Wild beast ahead. Prepare for battle.
    Pick a number between 0-1. (0/1)"                       # instructions

beast=$(( $RANDOM % 2  ))                                   # var1 = random 0-1 number (see 'n0-Math_Random')
read tarnished                                              # var2 = user input

    if [[ $beast == $tarnished && 9 > 3 ]]; then            # IF [[ var1 == var2 (AND always true) ]], then
        echo "Beast VANQUISHED! Well done Tarnished."       #   yay text
    else                                                    # OTHERWISE
        echo "YOU DIED"                                     #   nope text
        exit 1                                              #   GAME OVER
    fi                                                      # syntax end


# Boss battle!
echo "
Margit: 'I shall extinguish thy flame'.
    Pick a number between 0-9. (0/9)"                       # ask for user_input

margit=$(( $RANDOM % 10 ))                                  # var3 = random 0-9 number
read tarnished                                              # var4 = new var2

    if [[ $margit == $tarnished ||
        $tarnished == "coffee" ]]; then                     # IF [[ var3 == var4 (OR 'cheat') ]]; then
        echo "Margit DEFEATED! Well done Tarnished."        #   yay text
    else                                                    # OTHERWISE
        echo "YOU DIED"                                     #   nope text
    fi                                                      # syntax end











