from flask_restful import Resource,reqparse
from models.blogger import BloggerModel
from models.live_good import LiveGoodModel
from db import db


class Blogger_tags(Resource):

    def get(self):
        tags = BloggerModel.get_tags()
        print(tags)
        return {'blogger_tags':tags}, 200


class LiveGood_tags(Resource):

    def get(self):
        tags = LiveGoodModel.get_tags()
        print(tags)
        return {'livegood_tags':tags}, 200


def filter_tags(tags):
    return list(filter(lambda x: (x is not None) and (x != ''),tags))

class Tags(Resource):
    def get(self):
        blogger_tags = BloggerModel.get_tags()
        livegood_tags = LiveGoodModel.get_tags()
        blogger_tags = filter_tags(blogger_tags)
        livegood_tags = filter_tags(livegood_tags)
        return {"data":
                    {"blogger_tags":blogger_tags,
                    "goods_tags": livegood_tags},
                "message": "successful",
                "code": 200,
                "success": True}
