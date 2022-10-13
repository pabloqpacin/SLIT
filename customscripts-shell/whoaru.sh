#!/bin/bash


<<Introduction
Hello world.
Figure this script as a password prompt screen.
Run it in the terminal and it will ask your name, that's it.
Now, there are several scripted outcomes.
The way the script ends is fully up to you!
SPOILER: all three variables, if statements and loops are involved.
Let's break down the script below, hope you like it!
Introduction

<<BreakdownBeginning
(scroll down and you find a comment starting with "# 1")
(we explain that and every other line in this section)
1 - welcomes the user subtly prompting for user input
baits answer as provides the actual username system variable
2 - now user must type & enter answer in terminal to continue
3 - now different things may happen:
BreakdownBeginning

<<BreakdownOutcome1
3.1 - silly loop
This code keeps the user in a loop as long as the user input
doesn't match the scripted answers required to continue.
These two scripted answers are mentioned in loop statement:
1. baitword = system username (your username, whatever it might be) 
2. keyword = "tusupervieja"
While user input is different from that, the script will keep repeating
"excuse mey?" and prompting for user input again and again.
\# ojo, puedo escribir mejor esta sintaxis (de forma que no necesite "&&")? 
BreakdownOutcome1

<<BreakdownOutcome2
3.2 - baitword kick
Now this code has the script close itself.
If, at any time, the user input matches the current username (ie. $USER),
the script will basically tell the user "I'm busy, bye".
After two seconds, the script will *exit* itself, terminating the script.
BreakdownOutcome2

<<BreakdownOutcome3
3.3 - keyword continue
So how to break the loop? Using cheats.
The only possible answer to break the loop is the keyword "tusupervieja".
BreakdownOutcome3

<<BreakdownEnd
4 - actual welcome message
second bait question for this second part
5 - second user input prompt
6 - two possible ends:
6.1 - rickroll
Unless the second user input meets the system variable `hostname`,
the script will open the broswer to RickRoll the user and exit *exit*
\# needs HEAVY polishing
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
xdg-open https://youtu.be/dQw4w9WgXcQ &       # OJO xdg-open; thanks (https://www.linuxshelltips.com/linux-commands-to-open-url-in-browser)
exit
fi

# 6 - END 2 - farewell
echo "keep it up dawg!" && sleep 1
fortune | cowsay -f tux
