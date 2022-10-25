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
  - [Sign Up Page HTML](#sign-up-page-html)
  - [Login Page HTML](#login-page-html)
  - [HTTP Requests (POST, GET, ETC.)](#http-requests-post-get-etc)
  - [Handling POST Requests](#handling-post-requests)
  - [Message flashing](#message-flashing)

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

2. Now we are ready to use this template in other files (*template inheritance*), hence we create `home.html` in templates.

```html
{% extends "base.html" %}
{% block title %}Changed{% endblock %}
```

3. Gotta render these templates in `views.py`.

```python
from flask import render_template

@...
def home():
    return render_template("home.html")
```

> RUN THE WEBSITE
> ![FLASK1]()

4. Back in `base.html`, in between `</nav>` and `<script>` (to prepare a "space" for more content in each "view"):

```html
    <div class="container">{% block content %} {% endblock %}</div>

```

5. Now in `home.html`:

```html
{% block content %}
<h1>This is the home page</h1>
{% endblock %}
```

> RUN THE WEBSITE

6. Let's create more templates!!
   1. Correct `{% block title %}Home{% endblock %}` in `home.html`.
   2. For `login.html`, copypaste `home.html` contents and change as required.
   3. In `auth.py`:

```python
from flask import Blueprint, render_template

@auth.route('/login')
def login ():
    # return "<p>Login</p>"
    return render_template("login.html")

...
    return render_template("sign_up.html")
```
> RUN WEBSITE!

7. **Tim explains here about passing *variables* and *if-statements* to templates with JINJA (min 44)**.


## Sign Up Page HTML

Let's start working on the backend, user accounts, databases and all that fun stuff!

1. In `sign_up.html`, delete `<h1>This is the sign up page</h1>` and build up the sign-up form:

```html
{% extends "base.html" %}
{% block title %}Login{% endblock %}

{% block content %}
<form method="post">
    <h3 align="center">Sign Up</h3>
    <div class="form-group">
        <label for="email">Email Address</label>
        <input
            type="email"
            class="form-control"
            id="email"
            name="email"
            placeholder="Enter email"
        >
    </div>
</form>
{% endblock %}
```

2. Having explained the **classes** within `<input>`, let's add more fields:
   1. firstName
   2. password1
   3. password2

3. Include **button** after the previous elements to send info:

```html
<br />
<button type="submit" class="btn btn-primary">Submit</button>
```

4. **RECAP**: we are coding according with the ***Bootstrap*** CSS framework thanks to the relevant `<links/>` & `<scripts>` in `base.html`.


## Login Page HTML

1. Copypaste from `sign_up.html` and modify:
   1. Remove `firstName` and one of the `passwords`.
   2. "Signup" for "Login".
   3. "Submit" for "Login".

## HTTP Requests (POST, GET, ETC.)

HTTP: Hypertext Transfer Protocol

Methods (post, get, delete...) are useful to differenciate *requests* to our *routes*.
- Get (request): retrieve info, load site
- Post: change state of system, database, etc.

Currently we have only established the `<form method="post">` request (in Login, etc.); which is sent to the server and is expected to be managed, but we currently have no instructions for that.

## Handling POST Requests

1. In `auth.py`:

```python
@auth.route('/login', methods=['GET', 'POST'])

@auth.route('/sign-up', methods=['GET', 'POST'])
```

2. Import `request` to handle the information and...

```python
from flask import Blueprint, render_template, request

@auth.route('/login', methods=['GET', 'POST'])
def login ():
    data = request.form
    print(data)
    # return "<p>Login</p>"
    return render_template("login.html")
```

> Now I am struggling cause data only prints sometimes (when using `data=request.form.getlist('name[]'`) <!--https://stackoverflow.com/questions/23205577/python-flask-immutablemultidict-->

3. Next, same for 'Sign up'.
   1. We want to collect data for our database/backend; we also need to make sure data is valid for user creation.

```python
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up ():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            pass
        elif len(firstName) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            # add user to database
            pass

    return render_template("sign_up.html")
```
> still kinda struggling to print stuff

## Message flashing

