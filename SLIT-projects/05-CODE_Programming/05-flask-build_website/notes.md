<<OJALDRE>>
- linking:
    - SLIT/blob/week43 [file](/SLIT-projects/05-CODE_Programming/05-flask-build_website/)website
<<OJALDRE>>


notes commenting the [readme](readme.md) file


<!--jueves 27/10/2022-->
# notes

## context
about to start [message flashing](readme.md#message-flashing)
video timestamp [1:03:12](https://youtu.be/dam0GPOAvVI)


honestly I'm a bit lost since it was **two days ago** that I did all current progress

it's gonna be fine tho

just need to carry on and perhaps visit the *readme* every now and then
## TO-DO

1. Change background color --> I don't want boring annoying white 
2. Maybe... figure out why the `{% with messages = get_flashed_messages(with_categories=true) %}` aren't highligthed same way as Tim. Is it the *theme*? 🤔
3.  Tweak flashed messages to f* with the user
4. Add more `models` and ensure the `user` can access such info (ie. **reminders**)
5. Figure out why `database.db` is created in separate `instance` folder; why not in current `website` package?

## progress

### Message Flashing
- watch out with `data-dismiss`cuz not suggested


### Databasez
- Mind the `os` module/library
- **TBF** quite a few different lines here [Flask-SQLAlchemy db.create_all() got an unexpected keyword argument 'app'](https://stackoverflow.com/questions/73968584/flask-sqlalchemy-db-create-all-got-an-unexpected-keyword-argument-app)...
