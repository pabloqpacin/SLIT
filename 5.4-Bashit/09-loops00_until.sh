#!/bin/bash

until [[ $order == "coffee" ]]			            # condition: variable must be "coffee"
do						                                  # loop starts
  echo "Would you like coffee or tea?"		      # trick question
  read order					                          # user input = variable
done 						                                # loop ends
echo "Excellent choice, here is your coffee"	  # fun acknowledgment
