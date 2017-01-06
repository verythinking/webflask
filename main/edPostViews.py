from main import main
from models.posts import Posts
from flask_login import current_user
from models.roles import Permission
from flask import abort,flash,render_template,redirect,url_for
from postForms import PostForm
from init import db
@main.route('/edit/<int:id>',methods=['get','post'])
def edit_post(id):
    post = Posts.query.get_or_404(id)
    if not current_user.can(Permission.ADMINISTER) and current_user != post.author:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.body = form.body.data
        db.session.add(post)
        flash('The post has been updated')
        return redirect(url_for('main.show_post',id=post.id))
    form.body.data = post.body
    return render_template('edPost.html',form=form)