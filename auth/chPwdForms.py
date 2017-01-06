from flask_wtf import FlaskForm
from wtforms import PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

class ChangePassWordForm(FlaskForm):
    old_password = PasswordField('Old PassWord',validators=[DataRequired()])
    new_password1 = PasswordField('New PassWord',validators=[DataRequired()])
    new_password2 = PasswordField('Confirmed PassWord',validators=[DataRequired(),
                                EqualTo('new_password1',"PassWord must be same")])
    submit = SubmitField('Submit')