#!/bin/bash


# Selecting your starting class
echo "
Welcome Tarnished. Please select your starting class: (1-3)    
    1 - Samurai
    2 - Prisoner
    3 - Confessor
    "                                                   # user input should be a 1-3 number

read class                                              # var0 == user input

    case $class in                                      # case var0 in
        1)                                              # (1/3)
            type="Samurai" && hp=30 && attack=10;;      # new variables (ie. type, hp, attack)
        2)                                              # (2/3)
            type="Prisoner" && hp=20 && attack=20;;
        3)                                              # (3/3)
            type="Confessor" && hp=10 && attack=30;;
    esac                                                # syntax end

echo "
    Thou have chosen the $type class.
Your HP is $hp and your attack is $attack."             # returns new variables


# Now the core game should be tweaked developing new CLASS mechanics
#
#
#
#


# First beast battle
sleep 2

echo "
Wild beast ahead. Prepare for battle.
    Pick a number between 0-1. (0/1)"

beast=$(( $RANDOM % 2  ))
read tarnished

    if [[ $beast == $tarnished || $tarnished == "coffee" ]]; then
        echo "Beast VANQUISHED! Well done Tarnished."
    else
        echo "YOU DIED"
        exit 1
    fi


# Boss battle!
echo "
Margit: I shall extinguish thy flame'.
    Pick a number between 0-9. (0/9)"

margit=$(( $RANDOM % 10 ))
read tarnished

    if [[ $margit == $tarnished || $tarnished == "coffee" ]]; then
        echo "Margit DEFEATED! Well done Tarnished."
    elif [[ $USER == "root" ]]; then                        
        echo "Hey, root always wins. Margit DEFEATED!"
    else
        echo "YOU DIED"
    fi

