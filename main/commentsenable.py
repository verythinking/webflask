from main import main
from flask_login import login_required
from decorators import permission_required
from models.comments import Comments
from models.roles import Permission
from init import db
from flask import redirect,url_for,request

@main.route('/moderate/enable/<int:id>')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate_enable(id):
    comment = Comments.query.get_or_404(id)
    comment.disabled = False
    db.session.add(comment)
    return redirect(url_for('.moderate',
                            page=request.args.get('page', 1, type=int)))