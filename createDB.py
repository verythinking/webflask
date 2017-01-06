from run import app
from models.roles import Roles
from models.users import Users
from models.posts import Posts
from init import db
with app.app_context():
    db.create_all()
    Roles.insert_roles()
    Users.generate_fake()
    Posts.generate_fake()


