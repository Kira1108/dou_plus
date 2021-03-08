from flask_restful import Resource,reqparse
from models.blogger import BloggerModel
from models.blogger_stats import BloggerStatsModel
from db import db

class BloggerList(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('n',
    type = int, required = True, help = 'This field can not be left blank.')

    def get(self):

        data = BloggerList.parser.parse_args()
        # bloggers = [b.json() for b in BloggerModel.getn(data['n'])]
        bloggers = [b.json() for b in BloggerModel.getn(data['n'])]
        return {'bloggers':bloggers}, 200


class BloggerStatsList(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('n',
    type = int, required = True, help = 'This field can not be left blank.')

    def get(self):

        data = BloggerStatsList.parser.parse_args()
        # bloggers = [b.json() for b in BloggerModel.getn(data['n'])]
        bloggers = [b.json() for b in BloggerStatsModel.getn(data['n'])]
        return {'blogger_stats':bloggers}, 200


class BloggerListInfo(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('n',
    type = int, help = 'This field can not be left blank.')

    def get(self):
        data = BloggerListInfo.parser.parse_args()
        n = data['n'] if data['n'] else 30
        bloggers = [b.json() for b in BloggerStatsModel.getn(n)]

        for blogger in bloggers:
            blogger_info = BloggerModel.get_by_id(blogger['id'])
            if blogger_info:
                blogger.update(blogger_info.json_short())
        return bloggers
