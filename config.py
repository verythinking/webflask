import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = os.environ.get('MAIL_SENDER')
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    UPLOADED_PHOTOS_DEST = 'uploads'
    FLASKY_STATIC_DEST = 'static'
    FLASK_POSTS_PER_PAGE= 5


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'how do you do'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BOOTSTRAP_SERVE_LOCAL = True
    SQLALCHEMY_DATABASE_URI = ""

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ""


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = ""


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
