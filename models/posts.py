from init import db
from datetime import datetime
from markdown import markdown
import bleach

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comments',backref='post',lazy='dynamic')

    @staticmethod
    def generate_fake(count=100):
        from random import seed,randint
        import forgery_py

        seed()
        from models.users import Users
        user_count = Users.query.count()
        for i in range(count):
            u = Users.query.offset(randint(0,user_count-1)).first()
            p = Posts(body=forgery_py.lorem_ipsum.sentences(randint(1,3)),
                      timestamp=forgery_py.date.date(True),
                      author=u)
            db.session.add(p)
            db.session.commit()

    @staticmethod
    def on_changed_body(target,value,oldvalue,initiator):
        allowed_tags = ['a','abbr','acronym','b','blockquote','code','em',
                        'i','li','ol','pre','strong','ul','h1','h2','h3','p']
        target.body_html = bleach.linkify(bleach.clean(markdown(value,output_format='html'),
                                                       tags=allowed_tags,strip=True))

db.event.listen(Posts.body,'set',Posts.on_changed_body)
