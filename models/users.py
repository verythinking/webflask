from init import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from init import login_manager
from roles import Roles,Permission
from follows import Follows
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from datetime import datetime
import hashlib
from models.posts import Posts

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean,default=False)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    avatar_name = db.Column(db.String(128),default=None)
    member_since = db.Column(db.DateTime(),default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(),default=datetime.utcnow)
    posts = db.relationship('Posts',backref='author',lazy='dynamic')
    followed = db.relationship('Follows',
                               foreign_keys=[Follows.follower_id],
                               backref=db.backref('follower',lazy='joined'),
                               lazy='dynamic',
                               cascade='all,delete-orphan')
    follower = db.relationship('Follows',
                               foreign_keys=[Follows.followed_id],
                               backref=db.backref('followed',lazy='joined'),
                               lazy='dynamic',
                               cascade='all,delete-orphan')
    comments = db.relationship('Comments',backref='author',lazy='dynamic')


    def __init__(self,**kwargs):
        super(Users, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Roles.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Roles.query.filter_by(default=True).first()

    @property
    def password(self):
        raise AttributeError('password is not a readalbe attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def generate_confirmed_token(self,expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'],expiration)
        token = s.dumps({'confirmed':self.id})
        return token

    def confirmed_token(self,token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirmed') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        db.session.commit()
        return True

    def generate_email_change_token(self,email,expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'])
        token = s.dumps({'changemail':self.id,'newemail':email})
        return token

    def confirmed_email_change_token(self,token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('changemail') != self.id:
            return False
        newEmail = data.get('newemail')
        if newEmail is None:
            return False
        self.email = newEmail
        db.session.add(self)
        db.session.commit()
        return True

    def can(self,permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def generate_mail_hash(self):
        return hashlib.md5(self.email.encode('utf-8')).hexdigest()

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            u = Users(email=forgery_py.internet.email_address(),
                      username=forgery_py.internet.user_name(True),
                      password=forgery_py.lorem_ipsum.word(),
                      confirmed=True,
                      location=forgery_py.address.city(),
                      about_me=forgery_py.lorem_ipsum.sentence(),
                      member_since=forgery_py.date.date(True))
            db.session.add(u)
            try:
                db.session.commit()
            except:
                db.session.rollback()

    def follow(self,user):
        if not self.is_following(user):
            f = Follows(follower=self,followed=user)
            db.session.add(f)

    def unfollow(self,user):
        f = self.followed.filter_by(followed_id=user.id).first()
        if f:
            db.session.delete(f)
    def is_following(self,user):
        return self.followed.filter_by(followed_id=user.id).first() is not None

    def is_followed_by(self,user):
        return self.follower.filter_by(follower_id=user.id).first() is not None

    @property
    def followed_posts(self):
        return Posts.query.join(Follows,Follows.followed_id == Posts.author_id).filter(Follows.follower_id==self.id)


    def __repr__(self):
        return '<User %r>' % self.username
