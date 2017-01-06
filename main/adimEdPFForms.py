from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SelectField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Email,Length,Regexp,ValidationError
from models.roles import Roles
from models.users import Users

class EditProfileAdimForm(FlaskForm):
    email = StringField('Email',
            validators=[DataRequired(),Length(1,64),Email()])
    username = StringField('Username',
            validators=[DataRequired(),Length(1,64),
            Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
                   "Username must have only letters,numbers,dots or underscores")])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role',coerce=int)
    name = StringField('Real Name',validators=[Length(0,64)])
    location = StringField('Location',validators=[Length(0,64)])
    about_me = TextAreaField('About Me')
    submit = SubmitField('Submit')

    def __init__(self,user,*args,**kwargs):
        super(EditProfileAdimForm,self).__init__(*args,**kwargs)
        self.role.choices = [(role.id,role.name)
                             for role in Roles.query.order_by(Roles.name).all()]
        self.user = user

    def validate_email(self,field):
        if field.data != self.user.email and \
            Users.query.filter_by(email=field.data).first():
            raise ValidationError("Email has registered")

    def validate_username(self,field):
        if field.data != self.user.username and \
            Users.query.filter_by(username=field.data).first():
            raise ValidationError("Username has registered")
