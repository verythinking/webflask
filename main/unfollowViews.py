from main import main
from flask_login import login_required,current_user
from decorators import permission_required
from models.roles import Permission
from models.users import Users
from flask import flash,redirect,url_for


@main.route('/unfollow/<username>',methods=['get','post'])
@login_required
@permission_required(Permission.FOLLOW)
def unfollow(username):
    user = Users.query.filter_by(username=username).first()
    if user is None:
        flash('Invaild user')
        return redirect(url_for('mian.index'))
    if not current_user.is_following(user):
        flash('you do not follow this user')
        redirect(url_for('main.user',username=username))
    current_user.unfollow(user)
    return redirect(url_for('main.user',username=username))