# β - popos

<!--
user: gitgud
passwd: micro7
-->

## config

1. **Download**
   - ISO 'pop-os_22.04-amd64_intel_12.iso' from *website* (2.80 GB)
2. **Installation specs**
   - Processors: 4
   - Memory: 3072 MB
   - Storage: *.vdi* - Normal 20 GB
3. **Distro features**
   - Desktop environment: GNOME
   - Package manager: *apt*

<details>
<summary>Click to see Neofetch</summary>

![popos-neofetch](/SLIT-projects/02-Operating_Systems/images/VMs-L03-popos-neofetch.PNG)

</details>



> As of 20/11/2022: 'Low Disk Space' hence I may set up a new larger PopOS VM


## VM features


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

2. Written `kkk.sh` script:
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



## PopOS key features

1. Cosmic shell! <!--DOCUMENTATION LMAO-->
   1. Delighful **Window Tiling manager** pre-installed
   2. Delightful **system shortcuts / key-bindings**