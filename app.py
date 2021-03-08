from flask import Flask, request
from flask_restful import Api, Resource
from flask_jwt import JWT, jwt_required
from flask_cors import *
from resources.user import UserRegister
from resources.tags import Blogger_tags, LiveGood_tags, Tags
from resources.blogger import BloggerList,BloggerStatsList, BloggerListInfo
from resources.live_good import LiveGoodList
from security import authenticate, identity
from db import db
from config import DB_URI, APP_SECRET_KEY

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY

# database config for this app
# app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:////tmp/wanghuantest.db'
app.config['SQLALCHEMY_DATABASE_URI'] =  DB_URI #'mysql+pymysql://root:root123@127.0.0.1/delidou'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))

@app.before_first_request
def create_tables():
    db.create_all()


api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister,'/signup')
api.add_resource(Tags,'/tags')
api.add_resource(BloggerList,'/blogger/rank/live')
api.add_resource(LiveGoodList,'/goods/rank/live')
api.add_resource(BloggerListInfo,'/blogger/rank/live1')



if __name__ == '__main__':
    db.init_app(app)
    app.run(host = '0.0.0.0',port = 8080)
