# Python Website 'Windows' Tutorial - Django, Auth, Databases & More

Following a tutorial by #@TechWithTim : [Django For Beginners - Full Tutorial](https://youtu.be/sm1mokevMWk)

More documentation (Django docs):

- [How to install Django on Windows](https://docs.djangoproject.com/en/4.1/howto/windows/) <!-- Relevant because `activate dj` didn't work for me so I defo should read about the **'virtual environment'** config -->

<details>
<summary>Table of Contents</summary>

- [Python Website 'Windows' Tutorial - Django, Auth, Databases & More](#python-website-windows-tutorial---django-auth-databases--more)
  - [Part 1 - Installation, Setup and Page Navigation](#part-1---installation-setup-and-page-navigation)
  - [ABORT progress](#abort-progress)

</details>

## Part 1 - Installation, Setup and Page Navigation

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

![pip_install_django](/SLIT-projects/03-Software_Development/06-django-build_website/images/part1-pip_install_django.PNG)
</details>

```CMD
REM Tim enters `activate dj` because "virtual environment" - for me it doesn't work (must read documentation above)

REM 2. create Django project in designated location - project folder can be named 'mysite' or else
    REM (C:\Users\Usuario\Downloads\linwin\SLIT\SLIT-projects\03-Software_Development\06-django-build_website)
django-admin startproject websyte
```
A project folder should've been created under the name `websyte` containing the following:
```markdown
- websyte
    - websyte
        - __init__.py
        - asgi.py <!--not in the video-->
        - settings.py
        - urls.py
        - wsgi.py
    - manage.py 
```

Having created the main project files, let's test 'em run the site locally!

```CMD
REM access the just created project folder 
cd websyte

REM run the site!
python3 manage.py runserver
```

<details>
<summary>click to see `python manage.py runserver` screenshot</summary>

![python_manage.py_runserver](/SLIT-projects/03-Software_Development/06-django-build_website/images/part1-python_managepy_runserver.PNG)
</details>

---

## ABORT progress

For these reasons, project is halted, aborted and restarted:

1. Confusing CMD vs WSL config/setup
2. GitGuardian alert about **leaking** 'Django Secret Key' over GitHub

<details>
<summary>click to see GitGuardian alert</summary>

![GitGuardian leak alert](/SLIT-projects/03-Software_Development/06-django-build_website/images/issue-git_key_exposed.PNG)
</details>

<details>
<summary>click to see GitGuardian 'Fix This Secret Leak' redirect</summary> 

![GitGuardian auth](/SLIT-projects/03-Software_Development/06-django-build_website/images/issue--GitGuardian-auth.PNG)
</details>

