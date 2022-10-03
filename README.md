<!-- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/) -->
<!-- thanks [Stack Overflow](https://stackoverflow.com/questions/11948245/markdown-to-create-pages-and-table-of-contents) -->



<!-- v0.1.0 = add Open Source big time | downgrade kotlin | reconsider Unity/C# (eg.  Karmaggän project) || zsh, fetch Discord gamedev.... -->
<!-- v0.0.1 = add mind maps -->
v0.0.0 = stemming from wikiSLIT v0.4.0



# *Self-Learning IT* ~~~ materials


Hi there, welcome to my personal **IT Roadmap** 👋

July 2022 felt like time for a career change, thus I did sign up for ITEP's [Network and System Administration studies](https://www.itep.es/ciclos-formativos/distancia/tecnico-superior-administracion-sistemas-informaticos-red). Yet, unable to hold meself, took my own deep dive into **'self-taught Software Development'**.

📚 YouTube research was done and the algorithm was fairly spammy, still feeding me with quality content. Soon enough, [my playlists](https://www.youtube.com/channel/UC4yPJo9tFagP7ZMkMcCQNbw) were overwhelmed by the sheer amount and variety of videos I was saving. Tried Discord and [Reddit](https://www.reddit.com/r/selflearningIT/) severs too keep all stuff organized in a cross-platform fashion, but these tools haven't met my needs just yet. 

✨ Going through some 101s it became crystal clear: I figured **Git** and **markdown files** were all I needed. Now this very file is my self-taught roadmap, a custom wiki, my knowledge-base, my self-learning journal.

Now thanks for reading and I hope you find it useful too! You may fork this file, add your own sauces and share them with me! ⛏️


## Table of contents

0. [~ Mind Maps](#00--mind-maps)
1. [~ L10N](#10--l10n) - Software Localization 101s
2. [~ HARDWARE](#20--hardware) - Computer components and other electronics

    [~ TINKERING](#21b--tinkering)- Hardware projects
    
    - [DIY Circuits, Arduino UNO, Raspberry Pi]
    - [3R Computers —Repair, Restore, Repurpose—, Pentium]
    - [Consoles aka Game Stations, Smartphones & Tablets]

3. [~ SOFTWARE -GEN-](#30--software--gen) - Understanding the industry 101

    [~ Self-taught dev 101](#31--self-taught-dev-101)
    - *'Look afar and see the end from the beginning'*
    - Industry trends
    - Personal Protocol (programming-oriented)
    - Problem-solving and efficient habits

    [~ FIELDS](#32--fields) - General field-related info
    - [Computer Science, Data Science, DevOps, Ingeniería Informática, Software Engineerz]

    [~ TOPICS](#33--topics) - More specific materials
    - AI ~ Machine Learning + Neural Networks (+ TensorFlow)
    - [Algorithms, APIs, Backend, Browsers, Cloud Computing, Databases, Frontend ~ Design]
    - [Fullstack, $ Git, Math, OOP, Open Source, Tech Stacks (~ Web Dev), Testing]
    - WebDev


4. [~ SysAdmin || OSs](#40--sysadmin--oss) - ***Core content***

    * WINDOWS
    * ANDROID (ROOT & +more)
    * [LINUX](#43--linux)
        - 101s
        - Distros
    * WSL - Windows Subsystem for Linux

5. [~ CODE](#50--code) - Programming Languages & Project Ideas

    [~ PYTHON](#51--python)
    - 101s
    - Tutorials 101
    - Tutorials 10x

    [~ BASH](#53--bash) - Shell

    [~ +MORE](#more-languages) - [C#, PowerShell, ... ]

6. [~ Game Development](#60--game-development)

    - [Emulation, Engines, GameDev Community, GameDev Ideas, Mod-Making, Pygame limitations, Reverse Engineer (retro games)]

7. [~ NETWORKS | HACKING](#70--networks--hacking)

    - [Black Hat, BotNetz, Cryptography, CTF, Dark Web (+ Tor), Digital Forensics]
    - DIY_NAS aka 'Home Server'
    - Hacking
    - HomeLabz
    - [Malware ($python, $bash), Network Ports, Pentesting, Reverse Engineering, Routers]
    - Scambaiting
    - Virtualization
    - VPNs, VPSs

8. [~ IT Certificates](#80--it-certificates)

9. [~ OpenSource Development](#90--open-source-development)

## 0.0 ~ Mind Maps

The graph below was put together to illustrate how different IT *fields* and *topics* merge within my Self-Teaching process: [see Mind Map](https://www.mindomo.com/mindmap/devsysadmin-33a91323b6c84dc9a8a08af7a0d7e679).

The screenshot below shows the core of it:



## 1.0 ~ L10N 

[How To Manage Translations For Your Application | Crowdin & GitHub Tutorial](https://youtu.be/8baL6VWnnZg)
<!--
- [ ] blog_chaval
- [ ] [25 VSCode Tips](https://youtu.be/ifTF3ags0XI) @ Fireship
- [ ] South_Park
- [ ] Tomba
- [ ] [How Sekiro sets itself apart](https://youtu.be/jASlIZSpnJ4) @ Zullie the Witch
-->

## 2.0 ~ HARDWARE | TINKERING

### Theory
<!-- 
Electronic Engineering ~ [Electronic Engineers 2022](https://youtu.be/CGD8qeizblc)
-->

* #### Electricity 
    - [How Electricity works](https://youtu.be/mc979OhitAg) @ EngineeringMindset
    - [Basic Electricity - What is an amp?](https://youtu.be/8gvJzrjwjds) @ Afrotechmods
* #### Electronics 101s
    - [How to Use a Breadboard](https://youtu.be/6WReFkfrUIk)
    - [Electronic components](https://youtu.be/6Maq5IyHSuc) @ bigclivedotcom
* #### Computers 101s
    - [From Transistors to Tetris P.1](https://youtu.be/6caLyckwo7U)
    - [How are Microchips made?](https://youtu.be/bor0qLifjz4) <!-- | Linus in Israel-->

### Components
* #### CPUs
    - [How CPUs read machine code](https://youtu.be/yl8vPW5hydQ)
    - [CPU Clock Speed Explained](https://youtu.be/3PcO10iAXTk) @ Max's Tech
* #### Graphics -all
    - Custom video card ~ [Building a DIY video card](https://youtu.be/l7rce6IQDWs) @ Ben Eater
    - JPEG ~ [How are Images Compressed? JPEG In Depth](https://youtu.be/Kv1Hiv3ox8I) @ Branch Education
* #### HDMI
    - [HDMI vs MHL](https://lifewire.com/mhl-in-home-theater-1846852)
* #### Motherboards
    - [Motherboards Explained](https://youtu.be/b2pd3Y6aBag) @ PowerCert Animated Videos
* #### Power Supply
    - ... ~ [Probably the most used component nobody knows of! TL431 Guide!](https://youtu.be/isutYMU2HHU) @ Great Scott!
    - Alt Power Supplies ~ [Free Energy Devices Build and Science](https://youtu.be/15V0gUXUPko) @ ElectroBOOM
* #### SSDs
    - SSDs | Smartphones (?!) ~ [How do SSDs/Smartphones work?](https://youtu.be/5Mh3o886qpg) @ Branch Education

* #### (bonus) ~ Bluetooth
    - [How does Bluetooth Work?](https://youtu.be/1I1vxu5qIUM) @ Branch Education


## TINKERING
<!-- arranged as per relevant mindmap -->

### 2.1 ~ DIY Circuits
- Full DIY ~ [17 DIY inventions](https://youtu.be/twKkQaORKS4)
- w/ Arduino... ~ [Turning a car into a COMPUTER MOUSE](https://youtu.be/M2xqMZ6b85w) @ William Osman


### 2.2 ~ Arduino UNO
[Arduino vs Pico - Which is the Best Microcontroller For You?](https://youtu.be/dOa3570JM2M) @ Gary Explains
- Starting Kits ~ [5 best kits 2022](https://youtu.be/huKV8hdhsiY)
- 101s ~ [What is Arduino UNO](https://youtu.be/_ItSHuIJAJ8)
- Guide 00 ~ [learn Arduino in 15 minutes](https://youtu.be/nL34zDTPkcs)
- Course 00 ~ [fCCs course -4h-](https://youtu.be/zJ-LqeX_fLU)
- Projects 00 ~[15 Great Arduino Projects for beginners](https://youtu.be/Ox-9eOc3bQU) @ Maker Tutor
- Projects 01 ~ [Arduino based Guitar Tuner](https://youtu.be/tjKySKeDoCE)

### 2.3 ~ RPi RPico

#### RPi -gen-
* Regarding RPi4 8GB ~ [Choosing the right Raspberry Pi for you!](https://youtu.be/YAs1qdgiqPc) @ Android Authority

#### RPico
* 101s ~ [Pico Prototyping - Building a "Pico Uno"](https://youtu.be/jwIOxOzee0U) @ DroneBot Workshop

* MicroPython 00 ~ [Raspberry Pi PICO | Starting with MicroPython + Examples](https://youtu.be/zlKJ5hvfs6s) @ Electronoobs

* Bad USB ~ [Bad USBs are SCARY!! (build one with a Raspberry Pi Pico for $8)](https://youtu.be/e_f9p-_JWZw) @ Network Chuck


### 2.4 ~ 3R Computers - Repair Restor Repurpose
<!-- $SALVAGE -->
+ **GL76** ~ [MSI-GL76 Dissassembly](https://youtu.be/DF4HVW6Y_Fk)

* Laptops
    - Clean ~ [How to Clean a Laptop](https://youtu.be/bypESzEtZr4)
    - Motherboard ~ [Laptop Motherboard -Diagnose,Repair-](https://youtu.be/GCLflqmne6k)
    - Fix ~ [FREE BROKEN Laptop - But Can I Fix It? Acer Nitro 5 No Power](https://youtu.be/C4S6QL4keOQ) @ Tronics Fix
    - Repurpose ~ [Repurpose your old dead Laptop](https://youtu.be/WLP_L7Mgz6M)

- HDDs ~ [Fix your Hard Drive](https://youtu.be/zAMjdrUf9V4)

### 2.5 ~ Pentium
* Dusting off
    - [Restoring old Windows XP](https://youtu.be/1p5RUI9hIF8) @ Psivewri
    - Clean Pentium_3 ~ [This Pentium III hasn't been cleaned in 15 years](https://youtu.be/UyVHrxYZJJI) @ Phils Computer Lab
    - Restore Pentium_3 ~ [Pentium III Restoration](https://youtu.be/eSYOH_AfgEY)

* Upgrading Pentium_4 to Windows_10 ~ [Usuing Pentium 4 in 2020 with Windows 10](https://youtu.be/sSZNLAIL65M) @ Phils Computer Lab


* $salvage ~ [This PC Wasn't Worth Saving | Pentium 4 Build](https://youtu.be/sjfe9cQky5g) @ Tech Made Easy && [Build Retro PC from New Old Parts](https://youtu.be/xKChxv9jw74)

* BIOS in Pentium 4 ~ [Computer BIOS in Pentium4 MOBO](https://youtu.be/TuG2rsrI_tc)


### 2.6 ~ Consoles aka Game Stations
Game Boy ~ [Gameboy Restored & Upgraded](https://youtu.be/lMyb0erNuCE) @ Odd Tinkering

PS1 ~ [PS1 Restoration & Upgrade](https://youtu.be/eMUpTVMqueY) @ Odd Tinkering

Universal Wii Remote ~ [Wii Remote Working on PS5 (How-to)](https://youtu.be/BjgCvOfQek8) @ Basically Homeless

### 2.7 ~ Smartphones & Tablets

* $salvage smartphones ~ [10 GENIUS Ways to Reuse Your Old Smartphone](https://youtu.be/k2_qM7NF_Vg) @ C4ETech English & [What is worth salvaging from an old smartphone](https://youtu.be/dYnplx_DVHs) @ Great Scott!

* $salvage tablets ~ [OEM/ODM 7 Inch Tablet PC Touch Screen Replacement Disassembly Repair Guide](https://youtu.be/LeaulreONq0) @ ivifix.com


### 2.8 ~ bonus
- [Electronic Pinball Restoration](https://youtu.be/jh9dNaRqEpg) @ Odd Tinkering
- [Mining Lantern rest. -numismatics-](https://youtu.be/hqc0pQ7DV4I) @ TysyTube


<!-- #### 3.3.3 ~ $TINKERING et $SALVAGE <!-- SALVAGE = restore

* GL76
* EX2511
* Pentium
* supercobaya
* tablet android
* tablet iOS
* mobiles x9
* consoles x5 -->

---

## 3.0 ~ SOFTWARE -GEN-

### Self-taught dev 101

#### *'Look afar and see the end from the beginning'*

* ##### ~~[4 Steps to Become a Developer {Shorts}](https://youtu.be/nvlizC6koSc)~~ @ Fireship
    - Learn [HTML, CSS, JavaScript, React, Node]
    - Build something meaningful [1st Idea, 2nd Fail, 3rd Study, 4th Repeat]

* ##### ~~[Fastest way to Learn Coding and actually get a job](https://youtu.be/79pKwdiqcwI)~~ (First thing I actually did)
    - Learn **Python** for WebDev, DataSci, Automation...
    - Do [learnpython.org](https://learnpython.org), Download **VS Code** & Complete [12 Beginner Python Projects](https://youtu.be/8ext9G7xspg)] @ Kylieyying  (@ fCC)
    - Prepare Portfolio & Interviews
    - **Complete [Intro to Data Structures and Algorithms](https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513) & [LeetCode](https://leetcode.com/) ~~^^~~ (!!!)**
    <!-- (!!!) = STILL TO DO -->


* ##### ~~[1 - Self Taught Programmers... Listen Up](https://youtu.be/FrFY6Y1MJBQ) & [2 - Zero to Full-Time Programmer in 5 Steps](https://youtu.be/s9iPo9YMU70)~~ @ Keny Gunderman's
    * 1 || Self-taught ain’t easy, maybe more than 6 months | Don’t overthink, just code and learn to adapt | Networking: Discord, LinkedIn, events... REFERENCES! | Dive in to the deep end | Reconsider your choices
    * 2 || Language: **JavaScript (Fullstack & Mobile) [Frameworks: React, Vue, Angular, Node** | Learn variables, functions, conditions, loops, classes, objects | Visit *freeCodeCamp, Codeacademy Udemy...* | Imitate | Innovate, build a Portfolio and market yourself

* ##### ~~[Career Paths for Software Engineers & How to Navigate It](https://youtu.be/oGy_uK6FrgE)~~ @ TechLead
    - *Backend* [Python, PHP **+** node.js **+** Java, C]
    - (*^1) *Frontend* [JavaScript, CSS, HTML **+** frameworks [Angular, React, Vue.js] ]
    - ***Fullstack*** [ [RubyOnRails, Django, Golang] **+** SQL **+** Linux]
    - ***Mobile*** (Android [Kotlin, Java])
    - *Game/Graphics* [C++, physics, shaders, GPUs… VR+AR]
    - *Data* (see 08:56 - 09:20)
    - *Machine Learning* (math)
    - *Cybersecurity* (null)
    - (*^2) ***DevOps*** [Linux, Perl, scripting, bash, Unix commands]
    - *QA* (test automation software – Test Suites)
    - (*^1) **Frontend** = *API*s hookups & Rendering [UX, buttons, UI, color, fonts, graphics, positioning, layout]
    - (*^2) **DevOps** = site reliability

#### Industry Trends ~~^^~~ 2022 is gonna be wild for Developers

[Developer Trends in 2022](https://youtu.be/LOpFYMPXqE4) @ Fireship

- *Web 3* = decentralized internet if smart contracts | crypto
    - No more passwords but blockchain wallet addresses **(browser plugin like metamask)** | d-app = code in the blockchain as smart-contract (data ownership) | tech is in early stages, as an industry it’s not worth the trouble, although if successful and mainstream, then AYE!
    - ***to-do*** ~~^^~~ 'Entirely decentralized news network, where journalists could upload video, articles and other reporting, and be compensated based on its reach *(basically a good Twitter)*. It would incentivize good journalism and eliminate the possibility of a top-down propaganda machine. Journalists win, consumers win, and the establishment gets f*.

- *Metaverse* = hyper-real alternative world
    - internet-based platform with multiple access points [phone, VR, AR]
    - users require one single profile to interact with [businesses, apps, other users…] in a virtual environment
    - dangerous tho, as it may enhance [addiction, isolation]
    - **tools [unity, unreal engine, blender]** ~~^^~~ (!!!)
    - ***to-do*** ~~^^~~ sorta *Squarespace* or *Shopify* for the **Multiverse** (ie. a platform for businesses)


    ![Metaverse Market Map](/images/wiki-metaverse_market_map.png)

- *AI* = all over the place (see *GitHub copilot* affecting devs directly)

- *Databases* = (...) ~~^^~~

- *JavaScript* = (...) ~~^^~~

- *Other trends* = (...) ~~^^~~

- *Conclusion* = (...) ~~^^~~


#### Personal Protocol ~~^^~~ $CODE

* ##### ~~Comment_IQ, Documentation & Portfolio ~~^^~~ [If You're Learning to Code STOP Taking Notes](https://youtu.be/VCWzQpUwsaw)~~ @ Dorian Develops

    - ~~^^~~ Prepare **CompTIA certificates**
    - *memorizing != retaining:* for first_tutorials don’t bother with notes |
    work through curriculum for 1-2 months building projects from scratch
    - **Commenting code:** everything relevant if not obvious | overkill = all variables, even single-lines | slowly develop Comment_IQ | **later, comment = all I write and copypaste from online rss** so I understand and explain the process
    - ~~^^~~ **Documentation:** always start with a README file | **learn markdown & WYSIWYG** | **explain project (technologies, codebase, purpose) | *Documentation = notes* |overkill = ['Getting started' section, Examples of code snippets, Demos of what library/app does] | learn from my tools’ Documentation [structure, content, ...]
    - *Conclusion:*
        - explain [code-blocks do, application does]
        - do what real world 'good software development teams' do
        - figure out what is worth holding on to and what isn’t
        - **memorize = muscle memory**
        - **my output to the world ==** notes for GitHub *(clean clear code, solid Docm.)*
        - remember employers like solid portfolio w/ all explained


<!-- key skill to level-up: Debugging -->

* ##### ~~Analytical, creative & diffuse approach ~~^^~~ [Be a Better Programming by Mastering Debugging](https://youtu.be/DQEVZ5efnO0)~~ @ Andy Sterkowitz

    - **Key insights:**
        - **Computer Logic Understanding:** how to write instructions (code) for Computers to run Operations and return Output
        - **Programming** = bugs, errors (misspells, wrong references)... Avoid such by *commiting constantly*
        - **Debugging** is the assessment process of finding the cause for bugs in the code.
        - **Good debugger:** reads lots of code analytically, abstract thinker, 'code-doctor'

    - **Main points:**
        - **Mindset change**: if smth broken: from DOER to DOCTOR, be curious and inquisitive, slow-down and don't overlook
        - **Read error messages**: detailed info (where issue, what is it), copypaste online
        - **Use debugging tools**: aka surgery; breakpoints ~~^^~~ (!!!)
        - **General:**
            - Double check logic aka instructions
            - Assume human error: fight with clean code, tests;  question anything you may have written
            - Commit small changes: for consistant development
            - Take mental breaks: **'power-through approach' VS 'Diffuse Thinking'**

* ##### ~~Focus, deep-understanding, needfulness & growth ~~^^~~ [7 Habits of Senior Software Developers](https://youtu.be/zivngNtLiuY)~~

    - **Focus:** one thing for a long time; avoid multi-tasking and task-switching
    - ~~^^~~ **Automation:** avoid repetition (in code)
    - **Pragmatism** (biznez perspective): look at the bigger picture; avoid over-engineer and *refactoring*
    - **Teach others:** Unconscious Competence + explain in simple terms = Refine Mental Models + Communication
    - ~~^^~~ **Open-Minded:** learn new [frameworks, languages] = build preferences; seek cutting-edge
    - **Seek feedback**
    - **Follow your interest:** stay motivated, fresh and happy == dive into new things


#### Problem Solving & Efficient Habits

* ##### ~~Fitness, results, KISS & 'The Zone' ~~^^~~ [7 Habits of Highly Effective Programmers](https://youtu.be/W8ykZNSLDqE)~~ @ TechLead
    - **Intro:** right habits != burnout | long-term game == skills, tecniques; right career trajectory
    - **Fitness and sunshine:** because programming is physically demanding
    - **Results-oriented approach**: avoid *refactoring*; get projects done looking good
    - **KISS**: keep Code simple and consistant | *standarize* team methods | **all Code == read-write-debug easily**
    - **Getting in 'the Zone':** code and lose track of time = solid code (bc *large abstractions*) IF undistracted
    - **Sharpen yourself**: comfort zone == outdated | **key debug: adapt and diagnose**
    - **Collaboration:** share ideas | code integration in a team environment | networking
    - **Programming = solo:** lonely activity (code, documentation) in the digital world


* ##### TDD & prototyping ~~^^~~ [Problem-Solving for Developers - A Beginner's Guide](https://youtu.be/UFc-RPbq8kg) @ Fireship

    <!-- {Case study — Using GraphQL and JS to merge 600 PRs} -->
    - (*^1) **Identify** ~ Understand the problem | *Documentation* = *Problem Statement* [context, situation/issue, why do we care]
    - **Research & Refine** ~ Visit StackOverflow and assess others’ approach | Break down problem into *subproblems*
    - **Pseudocode** ~ Outline the code to-be = *focus on logic, not syntax*; comment and name things
    - ~~^^~~ **Test-Driven Development (TDD)** ~ Helps understanding code & prevents regression | *'Red Green Refactor'*
    - **Implement** ~*Hackathon approach*: Done = tests_OK + prototype_OK
    - **Reflect on prototype** ~ Improve readability, name things better, add comments, remove duplication, optimize time/space complexity of algorithms, add *caching* to reduce cloud computing costs, improve error handling...
    - **Practice and repeat** ~ Infinite problems and challenges, so develop *intuitive skills*; get feedback

    <!-- {Dev Mindset — For programming, look at a problem and visualize how a computer system can solve it} -->
    ######
    - (*^1) ~~^^~~ [**Agile approach:**](https://www.atlassian.com/agile/project-management/epics-stories-themes) stories, epics, initiatives


---

### FIELDS

#### Computer Science
[An entire CS Degree in 12 minutes](https://youtu.be/EJiVWoFk8GA)

[Math needed for CS](https://youtu.be/eSFA1Fp8jcU)

[Licenciatura en Ciencias de la Computación (UBA)](https://youtu.be/sLMsRewMTVk) @ Santi Fiorino

<!-- turn this $material into a document with all episodes summarized -->
- Crash Course: [Computer Science](https://www.youtube.com/playlist?list=PLH2l6uzC4UEW0s7-KewFLBC1D0l6XRfye) -40 episodes-

- THIS... [100+ Computer Science Concepts Explained](https://youtu.be/-uleG_Vecis) @ Fireship


#### Data Science
[What to Learn to get Hired as Data Scientist](https://youtu.be/pLI7T0clMxg)

[How I'd learn to code if I could start over](https://youtu.be/MHPGeQD8TvI) @ Tina Huang
- **Learn Python** (friendly syntax, versatile, popular)

    - **First weeks:** Learn variables, datatypes [strings, floats, ints, arrays], loops, functions, if statements, OOP | RSS = [interactive websites [fCC, Codeacademy], video-tutorials, books] | Objective = implement fundamental concepts = play around and expand tutorials’ content
    - **Late personal projects:**  interesting/useful, small, ~~copypaste~~
        - (n01-04) - n01 '(array(database)), random output IF input(x,y)' | n02 'snake = basics+OOP+UI' | n03 'stock trading bot' | **arrays < Pandas pydata // data-frame** |**learn APIs // (beginner 2 advanced)**
        - then: algorithms and data structures [dictionaries, linked lists, queues, heaps, trees, graphs] ~~^^~~ BUILD a MAZE and an ALGORITHM to solve it
    - **Eventually:** Documentation, '+topics = +projects (WebDev, AppsDev, AI)'

- **Mindset**: programmer = tinker(explore, dive-in) | problem-solving != StackOverflow | adaptability, constant learning, **growth mindset**
- **Overkill:** do DEV in a certain community | *code = powerful tool, freedom to self-learn*


#### DevOps
[DevOps Explained](https://youtu.be/Xrgk023l4lI) @ Simplilearn


#### Ingeniería Informática
- [4o de Ingeniería Informática en 15 Minutos - Itinerario Ingeniería de Computadores](_mKjNeb1lM4) @ Antonio Sarosi

#### Software Engineerz
- ~~[The Harsh Reality of being Software Engineer](https://youtu.be/Ws6zCMdp9Es)~~
    - Burnout: overwhelming **backlog** and interviews
    - Tough competition
    - Junior Devs tasks: learn **codebase** & knockout pull requests

- [What is a 10x Engineer (feat. ex-Google Tech Lead)](https://youtu.be/Iydpa_gPdes) @ Tech Lead

---

### TOPICS

#### AI ..... | Machine Learning + Neural Networks (+ TensorFlow

* ##### 101s | Neural Networks
    - [Deep Learning | Natural Language Processing | Machine Learning | Artificial Neural Networks | +more](https://levelup.gitconnected.com/top-7-deep-learning-methods-each-explained-in-less-than-10-seconds-3683120de455) @ LevelUpCoding
    - Neural Networks (!) ~ [Why Neural Networks can learn (almost) anything](https://youtu.be/0QczhVg5HaI) @ Emergent Garden

* ##### Techonologeez
    - [TensorFlow in 100 Seconds](https://youtu.be/i8NETqtGHms) @ Fireship

* ##### Models
    - [IA aprende a jugar Dino (Chrome)](https://youtu.be/gC85en0Vmh4) @ Santi Fiorino
    - [NN Learns to Play Snake](https://youtu.be/zIkBYwdkuTk) @ Greer Viau
    - [Self-Driving Car with JS (NNs | ML)](https://youtu.be/Rs_rAxEsAvI) @ fCC  <!--js = reference to '+more' (CODE .languages) -->
    - $ [Code a Discord Bot with Python - Host for Free in the Cloud](https://youtu.be/SPTfmiYiuok) @fCC
    - $ [Creating a Discord Bot in Python 3.9](https://youtu.be/fU-kWx-OYvE) @ Indently

    $BOTS  <!-- ojete -->


#### Algorithms
- [Researchers Use *Group Theory* to Speet Up Algorithms - Introduction to Groups](https://youtu.be/KufsL2VgELo) @ Nemean


#### APIs
- [RESTful APIs in 100 Seconds // Build an API from Scratch with **Node.js Express**](https://youtu.be/-MTSQjw5DrM) @ Fireship


#### Backend
[Complete overview of Backend WebDev (2021)](https://youtu.be/XBu54nfzxAQ) @ SuperSimpleDev


#### Browsers
- [How Google Search Works (in 5 minutes)](https://youtu.be/0eKVizvYSUQ) @ Google
- [BYE DuckDuckGo, here's my new search engine! Private Alternatives to Google](https://youtu.be/x9q3qPxrTqg) @ The Linux Experiment

#### Cloud Computing
- [Cloud Computing Explained](https://youtu.be/_a6us8kaq0g) @ PowerCert Animated Videos


#### Databases
- [SurrealDB in 100 Seconds](https://youtu.be/C7WFwgDRStM) @ Fireship

#### Frontend ~ Design
[8 Dev Portfolios-Websites that might be 10/10s in Graphic Design](https://youtu.be/At6XyItIHsE) @ Design Course
<!-- **@pabloqpacin:** *find #CodePen.io below* -->

#### Fullstack
[Fullstack Development Iceberg {Shorts}](https://youtu.be/JMWNYfPIF2U) @ Fireship

#### $ Git
How to Git ~[Git It? How to Use Git and GitHub?](https://youtu.be/HkdAHXoRtos) @ Fireship
- Git = history book of code; GitHub = makes open source software accessible to the world
- Git: version control system; system for managing my files.
- Building software = series of small milestones (writing code on different files); app = chaos to stability.
- Git keeps track of these change; multiple branches, and then merge. Easy collaboration.

    ![eg. Git Trunk](/images/wiki-git.png)


#### Math
- [why you NEED math for programming](https://youtu.be/sW9npZVpiMI) @ Joma Tech

#### OOP - Object Oriented Programming
- [OOP is Embarrasing: 4 Short Examples](https://youtu.be/IRTfhkiAqPw) @ Brian Will


#### Open Source
- [Contributing to Open Source can change your life](https://youtu.be/CML6vfKjQss)
- [How to Contribute to Open Source - Complete Guide](https://youtu.be/yzeVMecydCE) @ Eddie Jaoude -@ fCC-


#### Tech Stacks (~ WebDev)
- [How to OVER Engineer a Website // What's a Tech Stack?](https://youtu.be/Sxxw3qtb3_g) @ Fireship
- [My Bleeding Edge Tech Stack for 2025](https://youtu.be/rFP7rUYtOOg) @ Fireship


#### Testing (Software)
- TDD ~ [Software Testing Explained in 100 Seconds](https://youtu.be/u6QfIXgjwGQ) @ Fireship
- TDD ~ [Test-Driven Development // Fun TDD introduction with **JavaScript**](https://youtu.be/Jv2uxzhPFl4) @ Fireship

#### Web Dev
[100+ Web Dev things You Should Know](https://youtu.be/erEgovG9WBs) @ Fireship -GOLD-

### ~ Junior Dev Jobs
- [Lemon.IO](https://lemon.io/for-developers/)

---


## 4.0 ~ SysAdmin || Windows & Linux

### SysAdmin 101s
* [Types of OS afap](https://youtu.be/MR2ntdZW__A) @ Techquickie
* BIOS...
    - [BIOS and UEFI afap](https://youtu.be/zIYkol851dU) @ Techquickie
    - [BIOS, CMOS, UEFI - What's the difference?](https://youtu.be/LGz0Io_dh_I) @ PowerCert Animated Videos
* Dual Boot ~ [The Best Way do Dual Boot Windows and Ubuntu](https://youtu.be/CWQMYN12QD0) @ Techno Tim
* *Virtual Machines* ~ [see '7.0 ~ Networks | Hacking'](#70-networks--hacking)
* #### SysAdmin Career
    - [How it FEELS to be a SysAdmin (What is a System Administrator)](https://youtu.be/v9bZsmn-Aw4) @ Sir Sudo
    - [How to Be a Great System Adminstrator in 3 Steps](https://youtu.be/Biz_QnigwWI) @ IT Career Questions

...



### 4.1 ~ WINDOWS
<!-- - [PowerShell, BIOS...] -->
[I put Windows 10 on a Calculator - Stupid Setups](https://youtu.be/neD9_viUnS8) @ Basically Homeless

...
### 4.2 ~ ANDROID

#### ROOT
- Root 101 ~ [What is Root Access on Android? How to Root](https://youtu.be/eR26901B_0A)
- ROMs proper ~ [Android 13 Custom ROM List: Unofficially update your Android Smartphone!](https://xda-developers.com/android-13-custom-rom-list) @ XDA-Developers

#### Misc.
- Dual Boot for Windows ~ [Cómo INSTALAR Windows 11 ARM | Iniciar DOS Sistemas ANDROID y Windows](https://youtu.be/VkI476sGI4s)
- AndroNix' Linux ~ [Easily run Linux on Android with AndroNix - Linux Distro on Android without Root](https://youtu.be/jvuufPWKF3k)
- Calyx OS ~ [Calyx OS - The next big Android Competitor?](https://youtu.be/qTtgzNGRAfA) @ Mrwhosetheboss <!--(Hacking...)-->
* ROMS

...


### 4.3 ~ LINUX
<!-- possibly move pointer to its own 5.0, ending 4.0 with WSL -->
#### Linux 101s

* [Linux for the Absolute Beginner...](https://youtu.be/EN7mbRccT-8) @ Low Dough Tech
* [7 Linux Terminal Application and Utilities](https://youtu.be/ZNNqkeeOdrk) @ Tech Hut
* ☠️ [Why Linux Is Better For Programming](https://youtu.be/otDOHt_Jges) @ Kalle Hallden
* ##### $ VENTOY
    - [Ventoy - An Easy to Use MultiBoot USB Tool](https://youtu.be/K64sT0pQc-0) @ Mental Outlaw
    - [How to create the ULTIMATE multiboot flash drive using Ventoy!](https://youtu.be/7eQciSP91eI) @ Alfredo Sequeida
    - [How to Create a Multiboot USB with Ventoy | Fast, Simple and Easy Guide](https://youtu.be/z1FyoCswwAc) @ Techno Tim


#### Linux Distros
[What is the Best Linux Distro? -Its the one you Make the best](https://youtu.be/_f5uev7UTz0) @ Mental Outlaw

##### Linux Mint
- [How good is Linux Mint for beginners](https://youtu.be/pNWDnJ_kESM) @ The Linux Experiment
- [20 Different Types of Linux Mint Themes](https://youtu.be/PIrl3Eb0H44)
- [From Noob To Power User With Linux Mint Cinnamon](https://youtu.be/TKX29fJ8U2Y) @ Distro Tube


##### +more <!-- '7.0 ~ Networks | Hacking' -->
* Top 5 Arch-like ~ [Top Five Arch-Based Linux Distros 2022](https://youtu.be/zkmTpxVpj6Q) @ Distro Tube

* +more
    - ArcoLinux ~ [ArcoLinux - First Impressions and Install](https://youtu.be/S_dG79GhNfI) @ Tech Hut <!--install in VM-->
    - Chicago95 ~ [Bring Back Windows 95 with XFCE + Chicago](https://www.youtube.com/shorts/VcbzoOjMLHM) @ Tech Hut <!--find in GitHub>
    - Kali Linux ~ [Linux for Ethical Hackers (Kali Linux Tutorial)](https://youtu.be/lZAoFs75_cs) @ fCC && [Cómo instalar Kali Linux 2022 en VirtualBox y VMware](https://youtu.be/4lKQKxwjXbg) @ The Good Hacker
    - Manjaro | Arch ~ [Manjaro is NOT Arch](https://youtu.be/VzAw8a3Jx-k) @ Tech Hut
    - MX Linux ~ [From Noob to Power-User with MX Linux](https://youtu.be/IsnSSY2vTXQ) @ Distro Tube
    - Pop OS!


### 4.4 ~ WSL - Windows Subsystem for Linux 
- [BEST Web Dev Setup? Windows & Linux at the same time (WSL)](https://youtu.be/-atblwgc63E) @ Fireship
- [I Coded with WSL2 for a Week](https://youtu.be/LktFP0Dpl-c) @ Forrest Knight

<!-- VERY IMPORTANT LOCAL GL76'S DIRECTORY: 'LINUX' -->
<!-- ### 4.5 ~ +more -->
<!-- $consoles $JAILBREAK $TINKERING $cars -->
---

## 5.0 ~ CODE

### 101s
<!-- find Git pointer in 3.3 -->

* #### More Career (alike 3~Software-gen-)
    - [10 cosas que he aprendido en 7 años como Programador Freelance](https://youtu.be/vVMiKq0Ly1E) @ MoureDevrais
    - [Cómo MEJORAR en PROGRAMACIÓN (Y en ENTREVISTAS Técnicas)](https://youtu.be/14v4IINunvY) @ MoureDevrais

* #### VSCode Environment setup
    - [25 VSCode Productivity Tips and Speed Hacks](https://youtu.be/ifTF3ags0XI) @ Fireship
    - [Get started with Jupyter Notebooks in 4 minutes](https://youtu.be/h1sAzPojKMg) @ VSC
    - [My VS Code Setup for Web Development](https://youtu.be/H2gvHxC9gFY) @ Forrest Knight

* #### Project ideas -general-
    - [5 Coding Projects (from beginner to advanced)](https://youtu.be/n2B-FClr5rA) @ Forrest Knight

* #### Misc.
    -  Coding on Android device ~ [Can you code on a phone? Android Mobile Programming Tutorial](https://youtu.be/VZ6LifcOXfM) @ fCC
    - Debuggin ~ [Best Debuggin Tips for Beginners](https://youtu.be/gaminoBsQx0) @ WebDevSimplified
    - History... ~ [What was Coding like 40 years ago?](https://youtu.be/7r83N3c2kPw) @ The Coding Train
    - JSON ~ ~~[Learn JSON in 10 Minutes](https://youtu.be/iiADhChRriM)~~ @ WebDevSimplified
    - Repository Patterns ~ [What is a Repository Pattern](https://youtu.be/x6C20zhZHw8) @ Coding Concept

### PYTHON

#### 101s
- [Python Installation and Setup 101](https://youtu.be/W1iXIiF5iMw) @KylieYing
- [Learn How to Learn Python - Easy & simple!](https://youtu.be/5mJ_Qftw2_0) @ TechLead
- [25 nooby Python habits you need to ditch](https://youtu.be/qUeud6DvOWI) @ mCoding

* ##### Libraries
    - [All top 40 Python Libraries EXPLAINED in 20 minutes](https://youtu.be/-29x_deQQus) @ Kite

* ##### Modules
    - [Top 18 most useful Python Modules](https://youtu.be/Vi9Y9AL13Rc) @ Tech With Tim

#### Tutorials 101
* ##### fCC ~ (Gen, Data Structures, Pygame)
    - Gen ~ ~~[12 Beginner Python Projects - Coding Course](https://youtu.be/8ext9G7xspg)~~
    - Data Structures ~ [Data Structures for Python Developers (w/Flask) - Course](https://youtu.be/74NW-84BqbA)
    - Pygame ~ ~~[Pygame Tutorial for Beginners - Python Development Course](https://youtu.be/FfWpgLFMI7w)~~

* ##### Clear Code ~ (Gen, Pygame, +more)
    - Gen ~ [The ultimate introduction to Python in 2022 (+ exercises)](https://youtu.be/mDKM-JtUhhc)
    - Gen ~ [Snake in the PowerShell Terminal (with Python)](https://youtu.be/lAIawk2IVIM)
    - Pygame ~ ~~[The ultimate introduction to Pygame](https://youtu.be/AY9MnQ4x3zk)~~
    - Pygame ~ [Creating a Zelda style game in Python (+ Dark Souls elements)](https://youtu.be/QU1pPzEGrqw)
    - Pygame ~ [Creating a Mario style Pirates platformer in Python (Pygame)](https://youtu.be/KJpP85tnOKg)
    - +more ~ [Creating Minecraft in Python (with the Ursina Engine)](https://youtu.be/DHSRaVeQxIk)
    - PySimpleGui ~ [Creating 10 Apps in Python](https://youtu.be/kQ8DGP9p2LY)

* ##### Other
    - PyWhatKit ~ [Convert Image into ASCII art](https://youtu.be/rMHJig4-c4I) @ Smart Gurucool


#### Tutorials 10x
* AI ~ [**Chat Bot** with PyTorh - NLP and Deep Learning - Python Tutorial (Part 1)](https://youtu.be/RpWeNzfSUHw) @ Python Engineer
* AI ~ [Creating a **Desktop Notification/Reminder App** in Python || Run Python Scripts in the Background](https://youtu.be/K7R1yIgOqHc)
* AI ~ [Tu primera **red neuronal** en Python y Tensorflow](https://youtu.be/iX_on3VxZzk) @ Ringa Tech
* AI ~ [Program a Reddit Bot - Python](https://youtu.be/3FpqXyJsd1s) @ Clarity Coders
* TO-DO ~ [Manage Your To-Do Lists Using Python and Django](https://realpython.com/django-todo-lists) @ Real Python

#### Tutorials 1Mx
* [Make YOUR OWN Programming Language - EP 4 - Variables](https://youtu.be/3PW552YHwy0) @ Code Pulse


<!--### 5.2 ~ Kotlin

#### Context
- [Java vs Kotlin for Android App Development](https://youtu.be/9wWgw9smBJs) @ Keep On Coding
- [Learn Kotlin in 12 Minutes](https://youtu.be/iYrgWO2oibY) @ Rahul Pandey

#### ($) KOTLIN desde CERO
* [Kotlin: Curso Android desde Cero](https://youtu.be/ebQphhLpJG0) @ MoureDevrais
    <!-- - Android Studio & more ... is it?
    - [JETPACK COMPOSE: Curso ANDROID KOTLIN desde CERO para PRINCIPIANTES](https://youtu.be/yVIGAvMO3bc)

-->

### BASH

[Shell Scripting Tutorial -website-](https://shellscript.sh)

[212 Bash Scripting Examples]

[Write Your Own Bash Scripts for Automation (Tutorial)](https://youtu.be/PPQ8m8xQAs8) @ Null Byte


#### $ BASHIT (EX2511)
* ~~[Learn BASH right now!](https://youtu.be/SPwyp2NG-bE)~~ @ Network Chuck

* ~~[$ 212 Bash Scripts](https://youtu.be/q2z-MRoNbgM)~~ @ LinuxHint 


### +MORE Languages

* **C# (GameDev: Unity, ...)**

* CSS
    - CSS Art/Design: [CodePen.io](https://codepen.io/kassandrasanch/pen/yLOOgNy)
    - CSS Battles ~ [Can you beat me at a CSS Battle?](https://youtu.be/A0J-hB3kSQ4) @ Kevin Powell
    - [Reverse Engineer CSS Animations {Shorts}](https://youtu.be/ecl-eCbYFPM) @ Fireship

* 'Fullstack' (React, Firebase, ... )
    - [7 Full Stack Ideas for Developers w/ Instructions Included](https://youtu.be/JTOJsU3FSD8) @ Fireship
    - [I built a chat app in 7 minutes with React & Firebase](https://youtu.be/zQyrwxMPm88) @ Fireship

* GBDK
    - [Learn to code and write games on the Nintendo Game Boy | MVG](https://youtu.be/FzPTK91EJY8) @ Modern Vintage Gamer

* JS
    - [JavaScript Game Development Course for Beginners](https://youtu.be/GFO_txvwK_c) @ fCC

* **MicroPython**
    - [MicroPython - Python for microcontrollers](https://micropython.org/)


* Node.js
    - [I created a Command Line Game for you // 5-Minute Node.js CLI Project](https://youtu.be/_oHByo8tiEY) @ Fireship


- .PDE ([Sauce01: C syntax / Arduino IDE](https://stackoverflow.com/questions/1127175/which-language-uses-pde-extension), ...)
    - **@pabloqpacin:** *find @SantiFiorino's Dino AI above*

- **Windows' PowerShell**
    <!-- - **@pabloqpacin:** *find (3.1-Windows) above* -->

.

## 6.0 ~ Game Development | Emulation & Modmaking

### Emulation
Emulation: Game Cube ~ [Emulation on Gamecube - NES, SNES, GBA, PS1 & more](https://youtu.be/_rYVWzjVWmw) @ Blaine Locklair

* #### ROMs
    - Zophar ~ [Zophar's Domain](https://www.zophar.net/) 

* #### Systems
    + emudev.org ~ [emudev's hub of Discord servers for ALL systems](https://emudev.org/discord_related)

### Engines (Unity, ...)
- Strong C# ~ [Unity in 100 Seconds](https://youtu.be/iqlH4okiQqg) @ Fireship
- [I wish I had known this before I started Unity Game Development](https://youtu.be/286SGzpUx9o) @ But Why Levin

### GameDev community
- GMTK
    - [GMTK Game Jam 2022](https://youtu.be/XNCGdi2A6fQ) @ Game Maker's Toolkit
- itch.io ~ [itch.io](https://itch.io/)
- Minijuegos (Devs) ~ [Miniplay > Devs](https://ssl.miniplay.com/dev/user/login)
- reddit ~ [reddit communities compiled lol](https://reddit.com)

### GameDev ideas
- 2048 (JavaScript + CSS) ~ [Build a 2048 to level up your Game Development](https://youtu.be/wOVEe9eawXc) @ WebDevSimplified
- Geo Game idea ~ [I Tried Creating a Game Using Real-World Geographic Data](https://youtu.be/sLqXFF8mlEU) @ Sebastian Lague
- Pokémon (Lua) ~ [Pokémon Coding Tutorial - CS50's Intro to Game Development](https://youtu.be/gx_qorHxBpI) @ fCC

### Mod-Making
- Mod-making 101 ~ [Game Modding afap](https://youtu.be/4BB1HfvSqAI) @ Techquickie

### Pygame limitations
- [Pygame's Performance - what you need to know](https://youtu.be/hnKocNdF9-U) @ DaFluffyPotato

### Reverse Engineer (Retro Games)
- [Beginners Guide to Reverse Engineering (Retro Games)](https://www.retroreversing.com/tutorials/introduction) @ Retro Reversing

<!--
#### 6.1b ~ Gamez aye
---

### 6.1 ~ Karmaggän
 First off, peek into local **Jagger Dress Up** -->

.


## 7.0 ~ NETWORKS | HACKING

### 0 -gen-
- Internet Speed ~ [Is your Internet FAST enough?](https://youtu.be/2LOkI3Xyd_E) @ Techquickie
- Latency ~ [Latency afap](https://youtu.be/UWeMWIoUWQA) @ Techquickie
- Servers ~ [I put a computer in my computer](https://youtu.be/cVWF3u-y-Zg) @ Jeff Geerling
    - Server's IP KVM = Internet Protocol Keyboard Video Mouse | Remote KVM connection to a computer over a network |
- Tarifas ~ [Consejos para elegir la MEJOR TARIFA de FIBRA y MÓVIL](https://youtu.be/tDT9XAi8G40) @ Xataka TV


### Black Hat...
- Cyber Kill Chain (CKC) ~ [The Mind of a Black Hat Hacker](https://youtu.be/-aNXeevUDyU) @ TayOnTech
- about DarkSide's ethos ~ [DarkSide: The $90 Million Dollar Hackers](https://youtu.be/YSRkbDF0ydg) @ Forrest Knight

### Botnetz
- [How to Actually Escape the Botnet](https://youtu.be/V1PUDUfWe4M) @ Mental Outlaw
- Emotet ~ [The World's Worst Botnet Just Got Stronger](https://youtu.be/lct_NBCzVKY) @ Mental Outlaw

### Cryptography
- [7 Crypto Concepts EVERY Developer Should Know](https://youtu.be/NuyzuNBFWxQ) @ Fireship

### CTF
- [How to solve Python Sandbox Capture-The-Flag challenge?](https://youtu.be/Ub_BMOMDOx0) @ CTF School

<!-- ### Cybersecurity -->

### Dark Web | Tor
- [How Tor Works](https://youtu.be/QRYzre4bf7I) @ Computerphile
- [How to browse the Dark Web safely?](https://youtu.be/7icDhuOtJtU) @ Tech Raj
- [How to Access the Dark Web Safely in 2022 (Tor + Tails)](https://youtu.be/EgXeXmNecto) @ The Cyber Mentor
- [SURFING THE DARK WEB](https://youtu.be/pKt_U9ShZxE) @ Crypto NWO <!--ok for Malware-->

### Digital Forensics
- [Magnet AXIOM Forensics](https://www.magnetforensics.com/products/magnet-axiom/)


### DIY_NAS aka 'Home Server' <!--'20.3 ~ Tinkering'-->

- [Your old PC is your new Server](https://youtu.be/zPmqbtKwtgw) @ Linux Tech Tips
- [Convert an old PC to a Home Server using Unraid - SMB, Terraria, HomeAssistant, Jellyfin](https://youtu.be/7h0JVS0en3U) @ Hardware Haven
- [How to build a Budget Home Server and WHY You Should](https://youtu.be/irW0AiRED3w) @ Zach's Tech Turf
- [How to build a DIY NAS from an OLD PC | Budget TrueNAS](https://youtu.be/FN3NhrD3KWo) @ Torogi Pro
- [Turn Old Computer into a NAS with FreeNas!](https://youtu.be/OUz5vC0IZX4) @ Torogi Pro
- [Setting up an old laptop as a NAS](https://youtu.be/ZInPE-sG0Ug) @ Electronics Wizardry
- [Turning an OLD PC/Laptop into a Media Server! (Ubuntu/PLEX Guide)](https://youtu.be/lXcfKTNObOo) @ Tech Hut
- [What's on my Home Server? MUST HAVE Services!](https://youtu.be/c4rKWrH88F0) @ Tech Hut
- [Incredible Budget Home Server! (Minecraft, Plex, Home Assistant, NAS)](https://youtu.be/72D3MvPk3Xs) @ Hardware Haven
- [Turn an old PC into a powerful NAS solution using UNRAID!](https://youtu.be/r9n4hMFBqvo) @ The Bear Tech


### Hacking...
- Cybersecurity... ~ [Dejo que ataquen mi servidor y acaba mal](https://youtu.be/lAByu20XJt4) @ Ringa Tech
- [Let's hack your home network // FREE CCNA // EP 9](https://youtu.be/80vIin4xGp8) @ Network Chuck
- [Create your own Hacking Lab and Hack your first Machine! (Disposable Kali Linux)](https://youtu.be/ir3QhZp8864)
- [How Hackers Hack Companies With Microsoft Office](https://youtu.be/_O1zfm5wavo) @ Marcus Hutchins
- [How do hackers hide themselves? - staying anonymous online](https://youtu.be/BWVyp0wYpgA) @ Grant Collins
- ['Nmap' Tutorial to find Network Vulnerabilities](https://youtu.be/4t4kBkMsDbQ) @ Network Chuck


### HomeLab
- [Tour of Home Network](https://youtu.be/Ev0PL892zSE) @ The 8-Bit Guy
- [What is a HomeLab and How Do I Get Started](https://youtu.be/gPGf4Y8nQqM) @ Techno Tim
- [HomeLab Tools & Accessories - Network / Server/ PC Tool Kit](https://youtu.be/VX2dxFkahgs) @ Techo Tim
- [What is a HomeLab? How can you build your own and why it's useful](https://youtu.be/4O_MxTPmah4) @ IT Career Questions


<!-- ### Jailbreaking
for Android rooting, see *5~SysAdmin|OS* -->

### Malware ($python)
- Pretty bad video but still... [Comparison: Computer Viruses](https://youtu.be/VqgE7WO3RSQ). Dawg we need to show the actual guns here.
- [New 'Borat' Malware?](https://youtu.be/4EKksK_maTM) @ Seytonic
- [I created malware with **Python** (it's SCARY easy!!)](https://youtu.be/UtMMjXOlRQc) @ Network Chuck
- [Can They Defeat My Homemade Virus?](https://youtu.be/tswtqG8c_P0) @ Basically Homeless

### Network Ports
- [Network Ports Explained](https://youtu.be/g2fT-g9PX9o) @ PowerCert Animated Videos

### Pentesting
- [Ex-NSA hacker tools for real world pentesting](https://youtu.be/G8lrwmsx8KA) @ David Bombal

<!-- ### 'Red Hat' -->

### Reverse Engineering
- Reverse Engineering 101 ~ [Getting Started Learning Reverse Engineering | Tips for Complete Beginners](https://youtu.be/DFHug3Nq7eU) @ Marcus Hutchins
- Ghidra 101 ~ [INGENIERÍA INVERSA USANDO GUIDRA (Herramienta de la NSA) | Tutorial](https://youtu.be/aQICC0EtG90) @ Mr Código Fuente

### Routers
- *40 minutes...* ~ [Your home router SUCKS!! (use pfSense instead)](https://youtu.be/lUzSsX4T4WQ) @ Network Chuck


### Scambaiting...
* @ Engineer Man
    - [Using My Python Skills To Punish Credit Card Scammers](https://youtu.be/StmNWzHbQJU)
* @ Kitboga
    - [Scam Call Turns NUCLEAR Over Expected $1M Fortune](https://youtu.be/_Ma5RY2bG38)
    - [Spending All My Money While Scammers Watch (they're furious)](https://youtu.be/K8weeeK-BPQ)
    - [These Tech Scammers Can't Figure Out What To Say](https://youtu.be/LXNiNuvWDJQ)
    - [This AI Brings Down Scammer Call Centers (in world record time)](https://youtu.be/coNjpBa5m1E)
    - [When Scammers Lose Thousands To Ransomware](https://youtu.be/yjkPb2mU0DU)
    - [Will Scammers Notice Windows 'Really Good' Edition?](https://youtu.be/F0peLpovDB8)
* @ Scambaiter
    - [Filling Out A Scammers Form, But With HIS OWN REAL Details!](https://youtu.be/xLyrc_JZmF4)
* @ Scammer Payback
    - [First ever Anti-Scam Call Center](https://youtu.be/_u_JTddAYes)
    - ~~[We Created the First Ever ANTI-SCAM Call Center](https://youtu.be/_u_JTddAYes)~~
* @ Scammer Revolts
    - (!!!) ~ [How to Scambait and Expose a Tech Support Scammer!](https://youtu.be/orEUCHTvmW0)
* @ The Engineer Man
    - [Showing a Craiglist scammer who's the boss using Python](https://youtu.be/UtNYzv8gLbs)


### Virtualization
- [How to Setup a Virtual Machine for Malware Analysis](https://youtu.be/-40OBLWVsgo) @ Guided Hacking
- [Learn Virtual Machines RIGHT NOW! (Kali Linux, VM, Ubuntu, Windows)](https://youtu.be/wX75Z-4MEoM) @ Network Chuck
- [Ditch Virtualbox, Get QEMU/Virt Manager](https://youtu.be/wxxP39cNJOs) @ Mental Outlaw
- [Stop using Virtualbox, Here's how to use QEMU instead](https://youtu.be/Kq849CpGd88) @ Chris Titus Tech
- [20 Ways to Use a Virtual Machine (and other ideas for your homelab)](https://youtu.be/SVQmzaSabEQ) @ Techno Tim


### VPNs
<!-- set up? both in Windows and Linux? Decide machines -->

### VPSs
- [Best VPS hosting providers of 2022](https://www.techradar.com/news/best-vps-hosting) @ Tech Radar

---
## 8.0 ~ IT Certificates

### -GEN-

* [Network Chuck's *'If I had to start over... which IT path would I take?](https://youtu.be/E25SKW4-8wQ)
    - **Network+** recommended
    - (29:00) - Having any IT job, become BFF with **Network Engineers** around.
    - **Python** & **Linux** GOOD.
    - **Cloud** GOOD.
    * JOBS:
        - less popular = better paid
        - only coding = popular = average
### Networks

* #### [CISCO'S CCNA](https://www.cisco.com/c/en/us/training-events/training-certifications/certifications/associate/ccna.html)
     - A combination of lectures, hands-on labs, and self-study will prepare you to install, operate, configure, and verify basic IPv4 and IPv6 networks.

* #### CompTIA's Network+
    - [Reference Materials](https://youtu.be/vrh0epPAC5w) @ PowerCert Animated Videos



## 9.0 ~ Open-Source Development

* ### Mozilla -Web Development-

- General Web Dev. ~ [Resources for Developers, by Developers | Documenting **web technologies, including CSS, HTML and JavaScript**, since 2005](https://developer.mozilla.org/en-US/)
- Browser add-on dev. ~ [Add-on Developer Hub](https://addons.mozilla.org/en-US/developers/)


---
---

# Weird sociologicals

- [2007 | The Dark Side of the Web](https://youtu.be/U0nDoAML_QI)
- [2007 | Tech Talk: Linus Torvalds on git](https://youtu.be/4XpnKHJAok8) @ Google
- [2021 | Why the Simulation Hypothesis is Wrong](https://youtu.be/MqM_K9vL8is) @ Duncan
- (!!!) ~ [2022 | How many people might ever exist, calculated](https://youtu.be/r6sa_fWQB_4) @ Primer



