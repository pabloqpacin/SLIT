8. ## separated trunks


```mermaid
flowchart TD;

SLIT{SLIT}

AI[automation: bots/robots]
CS[Computer Science]
D{DEVSYSADMIN}
DIY[DIY: NAS, router, powerbank, -salvage-]
GD[GameDev]
E[Electronics -theory-]
LL[low-level computing]
homelab{homelab}
HS[Home Server]
HL[Hacking Lab]
KD[Kernel Development]
mc[microcontrollers]
ml[machine learning]
MP[Malware / Pentesting]
NS{4. Network Security}
PS[Programming -scripting-]
RE[Reverse Engineering]
repair[repair & upgrade electronics]
repurpose[repurpose]
SA{2. Operating Systems}
SC[salvaged components]
server[server admin]
SD{3. Software Development}
T{1. Tinkering}
V[Virtualization]
WD[Web Development]
?[college & job environment]

```


``` mermaid

graph LR;

?{?}

SLIT 

    SLIT --> IA(I - HOMELAB A)
        IA .- 1(1. Tinkering)
            1 .- |electronics| HP{homelab projects}

    SLIT --> II(II - PROGRAMMING)
        II .- 2(2. Operating Systems)
            2 .- HP

        II .- 3(3. Software Engineering)
            3 .- |self-taught dev| HP

    SLIT --> IB(I - HOMELAB B)
        IB .- 4(4. Network Security)
            4 .- |infosec| HP


HP

    HP .- LL(low-level)
        LL .- mc(microcontrollers)
        LL .- SC(salvaged components)
            mc .- |.ino python| ?
            SC .- |repair root upgrade| ?
            SC
        LL --> |smart DIY| HS(home server)
            HS .- |hack-proof| self-hosting

    HP .- N(networking)
        N --> HS
        N --> HL       


    HP .- |VMs| HL(hacking lab)
            HL .- |kali linux| pentesting
            HL .- |reverse-engineer| malware
            
    HP .- W(Windows)

        W .- Security
            Security .- malware
        W --> |code| CPS(CMD powershell)
        W .- |dev| WSL


    HP .- L(Linux)

        L --> Bash(Bash ZSH)
        L .- Distros
        L .- |dev| Kernel


    HP .- SD(software devel.)

        SD .- GD(game devel.)
            GD .- |reverse-engineering| mod-making
        SD --> PY(Python)
            PY .- ml(machine learning)
            PY .- Backend
        SD .- |flask / JS| WD(web devel.)
            WD --> Backend




```




``` mermaid

graph LR;

?{?}

SLIT 

    SLIT --> IA(I - HOMELAB A)
        IA .- 1(1. Tinkering)
            1 .- |electronics| HP{homelab projects}

    SLIT --> II(II - PROGRAMMING)
        II .- 2(2. Operating Systems)
            2 .- HP

        II .- 3(3. Software Engineering)
            3 .- |self-taught dev| HP

    SLIT --> IB(I - HOMELAB B)
        IB .- 4(4. Network Security)
            4 .- |infosec| HP


HP

    HP .- LL(low-level)
        LL .- mc(microcontrollers)
        LL .- SC(salvaged components)
            mc .- |.ino python| ?
            SC .- |repair root upgrade| ?
            SC
        LL --> |smart DIY| HS(home server)

    HP .- N(networking)
        N .- HS
            HS --> |hack-proof| self-hosting
        N .- HL       


    HP .- |VMs| HL(hacking lab)
            HL --> |kali linux| pentesting
            HL --> |reverse-engineering| malware
            
    HP .- W(Windows)

        W .- Security
        W --> |code| CPS(CMD powershell)
        W .- |dev| WSL


    HP .- L(Linux)

        L --> Bash(Bash ZSH)
            Bash .- S(Scripting)
        L .- Distros
            Distros .- distros(Ubuntu-based & Arch-based)
        L .- |dev| Kernel


    HP .- SD(software devel.)

        SD .- GD(game devel.)
            GD .- |reverse-engineering| mod-making
        SD --> PY(Python)
            PY .- S
            PY .- ml(machine learning)
            PY .- Backend
        SD .- |flask / JS| WD(web devel.)
            WD --> Backend




```


