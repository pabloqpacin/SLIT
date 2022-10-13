24/09/2022


<!-- v0.0.4 = ?? -->
v0.0.3 = actually started working on the scripts | 29/212
<!-- v0.0.2 = local git branches should be ready; action begins -->
<!-- v0.0.1 = file creation and git setup (in parallel with EX2511's scripts) -->

---

# bash212 ~ Documentation

local file in GL76, in Git's branch *bGL76*


0. [~ setup](#00--setup)

1. [~ scripts 0 - n]()

2. [~ scripts n - n2]()

---

## 0.0 ~ setup

### Git stuff

In a nutshell:
- Did *git init* in local GL76 dir. 
- Created repo in GitHub, then pushed (master) from GL76.
- Created local bGL76 branch and here is where I will handle the *Documentation.md* file.

- On EX2511, cloned GitHub's repo, created local bEX2511 branch.
- GL76's branch is for Documentation, EX2511's branch is for the actual scripts; them both should be merged successfully and consistantly.

---

## 1.0 ~ scripts 0 - n

[@linuxhint's video starts](https://youtu.be/q2z-MRoNbgM)

### n1
Explanation about files' group permissions (ie. owner, group, public permission).

### n7

For renaming files using git... [thanks Git Documentation](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)


### n15
Great **multi-line commenting** system:


    <<keyword
    commented text
    more commented text
    keyword

### n17

New *variables* something:
    
    a='this is a'
    b='this is b'
    c="${a} and ${b}"
    echo "${c}"


### n24 
links = copies (?)

### n26
interesting about writign rights 


### n27
IMPORTANT about users <!--didn't follow cuz didn't wanna create more users >

### n28
variables + append 

---
## Math

### n29
*let* for math with variables

### n30
*expr* for basic operations
need *\* for operations

### n31
interesting math with variables


### n33
OJO: math > remainderz (%)

### n35
kinda *echo* for math  

### n37
bit messed up

---

## Strings

### n39) Concatenate strings
        VAR3=${VAR1}${VAR2}


### n41) ...


### n42) HEREDOC
        VAR=$(cat<<'HEREDOC'
        text
        more text
        HEREDOC
        )


### n43)
ojo con lo de *$(whoami)*

### n45
OJO it all works, with 1 or 2 brackets, 1 or 2 '&'s, ';' or not

### n47 ~ Using *-ge*
ojito, que '>' != '-ge'
GT == Greater Than
GE == Greater or Equal (?)


### n48 ~ nesting if
needs a review...


