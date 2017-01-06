from init import db
from datetime import datetime

class Follows(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer,db.ForeignKey('users.id'),
                            primary_key=True)
    followed_id = db.Column(db.Integer,db.ForeignKey('users.id'),
                            primary_key=True)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow)