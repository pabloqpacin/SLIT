# Django - Python Website Full Tutorial

Following another tutorial by #@TechWithTim
- video-course (following): [Django For Beginners - Full Tutorial](https://youtu.be/sm1mokevMWk)

## Documentation:
- Django documentation
    - [How to install Django on Windows](https://docs.djangoproject.com/en/4.1/howto/windows/)
        - Relevant because `activate dj` didn't work for me so I defo should read about the **'virtual environment'** config

## Table of Contents
<details>
<summary>click to expand ToC</summary>

- [Django - Python Website Full Tutorial](#django---python-website-full-tutorial)
  - [Documentation:](#documentation)
  - [Table of Contents](#table-of-contents)
  - [Part 1 - Setup, Installation and Page Navigation](#part-1---setup-installation-and-page-navigation)
    - [CMD - `pip install django`](#cmd---pip-install-django)
    - [CMD - `django-admin startproject mysite`](#cmd---django-admin-startproject-mysite)
    - [CMD - `python manage.py runserver`](#cmd---python-managepy-runserver)


</details>

## Part 1 - Setup, Installation and Page Navigation

### CMD - `pip install django`

First of all, **Django** should be installed.

Assuming **Python** is installed, enter `pip install django` in the **Command Prompt** (CMD).

> In my case, I run CMD via the Windows Terminal application.

<details>
<summary>click to see screenshot</summary>

![pipinstalldjango](/SLIT-projects/03-Software_Development/06-django-build_website/images/part1-pipinstalldjango.PNG)
</details>

> Tim now runs `activate dj` upon saying he's running a "virtual environment", but this doesn't work for me (read [documentation](#documentation)).

### CMD - `django-admin startproject mysite`

Now in CMD go to the project folder and enter `django-admin startproject mysite`, which creates a **`mysite`** folder:

> Bear in mind CMD must be used (ie. wsl's zsh won't work)
> In fact, running `python3 -m django --version` in wsl's zsh returns "/usr/bin/python3: No module named django

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

### CMD - `python manage.py runserver`

Project is now created. Let's test it (running website locally as if it was over the internet)!

```markdown
In CMD:
- `cd mysite`
- `python3 manage.py runserver`

