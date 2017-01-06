from main import main
from flask import render_template,abort
from models.users import Users
from models.posts import Posts
@main.route('/user/<username>')
def user(username):
    user = Users.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    posts = user.posts.order_by(Posts.timestamp.desc()).all()
    return render_template('user.html',user=user,posts=posts)