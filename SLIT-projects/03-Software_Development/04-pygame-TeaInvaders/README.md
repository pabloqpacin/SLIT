# Tea Invaders (Pygame)


Early **Python** project using [Pygame](https://www.pygame.org/wiki/about) modules.

**Tea Invaders** is basically the result of tweaking [this tutorial](https://youtu.be/FfWpgLFMI7w) by [@attreyabhatt](https://github.com/attreyabhatt) with:
- custom images
- extra features:
  - lives/health system

## Screenshots
<img src="/pygame-TeaInvaders/images/game-screenshot.PNG" alt="screenshot" width="700"/>

![skreenshut](/SLIT-projects\03-Software_Development\04-pygame-TeaInvaders\images\game-screenshot.PNG)

[//]: <> (C:\Users\Usuario\Downloads\linwin\SLIT\SLIT-projects\03-Software_Development\04-pygame-TeaInvaders\images\game-screenshot.PNG)


## Requirements
- [Python](https://python.org) interpreter 
- [Pygame](https://www.pygame.org/wiki/GettingStarted)

[//]: <> (in Linux enter `sudo apt-get install python3-pygame`)
- **Recommended**: VSCode + Python extension

## How to play?
1. Open [download-directory.github.io](https://download-directory.github.io) and `ENTER` the folder URL "https://github.com/pabloqpacin/SLIT/tree/main/Pygame101-Tea_Invaders"
2. Find the **.zip file** in your designated Downloads folder, **extract** it and please open this **new folder** in **VSCode** or **Terminal** 
3. Now you probably want to make sure **python** and **pygame** are installed. Having done so, let's run the game!

   1. In VSCode, open the *main.py* file and press `Ctrl+Alt+N`
   2. In the Terminal, simply run `python3 main.py`   

4. **VANQUISH THE TEAS!**

Beware, game performance may vary from one machine to another and yours might render an utterly slow and clunky game. If so, please dive into the code and modify parameters such as `playerX_change=0.25` or `bulletY_change=0.4` to improve sprites' speed and overall performance. For the enemies you might want to change both `enemyX_change.append(0.02)` and `enemyX_change[i] = 0.2`.



## Gameplay

You are Atatürk, back and ready to defend your screen against the **Tea Invaders**

As the game starts you should find 12 *Teas* navigating the pink sky to the beat of [Altin Gün's 'Kısasa Kısas'](https://youtu.be/eXuGAOV0JH0)

Now prepare yourself a drink and start shooting *Gin-Tonics* at the enemies

- MOVE WITH `LEFT/RIGHT` ARROWS
- SHOOT WITH `SPACE`

The game will be over when the **Tea Invaders** reach your position or after missing 7 shots

Atatürk never missed a shot tho so have yourself some **rakı** for every invader army crushed aye!


## Coming soon

Improvements and general overhaul coming in due time!

Check [to-do](/Pygame101-Tea_Invaders/to-do.md) to find out more and contribute!



## Disclaimer

This project was completed within a few days back in August as means to learn:
  - programming 101s
  - how to use an IDE (ie. VSCode)
  - Python programming

My main computer runs *Windows10* and as of today (last commit date) I can't really figure out how did I set everything up so nicely back in the day (eg. python interpreter, vscode config, etc). Now I have indeed managed to run the game in some freshly installed Linux distros, so the given instructions should work for you just fine, plus documentation is close at hand. Thanks for reading and I hope you find it useful!


