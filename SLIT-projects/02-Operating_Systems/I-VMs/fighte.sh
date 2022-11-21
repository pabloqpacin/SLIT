#!/bin/bash

echo 'wilde beast. Pick a number to kill it! [0/1]'
beast=$((RANDOM%1))
read fighte

if [[ $fighte == $beast || $fighte == 'supdawg' ]] ;
then echo -e '\tnoice\n'
else echo -e '\tu died beatch\n'
fi

fortune