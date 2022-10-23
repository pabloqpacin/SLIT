#!/bin/bash


# n39) Combine two strings in one line with variables
VAR1="Hello World!"
VAR2=" Let's concatenate"
VAR3=${VAR1}${VAR2}             # or VAR3="${VAR1} ${VAR2}"" aka spaces ok but needs quotes
echo $VAR3


# n40) Combine three strings in one line with variables
echo ...


# n41) Plus Equal Operator to Combine Strins
VAR1+=$VAR2
echo $VAR1


# n42) Create Multi-Line String Variable with HEREDOC
VARR=$(cat<<'END_HEREDOC'
Here we could write
multi line string
using HEREDOC
END_HEREDOC
)
echo $VARR
echo "$VARR"


# n43) Cat Multi-Line HEREDOC text
cat<<LinuxHint
The current working directory is: $PWD
You are logged in as: $(whoami)
LinuxHint

