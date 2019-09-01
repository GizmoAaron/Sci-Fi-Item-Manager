from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(),Length(min=2,max=20)])

    lastname = StringField('Last Name', validators=[DataRequired(),Length(min=2,max=20)])

    password = PasswordField('Password', validators=[DataRequired()])

    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])

    phonenum = StringField('Phone Number',validators=[DataRequired()])

    email = StringField('Email',validators=[DataRequired(), Email()])

    submit = SubmitField('Submit')

class LoginForm(FlaskForm):

    password = PasswordField('Password', validators=[DataRequired()])

    email = StringField('Email',validators=[DataRequired(), Email()])

    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')