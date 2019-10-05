from flask import Flask, escape, request, flash, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from itsdangerous import Signer
app = Flask(__name__)

app.config.from_pyfile('config.cfg')
app.config['SECRET_KEY'] = '' #this is used to prevent modification of cookies and cross-site forgery
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from managerapp import routes