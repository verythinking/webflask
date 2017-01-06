from main import main
from models.users import Users
from flask import redirect,flash,url_for,render_template,request,current_app

@main.route('/followers/<username>')
def followers(username):
    user = Users.query.filter_by(username=username).first()
    if user is None:
        flash('Invaild user')
        return redirect(url_for('main.web_inddex'))
    page = request.args.get('page',1,type=int)
    pagination = user.follower.paginate(
                    page,per_page=current_app.config['FLASK_POSTS_PER_PAGE'],
                    error_out=False)
    follows = [{'user':item.follower,'timestamp':item.timestamp } for item in pagination.items]
    return render_template('follow.html',user=user,title="Followers of",
                           endpoint='main.followers',pagination=pagination,follows=follows)
