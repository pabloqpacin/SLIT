from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # print(data)
    # return "<p>Login</p>"
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # check for user in database (any email?)
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash ('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required # user needs to have logged-in to see this page
def logout():
    # return "<p>Logout</p>"
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
            pass
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            # add user to database & password hash
            print(email, first_name, password1) # do delete
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            # return redirect('/') --> fine but messy if routes ever change
            return redirect(url_for('views.home'))
            
    return render_template("sign_up.html", user=current_user)