from flask_wtf import FlaskForm
from wtforms import SubmitField,PasswordField
from wtforms.validators import DataRequired,EqualTo

class ConfirmRestPWDForm(FlaskForm):
    password1 = PasswordField('PassWord',validators=[DataRequired()])
    password2 = PasswordField('Confirmed PassWord',validators=[DataRequired(),
                                EqualTo('password1',"Password must be same")])
    submit = SubmitField('Submit')