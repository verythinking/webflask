from auth import auth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app,flash,redirect,render_template,url_for
from doRsPwdForms import ConfirmRestPWDForm
from init import db
from models.users import Users
@auth.route('/resetpassword/change/<token>',methods=['get','post'])
def do_reset_password(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    email=s.loads(token)
    form = ConfirmRestPWDForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=email).first()
        user.password = form.password1.data
        db.session.add(user)
        db.session.commit()
        flash("The password has reseted")
        return redirect(url_for("auth.login"))
    return render_template("auth/doRsPwd.html",form=form)

