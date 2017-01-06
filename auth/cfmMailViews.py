from auth import auth
from flask_login import current_user,login_required
from flask import redirect,url_for,flash

@auth.route('/confirm/<token>')
@login_required
def confirm_mail(token):
    if current_user.confirmed:
        flash("You have Confirmed Email Yet!")
    else:
        if current_user.confirmed_token(token):
            flash("Confirmed Email successful!")
        else:
            flash("Confirmed Email failed!")
    return redirect(url_for('main.index'))