from flask_restful import Resource,reqparse
from models.live_good import LiveGoodModel
from db import db



class LiveGoodList(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('n',
    type = int, required = True, help = 'This field can not be left blank.')

    def get(self):

        data = LiveGoodList.parser.parse_args()
        bloggers = [b.json() for b in LiveGoodModel.getn(data['n'])]
        return {'data':bloggers}, 200
