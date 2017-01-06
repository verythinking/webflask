from auth import auth
from rsPwdForms import PasswordResetForm
from models.users import Users
from mailSender import send_email
from flask import render_template,redirect,url_for,request,flash,current_app
from flask_login import current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
@auth.route('/resetpassword',methods=['get','post'])
def reset_password():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form =PasswordResetForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        s = Serializer(current_app.config['SECRET_KEY'],3600)
        token = s.dumps(user.email)
        send_email(user.email,"Reset PassWord","auth/mail/rsPwd",
                   token=token,next=request.args.get('next'))
        flash('The reset mail has been post')
        return redirect(url_for('main.index'))
    return render_template("auth/rsPwd.html", form=form)

