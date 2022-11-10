#!/bin/bash


# n29) Let Command Arithmetic
let a=3 b=7 c=a+b
# a=3 b=7 c=a+b           # Here c wouldn't work because inop math
echo "$a + $b = $c"


# n30) 4 Basic OPerators: Add, Subtract, Multiply & Divide
num1=10
num2=2
expr $num1 / $num2
expr $num1 - $num2
expr $num1 + $num2
expr $num1 \* $num2
# NOTE: (6) '\' needed to Multiply


# n31) Incremet a variable 3 times with increment operator
VAR=1
echo $VAR
VAR=$((VAR+=1))
echo $VAR
VAR=$((VAR+=1))
echo $VAR
VAR=$((VAR+=1))
echo $VAR


# n32) Decrement
VARR=7
echo $VARR
VARR=$((VARR-=1))
echo $VARR
VARR=$((VARR-=1))
echo $VARR
VARR=$((VARR-=1))
echo $VARR


# n33) Echo Number Modulus Second NUmber
num00=2
num01=4
num02=5
echo $(($num01 % $num00))
echo $(($num02 % $num00))
# NOTE: (7) RETURNS REMAINDER


# n34) Echo Number to exponent of second number
varexp=$((8**2))
echo $varexp


# n35) 5 mathematical expressions using *expr*
nnum1=25
nnum2=5
expr $nnum1 % $nnum2
expr $nnum1 / $nnum2
expr $nnum1 - $nnum2
expr $nnum1 + $nnum2
expr $nnum1 \* $nnum2


# n36) 5 mathematical expressinos using parenthesis
numm1=15
numm2=5
echo $(($numm1 % $numm2))
echo $(($numm1 / $numm2))
echo $(($numm1 - $numm2))
echo $(($numm1 + $numm2))
echo $(($numm1 * $numm2))


# n37) Double parenthesis with dollar operator to assign a variable
nam1=100
VER=$((nam1+10))
echo $VER


# n38) Multiplication > addition regardless of the order
VERR=$((3*(2+1)))
echo $VERR
NEW=$(((2+1)*3))
echo $NEW



