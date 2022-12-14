#!/bin/bash


# NOTE regarding Ln32 --> (1) user -> root {$ sudo su} (2) root -> user {$ su $USER}

# First beast battle
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

# NESTED IFs as ELIF alternative:

    # if [[ $margit == $tarnished || $tarnished == "coffee" ]]; then
    #     if [[ $USER == "root" ]]; then
    #             echo "Margit DEFEATED! Well done Tarnished."
    #     else
    #         echo "YOU DIED"
    #     fi
    # else
    #         echo "YOU DIED"
    # fi

