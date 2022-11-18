# Python Website 'Windows' Tutorial - Django, Auth, Databases & More

Following a tutorial by #@TechWithTim : [Django For Beginners - Full Tutorial](https://youtu.be/sm1mokevMWk)

Main takes:
- Django developer environment via WSL (Linux on Windows) 

## Documentation

- must-read
    - @ Django devs - [How to install Django on Windows](https://docs.djangoproject.com/en/4.1/howto/windows/) (important for the video but **I don't do Windows, I do Linux because WSL** <!-- Relevant because `activate dj` didn't work for me so I defo should read about the **'virtual environment'** config -->)
    
    - **WSL - [Installing Python, Postgres, Django and other CLI tools inside WSL](https://www.agiliq.com/blog/2018/07/using-django-on-windows-with-wsl/)** (*research server's "port 8000"*)
    - **.gitignore - [hiding secret key in django project on github after uploading project](https://stackoverflow.com/questions/64208678/hiding-secret-key-in-django-project-on-github-after-uploading-project)**
- Other
    - CMD `REM` - (1) [StackOverflow: How to write CMD comments](https://stackoverflow.com/questions/2997578/how-do-i-comment-on-the-windows-command-line) (2) [superuser: How to CMD comment](https://superuser.com/questions/82231/how-do-i-do-comments-at-a-windows-command-prompt)
    - CMD `cls` - Google: how to clear CMD terminal output

<details>
<summary>Table of Contents</summary>

- [Python Website 'Windows' Tutorial - Django, Auth, Databases & More](#python-website-windows-tutorial---django-auth-databases--more)
  - [Documentation](#documentation)
  - [~~Part 1 - Installation, Setup and Page Navigation~~](#part-1---installation-setup-and-page-navigation)
  - [REWORK](#rework)
    - [Django re-install for WSL](#django-re-install-for-wsl)
    - [.gitignore file creation](#gitignore-file-creation)
  - [Part 1 - WEBSYTEEEEE](#part-1---websyteeeee)

</details>

## ~~Part 1 - Installation, Setup and Page Navigation~~

Assuming your machine runs Windows and **Python** is already installed, open the **Command Prompt** - CMD (I use the Terminal Preview app) and access the folder you want your project files to be in.

<!-- ??
Bear in mind CMD must be used (ie. WSL's ZSH doesn't work) since machine runs Windows_10
Although `python3 --version` works fine, after installing Django via CMD (`pip install django`)
running `python3 -m django --version` in WSL's ZSH returns "/usr/bin/python3: No module named django
-->

```CMD
REM (lines starting with REM are comments)

REM make sure python is installed
python --version

REM 1. install Django
pip install django
```
<details>
<summary>click to see `pip install django` screenshot</summary>

![pip_install_django](/SLIT-projects/03-Software_Development/06-django-build_website/images/aborted--cmd-pip_install.PNG)
</details>

```CMD
REM Tim enters `activate dj` because "virtual environment" - for me it doesn't work (must read documentation above)

REM 2. create Django project in designated location - project folder can be named 'mysite' or else
    REM (C:\Users\Usuario\Downloads\linwin\SLIT\SLIT-projects\03-Software_Development\06-django-build_website)
django-admin startproject mysite
```
A project folder should've been created under the name `mysite` containing the following:
```markdown
- mysite
    - mysite
        - __init__.py
        - asgi.py <!--not in the video-->
        - settings.py
        - urls.py
        - wsgi.py
    - manage.py 
```

Having created the main project files, let's test 'em running the site locally!

```CMD
REM access the just created project folder 
cd mysite

REM run the site!
python manage.py runserver
```

The two screenshots below display (1) CMD terminal output to `python manage.py runserver` + site access output & (2) *'development server'* site at local network port 8000 (`http://127.0.0.1:8000/`) via Google's Chrome browser.

<details>
<summary>(1)</summary>

![manage.py_runserver](/SLIT-projects/03-Software_Development/06-django-build_website/images/aborted--cmd_runserver_outupt.PNG)
</details>

<details>
<summary>(2)</summary>

![server-8000--dev-env](/SLIT-projects/03-Software_Development/06-django-build_website/images/aborted--dev_server.PNG)
</details>




---

## REWORK


Project is halted and all current progress aborted and restarted.

### Django re-install for WSL

Due to confusing CMD vs WSL's ZSH Django config/setup, we should uninstall Django.

```CMD
REM delete current `mysite` from within the file explorer
    REM freely git-commit their removal

REM uninstall Django via CMD
pip uninstall django.........

```

MUST READ documentation about the **virtual environment** config.

### .gitignore file creation

<!-- GitGuardian alert about **leaking** 'Django Secret Key' over GitHub -->

Given *Django Secret Key leaks*, a **.gitignore** file should be created following the [documentation](#documentation) above.

- **yadda yadda**
    - **yadda yadda**

<details>
<summary>click to see GitGuardian alert</summary>

![GitGuardian leak alert](/SLIT-projects/03-Software_Development/06-django-build_website/images/leak--git_key_exposed.PNG)
</details>

<details>
<summary>click to see GitGuardian 'Fix This Secret Leak' redirect</summary> 

![GitGuardian auth](/SLIT-projects/03-Software_Development/06-django-build_website/images/leak--GitGuardian-auth.PNG)
</details>

---







## Part 1 - WEBSYTEEEEE