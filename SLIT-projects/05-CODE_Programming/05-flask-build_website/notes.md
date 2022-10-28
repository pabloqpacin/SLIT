# NOTES

> following 'main [readme](readme.md)'

## RIGHT NOW
- Create *package*: app + package/container/image (for Flask)
    - so that I can just run the thing and auto-install the required:
        - `pip install flask`
        - `pip install flask-login`
        - `pip install flask-sqlalchemy`
- Figure out HOW to access the website from *two devices* having the app running in one only 
- Transformation: from **Python Website Full Tutorial** to ***Custom Flask Website***
    - update README:

```markdown
# flask website tal
- brief description
    - Flask, Authentication, Databases...
        - auth: hashing
        - databases: ForeignKey
    - HTML, Bootstrap, JavaScript...
- screenshots
- instructions
    - installation & usage
    - tutorial documentation
        - each and every block of code present in the project files (ie. `.py`, `.html` and `.js` files) are documented as snippets
# full tutorial documentation - step by step
documentation, table of contents (?!)
## Getting started
## Creating a Flask App
## Creating Routes/VIews
## Jinja Templating Languag & HTML TEmplates
## Sign Up Page HTML
## ...
```


## TO-DO
1. Change **background color** because nobody likes empty boring annoying white 
2. Tweak **flashed messages** to f* with the user
3. Add more `models` and ensure the `user` can access such info (ie. **reminders**)
4. Create tags for **NOTES** so that info can be stored thematically (eg. programming, linux, tinkering)
5. How can I retrieve *all* database info (aka `cat`)


## progress

### GEN
- linking in GL76 <!-- SLIT/blob/week43 [file](/SLIT-projects/05-CODE_Programming/05-flask-build_website/)website -->
- current timestamp [1:03:12](https://youtu.be/dam0GPOAvVI) ([message flashing](readme.md#message-flashing))
- mind `{% with messages = get_flashed_messages(with_categories=true) %}` isn't highligthed for me as for Tim (theme-wise?)
- ... what does `path` in `__init__.py` do
- why is `database.db` created in separate `instance` folder? (it goes to `website` package for Tim)

### Message Flashing
- watch out with `data-dismiss`cuz not suggested

### Databasez
- Mind the `os` module/library
- **TBF** quite a few different lines here [Flask-SQLAlchemy db.create_all() got an unexpected keyword argument 'app'](https://stackoverflow.com/questions/73968584/flask-sqlalchemy-db-create-all-got-an-unexpected-keyword-argument-app)...

### User accounts & passwords
In `auth.py`:
```python
from werkzeug.security import generate_password_hash, check_password_hash
```
Now see the whole **hash** rant in `readme.md`.

### Deleting User Notes
- Mind JS errors `',' expected` for `home.html` (Ln 10).
> boss continues nevertheless...

🛰️ 🚀 🛸 🪐 🌠 🌌