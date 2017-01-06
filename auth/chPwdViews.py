from auth import auth
from chPwdForms import ChangePassWordForm
from flask_login import current_user
from init import db
from flask import flash,render_template,redirect,url_for
@auth.route('/changepassword',methods=['get','post'])
def change_password():
    form = ChangePassWordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.new_password1.data
            db.session.add(current_user)
            flash("Your password has changed")
            return redirect(url_for('main.index'))
        else:
            flash("The old password is not right")
    return render_template("auth/chPwd.html",form=form)
