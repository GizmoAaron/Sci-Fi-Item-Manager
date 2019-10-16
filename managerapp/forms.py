# Copyright (C) 2019 Gotanks, GizmoAaron

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from managerapp.models import User

class RegForm(FlaskForm):#A form for users to meet all credentials when they sign up
    firstname = StringField('First Name', validators = [DataRequired(),Length(min=2,max=20)])

    lastname = StringField('Last Name', validators = [DataRequired(),Length(min=2,max=20)])

    password = PasswordField('Password', validators = [DataRequired()])

    confirmpassword = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('Password')])

    phonenum = StringField('Phone Number',validators=[DataRequired()])

    email = StringField('Email',validators=[DataRequired(), Email()])

    confirmemail = StringField('Confirm Email', validators = (DataRequired(), EqualTo('Email')))

    submit = SubmitField('Submit')

    def validate_email(self, email):#This checks to see if the users name and email are already registered and will reject the use of an already used email
        user = User.query.filter_by(email = email.data).first()
        if user:
                raise ValidationError('Email already in use. If you already made and account, please ask E-Board for information')
    def validate_username(self, phonenum):
        user = User.query.filter_by(phoneNumber = phonenum.data).first()
        if user:
                raise ValidationError('Username already in use. If you already made and account, please ask E-Board for information')

class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])

    email = StringField('Email', validators=[DataRequired(), Email()])

    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')
