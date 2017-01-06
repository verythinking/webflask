from flask import render_template,request,current_app
from flask_login import login_required
from decorators import permission_required
from models.roles import Permission
from main import main
from models.comments import Comments

@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def moderate():
    page = request.args.get('page',1,int)
    pagination = Comments.query.order_by(Comments.timestamp.asc()).paginate(page,
                        current_app.config['FLASK_POSTS_PER_PAGE'],error_out=True)
    comments = pagination.items
    return render_template('moderate.html',pagination=pagination,
                           comments=comments,page=page)