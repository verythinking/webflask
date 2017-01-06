from auth import auth
from flask import redirect,url_for,flash
from flask_login import current_user

@auth.route('/changemail/change/<token>')
def do_change_mail(token):
    if current_user.confirmed_email_change_token(token):
        flash("The Email has been update!")
    else:
        flash("change email failure!")
    return redirect(url_for('main.index'))