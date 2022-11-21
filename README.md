# *Self-Learning IT* ~ materials & projects




For general learning materials see [SLIT-materials](/SLIT-materials.md).

For actual code and much more, dive into the waters of [SLIT-projects](/SLIT-projects):
1. **Tinkering Devices**
2. **Operating Systems**
3. **Software Development**
4. **Network Security**



Please bear in mind $SLIT$ comprises much former and ongoing **hands-on-learning**. Now please observe the graphs below to actually grasp the scope of SLIT.

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
            2 .- |sysadmin| SP

        II .- 3(3. Software Engineering)
            3 .- |self-taught dev| SP

    SLIT --> IB(I - HOMELAB B)
        IB .- 4(4. Network Security)
            4 .- |infosec| SP


SP

    SP .- T(Tinkering*)
        T .- |repair upgrade salvage| electronics(microcontrollers / components)
            electronics .- robots{robots}
            electronics .- IoT{IoT}
                robots .- |programming| ha(home automation)
            electronics  --> |DIY| HS{home server}
                HS .- self-hosting



    SP .- NSA(net/sysadmin)

        NSA --> Android
            Android .- IoT

        NSA .- |net/system hacking| IS(INFOSEC)
            IS .- HS
            IS .- HL
        NSA --> |Bash| Linux
            Linux .- D[distrohopping]
            Linux .- Kernel
            Linux .- servers{servers}
                Kernel --> os{opensource}
        NSA --> |cmd powershell| Windows
            Windows .- servers
            Windows .- WSL

    T .- HL(hacking lab)
                    HL .- |kali| pentesting
                    HL .- |Windows| malware-analysis


    SP .- SD(self-taught dev)

        SD --> os
        SD .- |Python| AI(AI machine  learning)
            AI .- |programming scripting| bots{bots}
        SD .- GD(game devel.)
            GD .- |reverse-engineering| mod-making
        SD .- |programming| WD(web devel.)
            WD --> |framewors...| B{Backend}

```

---

## DISCLAIMER

As of November 2022, the [**SLIT**](https://github.com/pabloqpacin/SLIT/tree/main) repo is set to be in **permanent development**.

Weekly progress is documented in specific branches (eg. `week46`) and later merged to `main`.