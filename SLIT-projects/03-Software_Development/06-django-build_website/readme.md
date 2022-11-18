# Django - Python Website Full Tutorial

Following another tutorial by #@TechWithTim
- video-course (following): [Django For Beginners - Full Tutorial](https://youtu.be/sm1mokevMWk)

Django documentation
- [How to install Django on Windows](https://docs.djangoproject.com/en/4.1/howto/windows/)
    - Relevant because `activate dj` didn't work for me so I defo should read about the **'virtual environment'** config

<details>
<summary>Table of Contents</summary>

- [Django - Python Website Full Tutorial](#django---python-website-full-tutorial)
- [Part 1 - Setup, Installation and Page Navigation](#part-1---setup-installation-and-page-navigation)

</details>

# Part 1 - Setup, Installation and Page Navigation

This section covers Django installation & setup assuming your machine runs Windows and **Python** is already installed.

Now open the **Command Prompt** - CMD (I use the Windows Terminal app) and access the folder you want your project files to be in.

> Bear in mind CMD must be used (ie. WSL's ZSH doesn't work) since machine runs Windows_10
> 
> In fact, running `python3 -m django --version` in WSL's ZSH returns "/usr/bin/python3: No module named django

```CMD
REM REAMDE: lines starting with REM are comments

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
REM (my location is 'C:\Users\Usuario\Downloads\linwin\SLIT\SLIT-projects\03-Software_Development\06-django-build_website')
django-admin startproject websyte
```
Basic project folder `websyte` is created with the following contents:
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

Now the project files are created, let's test to run the site locally

```CMD
REM make sure you're in the main project folder
cd websyte

REM run the site!
python3 manage.py runserver
```

<details>
<summary>click to see `python manage.py runserver` screenshot</summary>

![python_manage.py_runserver](/SLIT-projects/03-Software_Development/06-django-build_website/images/part1-python_managepy_runserver.PNG)
</details>
