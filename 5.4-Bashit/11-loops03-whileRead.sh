#!/bin/bash

x=1							                            # var = number 1

while [[ $x -le 10 ]]					                # condition: while [[ var (is less than) number 10 ]]
do							                            # loop starts
                                                        # echo "Hey, I just did $x pushups."			# (not in effect; can work if next line is not in effect) updates text + variable every loop
    read -p "Pushup $x: Press enter to continue."		# (WTF IS -P, prompt?) updates text + variable upon user input being enter
    (( x ++ ))						                    # every loop, variable increases by 1 (COULD BE TWEAKED?)
done							                        # syntax' end

echo "
Yay! 10 pushups done!!"				                    # script completed celebration
