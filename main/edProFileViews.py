from main import main
from flask_login import login_required,current_user
from edProFileForms import EditProfileForm
from flask import flash,redirect,render_template,url_for,current_app
from init import db,photos
from picMaker import make_pic

@main.route('/edit-profile',methods=['get','post'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        mail_hash = current_user.generate_mail_hash()
        file_name = photos.save(form.avatar.data)
        file_extensions = file_name.split('.')[-1]
        avatar_name = '{}.{}'.format(mail_hash,file_extensions)
        make_pic(file_name,(300,300),"x300",avatar_name)
        make_pic(file_name,(65,65),"x65",avatar_name)
        current_user.avatar_name = avatar_name
        db.session.add(current_user)
        flash('Your profile has been updated')
        return redirect(url_for('main.user',username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edProfile.html',form=form)