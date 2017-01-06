from main import main
from flask_login import login_required
from flask import make_response,redirect,url_for

@main.route('/posts-all')
@login_required
def posts_all():
    resp = make_response(redirect(url_for('main.index')))
    resp.set_cookie('show_followed','',max_age=30*24*60*60)
    return resp