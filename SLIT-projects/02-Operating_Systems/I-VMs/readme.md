# (I) VMs - Linux Distros & Windows

This project documents fundamental **setup info & config actions** for numerous `virtual machines` in 2 host machines using the VirtualBox application.

Our VMs are running a wide variety of Linux distributions as well as certain Windows releases. Below... As a matter of fact, the most relevant Linux distros covered may be **(DRAFT)**:
- [L03-PopOS](/SLIT-projects/02-Operating_Systems/I-VMs/L03-PopOS/)
- [L06-SUSE](/SLIT-projects/02-Operating_Systems/I-VMs/L06-SUSE/)
- [L07-Kali](/SLIT-projects/02-Operating_Systems/I-VMs/L07-Kali)

> Might turn the [EX2511](/SLIT-projects/01-Tinkering_Devices/_devices/C02-EX2511.md) machine into my main VM lab after successfully carrying out its *memory upgrade*


<details>
<summary>Table of Contents</summary>

- [(I) VMs - Linux Distros \& Windows](#i-vms---linux-distros--windows)
  - [current setup](#current-setup)
  - [documentation](#documentation)
  - [Linux Distros](#linux-distros)
    - [Debian-based](#debian-based)
      - [Mint](#mint)
      - [Ubuntu](#ubuntu)
      - [Xubuntu](#xubuntu)
      - [PopOS](#popos)
      - [Kali](#kali)
    - [RPM-based](#rpm-based)
      - [openSUSE Tumbleweed](#opensuse-tumbleweed)
    - [Arch-based](#arch-based)
      - [Manjaro](#manjaro)
      - [...](#)
  - ['Linux cheat-sheet'](#linux-cheat-sheet)
    - [Debian-based distros](#debian-based-distros)
    - [Arch-based distros](#arch-based-distros)
  - [β-VMs (GL76)](#β-vms-gl76)
  - [Ω-VMs (GL76)](#ω-vms-gl76)

</details>


## current setup

- **Host Machines Specs**

|specs|[C01-GL76](/SLIT-projects/01-Tinkering_Devices/_devices/C01-GL76.md)|[C02-EX2511](/SLIT-projects/01-Tinkering_Devices/_devices/C02-EX2511.md)|
|---|---|---|
|OS|Windows 10|PopOS|
|CPU|i7-11800H| - |
|Memory|16 GB| - |
|Storage|1 TB SSD| - |
|Resolution|1920 x 1080| - |


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

```markdown
<details>
<summary></summary>

</details>
```

### Debian-based

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

<details>
<summary>Click to see Neofetch</summary>

![ubuntu00-neofetch](/SLIT-projects/02-Operating_Systems/images/VMs-A01-ubuntu00-neofetch.PNG)
</details>

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

<details>
<summary>Click to see Neofetch</summary>

![chicago95-neofetch](/SLIT-projects/02-Operating_Systems/images/VMs-L02-chicago95-neofetch.PNG)
</details>

</details>


#### PopOS

```markdown
## PopOS Deskey features 
- Cosmic shell!
   - Delighful **Window Tiling manager** pre-installed
   - Delightful **system shortcuts / key-bindings**
```


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

2. Written an improved `kkk.sh` script:
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


<details>
<summary>Click to see Neofetch</summary>

![popos-neofetch](/SLIT-projects/02-Operating_Systems/images/VMs-L03-popos-neofetch.PNG)
</details>

</details>


#### Kali

### RPM-based

#### openSUSE Tumbleweed

### Arch-based

#### Manjaro

#### ...




## 'Linux cheat-sheet'


<details>
<summary>(DRAFT) Distros knowledge-base</summary>


### Debian-based distros

Basically `Ubuntu` and many similar distros work the same way and below you may find the steps I believe should be taken after installing.

Many examples in next section [β-VMs (GL76)](#β-vms-gl76). This below is a recap of First things to do after installing these Distros

```bash
# update your repositories
sudo apt update
apt list --upgradable
sudo apt upgrade -y
```


### Arch-based distros

```bullshie
bullshie
```


</details>



## β-VMs (GL76)


<details>
<summary>See relevant spreadsheet</summary>


<!--
> β == Beta (to be deleted) --- Ω == Omega (to be maintained)
>
> A == ASIR --- L == Linux --- W == Windows
-->

|specs/features|[ubuntu00](/SLIT-projects/02-Operating_Systems/I-VMs/A01-Ubuntu/β-ubuntu00_VM.md)|[chicago95](/SLIT-projects/02-Operating_Systems/I-VMs/L02-Xubuntu/β-chicago95_VM.md)|[popos](/SLIT-projects/02-Operating_Systems/I-VMs/L03-PopOS/β-popos_VM.md)|[manjaro00](/SLIT-projects/02-Operating_Systems/I-VMs/L04-Manjaro/β-manjaro00_VM.md)|[manjey-i3](/SLIT-projects/02-Operating_Systems/I-VMs/L04-Manjaro/β-manjey-i3_VM.md)|[susey](/SLIT-projects/02-Operating_Systems/I-VMs/L06-SUSE/β-susey_VM.md)|[kaley](/SLIT-projects/02-Operating_Systems/I-VMs/L07-Kali/β-kaley_VM.md)|[10VM](/SLIT-projects/02-Operating_Systems/I-VMs/W01-Windows10/β-10VM_VM.md)|[win10](/SLIT-projects/02-Operating_Systems/I-VMs/W01-Windows10/β-win10_VM.md)|
|---|---|---|---|---|---|---|---|---|---|
|OS|Ubuntu 22.04|Xubuntu 22.04|PopOS|Manjaro|Manjaro|Tumbleweed|Kali Linux|Windows 10|Windows 10|
|ISO size|3.56 GB|2.30 GB|
|Desktop Env.|GNOME|XFCE|GNOME||||| - | - |
|Processors|2|2|4|4|4|4|2|4|6|
|Memory|2000 MB|3072 MB|3072 MB|4096 MB|4096 MB|4096 MB|2048 MB|4096 MB|8000 MB|
|Storage (*'Normal' .vdi*)|20 GB|20 GB|20 GB|20 GB|20 GB|20 GB|80 GB|50 GB|80 GB|
|Resolution|
|notes...| - |Chicago95 Theme|**proper**||Arch-based||Kali ISO for VMs

</details>




## Ω-VMs (GL76)

<!--
<details>
<summary>See relevant spreadsheet</summary>


</details>
-->




