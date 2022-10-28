# Python Website Full Tutorial - Flask, Authentication, Databases & More

Following a tutorial by @ Tech With Tim
- long video (following): [Python Website Full Tutorial - Flask, Authentication, Databases & More](https://youtu.be/dam0GPOAvVI)
- short video (might watch): [Make A Python Website As Fast As Possible!](https://youtu.be/kng-mJJby8g)
- if anything, source code: [github](https://github.com/techwithtim/Flask-Web-App-Tutorial)

More related content:
- [GeekForGeeks00](https://www.geeksforgeeks.org/how-to-get-data-from-immutablemultidict-in-flask/)


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
  - [Flask SQLAlchemy setup](#flask-sqlalchemy-setup)
  - [Database Models](#database-models)
  - [Foreign Key Relationships](#foreign-key-relationships)
  - [Database Creation](#database-creation)
    - [error - SQLAlchemy db.create_all() got an unexpected keyword argument 'app'](#error---sqlalchemy-dbcreate_all-got-an-unexpected-keyword-argument-app)
    - [database.db - weird behaviour](#databasedb---weird-behaviour)
  - [Creating New User Accounts](#creating-new-user-accounts)
    - [Tim's `first_name` error](#tims-first_name-error)
    - [Account created!](#account-created)
  - [Logging In Users](#logging-in-users)
  - [Flask Login Module](#flask-login-module)

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

<!--jueves 27/10/2022-->
## Message flashing

1. Write the messages inn `auth.py`:
      - In contrast with Tim, I keep the `print(email, firstName, password1)` line because it didn't work earlier so better keep it for *research*.
      - mark in mind the `category` **parameter**.

```python
# Import flash
from flask import Blueprint, render_template, request, flash

# (...)

        if len(email) < 4:
            # previously `pass` here
            flash('Email must be greater than 4 characters.', category="error" )
        # (...)
        else:
            # add user to database
            # previously `pass` here
            flash('Account created!', category='success')
                        print(email, firstName, password1)
```


2. How to display the messages! Need to write a block of code in `base.html`; this way the block will work in any **route**.

    1. Must write underneath the `nav` bar but above the main content (`div ... % block content %`)
    2. Must write a **for-loop**.
       1. First define `messages` variable to equal `flash` function in `auth.py` (because Flask!) and
       2. write the **if-statment**
    3. Then write the [`<div>` tag](https://www.w3schools.com/tags/tag_div.ASP) using ***Bootstrap's*** `alert` for `class` 

```html
<!--this block is for error/success messages in `auth.py`-->
{% with messages = get_flashed_messages(with_categories=true) %}
{% if messages %}
    {% for category, message in messages %}
    <!--error messages: `danger` for red-->
    {% if category == 'error' %}
    <div class="alert alert-danger alert-dismissable fade show" role="alert">
        <!--pull the message-->
        {{ message }}
        <!--dismiss button-->
        <button type="button" class="close" data-dismiss="alert">
            <!--include icon-->
            <span aria-hidden="true">&times;></span>
        </button>
    </div>
    <!--success messages: `success` for green-->
    {% else %}
    <div class="alert alert-success alert-dismissable fade show" role="alert">
        <!--pull the message-->
        {{ message }}
        <!--dismiss button-->
        <button type="button" class="close" data-dismiss="alert">
            <!--include icon-->
            <span aria-hidden="true">&times;></span>
        </button>
    </div>
    {% endif %}
    {% endfor %}
{% endif %}
{% endwith %}
```


## Flask SQLAlchemy setup

Let's start with our **database** in `__init__.py`,importing `SQLAlchemy` module from `flask_sqlalchemy`  library and defining a new database.

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

# To interact with the database (`database.db`)  (eg. create users) we'll use the **database object** `db`

def create_app():
    # (...)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
```

## Database Models

In `models.py`, let's define the structure. We want database (*DB*) model for (1) users and (2) *notes*.

1. Must use `flask_login` module and `UserMixin` for object inheritance, as means to log in users.

2. Define **classes** (first, `Users`):
   1. Try to use singular.
   2. Importance of **primary keys** as unique identifiers for different entries (ie. same 'first name' twice), tipically an integer; therefore **variable** `id = ... integer, primary_key...`.
   3. 99% times we use `db.Column`.
   4. For `Strings`, max lenght.
   5. `unique=True` so that no other users can have same `email` variable.

```python
from . import db # . = website package
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
```

3. Now `Note`:
   1. Also *inherites* from `db.Model`.
   2. Recap `primary_key` will add +1 to last id integer.

```python
from sqlalchemy.sql import func # to set DateTime automatically :D

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
```

## Foreign Key Relationships

Time to associate *notes* with *users* aka associate different info with different users.

Each user may have multiple notes, so we must establish a **relationship** between the *Note object* and the *User object*.

To do that we use **foreign keys** aka a column in our database that refs a different DB column.

So now, for every *note* we want to store the `id` of the *user* who created it. So let's integrate such `user_id`:

```python
# In `class Note`:
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # type of column = integer
    # ForeignKey = must pass valid ID to this field AKA 'one to many' relationship --> 1 user but many notes AKA 1 object and many children
    # so! we store a ForeignKey on the child object that references the parent object
    # now! every note links to a user thanks to `user_id` and their `primary_key`
```

Now we also want *users* to find their *notes*:

```python
# In `class User`:
    notes = db.relationship('Note')
    # now every note created generates a relationship with the user
```

Mind the capitals: `Note` must be uppercase but `user.id` lowercase  because 'foreignKey'.

Also mind the differences between "one to many" relationships and "many to one" (ie. 1 note many users).


## Database Creation

We have set it up in `__init__.py` and defined what it would look like in `models.py`.

Now back in `__init__.py` we'll write a script for the **app** to check, before ever running the server, whether a database is created.

1. First `from .models import User, Note` before the app is initialized, right after *blueprints register*.

2. Then the DB function!

```python
from os import path # to determine whether there's a path to the database

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

```

> RUN THE APP
### error - SQLAlchemy db.create_all() got an unexpected keyword argument 'app'

Documentation: [stackoverflow.com](https://stackoverflow.com/questions/73968584/flask-sqlalchemy-db-create-all-got-an-unexpected-keyword-argument-app) ->

See [comments](/SLIT-projects/05-CODE_Programming/05-flask-build_website/website/__init__.py) in `__init__.py`.

> RUN THE APP

### database.db - weird behaviour

Database file `database.db` is created in automatically generated `instance` folder; Tim gets it in `website` package tho 😕

## Creating New User Accounts

> importancia de **linking** en [notes.md](/SLIT-projects/05-CODE_Programming/05-flask-build_website/notes.md)
> <!--==linktest2.0==-->

1. In `auth.py`, use the `sign_up()` function to create accounts.
   1. Call `User` class model
   2. Need to import thingies from `flask_login` to **hash** passwords.
   3. ... free choice of `sha256` hashing algorithm

```markdown
# hash

## **HASHING** to secure a password
- passwords shouldn't be stored as plain text; password shouldn't be stored as password is.
- So password is converted into a secure format AKA *hash*.

## **HASHING FUNCTIONS**
'one-way function', ie. doesn't have inverse

### example of an inverse function in **python**
x -> y
f(x) = x + 1

"Inverse" means that having 'y' ('x + 1'), you can get back to x:

f(y) = y - 1

eg.
f(2) -> 3
f'(3) -> 2

ie.
Given the output, you can find the input

### hashing means no inverse

Ouput can't retrace input:

X -> Y
Y -> ?

So, password x and you *hash* it to y.
Now having y, no one can find out x.
Still, "you can check if the password you're typing is correct by running it through the same hashing function".
That is, whether your 'password' equals the **hash** that's stored :)

(Therefore `password=generate_password_hash` below)
```

2. Now we also want to redirect the users!

> Finally here's codey:

```python
from flask import ... redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db # ...

# (...)

    else:   
        new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='sha256'))
            # error 'db not defined' so import it... 
            db.session.add(new_user)
            db.session.commit()
            # flash ...
            # return redirect('/') --> fine but messy if routes ever change
            return redirect(url_for('views.home'))

```

> LET'S CREATE THE FIRST ACCOUNT AYE!!

### Tim's `first_name` error

Yes, four timez in `auth.py`.

### Account created!

|email|pquevedo @ G|
|---|---|
|name|pablerasyo
|passwd| micro7

## Logging In Users

Back in `auth.py`. Don't forget to redirect to ~.

Besides granting loggin to the user, also make sure at signup that email is available (not yet used).

```python
# @auth.route
# def login():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash ('Email does not exist.', category='error')

    return render_template("login.html")

# (...)

# @auth.route
# def sign_up():
    # (...)
    user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            # (...)
```

> RUN THE WEBSITE: login & signup work as intended :D


## Flask Login Module

Need to make sure 'homepage' is only available to logged-in users!
