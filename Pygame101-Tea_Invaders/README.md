# Tea Invaders (Pygame)


Early **Python** project using [Pygame](https://www.pygame.org/wiki/about) modules.

**Tea Invaders** is basically the result of tweaking [this tutorial](https://youtu.be/FfWpgLFMI7w) by [@attreyabhatt](https://github.com/attreyabhatt) with:
- custom images
- extra features:
  - lives/health system

## Screenshots
<img src="/Pygame101-Tea_Invaders/images/game-screenshot.PNG" alt="screenshot" width="700"/>


## Requirements
- [Python](https://python.org) interpreter 
- [Pygame](https://www.pygame.org/wiki/GettingStarted)

[//]: <> (in Linux enter `sudo apt-get install python3-pygame`)
- **Recommended**: VSCode + Python extension

## How to play?
1. Open [download-directory.github.io](https://download-directory.github.io), enter the folder URL "https://github.com/pabloqpacin/SLIT/tree/main/Pygame101-Tea_Invaders" and press `ENTER` 
2. Find the **.zip file** in your designated Downloads folder, **extract** it, right-click it and please open it in **VSCode** or **Terminal** 
3. Now you probably want to make sure **python** and **pygame** are installed! Having done so, let's run the game!

   1. Run `python3 main.py` in your Terminal window
   2. Run `Ctrl+Alt+N` in the VSCode window



Now beware, the game performance may vary from one machine to another, so please tinker with settings such as `playerX_change=0.25` or `bulletY_change=0.4` to improve the speed of any sprites. For the enemies you should change both `enemyX_change.append(0.02)` and `enemyX_change[i] = 0.2`.



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

My main computer runs *Windows10* and as of today (last commit date) I don't remember exactly how I set everything up back in the day (eg. python interpreter, vscode config, etc). Now I have managed to run the game in a freshly installed Pop!OS Linux virtual machine, so the given instructions should work for you as well. Ngl, the game keeps crashing in my VM but it works like a charm in my actual Windows machine. Thanks for reading and I hope you find it useful!


