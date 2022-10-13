#!/bin/bash


VAR=15

# n44) IF conditional statement
if [ $VAR -gt 5 ]
then echo "good"
fi
# NOTE: (8) importance of spaces (9) -gt == greater than == '>'


# n45) Logical AND in conditional statement (ie. &&)
if [ $VAR -gt 5 ] | [ $VAR -lt 20 ]
then echo "super"
fi
# NOTE: (10) AND = & = && = \   (...?)


# n46) Logical OR in conditional statement
if [ $VAR -gt 5 ] || [ $VAR -lt 10 ]
then echo "nice"
fi


# n47) IF ELIF ELSE conditional statement
# marks=80
read marks                  # 10x strat
if [ $marks -ge 90 ]
then echo Yay!
elif [ $marks -ge 60 ]
then echo Awright!
elif [ $marks -ge 50 ]
then echo Watchout!
else echo Oopseys!
fi


# n48) Nesting IF condition
# NEST=6
read NEST
if [ $NEST -gt 1 ]
then
    if [ $NEST -lt 10 ]
    then echo "Number is between 1 and 10"
    fi
fi


