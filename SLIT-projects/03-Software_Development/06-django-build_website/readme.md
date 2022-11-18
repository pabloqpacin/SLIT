# Django - Python Website Full Tutorial

Following another tutorial by @ Tech With Tim
- video (following): [Django For Beginners - Full Tutorial](https://youtu.be/sm1mokevMWk)

More documentation:
- [How to install Django on Windows](https://docs.djangoproject.com/en/4.1/howto/windows/)
    - this is relevant because `activate dj` didn't work for me and...
    - because perhaps I should look more into the **'virtual environment'** thing


<details>
<summary>Table of Contents</summary>

- [Django - Python Website Full Tutorial](#django---python-website-full-tutorial)
  - [Part 1 - Setup, Installation and Page Navigation](#part-1---setup-installation-and-page-navigation)


</details>

## Part 1 - Setup, Installation and Page Navigation

First of all we need to install **Django**. Assuming **Python** is installed, open *Command Prompt* and enter `pip install django`.
<details>
<summary>Click to view screenshot</summary>

![pipinstalldjango](/SLIT-projects/03-Software_Development/06-django-build_website/images/part1-pipinstalldjango.PNG)

</details>

<!-- ~~Now, `activate dj`...~~ -->

Now in *CMD* go to the project folder and enter `django-admin startproject mysite`, which creates a **`mysite`** folder:

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

Project is now created. Let's test it (running website locally as if it was over the internet)!

```markdown
In *CMD*:
- `cd mysite`
- `python3 manage.py runserver`

