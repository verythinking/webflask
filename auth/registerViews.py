from auth import auth
from auth.registerFroms import RegisterForm
from models.users import Users
from init import db
from flask import redirect,render_template,url_for,flash
from mailSender import send_email
from flask_login import current_user

@auth.route('/register',methods=['get','post'])
def register():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = Users(email=form.email.data,username=form.username.data,
                    password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmed_token()
        send_email(user.email,'Confirm Your Email','auth/mail/cfmMail',token=token)
        flash("the email has been posted")
        return redirect(url_for('auth.login'))
    return render_template("auth/register.html",form=form)