``` mermaid

graph LR;

?{?}

SLIT{SLIT materials} 

    SLIT --> IA(I - HOMELAB A)
        IA .- 1(1. Hardware Tinkering)
            1 .- |electronics| SP{SLIT projects}

    SLIT --> II(II - PROGRAMMING)
        II .- 2(2. Operating Systems)
            2 .- SP

        II .- 3(3. Software Engineering)
            3 .- |self-taught dev| SP

    SLIT --> IB(I - HOMELAB B)
        IB .- 4(4. Network Security)
            4 .- |infosec| SP


SP

    SP .- T(Tinkering*)
        T .- |repair upgrade salvage| electronics(microcontrollers / components)
            electronics .- robots{robots}
            electronics  --> |DIY| HS{home server}
                HS .- self-hosting



    SP .- NSA(net/sysadmin)

        NSA .- IS(INFOSEC)
            IS .- HS
        NSA --> |Bash| Linux
            Linux .- D{distrohopping}
            Linux .- Kernel
                Kernel .- os{opensource}
        NSA --> |cmd powershell| Windows
            Windows .- WSL



    SP .- SD(Software Devel.)

        SD --> os
        SD .- |Python| AI(AI machine  learning)
            AI .- bots{bots}
        SD .- GD(game devel.)
            GD .- |reverse-engineering| mod-making
        SD .- |Flask JS| WD(web devel.)
            WD --> B{Backend}


    SP .- HL(hacking lab)
                    HL --> |kali-linux| pentesting .- |networks / websites| pentesting
                    HL --> |Windows| malware-analysis .- |scripting / reverse-engineering| malware-analysis


```

```markdwon

# SLIT materials

1. ## Hardware Tinkering

2. ## Operating Systems

3. ## Software Engineering

4. ## Network Security

# SLIT homelab projects

1. ## Tinkering

### microcontrollers > robots

### salvaged components > (DIY) home server > (infosec) self-hosting

2. ## netsysadmin

### Linux > Bash

### Linux > distros

### Windows > WSL


4. ## INFOSEC

### hacking lab > malware analysis

### hacking lab > pentesting

```

---

# previously in SLIT readme


1. ## SLIT graph

```mermaid

graph LR;


SLIT{SLIT}

SLIT --> T
T[Tinkering]
T.- |security| N
T .- |repair-salvage| E


E[electronics]
E .- |smart DIY| H
N[networking]
N .- |NAS| H


H{HOMELAB}
H .- |robotics| automation
H .- |malware| hacking-lab
H .- |self-hosting| home-server
H --> 2022


2022{pabloqpacin 2022+}
D --> 2022
D{DEVSYSADMIN}
D .- |Python| AI(artificial intelligence)
D .- |reverse engineering| game(gamedev/modding)
D .- |frameworks| web-dev


SLIT --> P
P[Programming]
sysadmin[sysadmin]
SD[software dev.]


P .- |OS config| sysadmin
P .- |languages| SD

sysadmin .- |shell dev.| D
SD .- |backend| D


```


2. ## ↓ DEVSYSADMIN


```mermaid
graph LR;

CS[Computer Science]

CS .- |electronics| OSs
OSs .- Android
OSs .- Linux
OSs .- Windows

CS --> |sysadmin| D
HOMELAB --> |networking| D
SD(Software Development) --> |developer| D
SD .- P(programming)
D{DEVSYSADMIN}
P .- AIML(Artificial Intelligence & Machine Learning)
P .- GameDev
P .- L(languages -a)
P .- Python
P .- web-dev
```

3. ## ↑ HOMELAB-short

```mermaid

graph LR;

    HOMELAB --> electronics
    electronics.-microcontrollers-->Tinkering
    electronics.-salvage.-computer_components-->Tinkering
    HOMELAB --> networking --> Tinkering
```

4. ## ↑ HOMELAB-long


5. ## ↑ HOMELAB-devices



# *SLIT-materials* taglist(rows)

