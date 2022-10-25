# Python Website Full Tutorial - Flask, Authentication, Databases & More

Following a tutorial by @ Tech With Tim
- long video (following): [Python Website Full Tutorial - Flask, Authentication, Databases & More](https://youtu.bem/dam0GPOAvVI)
- short video (might watch): [Make A Python Website As Fast As Possible!](https://youtu.be/kng-mJJby8g)
- if anything, source code: [github](https://github.com/techwithtim/Flask-Web-App-Tutorial)

<details>
<summary>Table of Contents</summary>

- [Python Website Full Tutorial - Flask, Authentication, Databases & More](#python-website-full-tutorial---flask-authentication-databases--more)
  - [Getting started](#getting-started)
  - [Creating a Flask App](#creating-a-flask-app)
  - [Creating Routes/Views](#creating-routesviews)
  - [Jinja Templating Language & HTML Templates](#jinja-templating-language--html-templates)

</details>

## Getting started

- Basic project folder structure
```markdown
- python-build_website
    - website
        - statit
        - templates
        - __init__.py
        - auth.py
        - models.py
        - views.py
    - main.py
```

- Having **pip** already installed, install necessary **flask** modules via via [command line] [vscode wsl terminal]:
    - `pip install flask`
    - `pip install flask-login`
    - `pip install flask-sqlalchemy`

## Creating a Flask App
1. Go to `init.py`:
```python
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'tusupervieja'

    return app
```
The `website` folder is now a package thanks to `__init__.py` 

2. In `main.py`:
```python
from website import create_app
```
Since `website` is a package, importing it will run the code within `__init__.py` —for now only the `create_app` function—.

Adding on:
```python
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)     # Changing any files will re-run the web server; 'False' if in Production
```

3. Make sure your **python interpreter** is correctly set up.

4. Run `main.py` and visit http://127.0.0.1:5000!

## Creating Routes/Views

1. To create our first website route, go to `views.py`. There we'll store our web routes (homepage and other user navigation sites). <!--`auth.py` will have the login page and other auth files -->

```python
from flask import Blueprint

# Now we'll define this file as a blueprint of our app (ie. routes, urls)
views = Blueprint('views', __name__)
# Doesn't need to be 'views, but sharing name with the file itself makes everything easier
```

2. Now same thing but for `auth.py`:

```python
from flask import Blueprint

auth = Blueprint('auth', __name__)
```

3. Back in `views.py`, define a function to run whenever we go to the route ("/").

```python
@views.route('/')
def home():
    return <h1>Test</h1>
```

4. Register these **blueprints** in `__init__.py`:
```python
app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
```

`url_prefix` could be "/auth/" for example, but that makes it more difficult!

> RUN THE WEBPAGE

5. Add more routes in `auth.py`:

```python
@auth.route('/login')
def login ():
    return "<p>Login</p>"

@auth.route('/logout')
def logout ():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up ():
    return "<p>Sign up</p>"
```

> RUN THE WEBPAGE

## Jinja Templating Language & HTML Templates

Let's improve our **routes** with some **HTML**.

Besides, **Flask** uses a template language called **Jinja** (mixing python + HTML while avoiding JavaScript).

1. Let's start in `Templates` creating `base.html`.
- This is going to be the **Frontend**, `base.html` will have like the basic website theme; other html files will add stuff to this basics.
- If I wanted to use my own JS stuff, I should add it to `static` so that the script pulls 'em nicely. Also reme
- Python expressions work if inside double curly, like `{{ print("sup dawg") }}`.
- As we paste the `<scripts>`, we may create `index.js` in `static` folder.
- Things like `<nav class>` are still bootstrap and we should look into that on Bootstrap website 🤔!
- <!--install VSC 'Prettier'!-->
- 

```HTML
<!DOCTYPE html>
<html>
    <head>
        <meta ...>
        <meta ...>
        <link ...> <!--this is CSS bootstrap...-->
        <link ...>

        <!--This is Jinja; python syntax OK in curly braces-->
        <title> {% block title %}Home{% endblock %}</title>
    </head>
    
    <!--Now for the body, starting with the scripts-->
    <body>
        <nav class=...>
            <button
            class=...
            ...
            >
                <span class=...>
            </button>
            <div class=...>
                <div class=...>
                    <a class=...>Login</a> <!--HERE IS REDIRECT TO LOGIN-->
                    <a class=...>Sign Up</a>
                    <a class=...>Logout</a>
                    <a class=...>Home</a>
        </nav>
        <script
            src=...
            integrity=sha384-...
            crossorigin=...
        ></script>
        <script
            ...
        ></script>
        <script
            ...
        ></script>
        <script
            type="text/javascript"
            src="{{ url_for('static', filename='index.js') }}"
        ></script>
    </body>
</html>
```

2. Now we are ready to use this template in other files, hence we create `home.html` in templates.

```html
{% extend "base.html" %}
{% block title %}Changed{% endblock %}
```

3. Gotta render these templates in `views.py`.

```python
from flask import render_template

@...
def home():
    return render_template("home.html")
