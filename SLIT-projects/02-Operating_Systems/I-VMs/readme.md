# (02) OSs - (I) VMs

This project documents fundamental **setup info & config actions** for numerous `virtual machines` in 2 host machines using the VirtualBox application.

Our VMs are running a wide variety of Linux distributions as well as certain Windows releases. Below... As a matter of fact, the most relevant Linux distros covered may be:
- [L03-PopOS](/SLIT-projects/02-Operating_Systems/I-VMs/L03-PopOS/)
- [L06-SUSE](/SLIT-projects/02-Operating_Systems/I-VMs/L06-SUSE/)
- [L07-Kali](/SLIT-projects/02-Operating_Systems/I-VMs/L07-Kali)

> Might turn the [EX2511](/SLIT-projects/01-Tinkering_Devices/_devices/C02-EX2511.md) machine into my main VM lab after successfully carrying out its *memory upgrade*


<details>
<summary>Table of Contents</summary>

- [(02) OSs - (I) VMs](#02-oss---i-vms)
  - [current setup](#current-setup)
  - [documentation](#documentation)
  - ['Linux cheat-sheet'](#linux-cheat-sheet)
    - [Debian-based distros](#debian-based-distros)
    - [Arch-based distros](#arch-based-distros)
  - [β-VMs (GL76)](#β-vms-gl76)
  - [Ω-VMs (GL76)](#ω-vms-gl76)

</details>


## current setup

**Host Machines Specs**

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
- for #Linux documentation see [SLIT/OSs/_GEN](/SLIT-projects/02-Operating_Systems/_GEN/)


## 'Linux cheat-sheet'


<details>
<summary>(DRAFT) Distros knowledge-base</summary>


### Debian-based distros

Basically `Ubuntu` and many similar distros work the same way and below you may find the steps I believe should be taken after installing.

Many examples in next section [β-VMs (GL76)](#β-vms-gl76). This below is a recap of First things to do after installing these Distros

```bash
# update your repositories
# first check for updates (assuming you don't change your mirrors)
sudo apt update

# assess new packages
apt list --upgradable

# actually update your system
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




