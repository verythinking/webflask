from main import main
from models.users import Users
from flask_login import current_user,login_required
from flask import redirect,url_for,flash
from decorators import permission_required
from models.roles import Permission

@main.route('/follow/<username>',methods=['get','post'])
@login_required
@permission_required(Permission.FOLLOW)
def follow(username):
    user = Users.query.filter_by(username=username).first()
    if user is None:
        flash('Invaild user')
        return redirect(url_for('main.index'))
    if current_user.is_following(user):
        flash('your are already following this user')
        return redirect(url_for('main.user',username=username))
    current_user.follow(user)
    return redirect(url_for('main.user',username=username))
