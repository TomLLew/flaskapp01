from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User
from flask_login import LoginManager, current_user

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostForm(FlaskForm):
    title = StringField('Title',
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    content = StringField('Content',
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    submit = SubmitField('Post Content')

class RegistrationForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=2, max=50)
        ]
    )

    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=2, max=50)
        ]
    )

    password = PasswordField('Password', 
        validators=[
            DataRequired()
        ]
    )

    confirm_password = PasswordField('Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )

    submit = SubmitField('Sign up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use!')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=2, max=60)
        ])

    last_name = StringField('Last name',
        validators=[
            DataRequired(),
            Length(min=2, max=60)
        ])

    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])

    submit = SubmitField('Update')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use - Please choose another')




