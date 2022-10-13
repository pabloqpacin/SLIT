#!/bin/bash


# NOTE: (4) 10x approach = automate another useful .sh (instead of .txt)

# n10) Write a file from inside a script
echo "My favorite movie is \"Limitless\"" > ./n10-limitless.txt


# n11) Overwrite to a file from inside a script
echo "My favorite movie is \"Limitless\"" > ./n11-justine.txt

echo "My favorite book is \"Justine\"" > ./n11-justine.txt


# n12) Append to File inside Script
echo "My favorite movie is \"Limitless\"" > ./n12-allthemwitches.txt

echo "My favorite book is \"Justine\"" >> ./n12-allthemwitches.txt

echo "My favorite band is \"All Them Witches\"" >> ./n12-allthemwitches.txt 