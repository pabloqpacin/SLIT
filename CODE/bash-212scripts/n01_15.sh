#!/bin/bash


# n1) Simple Hello World Script
echo "Hello World"

# n2) Echo Command without new lines
echo -n "Hello"
echo "World"

echo -n "No "
echo "New Lines"

# n3) String Concatenation with Echo
echo "one" "two" "three"

# n4) String Concatenation Character
echo "one" "two" \
"three"
# NOTE: (1) no space after backslash (2) thanks for the Ctrl+1 [VSCode](https://vscode-shortcuts.com/#integrated-terminal)

# n5) Echo With Tab Characters
echo -e "one \t two \t three"
# '$ man echo' for more info

# n6) Echo with Newline Characters
echo -e "one\ntwo\nthree"

# n7) --- separate file n7

# n8) Printing Strings that contain single quotes
echo "Welcome to Joe's bbq"

# n9) Printing Strings that contain double quotes
echo "My favorite movie is \"Limitless\""

# n10) ~ separate file m10_12

# n11) ~ separate file n10_12

# n12) ~ separate file n10_12

# n13) Single line comment
# this is a comment

# n14) Comments from middle of line
echo "Hi Mom" # this is a comment

# n15) Multi line comments using heredocs
<<linuxhint
whatever is written here will be considered a comment
yup still
linuxhint
echo "Copy?"
