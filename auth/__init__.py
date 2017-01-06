from flask import Blueprint

auth = Blueprint('auth',__name__)

import loginViews,logoutViews,registerViews,\
        cfmMailViews,unCfmViews,reCfmViews,\
        chPwdViews,rsPwdViews,doRsPwdViews,\
        chMailViews,doChMailViews