
'''
It is extremly safe to copy and past this file
This is just copied from Flask-JWT documentation.
Don't worry about user authentication staff.
'''

from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.get_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.get_by_id(user_id)
