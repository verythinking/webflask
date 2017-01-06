from main import main
from flask_login import login_required
from decorators import admin_required
from models.users import Users
from models.roles import Roles
from init import db
from flask import flash,redirect,render_template,url_for
from adimEdPfForms import EditProfileAdimForm

@main.route('/edit-profile/<int:ids>',methods=['get','post'])
@login_required
@admin_required
def edit_profile_admin(ids):
    user = Users.query.get_or_404(ids)
    form = EditProfileAdimForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Roles.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        flash("The profile has been updated")
        return redirect(url_for('main.user',username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edProfile.html',form=form,user=user)