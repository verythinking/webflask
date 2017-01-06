from main import main
from models.posts import Posts
from flask import render_template,flash,redirect,url_for,request,current_app
from commentForms import CommentForm
from models.comments import Comments
from flask_login import current_user
from init import db

@main.route('/post/<int:id>',methods=['GET','POST'])
def show_post(id):
    post = Posts.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comments(body=form.body.data,post=post,
                           author=current_user._get_current_object())
        db.session.add(comment)
        flash('comment is update')
        return redirect(url_for('main.show_post',id=post.id,page=-1))
    page = request.args.get('page',1,type=int)
    if page == -1:
        page = (post.comments.count()/current_app.config['FLASK_POSTS_PER_PAGE']+1)
    pagination = post.comments.order_by(Comments.timestamp.asc()).paginate(
        page,per_page=current_app.config['FLASK_POSTS_PER_PAGE'],error_out=True)
    comments = pagination.items
    return render_template('post.html',posts=[post],
                           form=form,comments=comments,pagination=pagination,page=page)