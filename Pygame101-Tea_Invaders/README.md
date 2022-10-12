# Tea Invaders (Pygame)


Early **Python** project using [Pygame](https://www.pygame.org/wiki/about) modules.

**Tea Invaders** is basically the result of tweaking [this tutorial](https://youtu.be/FfWpgLFMI7w) by [@attreyabhatt)](https://github.com/attreyabhatt) with
- custom images
- background music
- extra features:
  - lives/health system


![screenshot](/images/game-screenshot.PNG)


## Requirements
- [Python](https://python.org) interpreter 
- [Pygame](https://www.pygame.org/wiki/GettingStarted)

[//]: <> (in Linux enter `sudo apt-get install python3-pygame`)
- Visual Studio Code
- VSCode Python extension (by Microsoft) <!--It should take a bit to install-->


## How to play?
1. Open [download-directory.github.io](https://download-directory.github.io)
2. Enter the folder URL `https://github.com/pabloqpacin/SLIT/tree/main/Pygame101-Tea_Invaders`
3. Find the **project .zip file** in your Downloads folder and **extract** it
4. Now open the folder directly with **VSCode** (so that all image and audio assets are available for the the game to run successfully)
5. Now VSCode may ask you to install "the recommended extensions for Python",and we do clicking on `Install`
6. If everything is installed correctly, you could open the **main.py** file from within VSCode, run the code (enter `Ctrl+Alt+N`) and the game screen will come up ready to play!

Now beware, the program speed and performance may vary from one machine to other, so please tinker with speed-related settings such as `playerX_change=0.25` or `bulletY_change=0.4`.


## Gameplay

You are Atatürk, back and ready to defend your screen against the **Tea Invaders**.

As the game starts you should find 12 *Teas* navigating the pink sky to the beat of [Altin Gün's 'Kısasa Kısas'](https://youtu.be/eXuGAOV0JH0).

Now prepare yourself a drink and start shooting *Gin-Tonics* at the enemies.

- MOVE WITH `LEFT/RIGHT` ARROWS
- SHOOT WITH `SPACE`

The game will be over when the **Tea Invaders** reach your position or after missing 7 shots.

Atatürk never missed a shot so have yourself some **rakı** for every invader army crushed aye!


## Coming soon

Improvements and general overhaul coming in due time!

Check [to-do](/to-do.md) to find out more and contribute!



## Disclaimer

This project was completed within a few days back in August as means to learn:
  - programming 101s
  - how to use an IDE (ie. VSCode)
  - Python programming

My main computer runs *Windows10* and as of today (last commit date) I don't remember exactly how I set everything up back in the day (eg. python interpreter, vscode config, etc). Now I have managed to run the game in a freshly installed Pop!OS Linux virtual machine, so the given instructions should work for you as well. Ngl, the game keeps crashing in my VM but it works like a charm in my actual Windows machine. Thanks for reading and I hope you find it useful!


