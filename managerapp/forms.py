from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(),Length(min=2,max=20)])

    lastname = StringField('Last Name', validators=[DataRequired(),Length(min=2,max=20)])

    password = PasswordField('Password', validators=[DataRequired()])

    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])

    phonenum = StringField('Phone Number',validators=[DataRequired()])

    email = StringField('Email',validators=[DataRequired(), Email()])

    submit = SubmitField('Submit')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:#this checks to see if there is a email already in the database based on the credentials
                raise ValidationError('Email already in use. If you already made and account, please ask E-Board for information')
    def validate_username(self, phonenum):
        user = User.query.filter_by(phoneNumber = phonenum.data).first()
        if user:#this checks to see if there is a username already in the database based on the credentials
                raise ValidationError('Username already in use. If you already made and account, please ask E-Board for information')

class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])

    email = StringField('Email',validators=[DataRequired(), Email()])

    remember = BooleanField('Remember Me')
    
    submit = SubmitField('Login')