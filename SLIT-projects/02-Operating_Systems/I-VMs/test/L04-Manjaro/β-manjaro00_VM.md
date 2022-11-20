# β - manjaro00

<!--
user: gitgud
passwd: sh8
-->

## config

1. **Download**
   - ISO 'manjaro-gnome-21.3.7-220816-linux515.iso' from *website* (3.33 GB)
2. **Installation specs**
   - Processors: 4
   - Memory: 4096 MB
   - Storage: *.vdi* - Normal 20 GB
3. **Distro features**
   - Desktop environment: GNOME
   - Package manager: `pacman`

<details>
<summary>Click to see Neofetch</summary>

![Manjaro_GNOME-neofetch]()

</details>

## install/system update - `pacman`

All previous VMs in this repo were **Ubuntu-based** (ie. Debian-based) Linux distributions.
Now Manjaro is different, Manjaro is an **Arch-based**, 'rolling release' distro. Among other things, that means that it doesn't use the `apt` package manager, but all `pacman`, `octopi` and `pamac` instead ([documentation](https://youtu.be/dQw4w9WgXcQ)). <!--how about `calamares`? and where should I discuss `snap`, `flatpack` and all that?? lmao-->

- **Install Manjaro**
  - create VM
  - select ISO
  - boot up
  - install Manjaro
  - reboot

Now that Manjaro is installed in our VM, these are the `pacman` commands necessary to actually use the system.

```bash
# Update all packages
sudo pacman -Syu
	# -S --> synchronizes local packages with official database
	# -y --> downloads latest packages from database
	# -u --> after sync and download pkgs, they will be updated

# Enter YES when prompted
y

# Install programs
sudo pacman -S neofetch
sudo pacman -S vscode

```




## VM features

1. Setup as per [02-OpSystems/_GEN](/SLIT-projects/02-Operating_Systems/_GEN/)...
- [ ] [oh-my-zsh]
- [ ] VSCode
- [ ] basic CLI programs:
    - [ ] cmatrix
    - [ ] cowsay
    - [ ] fortune
    - [ ] lolcat
    - [ ] neofetch
    - [ ] oneko

2. Written `kkk.sh` script:
```bash
#!/bin/bash

echo -e '\nH-' && sleep 2
echo "Hi $USER" && sleep 2
echo -e '\nDoes you like rainbows?'
    read daigual

while true
do echo 'Are you scared?' | lolcat
echo -e '\tAre you scared?' | lolcat
done
```


3. Written `sakura.sh` script:
```bash
#!/bin/bash
oneko -sakura &
```

<!--
Y TF can't I run it on WSL tho lol
-->

4. Tweaked `.zshrc` config (see [_CLI](/SLIT-projects/02-Operating_Systems/_GEN/_CLI.md) documentation for more details)

```bash
ZSH_THEME="random"

ZSH_THEME_RANDOM_CANDIDATES=("3den" "afowler" "apple" # ...
    "tjkirch_mod" "wedisagree" "wezm" "wuffers" "zhann")
```

<!--
5. Tested TEA_INVADERS in this machine lol
-->



## **Manjaro** key features

1. `pacman`