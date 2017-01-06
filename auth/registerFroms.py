from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length,Regexp,ValidationError
from models.users import Users

class RegisterForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),
                                            Length(1,64),Email()])
    username = StringField('UserName',validators=[DataRequired(),
                            Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
                                                'username must have only letters,numbers,dots or underscores')])
    password1 = PasswordField('PassWord',validators=[DataRequired()])
    password2 = PasswordField('Confired PassWord',validators=[DataRequired(),
                            EqualTo('password1',message='Password must be same.')])
    submit = SubmitField('Register')

    def validate_email(self,field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError("Email has already registered.")
    def validate_username(self,field):
        if Users.query.filter_by(username=field.data).first():
            raise ValidationError("UserName has already registered.")