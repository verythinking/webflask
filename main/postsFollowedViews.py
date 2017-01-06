from main import main
from flask_login import login_required
from flask import make_response,redirect,url_for

@main.route('/posts-followed')
@login_required
def posts_followed():
    resp = make_response(redirect(url_for('main.index')))
    resp.set_cookie('show_followed','1',max_age=30*24*60*60)
    return resp