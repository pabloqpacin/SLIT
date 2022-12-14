#!/bin/bash


echo "Do you like coffee dawg? (y/n)"       # Ask for user input
    read coffee                             # User input becomes the variable
        if [[ $coffee == "y" ]]; then       # If the variable AKA user input equals "yes", then
        	echo "Ye rock"                  #   print this
        else                                # otherwise
        	echo "Ye suck"                  #   print that
        fi                                  # end of IF statement
    
    echo "YOU DIED"                         #   print leitmotif
