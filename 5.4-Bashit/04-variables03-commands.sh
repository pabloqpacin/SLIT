#!/bin/bash


name=$1                                # Again, positional arguments
outfit=$2

user=$(whoami)                         # (ie. variable = $(command) )
date=$(date)
whereami=$(pwd)

echo "Morning $name!"
sleep 1
echo "Looking good aye."
sleep 1
echo "Ya got some noice $outfit today $name!!"
sleep 2

echo "Yer logged in as $user."        # Variable returns relevant command (eg. $whoami)
echo "Thy currently dir is $whereami."
echo "Also today is $date... make it count!"
