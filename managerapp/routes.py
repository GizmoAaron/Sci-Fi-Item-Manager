# Copyright (C) 2019 Gotanks, GizmoAaron

from flask import render_template, url_for, flash, redirect, request
from managerapp import app,db,bcrypt
from managerapp.forms import RegistrationForm, LoginForm
@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html', posts = posts)
@app.route('/Login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('you have been logged in','Success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('Login.html', title='Login', form=form)
@app.route('/Register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrpyt.generate_password_hash(form.password.data).decode('utf-8') #We encryption of the password is stored once the user enters their initial password
        user = User(username = form.username.data, email = form.email.data, password = hashed_password) #The password is then assign to the user and is then added to the database
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('Register.html', title='Register', form=form)
