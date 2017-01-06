from flask import Blueprint,redirect,request,url_for
from models.roles import Permission
from flask_login import current_user

main = Blueprint('main', __name__,static_folder='/static',static_url_path='/static')

import indexViews, errorsViews,userViews,edProFileViews,admiEdPfViews,\
        postViews,edPostViews,indexViews,followViews,unfollowViews,followersViews,\
        followedbyViews,postsAllViews,postsFollowedViews,moderateViews,commentsenable,commentsdisable

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
