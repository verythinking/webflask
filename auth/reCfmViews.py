from auth import auth
from flask_login import login_required,current_user
from flask import redirect,flash,url_for
from mailSender import send_email

@auth.route('/reconfirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmed_token()
    send_email(current_user.email,"Confirm Your Email","auth/mail/cfmMail",token=token)
    flash('A new mail has posted')
    return redirect(url_for('main.index'))