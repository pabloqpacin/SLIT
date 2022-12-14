# WIP-REWORK

*14/12/2022*

> REWORK2023


- [WIP-REWORK](#wip-rework)
  - [**f817bd0**](#f817bd0)
    - [SLIT-PROJECTS...](#slit-projects)
  - [1f47cc2](#1f47cc2)
  - [??](#)
  - [??](#-1)



## **f817bd0**


```bash
# Save current 'main' branch as `main-bk`
git checkout -b main-bk
git checkout main

# Create WIP branch
git checkout -b wip-rework

# Hide the crap
echo .test > .gitignore
mv -t .test images SLIT test SLIT-materials.md SLIT-projects


# COMMIT!
git add .
git commit -m "Start REWORK-2023

- Set WIP branch in 'wip-rework'
- Create '.gitignore' for odd documentation
- Planning to focus of 'SLIT-projects' rework!
"

# PUSH!
git push -u origin wip-rework


# SUPA LATE
git checkout main && git merge wip-rework
...
```


### SLIT-PROJECTS...

1. Tinkering Hardware
   - (ANY PROJECT HERE?? MAYBE NOT)
2. Operating Systems
   - VMs??
3. Software Development
   - bash-custom
   - bash-Chuck
   - bash-extra
   - python-fcc
   - python-TeaInvs
   - flask
   - ~~django~~
   - ~~mySQL~~
   - ~~Golang~~
4. Networking Security 
   - (NO PROJECTS!!)





## 1f47cc2


```bash
# keeping most stuff ignored, especially 'materials'

# resurface'projects' as 'scripts' and 'src'


# improve '.gitignore'
echo -e '\n__pycache__ \ninstance/ \n ' >> .gitignore


# COMMIT!
git commit -m "Resurface PROJECTS & grow '.gitignore'

- Bash projects to 'scripts'
- Python projects to 'src'
- Improve '.gitignore' for Python stuff
"
```


## ??

```bash
# supdawg
git log --oneline

<<...
...

git commit -m "Basic README presentation

- Include BREAKDOWN list with links to sub-directories
"
```



## ??

```bash
<<...
...

git commit -m "



- Readmes
  - IMPROVE THEM ALL! (6)


- Screenshots for 
  - pythonTerminalGames
  - pygameTea-Invaders
  - flaskDevWebsite

- Else
"
```
