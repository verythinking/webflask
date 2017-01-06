from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Email,ValidationError
from init import db
from models.users import Users
class PasswordResetForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    submit = SubmitField('Submit')

    def validate_email(self,field):
        user = Users.query.filter_by(email=field.data).first()
        if user is None:
            raise ValidationError('The mail is not register')

