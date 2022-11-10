#!/bin/bash

# n23) Simple Touch Command
touch n23-filetouch.txt
ls

# n24) Create a Symbol Link, Write to Linked FIle, Cat link file
ln -s n23-filetouch.txt link1
ls
echo "Now I am writing inside the link1" >> link1
cat link1