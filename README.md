# *Self-Learning IT* ~ materials & projects




For general learning materials see [SLIT-materials]().

For actual projects see [SLIT-projects](/SLIT-projects/readme.md).

Observe the graphs below to understand the scope of SLIT and see [graphs-sandbox]

## *SLIT materials* visualized


```mermaid
flowchart LR;

SLIT{SLIT materials}

SP{SLIT projects}
E[Electronics]
LL[low-level computing]
NS[Network Security]
PS[Programming / Scripting]
repair[repair, restore]
repurpose[repurpose]
SA[System Admin]
server[server admin]
SD[Software Development]
T[Tinkering]


SLIT .- 4 .- NS
    NS .- server
        server .- SP


SLIT .- 1 .- T
    T .- E
    E .- LL
        LL .- repair
            repair .- SP
        LL .- repurpose
            repurpose .- server
        LL .- PS
  

SLIT .- 2 .- SA
    SA .- LL



SLIT .- 3 .- SD
    SD .- PS
    PS .- SP




```



## *SLIT projects* visualized

``` mermaid

graph LR;


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
