from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo

class CreateUserForm(FlaskForm):
    username = StringField(label='User Name:', validators=[Length(min=3, max=20, message='Input must be within 3 and 20 characters'), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create User')

class CreateAccountForm(FlaskForm):
    first_name = StringField(label='First Name:', validators=[Length(min=3, max=20, message='Input must be within 3 and 20 characters'), DataRequired()])
    last_name = StringField(label='Last Name:', validators=[Length(min=20, message='Input must be within 3 and 20 characters'), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    address = StringField(label='Customer Address:', validators=[DataRequired()])
