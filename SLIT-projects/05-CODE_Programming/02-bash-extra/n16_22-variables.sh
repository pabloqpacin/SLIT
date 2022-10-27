#!/bin/bash



# n16) Simple Variable Usage
VAR='Hello World!'
echo $VAR


# n17) Multi Word Variabls Combinations with quotes
a='this is a'
b='this is b'
c="${a} and ${b}"
echo "${c}"
# NOTE: (5) double-quotes required to have brackets working


# n18) HOME variable
VAR_PATH=$HOME
echo "$VAR_PATH"
ls "$VAR_PATH"


# n19) USER variable
VAR_USER=$USER
echo "$VAR_USER"


# n20) HOSTNAME variable
VAR_HOST=$HOSTNAME
echo "$VAR_HOST"


# n21) Echo $HOME with Escape to Avoid Expansion
echo "\$HOME"


# n22) Writing to file in Home directory using $HOME Environment Variables
cd $HOME
echo "Yay!" > n22-yay.txt
cat n22-yay.txt
















