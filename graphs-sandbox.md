# DELETE: graphs-sandbox

- [DELETE: graphs-sandbox](#delete-graphs-sandbox)


1. ## from DEVSYSADMIN with HOMELAB to SLIT



```mermaid
graph LR;


H{HOMELAB}


T[Tinkering]
H .- T


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


NS[Networking & Security]





SLIT{SLIT}


```


2. ## DEVSYSADMIN

```mermaid
flowchart LR;

SLIT{SLIT}

AI[automation: bots/robots]
D{DEVSYSADMIN}
GD[GameDev]
LL[low-level / computer components circuits]
HS[Home Server]
HL[HackingLab]
KD[Kernel Development]
ml[machine learning]
MP[Malware / Pentesting]
NS[Network Security]
OS[OS]
py[Python]
PS[Programming / Scripting]
RE[Reverse Engineering]
repair[repair, restore]
repurpose[repurpose]
SA[System Admin]
salvage[salvage]
SD[Software Development]
TE[Tinkering / Electronics]
WD[Web-Dev]




SLIT .- 4 .- NS
    NS .- HS


SLIT .- 1 .- TE
    TE .- LL
        LL .- repair
        LL .- repurpose
            repurpose .- HS
                HS .- D
        LL .- PS
  

SLIT .- 2 .- SA
    SA .- PS
        PS .- SD



SLIT .- 3 .- SD
    SD .- D





```
3. ## BRAINSTORM

```mermaid
flowchart LR;

SLIT{SLIT}

AI[automation: bots/robots]
D{DEVSYSADMIN}
GD[GameDev]
E[Electronics]
LL[low-level computing]
HS[Home Server]
HL[HackingLab]
KD[Kernel Development]
ml[machine learning]
MP[Malware / Pentesting]
NS[Network Security]
OS[OS]
py[Python]
PS[Programming / Scripting]
RE[Reverse Engineering]
repair[repair, restore]
repurpose[repurpose]
SA[System Admin]
salvage[salvage]
server[server admin]
SD[Software Development]
T[Tinkering]
WD[Web-Dev]




SLIT .- 4 .- NS
    NS .- server
        server .- D


SLIT .- 1 .- T
    T .- E
    E .- LL
        LL .- repair
            repair .- D
        LL .- repurpose
            repurpose .- server
        LL .- PS
  

SLIT .- 2 .- SA
    SA .- LL



SLIT .- 3 .- SD
    SD .- PS
    PS .- D




```


4. ## pos-devsysadmin

```mermaid
flowchart LR;

SLIT{SLIT}

AI[automation: bots/robots]
CS{Computer Science}
D{DEVSYSADMIN}
DIY[DIY: NAS, router, powerbank, -salvage-]
GD[GameDev]
E[Electronics -theory-]
LL[low-level computing]
homelab{homelab}
HS{Home Server}
HL[HackingLab]
KD[Kernel Development]
mc[microcontrollers: RPico, UNO]
ml[machine learning]
MP[Malware / Pentesting]
NS{Network Security}
OS[OS]
Py[Python]
PS[Programming / Scripting]
RE[Reverse Engineering]
repair[repair, restore]
repurpose[repurpose]
SA{Operating Systems}
salvage[salvage]
server[server admin]
SD{Software Development}
T{Tinkering}
V[Virtualization]
WD[Web-Dev]


CS .- E
    E .- LL
        LL .- T
            T .- mc
            T .- salvage
                salvage .- repair
                salvage .- repurpose
                    homelab .- DIY
                    homelab .- MP
                    homelab .- WD
            T --> homelab
        LL .- PS


            PS .- SA
                SA .- V
                    V --> homelab
                SA .- RE
                    RE .- MP
                    RE .- GD
                SA .- KD

            PS .- SD
                SD .- KD
                SD .- AI .- homelab
                SD .- AI
                SD .- GD
                SD .- WD

CS .- NS
    NS --> homelab


```


5. ## TD beta ~~proper SD~~

```mermaid
flowchart TD;

SLIT{SLIT}

AI[automation: bots/robots]
CS{Computer Science}
D{DEVSYSADMIN}
DIY[DIY: NAS, router, powerbank, -salvage-]
GD[GameDev]
E[Electronics -theory-]
LL[low-level computing]
homelab{homelab}
HS{Home Server}
HL[HackingLab]
KD[Kernel Development]
mc[microcontrollers: RPico, UNO]
ml[machine learning]
MP[Malware / Pentesting]
NS{Network Security}
PS[Programming / Scripting]
RE[Reverse Engineering]
repair[repair, restore]
repurpose[repurpose]
SA{Operating Systems}
salvage[salvage]
server[server admin]
SD{Software Development}
T{Tinkering}
V[Virtualization]
WD[Web-Dev]



CS

    CS .- E

        E .- 1 .- T

            T .- LL


                LL .- 2 .- SA




                LL .- PS

                    PS .- SD

                        SD .- AI
                        SD .- GD
                        SD .- ml
                        SD .- WD

            T .- DIY


                DIY .- homelab


    CS .- 4 .- NS

            NS .- homelab

          


```



6. ## TD more

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
HS{Home Server}
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




SLIT .- E .- CS

    CS .- LL
    SLIT .- PS


        LL .- T
            T .- repair
            T .- |microcontrollers & salvaged components| homelab
                homelab .- DIY .- HS
                homelab .- |UNO, RPico| AI


        LL .- |sysadmin| SA
            SA .-V
            SA .- Linux
                Linux .- homelab
                Linux .- KD
            SA .- Windows



SLIT 

    PS .- |sysadmin| SA

    PS .- |CODE| SD

            SD .- GD
            SD .- ml
            SD .- KD
            SD .- WD



SLIT .- |netadmin| NS

            NS .- |netadmin| HS


                HS .- HL

                    HL .- |reverse-engineer| MP


                HS .- |self-host| WD

            NS .- homelab


```


7. ## good night ffs


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



SLIT


SLIT .- 1
SLIT .- 2
SLIT .- 3






    1 .- E

        E .- T

            T .- repair



            T .- |microcontrollers & salvaged components| homelab




    2 .- D



        D .- ?
        
            ? .- CS


                

            ? .- PS


        D .- SA


            SA .- Windows

            SA .- Linux


            SA .- V



                V --> homelab






        D .- SD


            SD .-






    3 .- NS


        NS .- homelab



            homelab .- HS

            HS .- |selfhosting| WD


            homelab .- HL

                HL .- |reverse-engineer| MP









```



