#!/bin/bash


# n25) chmod Command, Make Executable
echo "fortune | lolcat" > n25-deletemey.sh
chmod +x n25-deletemey.sh
./n25-deletemey.sh


# n26) chmod Command, make non-writeable, try to write in it
echo "You can't edit me nerd" > n26-deletemey
chmod -w n26-deletemey
nano n26-deletemey


# n27) chown file to different user, rn ls before and after
## TO-DO


# n28) Underscore variable, touch file, user underscore variable to append it
UND_VAR="Sup dawg"
touch n28-deletemey
echo "$UND_VAR" >> n28-deletemey
cat n28-deletemey




