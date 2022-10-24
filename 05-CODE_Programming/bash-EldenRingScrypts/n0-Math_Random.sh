#!/bin/bash


## ISSUE NOTE: custom 'environment commands' caused issue. Such commands had been exported via '~$ nano .bashrc'. See Chuck's video for reference.

# Variable 1 -> user input 1
echo "Hi there, what's your name?"
    read name

# Variable 2 -> user input 2
echo "Tell me, how old are you?"
    read age

# Variable 3 == random Math; ie. var3 == var2 + (random_number 0-15)
getrich=$(( $age + ( $RANDOM % 15 ) ))

# (1) { 5=$((3+2)) } as if { $((math))=result } | eg. {  }
# (2) $RANDOM -> random 0-32767 number ; echo $(($RANDOM % 10)) == 0-10
# (3) any_number % 10 

echo $morning", $name, you are $age years old."         ## ISSUE: $morning denied or denying
sleep 1
echo "Calculating richey time..."
sleep 1
echo "You're becoming rich at $getrich years old!"
