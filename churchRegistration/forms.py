from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField, PasswordField, SubmitField, IntegerRangeField, SelectField
=======
from wtforms import StringField, PasswordField, SubmitField, BooleanField
>>>>>>> 003623faa5ade10c2d54108bd0f2b082aac6ccca
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired, Email, EqualTo,Length
from wtforms import ValidationError


class CreateChurchServiceForm(FlaskForm):
    name = StringField("Name of Service", validators = [DataRequired()])
    date = DateField("Date of Service", format = '%Y-%m-%d')
    time = TimeField("Time Service Begins", format = '%H.%M')
    submit = SubmitField("Create Service")

<<<<<<< HEAD
class JoinServiceForm(FlaskForm):
    '''
    The form to fill when requesting to join a service
    '''
    name = StringField("Name: ")
=======

class AdminRegister(FlaskForm):
    church_name = StringField("Name of Church", validators=[DataRequired(), Length(min=5, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class AdminLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
>>>>>>> 003623faa5ade10c2d54108bd0f2b082aac6ccca
