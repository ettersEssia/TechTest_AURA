# In this file we define our application forms

from flask_wtf import FlaskForm
# if you submit with an empty textfield do somthing like a popup
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms import StringField, EmailField, SubmitField, PasswordField, BooleanField, ValidationError

# Create our forms for our app

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("E-mail", validators=[DataRequired()])
    password_hash = PasswordField("Password", validators=[DataRequired(), EqualTo('password_hash2', message="Password doesn't much")])
    password_hash2 = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email = EmailField("E-mail", validators=[DataRequired()])
    password_hash = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")