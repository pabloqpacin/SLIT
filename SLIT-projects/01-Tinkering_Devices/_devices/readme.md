# Tinkering Devices

*10/11/2022*

Summary-graph copypasted from [SLIT-materials](/SLIT-materials.md):

```mermaid

flowchart LR;

D{TINKERING DEVICES}
H{HOMELAB}

P{programming}
    P --> H


D --> mc
    mc[Microcontrollers] .- |arduino UNO / RPi Pico| mc
        mc .- |python / .ino| H

D --> C
    C[Computers] .- |Pentium A5920 EX2511| C
        C .- |repair upgrade salvage| H

D --> ad
    ad[Android devices] .- |tablets / smartphones| ad
        ad .- |salvage / root| H

D --> gc
    gc[game-consoles] .- |GB GBA NDS - Wii PS1 PS3| gc
        gc .- |repair / root| H


N{NETWORKING}
    N --> H


H .- robotics
    robotics .- AI & automation
H .- powerbank-DIY
H .- homeserver
    homeserver .- selfhosting-VPN
    homeserver .- selfhosting-websites
H .- hacking-lab
    hacking-lab .- malware-analysis
    hacking-lab .- pentesting

```

Graph 2.0:

```mermaid

graph LR;

D{DEVICES}

    D .- EC[electronic components]
        EC .- bcs[basic cirtuit stuff]
        EC .- mc[microcontrollers]
            mc .- UNO[arduino UNO]
            mc .- RPico(RPi Pico)
    D .- CC[computers' components]
        CC .- laptops
            laptops .- EX2511
            laptops .- A5920
        CC .- other
            other .- Pentium
    D .- A[Android]
        A .- sm[smartphones]
            sm .- sm1
            sm .- sm2
            sm .- sm3
            sm .- sm4
            sm .- sm5
            sm .- sm6
            sm .- sm7


        A .- tab[tablets]
            tab .- supernova[supernova]
            tab .- iPad[old iPad too]

    D .- GC[Game Consoles]
        GC .- handheld
            handheld .- GB
            handheld .- GBA
            handheld .- NDS

        GC .- stations
            stations .- Wii
            stations .- PS1
            stations .- PS3






P{Programming}
N{Networking}



    P .- GD{Game Devel.}
        GC .- GD
        sm .- GDG





```


---
*first commit lmao*

Pulling data from local LinWin Obsidian documentation!

- [Tinkering Devices](#tinkering-devices)
  - [Tablets](#tablets)
    - [Supernova](#supernova)
    - [iPAD model A1337](#ipad-model-a1337)
  - [Smartphones](#smartphones)
  - [Computers & Components](#computers--components)
    - [Pentium](#pentium)
    - [A5920](#a5920)
    - [EX2511](#ex2511)
    - [GL76](#gl76)
  - [Microcontrollers](#microcontrollers)
    - [Arduino UNO (in fact *Elegoo*)](#arduino-uno-in-fact-elegoo)
    - [Raspberry Pi Pico](#raspberry-pi-pico)
  - [Game consoles](#game-consoles)
    - [GameBoy](#gameboy)
    - [GameBoy Advance](#gameboy-advance)
    - [PS1](#ps1)
    - [PS3](#ps3)
    - [Wii](#wii)

## Tablets
### Supernova
### iPAD model A1337

## Smartphones


## Computers & Components
### Pentium
### A5920

<!--pre-dissassemble-->

| component | about |
| --- | --- |
| Machine | Acer Aspire 5920
| BIOS | v1.3809
| CPU | Intel Core 2 Duo T8100 (2) @ 2.101GHz
| GPU | Intel Mobile GM965/GL960
| Memory |  ... / 4 GB (2 GB x 2)
| Storage | |
| Battery | | 
| Resolution | 1280x800
| OS-00 | Windows 7
| OS-01 | Pop!OS 22.04 

**Troubleshooting?**


**software performance**

lorem ipsum




### EX2511
### GL76

## Microcontrollers
### Arduino UNO (in fact *Elegoo*)
### Raspberry Pi Pico

## Game consoles
### GameBoy
### GameBoy Advance
### PS1
### PS3
### Wii

