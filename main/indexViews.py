from flask import render_template, redirect, url_for,request,current_app,make_response
from main import main
from postForms import PostForm
from flask_login import current_user
from models.roles import Permission
from models.posts import Posts
from init import db

@main.route('/')
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and \
            form.validate_on_submit():
        post = Posts(body=form.body.data,
                     author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('main.index'))
    if current_user.is_authenticated:
        show_followed = bool(request.cookies.get('show_followed',''))
    else:
        show_followed = False
    if show_followed:
        query = current_user.followed_posts
    else:
        query = Posts.query

    page = request.args.get('page',1,type=int)
    pagination = query.order_by(Posts.timestamp.desc()).paginate(
        page,per_page=current_app.config['FLASK_POSTS_PER_PAGE'],error_out=False)
    posts =pagination.items
    return render_template('index.html',form=form,pagination=pagination,posts=posts,show_followed=show_followed)

