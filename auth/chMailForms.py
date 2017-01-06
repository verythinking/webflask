from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,ValidationError
from models.users import Users

class ChangeMailForm(FlaskForm):
    email = StringField('New Email',validators=[DataRequired(),Email()])
    password = PasswordField('PassWord',validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_email(self,field):
        if Users.query.filter_by(email=field.data).first():
            raise ValidationError('The email has been registered!')

