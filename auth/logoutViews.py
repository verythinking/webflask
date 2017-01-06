from flask_login import logout_user,login_required
from auth import auth
from flask import flash,redirect,url_for
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out')
    return redirect(url_for('main.index'))