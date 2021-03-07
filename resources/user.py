from flask_restful import Resource,reqparse
from models.user import UserModel
from db import db


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type = str, required = True, help = 'This field can not be left blank.')
    parser.add_argument('password',
    type = str, required = True, help = 'This field can not be left blank')
    parser.add_argument('email',
    type = str, help = 'Enter you email for if you want to receive ads routinly.')

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.get_by_username(data['username']):
            return {'message':f'User with name {data["username"]} already exists.'}, 400

        user = UserModel(username = data['username'], password = data['password'], email = data['email'])
        db.session.add(user)
        db.session.commit()
        return user.json(), 201
