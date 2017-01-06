from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired,FileAllowed,FileField
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length
from init import photos
class EditProfileForm(FlaskForm):
    name = StringField('Real Name',validators=[Length(0,64)])
    location = StringField('Location',validators=[Length(0,64)])
    about_me = TextAreaField('About Me')
    avatar = FileField('Avatar',validators=[FileRequired('No File selected'),
                                            FileAllowed(photos,'only picture')])
    submit = SubmitField('Submit')