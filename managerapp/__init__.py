from flask import Flask, escape, request, flash, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
app = Flask(__name__)

app.config['SECRET_KEY'] = '' #this is used to prevent modification of cookies and cross-site forgery
app.config['SQLALCHEMY_DATABASE_URI'] = ''

from managerapp import routes