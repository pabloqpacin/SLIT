# Tinkering Devices

*10/11/2022*


<details>
<summary>Click to see graph n.1</summary>

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

</details>




<details>
<summary>Click to see graph n.2</summary>

Graph 2.0:

```mermaid

graph LR;

D{DEVICES}

    EC[electronic components]
        EC .- bcs[basic cirtuit stuff]
        EC .- mc[microcontrollers]
            mc .- UNO[arduino UNO]
            mc .- RPico(RPi Pico)
    CC[computers' components]
        CC .- laptops
            laptops .- EX2511
            laptops .- A5920
        CC .- other
            other .- Pentium
    A[Android]
        A .- sm[smartphones]
            sm .- sm1
            sm .- sm2
            sm .- sm3
            sm .- sm4
            sm .- sm5



        A .- tab[tablets]
            tab .- supernova[supernova]
            tab .- iPad[old iPad too]

    GC[Game Consoles]
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
        GC --> GD
        sm .- GDG


```

</details>



---


Current set of *devices* I own, may tinker with and salvage from:

|computers|tablets|smartphones|SBCs|MCs|GC-handheld|GC-stations|
|---|---|---|---|---|---|---|
|C01-GL76|T01-Supernova|S01-...||MC01-Elegoo_UNO|GB|Wii
|C02-EX2511|T02-A1337|S02-...||MC02-RPico|GBA|PS1
|C03-A5920||S03-...|||NDS|PS3
|C04-Pentium||S04-...||||


> General specs-chart might be here for as many devices as possible aye!

<details>
<summary>Click to see a draft for the 'specs-chart'</summary>


|C01-GL76|...|S02-nokia|...|
|---|---|---|---|
|manufacturer|
|model name|
|CPU|
|GPU|
|RAM|
|storage|
|battery|
|resolution|
|OS|
|fate|



</details>