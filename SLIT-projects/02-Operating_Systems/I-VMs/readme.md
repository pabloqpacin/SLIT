# (I) VMs - Linux Distros & Windows OSs

This project documents the process of **setup, config and admin** of numerous 'virtual machines' using *VirtualBox* within several host machines.

Our VMs are running multiple Linux distributions and certain Windows releases. TLDR- these are perhaps our favourite distros:
- [PopOS](#popos)
- [SUSE](#opensuse-tumbleweed)
- [Kali](#kali)


<details>
<summary>Table of Contents</summary>

- [(I) VMs - Linux Distros \& Windows OSs](#i-vms---linux-distros--windows-oss)
  - [current setup](#current-setup)
  - [documentation](#documentation)
  - [Linux Distros](#linux-distros)
    - [Debian-based](#debian-based)
      - [Mint](#mint)
      - [Ubuntu](#ubuntu)
      - [Xubuntu](#xubuntu)
      - [PopOS](#popos)
      - [Kali](#kali)
      - [Debian](#debian)
    - [RPM-based](#rpm-based)
      - [openSUSE-Tumbleweed](#opensuse-tumbleweed)
      - [Fedora](#fedora)
    - [Arch-based](#arch-based)
      - [Manjaro](#manjaro)
      - [EndeavourOS](#endeavouros)
  - [Windows](#windows)
    - [Windows 10](#windows-10)
    - [Windows 11](#windows-11)
  - [ASIR](#asir)
    - [A01-Ubuntu](#a01-ubuntu)
    - [A02-Windows10](#a02-windows10)
    - [A03-WindowsServerYYYY](#a03-windowsserveryyyy)

</details>


## current setup

- **Host Machines**
    - [C01-GL76](/SLIT-projects/01-Tinkering_Devices/_devices/C01-GL76.md) running **Windows 10** with i7-11800H processor and 16 GB of memory 
    - [C02-EX2511](/SLIT-projects/01-Tinkering_Devices/_devices/C02-EX2511.md) running **PopOS** with i5-4210U processor and *??* GB of memory

- ***v12n* software**
   - **VirtualBox 6.1.38** - all current VMs
   - **VirtualBox 7.0.4** - *not yet installed*


## documentation

- for #virtualization see [v12n-c14n](/SLIT-projects/02-Operating_Systems/_GEN/v12n-c14n.md) 
- for #Linux documentation see [linux-wiki](/SLIT-projects/02-Operating_Systems/_GEN/linux-wiki-md)

<!--
so...
what about 'validating' the ISOs tho?
(eg. Linux_Mint, Manjaro)
-->

## Linux Distros


<details>
<summary>see β-VMs (GL76)</summary>


|VMs|OS|imho|
|---|---|---|
|ubuntu00|Ubuntu 22.04|boring
|chicago95|Xubuntu 22.04|fun cuz *chicago95* theme
|popos|pop-os 22.04|best so far
|kaley|kali-linux 2022.3|kinda overwhelming, good stuff
|susey|openSUSE-Tumbleweed 20221008|smth wrong rn, must re-do cuz somehow luved it
|manjey-gnomey|manjaro-gnome 21.3.7|awkward but exciting
|manjey-i3|manjaro-i3 21.3.7|pretty awkward
|win10|Windows 10 22H2|strangely awkward too

</details>

### Debian-based

**Ubuntu** and similar distributions use `apt` to manage their packages (as well as `snap` and a few more tools as explained in [linux-wiki](/SLIT-projects/02-Operating_Systems/_GEN/linux-wiki.md)). Therefore `apt` commands should be used keep most software and computer programs updated and functional. These below are the standard commands to use in order to maintain a healthy system.

```bash
# update the system after installing it!
sudo apt update
apt list --upgradable
sudo apt upgrade -y
```

#### Mint

#### Ubuntu

<details>
<summary>ubuntu00-VM</summary>

<!--
user: gitgud
passwd: micro7
-->

```markdown
# CONFIG
1. Download
    - ISO 'ubuntu-22.04.1-desktop-amd64.iso' from *website* (3.56 GB)
2. Installation specs
    - Processors: 2
    - Memory: 2000 MB
    - Storage: *.vdi* - Normal 20 GB
3. Distro features
    - Desktop environment: GNOME
    - Package manager: `apt`
```

**FEATURES**

1. Written `kkk.sh` script:
```bash
#!/bin/bash

while true
do echo 'Are you scared?' | lolcat
done
```

</details>


<details>
<summary>NEOFETCH</summary>

![ubuntu00-neofetch](/SLIT-projects/02-Operating_Systems/images/VMs-A01-ubuntu00-neofetch.PNG)
</details>




#### Xubuntu

<details>
<summary>chicago95-VM</summary>

<!--
user: win95
passwd: piro12
-->

```markdown
# CONFIG
1. Download
    - ISO 'xubuntu-22.04.1-desktop-amd64.iso' from *website* (2.30 GB)
2. Installation specs
    - Processors: 2
    - Memory: 3072 MB
    - Storage: *.vdi* - Normal 20 GB
3. Distro features
    - Desktop environment: XFCE
    - Package manager: `apt`
```

**FEATURES**

1. Showcase **'Chicago95'** theme:
    - In a nutshell, run ['Chicagofier' script](https://github.com/dominichayesferen/Chicagofier) to easily install and enable the [Chicago95](https://github.com/grassmunk/Chicago95) Windows95-inspired XFCE Theme. Lotta fun!!

</details>

<details>
<summary>NEOFETCH</summary>

![chicago95-neofetch](/SLIT-projects/02-Operating_Systems/images/VMs-L02-chicago95-neofetch.PNG)
</details>


#### PopOS

In a nutshell... **cosmic shell**! Window Tiling manager pre-installed.

<details>
<summary>popos-VM</summary>

<!--
user: gitgud
passwd: micro7
-->

```markdown
# CONFIG
1. Download
   - ISO 'pop-os_22.04-amd64_intel_12.iso' from *website* (2.80 GB)
2. Installation specs
   - Processors: 4
   - Memory: 3072 MB
   - Storage: *.vdi* - Normal 20 GB
3. Distro features
   - Desktop environment: GNOME
   - Package manager: `apt`
```

> As of 20/11/2022: 'Low Disk Space' hence I may set up a new larger PopOS VM

**FEATURES**

1. Full setup as per relevant [02-OpSystems/_GEN](/SLIT-projects/02-Operating_Systems/_GEN/) documentation:
```markdown
- [oh-my-zsh]
- VSCode
- basic CLI programs:
    - cmatrix
    - cowsay
    - fortune
    - lolcat
    - neofetch
    - oneko
```

2. Written and improved `kkk.sh` script:
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


</details>

<details>
<summary>NEOFETCH</summary>

![popos-neofetch](/SLIT-projects/02-Operating_Systems/images/VMs-L03-popos-neofetch.PNG)
</details>


#### Kali

<details>
<summary>kaley-VM</summary>

<!--
user: kali
passwd: k
-->

```markdown
# CONFIG
1. Download
    - release 'kali-linux-2022.3-virtualbox-amd64.7z' from *website* (2.46 GB)
2. Installation specs
    - Processors: 2
    - Memory: 2048
    - Storage: *.vdi* - Normal 80 GB
3. Distro features
    - Desktop environment: XFCE
    - Package manager: `apt`
```


**FEATURES**

1. Written a `fighte.sh` script
```bash
#!/bin/bash

echo 'wilde beast. Pick a number to kill it! [0/1]'
beast=$((RANDOM%1))
read fighte

if [[ $fighte == $beast ]] ;
then echo 'ayee'
else echo -e 'u died beatch\n'
fi

fortune
```

</details>

<details>
<summary>NEOFETCH</summary>

![kaley-VM-neofetch](/SLIT-projects/02-Operating_Systems/images/VMs-kaley-neofetch.PNG)
</details>


#### Debian

### RPM-based

#### openSUSE-Tumbleweed

<details>
<summary>susey-VM</summary>

```markdown
# CONFIG
1. Download
2. Installation specs
3. Distro features
```

**FEATURES**

> Imma have to reinstall SUSE from scratch

</details>

<details>
<summary>NEOFETCH</summary>

![susey-VM-neofetch](/SLIT-projects/02-Operating_Systems/images/VMs-susey-neofetch.PNG)
</details>


#### Fedora

### Arch-based

These distros are different. Manjaro below is an **Arch-based**, 'rolling release' distro. Among other things, that means that it doesn't use the `apt` package manager, but all `pacman`, `octopi` and `pamac` (see [linux-wiki](/SLIT-projects/02-Operating_Systems/_GEN/linux-wiki.md) documentation).

#### Manjaro

<details>
<summary>manjey-GNOME-VM</summary>

<!--
user: gitgud
passwd: sh8
-->

```markdown
# CONFIG
1. Download
   - ISO 'manjaro-gnome-21.3.7-220816-linux515.iso' from *website* (3.33 GB)
2. Installation specs
   - Processors: 4
   - Memory: 4096 MB
   - Storage: *.vdi* - Normal 20 GB
3. Distro features
   - Desktop environment: GNOME
   - Package manager: `pacman`
```

- **Install Manjaro**: create VM, select ISO, boot up, install Manjaro, reboot and...

- **Update packages**

Now that Manjaro is installed in our VM, these are the `pacman` commands necessary to actually use the system.

```bash
# Update all packages
sudo pacman -Syu
	# -S --> synchronizes local packages with official database
	# -y --> downloads latest packages from database
	# -u --> after sync and download pkgs, they will be updated

# Enter YES when prompted
y

# Installing programs
sudo pacman -S neofetch
sudo pacman -S vscode
```

</details>

<details>
<summary>NEOFETCH</summary>

![manjey_gnome-VM-neofetch](/SLIT-projects/02-Operating_Systems/images/VMs-manjey-gnome-neofetch.PNG)
</details>

<details>
<summary>manjey-i3-VM</summary>

<!--
user: gitgud
passwd: sh8
-->



```markdown
# CONFIG
1. Download
2. Installation specs
3. Distro features
```

**FEATURES**

> Whatever this distro is... it is **pain**.


</details>


<details>
<summary>NEOFETCH</summary>

![manjey-i3-neofetch](/SLIT-projects/02-Operating_Systems/images/VMs-manjey-i3-neofetch.PNG)
</details>


#### EndeavourOS


## Windows

### Windows 10

### Windows 11

---

## ASIR

### A01-Ubuntu
### A02-Windows10
### A03-WindowsServerYYYY

