from flask import Flask, escape, request, flash, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '' #this is used to prevent modification of cookies and cross-site forgery
app.config['SQLALCHEMY_DATABASE_URI'] = ''
@app.route('/')
def home():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
@app.route('/Login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test' and form.password.data == 'testpassword':
            flash('you have been logged in','Success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('Login.html', title='Login', form=form)
@app.route('/Register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'Success')
        return redirect(url_for('home'))
    return render_template('Register.html', title='Register', form=form)
if __name__ == '__main__':
    app.run(debug=True)