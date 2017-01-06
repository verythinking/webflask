from auth import auth
from chMailForms import ChangeMailForm
from flask import redirect,render_template,url_for,flash
from flask_login import current_user
from mailSender import send_email

@auth.route('/changemail',methods=['get','post'])
def change_email():
    form = ChangeMailForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            token = current_user.generate_email_change_token(form.email.data)
            send_email(form.email.data,'Change Mail','auth/mail/cfmChMail',token=token)
            flash('The mail is posted!')
            return redirect(url_for('main.index'))
        else:
            flash('The password is not right!')
    return render_template('auth/chMail.html',form=form)