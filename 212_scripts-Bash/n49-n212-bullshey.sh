#!/bin/bash


## GENERAL BS
VAR="Hello"
RAV="World"

<<bs
# n49) Equal VS double equal operator... THEY AR SAME! (?!)
if [ $VAR = $RAV ]
then echo "tuvieja"
else echo "tusupervieja"
fi

if [ $VAR == $RAV ]
then echo "tuvieja"
else echo "tusupervieja"
fi
bs

# n50) Test Not Equal Strings
if [ $VAR != $RAV ]
then echo "ain't same"
else echo "are same"
fi

<<bs
# n51) Test two strings' alphabetical order
VER="Hi"
REV="Yo"

if [ $VER == $REV ]
then echo "Same ordah"
else echo "Not same ordah"
fi
bs

# n52 to n212 --> BULLSHEY not-done



