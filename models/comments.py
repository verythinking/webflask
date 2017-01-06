from init import db
from datetime import datetime
import bleach
from markdown import markdown

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    disabled = db.Column(db.Boolean)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))

    @staticmethod
    def on_changed_body(target,value,oldvalue,initiator):
        allowed_tags = ['a','abbr','b','code','em','i','strong']
        target.body_html = bleach.linkify(bleach.clean(
                        markdown(value,output_format='html'),
                        tags=allowed_tags,strip=True))

db.event.listen(Comments.body,'set',Comments.on_changed_body)