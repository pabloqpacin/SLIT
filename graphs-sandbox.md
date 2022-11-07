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


2. ## BRAINSTORM

```mermaid
flowchart LR;

SLIT{SLIT}


AI[automation: bots/robots]
GD[GameDev]
LL[low-level]
HS[Home Server]
HL[HackingLab]
MP[Malware / Pentesting]
NS[Network Security]
PS[Programming / Scripting]
RE[Reverse Engineering]
SA[System Admin]
SH[self-hosting]
SD[Software Development]
TE[Tinkering / Electronics]
WD[Web-Dev]






SLIT .- 1 .- TE
    TE .- HS
        HS .- WD


SLIT .- 2 .- SA
    SA .- PS
    SA .- HL
        HL .- MP
            RE .- MP
            RE .- GD


SLIT .- 3 .- SD
    SD .- PS
        PS .- AI
        PS .- WD
        PS .- GD


SLIT .- 4 .- NS
    NS .- HL


```

(1)

N .- HS

HS .- RE

RE .- GD
P .- GD

E .- N

HS .- M

T .- E

P .- WD
WD .- N
SD .- P

P .- A
P .- S
P .- AI
P .- Py

S .- A

E .- P

P .- OSs

(2)

HS .- MP
N .- HS
N .- WD
OA .- HS
OA .- PS
PS .- GD
PS .- MP
PS .- Py
PS .- RE
PS .- WD
Py .- WD
Py .- AI
RE .- GD
SD .- OA
SD .- PS
TE .- AI
TE .- N
TE .- OA
TE .- PS