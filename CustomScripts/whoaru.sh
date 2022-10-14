#!/bin/bash


<<Introduction
Hello world.
Figure this script as a password prompt screen.
Run it in the terminal and will ask your name, that's it.
Now, there are several scripted outcomes.
The way the script ends is fully up to you!
SPOILER: all three (1) variables, (2) if statements and (3) loops are involved.
Let's break down the script below, hope you like it!
(scroll down and you'll find comments starting with "# 1,2,")
(we are explaining them in these initial comments below)
Introduction

<<BreakdownBeginning
1 - welcomes the user and begs an answer
(serves as bait providing the system username variable)
2 - now the user must type & enter some input in the terminal
3 - from now on, different things may happen:
BreakdownBeginning

<<BreakdownOutcome1
3.1 - silly loop
This piece of code returns "excuse mey?" and prompts for user input
for as long as that input doesn't match either of the two scripted answers.
These are actually mentioned in the loop statement:
a. baitword = system username (your username, whatever it may be) 
b. keyword = "tusupervieja"
# ojo, puedo escribir mejor esta sintaxis (de forma que no necesite "&&")? 
BreakdownOutcome1

<<BreakdownOutcomes23
3.2 - baitword kick
If the user input matches the current username (ie. $USER)
the script will return "I'm busy, bye", wait 2 seconds and `exit` itself.
3.3 - keyword continue
So how to break the loop? Using cheats.
The only possible answer to break the loop is the keyword "tusupervieja".
BreakdownOutcomes23

<<BreakdownEnd
4 - actual welcome message & second bait question
5 - second user input prompt
6 - two possible ends:
6.1 - rickroll
Unless the second user input meets the system variable `hostname`,
the script will open the broswer to RickRoll the user and `exit` itself.
\# needs HEAVY polishing & INOP if using WSL...
6.2 - farewell
If the user input matches the config variable `hostname`,
then best wishes are given and the 'cowsay' command is run.
BreakdownEnd




# 1 - welcome prompt
echo "hi, are you $USER? 
what's your name?"

# 2 - user input
read whoaru

# 3 - OUTCOME 1 - silly loop
while [[ $whoaru != $USER && $whoaru != "tusupervieja" ]]
do
echo "excuse mey?" # OR echo "sorry, who?" .... hacer algo random tipo %
read whoaru
done

# 3 - OUTCOME 2 - baitword kick 
if [[ $whoaru == $USER ]]; then
echo "well i'm busy now
come sea me later"
sleep 2 && exit 1
fi 

# 3 - OUTCOME 3 - keyword continue
if [[ $whoaru == "tusupervieja" ]]; then
echo "NOICE" | lolcat
fi

# 4 - next question
echo "welcom $USER
how's your day going"

# 5 - second user input
read today

# 6 - END 1 - rickroll
if [[ $today != "$HOSTNAME" ]]; then
echo "well idc :)"
sleep 2
gio open https://youtu.be/dQw4w9WgXcQ &       # OJO xdg-open; thanks (https://www.linuxshelltips.com/linux-commands-to-open-url-in-browser)
exit
fi

# 6 - END 2 - farewell
echo "keep it up dawg!" && sleep 1
fortune | cowsay -f tux | lolcat
