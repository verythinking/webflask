from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField

class PostForm(FlaskForm):
    body = PageDownField('what\'s on your mind?',validators=[DataRequired()])
    submit = SubmitField('Submit')