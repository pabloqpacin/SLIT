# (02) OSs - (I) VMs

> must read [v12n-c14n](/SLIT-projects/02-Operating_Systems/_GEN/v12n-c14n.md)

This project aims at documenting fundamental **setup info & config actions** for both Windows and Linux VMs using VirtualBox in my host machine [GL76](/SLIT-projects/01-Tinkering_Devices/_devices/C01-GL76.md) running *Windows 10* with [WSL](/SLIT-projects/02-Operating_Systems/_GEN/WSL.md) enabled.

As a matter of fact, the most relevant Linux distros covered may be:
- [L03-PopOS](/SLIT-projects/02-Operating_Systems/I-VMs/L03-PopOS/)
- [L06-SUSE](/SLIT-projects/02-Operating_Systems/I-VMs/L06-SUSE/)
- [L07-Kali](/SLIT-projects/02-Operating_Systems/I-VMs/L07-Kali)

> Might turn the [EX2511](/SLIT-projects/01-Tinkering_Devices/_devices/C02-EX2511.md) machine into my main VM lab after successfully carrying out its *memory upgrade*


## current setup

1. **Host machines specs:**

|specs|[C01-GL76](/SLIT-projects/01-Tinkering_Devices/_devices/C01-GL76.md)|[C02-EX2511](/SLIT-projects/01-Tinkering_Devices/_devices/C02-EX2511.md)|
|---|---|---|
|OS|Windows 10|PopOS|
|CPU|i7-11800H| - |
|Memory|16 GB| - |
|Storage|1 TB SSD| - |
|Resolution|1920 x 1080| - |



2. ***v12n* software:**
- **VirtualBox 6.1.38** - all current VMs
- **VirtualBox 7.0.4** - *not yet installed*




3. **Beta *β*-VMs specs given host (GL76) specs:**

<!--
> β == Beta (to be deleted) --- Ω == Omega (to be maintained)
>
> A == ASIR --- L == Linux --- W == Windows
-->

|specs/features|[ubuntu00](/SLIT-projects/02-Operating_Systems/I-VMs/A01-Ubuntu/β-ubuntu00_VM.md)|[chicago95](/SLIT-projects/02-Operating_Systems/I-VMs/L02-Xubuntu/β-chicago95_VM.md)|[popos](/SLIT-projects/02-Operating_Systems/I-VMs/L03-PopOS/β-popos_VM.md)|[manjaro00](/SLIT-projects/02-Operating_Systems/I-VMs/L04-Manjaro/β-manjaro00_VM.md)|[manjey-i3](/SLIT-projects/02-Operating_Systems/I-VMs/L04-Manjaro/β-manjey-i3_VM.md)|[susey](/SLIT-projects/02-Operating_Systems/I-VMs/L06-SUSE/β-susey_VM.md)|[kaley](/SLIT-projects/02-Operating_Systems/I-VMs/L07-Kali/β-kaley_VM.md)|[10VM](/SLIT-projects/02-Operating_Systems/I-VMs/W01-Windows10/β-10VM_VM.md)|[win10](/SLIT-projects/02-Operating_Systems/I-VMs/W01-Windows10/β-win10_VM.md)|
|---|---|---|---|---|---|---|---|---|---|
|OS|Ubuntu|Xubuntu|PopOS|Manjaro|Manjaro|Tumbleweed|Kali Linux|Windows 10|Windows 10|
|ISO size|
|Processors|2|2|2|4|4|4|2|4|6|
|Memory|2000 MB|3072 MB|3072 MB|4096 MB|4096 MB|4096 MB|2048 MB|4096 MB|8000 MB|
|Storage (*'Normal' .vdi*)|20 GB|20 GB|20 GB|20 GB|20 GB|20 GB|80 GB|50 GB|80 GB|
|Resolution|
|notes...| - |Chicago95 Theme|**proper**||Arch-based||Kali ISO for VMs
|Desktop Env.|Gnome|XFCE|Gnome||||| - | - |
|Package Manager|apt|apt|apt| - | - | - | apt | 



