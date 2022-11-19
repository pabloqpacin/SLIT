# Python Website 'WSL' Tutorial - Django, Auth, Databases & More

Following a tutorial by #@TechWithTim : [Django For Beginners - Full Tutorial](https://youtu.be/sm1mokevMWk)

Main takes:
- *Django developer environment via **WSL** (Linux on Windows)*
- ***devops** security - .gitignore & GitGuardian*
- no disrespect but... tutorial is misleading since first thing done is installing Django, rather than setting up the virtual environment (which is recommended for both Windows and Linux builds)


<details>
<summary>Table of Contents</summary>

- [Python Website 'WSL' Tutorial - Django, Auth, Databases & More](#python-website-wsl-tutorial---django-auth-databases--more)
  - [Documentation](#documentation)
  - [~~Part 1 🌑- Installation, Setup and Page Navigation~~](#part-1---installation-setup-and-page-navigation)
  - [--REWORK--](#--rework--)
    - [uninstall Django for WSL reinstall](#uninstall-django-for-wsl-reinstall)
  - [Part 1 ☀️ - Setup, Installation, and Page Navigation](#part-1-️---setup-installation-and-page-navigation)
    - [Virtual Environment setup (TO-DO always!)](#virtual-environment-setup-to-do-always)
    - [Installing Django](#installing-django)
    - [Creating a Django project](#creating-a-django-project)
    - [.gitignore file creation](#gitignore-file-creation)
  - [PENDIENTE](#pendiente)
    - [Test local server](#test-local-server)

</details>


## Documentation

- must-read
    - @ Django Docs - [How to install Django on Windows](https://docs.djangoproject.com/en/4.1/howto/windows/) (important for the video but **I don't do Windows, I do Linux because WSL** <!-- Relevant because `activate dj` didn't work for me so I defo should read about the **'virtual environment'** config -->)
    - **@ Django Docs - [How to install Django](https://docs.djangoproject.com/en/4.1/topics/install/) (for after REWORK)** <!--mind the first steps meant for a **PRODUCTION DEPLOYMENT**, including Apache and more-->
    -  @ Django Docs - [... Create a virtual environment](https://docs.djangoproject.com/en/4.1/intro/contributing/#getting-a-copy-of-django-s-development-version)
    
    - **WSL - [Installing Python, Postgres, Django and other CLI tools inside WSL](https://www.agiliq.com/blog/2018/07/using-django-on-windows-with-wsl/)** (*research* server's "port 8000")
    - **.gitignore - [hiding secret key in django project on github after uploading project](https://stackoverflow.com/questions/64208678/hiding-secret-key-in-django-project-on-github-after-uploading-project)**
    - for .gitignore - [Python Decouple](https://pypi.org/project/python-decouple/)
- Other
    - CMD `REM` - (1) [StackOverflow: How to write CMD comments](https://stackoverflow.com/questions/2997578/how-do-i-comment-on-the-windows-command-line) (2) [superuser: How to CMD comment](https://superuser.com/questions/82231/how-do-i-do-comments-at-a-windows-command-prompt)
    - CMD `cls` - Google: how to clear CMD terminal output
    - [GitGuardian](https://github.com/GitGuardian) - see [REWORK](#rework) for context
    - [StackOverflow: uninstalling Django (Windows)](https://stackoverflow.com/questions/20897851/uninstall-django-completely)


## ~~Part 1 🌑- Installation, Setup and Page Navigation~~

<details>
<summary>Can skip cause t'was reworked</summary>

Assuming your machine runs Windows and **Python** is already installed, open the **Command Prompt** - CMD (via VSCode integrated terminal or the Terminal Preview app) and access the folder you want your project files to be in.

<!-- ??
Bear in mind CMD must be used (ie. WSL's ZSH doesn't work) since machine runs Windows_10
Although `python3 --version` works fine, after installing Django via CMD (`pip install django`)
running `python3 -m django --version` in WSL's ZSH returns "/usr/bin/python3: No module named django
-->

```CMD
REM (lines starting with REM are comments)

REM make sure Python is installed
python --version

REM (1.) install Django
pip install django
```
<details>
<summary>see Windows Terminal output screenshot</summary>

![pip_install_django](/SLIT-projects/03-Software_Development/06-django-build_website/images/aborted--cmd-pip_install.PNG)
</details>

```CMD
REM Tim enters `activate dj` because "virtual environment" - for me it doesn't work (must read documentation above)

REM (2.) create Django project in designated location - project folder can be named 'mysite' or else
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

REM (3) run the site!
python manage.py runserver

REM unless encountering an error, access the given address via web browser (as shown below) 
```

The two screenshots below display:

<details>
<summary>(1) CMD terminal output to `python manage.py runserver` + site access output</summary>

![manage.py_runserver](/SLIT-projects/03-Software_Development/06-django-build_website/images/aborted--cmd_runserver_outupt.PNG)
</details>

<details>
<summary>(2) "development server" site at local network port 8000 (`http://127.0.0.1:8000/`) via Google's Chrome browser</summary>

![server-8000--dev-env](/SLIT-projects/03-Software_Development/06-django-build_website/images/aborted--dev_server.PNG)
</details>


</details>

## --REWORK--

<details>
<summary>Can skip cause t'was reworked too</summary>

Project is halted and all current progress aborted and restarted to optimize the **development environment**.

Although we will continue the tutorial, **major changes** will apply according with our [documentation](#documentation):

- our Django project won't be a Windows install but a Linux one, since we run WSL

### uninstall Django for WSL reinstall

Due to confusing CMD vs WSL's ZSH Django config/setup/admin (as we use Bash for **git** and for other projects' development), we decide to uninstall Django, read the **virtual environment** config [documentation](#documentation) for Windows and finally reinstall Django for our WSL system.

In other words, let's undo our Django Windows install to reinstall it [later](#part-1-☀️---setup-installation-and-page-navigation) (we may install Django for Linux since we plan on running the framework via WSL and **VSCode's integrated WSL's ZSH terminal**).

1. First off, delete current `mysite` local folder from within the file explorer. Freely git-commit their removal.

```markdown
I try via file explorer but ERROR:
- La acción no se puede completar porque otro programa abrió la carpeta o uno de sus archivos. Cierre la carpeta o el archivo e inténtelo de nuevo.

I try deleting via vscode Explorer but ERROR:
- Error: EBUSY: resource busy or locked, rmdir
- 'c:Users\Usuario\...\linwin\SLIT\...\mysite'
```

As a result, I skip to step 2:

2. Secondly, uninstall Django via CMD.

```CMD
REM make sure Django is installed
python -m django --version
    REM '4.1.3'


REM uninstall Django via CMD with Python's pip installer
pip uninstall django
    REM 'Found  Django 4.1.3 ... Would remove:
    REM C:\users\usuario\appdata\local\programs\python\python310\lib\site-packages\django-3.1.3.dist-info\*
    REM C:\users\...\python310\lib\site-packages\django\*
    REM C:\users\...\python310\scripts\django-admin.exe
    REM Proceed (Y/n)?'
Y
    REM 'Successfully uninstalled Django-4.1.3'

REM double-check Django is uninstalled
python -m django --version
    REM 'No module named django'

REM assess Python config
python --version
    REM Python 3.10.5
```
3. Again, let's try to delete the local `mysite` project (this time after closing this VSCode window).

> It worked so, let's reinstall! - Don't forget to read Django Docs documentation!

</details>

## Part 1 ☀️ - Setup, Installation, and Page Navigation

<!-- I might cover a complete WSL/Python-VM setup
(( Windows10 > WSL > Ubuntu > OhMyZsh > VSCode >> Python(pip) > Django )) -->

> Considering all previous documentation here... we are actually restarting the project yay! 🌌

Now, as for a fresh start, let's install Django for Linux, since we are running Ubuntu in our Windows 10 **WSL** environment. This is actually a major twist from the Tim's tutorial, nonetheless, it is what must be done.

For using the command-line in our Windows 10 machine, we could either resort to the Windows Terminal app (running the Ubuntu *profile*) or the good ol' VSCode's integrated WSL terminal. Either way, we are using Bash commands and [OhMyZsh](https://youtu.be/dQw4w9WgXcQ) features.


```bash
# using ZSH btw, rather than Bash
which $SHELL        # /usr/bin/zsh

# make sure Python is installed
python3 --version   # Python 3.10.6
```

Reading the [Django documentation](#documentation) above, we decide to closely follow the steps below: 

### Virtual Environment setup (TO-DO always!) 

First off, time to set up a proper virtual environment with `venv` following [official documentation](https://docs.djangoproject.com/en/4.1/intro/contributing/#getting-a-copy-of-django-s-development-version).

```bash
# create a new virtual environment
python3 -m venv ~/.virtualenvs/djangodev
    # ERROR because 'ensurepip' is not available

# install the 'python3-venv' package
apt install python3.10-venv
    # the following NEW packages will be installed:
    # 'python3-pip-whl' 'python3-setuptools-whl' 'python3.10-venv'

# now again, properly
python3 -m venv ~/.virtualenvs/djangodev
```

Now `~/.virtualenvs/djangodev` is the path where the new environment will be saved. Out of curiosity, these are the contents of such dir.
```bash
cd ~/.virtualenvs/djangodev

ls
# bin include lib lib64 pyvenv.cfg

ls bin
# Activate.ps1 activate activate.csh activate.fish pip pip3 python python3 python3.10
```

Moving on, let's **activate** the the environment:
```bash
source ~/.virtualenvs/djangodev/bin/activate
# It should have worked as per screenshot below
```

**Important!!** See documentation:
```markdown
You have to **activate** the virtual environment whenever you open a new terminal window.

---
The name of the currently activated virtual environment is displayed on the command line to help you keep track of which one you are using.

Anything you install through **pip** while this name is displayed will be installed in that virtual environment, isolated from other environments and system-wide packages.
```


<details>
<summary>see virtual env. flair on Terminal</summary>

![(djangodev) in Terminal](/SLIT-projects/03-Software_Development/06-django-build_website/images/part1--source_activate.PNG)
</details>

---

### Installing Django

Having setup and activated a `(djangodev)` virtual environment, let's `pip install` Django according with [Django documentation](https://docs.djangoproject.com/en/4.1/topics/install/#installing-an-official-release-with-pip)!

```bash
# install Django in the (djangodev) virtual environment
python -m pip install Django

# make sure django is installed
python3 -m django --version
    # '4.1.3'
```
<details>
<summary>see Terminal output</summary>

![pip install Django](/SLIT-projects/03-Software_Development/06-django-build_website/images/part1--pip_install_django.PNG)
</details>

### Creating a Django project

Having Django installed in our `(djangodev)` virtual environment, let's create our Django project, that is, `websyte`.

```bash
cd <designated-directory>
# in our case '/mnt/c/Users/Usuario/.../SLIT/.../06-django-build_website'

# create Django project
django-admin startproject websyte
```

The dir/folder `websyte` has been created in our designated folder. These are the contents of such 'root directory':
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


### .gitignore file creation

<!-- GitGuardian alert about **leaking** 'Django Secret Key' over GitHub -->

Now that our `websyte` project is created, and considering previous 'Django Secret Key leaks' during our first (Windows-aimed) approach to Django, let's set up a proper **.gitignore** file following the relevant [documentation](#documentation) above.

```markdown
1. In the same directory where `manage.py` is, create a file whose name is `.env`.

2. Open `settings.py`, cut `SECRET_KEY = '....your secret key ....'` and paste it to `.env`.

3. In the same directory, create a file whose name is `.gitignore`, and write `.env` inside it.

4. Then in your `settings.py`, where previously you had `SECRET_KEY = '....your secret key ....'`, put:

`from decouple import config`
`SECRET_KEY = config("SECRET_KEY") # this is to replace the secret key you cut away before`

5. then in your command prompts run:

`pip install python-decouple`
`pip freeze > requirements.txt`

6. then add, commit and push on Github.

[Here](https://git-scm.com/docs/gitignore) you can find out more information on how .gitignore works.
```

<details>
<summary>click to see GitGuardian alert</summary>

![GitGuardian leak alert](/SLIT-projects/03-Software_Development/06-django-build_website/images/leak--git_key_exposed.PNG)
</details>

<details>
<summary>click to see GitGuardian 'Fix This Secret Leak' redirect</summary> 

![GitGuardian auth](/SLIT-projects/03-Software_Development/06-django-build_website/images/leak--GitGuardian-auth.PNG)
</details>

## PENDIENTE

okay i'm about to call it a day. Recap:
- virtual environment activated
- django installed
- project created
    - in '/mnt/c/../SLIT/...'
    - **SHOULD it be in WSL's '~'?!**
- .gitignore attempted
    - python problem in `settings.py`:
    - 'Import "decouple" could not be resolved'... 

```python
[{
	"resource": "/c:/Users/Usuario/Downloads/linwin/SLIT/SLIT-projects/03-Software_Development/06-django-build_website/websyte/websyte/settings.py",
	"owner": "_generated_diagnostic_collection_name_#4",
	"code": {
		"value": "reportMissingImports",
		"target": {
			"$mid": 1,
			"external": "https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingImports",
			"path": "/microsoft/pyright/blob/main/docs/configuration.md",
			"scheme": "https",
			"authority": "github.com",
			"fragment": "reportMissingImports"
		}
	},
	"severity": 4,
	"message": "Import \"decouple\" could not be resolved",
	"source": "Pylance",
	"startLineNumber": 26,
	"startColumn": 6,
	"endLineNumber": 26,
	"endColumn": 14
}]
```

SO...
- since I wanna go, guess I should de-activate the `(djangodev)` virtual environment
    - according with [this documentation](https://stackoverflow.com/questions/990754/how-to-leave-exit-deactivate-a-python-virtualenv) (not yet present above), all I should do is type int `deactivate`
    - it seems to work!!
    - regardless, I type in `source ~/.virtualenvs/djangodev/bin/activate` again to test **gittin'**
- add, commit and push current `week46` to GitHub
- when DONE so, I'll enter `deactivate`, close VSCode and call it a day 😅



<details>
<summary> pendiente - runserver </summary>

### Test local server

Having created our `websyte` Django project, let's test whether it's working fine by "running a server in our local machine", which should allow us to connect to our website.

> What we're doing is known as "Development": working on our local machine, website is not live on the Internet, but connecting to it with our web browser allow us to see it 'as if' it was live.

```bash
# move to relevant dir
cd websyte

# run local server
python3 manage.py runserver
```

</details>