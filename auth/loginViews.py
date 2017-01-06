from flask import render_template,redirect,url_for,request,flash
from flask_login import login_user,current_user
from auth import auth
from models.users import Users
from loginForms import LoginForm

@auth.route('/login',methods=['get','post'])
def login():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invaild username or password')
    return render_template('auth/login.html',form=form)