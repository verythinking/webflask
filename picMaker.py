import os
from PIL import Image
from flask import current_app

def make_pic(pic_name,size,dir,avatar_name):
    app = current_app._get_current_object()
    os.chdir(app.config['UPLOADED_PHOTOS_DEST'])
    im = Image.open(pic_name)
    im.thumbnail(size)
    im.save(os.path.join(app.config['FLASKY_STATIC_DEST'],dir,avatar_name))
